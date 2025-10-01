import json
import time
import hashlib
from typing import Dict, Any, Optional, Callable, List
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from threading import Lock
import logging

logger = logging.getLogger(__name__)


@dataclass
class CacheEntry:
    """Represents a cache entry with metadata."""
    key: str
    value: Any
    created_at: float
    expires_at: float
    access_count: int = 0
    last_accessed: float = 0
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.last_accessed == 0:
            self.last_accessed = self.created_at
    
    def is_expired(self) -> bool:
        """Check if cache entry is expired."""
        return time.time() > self.expires_at
    
    def is_stale(self, stale_threshold: float = 300) -> bool:
        """Check if cache entry is stale (not accessed recently)."""
        return time.time() - self.last_accessed > stale_threshold
    
    def access(self):
        """Record cache access."""
        self.access_count += 1
        self.last_accessed = time.time()


@dataclass
class CacheStats:
    """Cache statistics and metrics."""
    total_entries: int
    hit_count: int
    miss_count: int
    eviction_count: int
    memory_usage: int
    hit_rate: float
    
    @property
    def hit_rate_percentage(self) -> float:
        """Get hit rate as percentage."""
        return self.hit_rate * 100


class AdvancedCacheService:
    """
    Advanced caching service with multiple strategies and features.
    
    Features:
    - TTL-based expiration
    - LRU eviction
    - Tag-based invalidation
    - Memory usage tracking
    - Cache statistics
    - Granular cache control
    """
    
    def __init__(self, max_size: int = 1000, default_ttl: int = 300):
        """
        Initialize cache service.
        
        Args:
            max_size: Maximum number of cache entries
            default_ttl: Default time-to-live in seconds
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        
        # Cache storage
        self._cache: Dict[str, CacheEntry] = {}
        
        # Statistics
        self._hit_count = 0
        self._miss_count = 0
        self._eviction_count = 0
        
        # Thread safety
        self._lock = Lock()
        
        # Cache strategies
        self._strategies = {
            "lru": self._evict_lru,
            "ttl": self._evict_expired,
            "size": self._evict_by_size
        }
    
    def _generate_key(self, prefix: str, *args, **kwargs) -> str:
        """Generate cache key from arguments."""
        # Create a deterministic key from arguments
        key_data = {
            "prefix": prefix,
            "args": args,
            "kwargs": sorted(kwargs.items()) if kwargs else {}
        }
        
        # Convert to JSON string and hash
        key_string = json.dumps(key_data, sort_keys=True)
        return f"{prefix}:{hashlib.md5(key_string.encode()).hexdigest()}"
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found/expired
        """
        with self._lock:
            if key not in self._cache:
                self._miss_count += 1
                return None
            
            entry = self._cache[key]
            
            # Check if expired
            if entry.is_expired():
                del self._cache[key]
                self._miss_count += 1
                return None
            
            # Record access
            entry.access()
            self._hit_count += 1
            
            return entry.value
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None, tags: Optional[List[str]] = None) -> bool:
        """
        Set value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (uses default if None)
            tags: Optional tags for cache invalidation
            
        Returns:
            True if successfully cached
        """
        with self._lock:
            # Use default TTL if not specified
            if ttl is None:
                ttl = self.default_ttl
            
            # Check if we need to evict entries
            if len(self._cache) >= self.max_size and key not in self._cache:
                self._evict_entries()
            
            # Create cache entry
            now = time.time()
            entry = CacheEntry(
                key=key,
                value=value,
                created_at=now,
                expires_at=now + ttl,
                tags=tags or []
            )
            
            self._cache[key] = entry
            return True
    
    def delete(self, key: str) -> bool:
        """
        Delete cache entry.
        
        Args:
            key: Cache key
            
        Returns:
            True if entry was deleted
        """
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                return True
            return False
    
    def invalidate_by_tags(self, tags: List[str]) -> int:
        """
        Invalidate cache entries by tags.
        
        Args:
            tags: List of tags to invalidate
            
        Returns:
            Number of entries invalidated
        """
        with self._lock:
            invalidated = 0
            keys_to_delete = []
            
            for key, entry in self._cache.items():
                if any(tag in entry.tags for tag in tags):
                    keys_to_delete.append(key)
            
            for key in keys_to_delete:
                del self._cache[key]
                invalidated += 1
            
            return invalidated
    
    def clear(self) -> int:
        """
        Clear all cache entries.
        
        Returns:
            Number of entries cleared
        """
        with self._lock:
            count = len(self._cache)
            self._cache.clear()
            return count
    
    def get_stats(self) -> CacheStats:
        """Get cache statistics."""
        with self._lock:
            total_requests = self._hit_count + self._miss_count
            hit_rate = self._hit_count / total_requests if total_requests > 0 else 0
            
            # Estimate memory usage (simplified)
            memory_usage = len(str(self._cache))
            
            return CacheStats(
                total_entries=len(self._cache),
                hit_count=self._hit_count,
                miss_count=self._miss_count,
                eviction_count=self._eviction_count,
                memory_usage=memory_usage,
                hit_rate=hit_rate
            )
    
    def _evict_entries(self):
        """Evict cache entries using configured strategy."""
        # Use LRU strategy by default
        self._evict_lru()
    
    def _evict_lru(self, count: int = 1):
        """Evict least recently used entries."""
        if not self._cache:
            return
        
        # Sort by last access time (oldest first)
        sorted_entries = sorted(
            self._cache.items(),
            key=lambda x: x[1].last_accessed
        )
        
        # Remove oldest entries
        for i in range(min(count, len(sorted_entries))):
            key, _ = sorted_entries[i]
            del self._cache[key]
            self._eviction_count += 1
    
    def _evict_expired(self):
        """Evict expired entries."""
        expired_keys = [
            key for key, entry in self._cache.items()
            if entry.is_expired()
        ]
        
        for key in expired_keys:
            del self._cache[key]
            self._eviction_count += 1
    
    def _evict_by_size(self, target_size: int):
        """Evict entries to reach target size."""
        if len(self._cache) <= target_size:
            return
        
        entries_to_remove = len(self._cache) - target_size
        self._evict_lru(entries_to_remove)
    
    def cache_result(self, prefix: str, ttl: Optional[int] = None, tags: Optional[List[str]] = None):
        """
        Decorator to cache function results.
        
        Args:
            prefix: Cache key prefix
            ttl: Time-to-live in seconds
            tags: Optional tags for cache invalidation
        """
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                # Generate cache key
                key = self._generate_key(prefix, *args, **kwargs)
                
                # Try to get from cache
                cached_result = self.get(key)
                if cached_result is not None:
                    return cached_result
                
                # Execute function and cache result
                result = func(*args, **kwargs)
                self.set(key, result, ttl, tags)
                
                return result
            
            return wrapper
        return decorator
    
    def warm_cache(self, warmup_functions: List[Callable]):
        """
        Warm up cache with predefined functions.
        
        Args:
            warmup_functions: List of functions to execute for cache warming
        """
        for func in warmup_functions:
            try:
                func()
            except Exception as e:
                logger.warning(f"Failed to warm cache with function {func.__name__}: {e}")
    
    def cleanup_expired(self):
        """Clean up expired entries (can be called periodically)."""
        with self._lock:
            self._evict_expired()
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get detailed cache information."""
        with self._lock:
            stats = self.get_stats()
            
            return {
                "stats": asdict(stats),
                "configuration": {
                    "max_size": self.max_size,
                    "default_ttl": self.default_ttl,
                    "current_size": len(self._cache)
                },
                "entries": {
                    "total": len(self._cache),
                    "expired": len([e for e in self._cache.values() if e.is_expired()]),
                    "stale": len([e for e in self._cache.values() if e.is_stale()])
                }
            }


# Global cache service instance
cache_service = AdvancedCacheService(max_size=1000, default_ttl=300)


# Convenience functions for common cache operations
def cache_metric_result(metric_type: str, entity_id: str, ttl: int = 600):
    """Cache decorator for metric calculations."""
    return cache_service.cache_result(
        prefix=f"metrics:{metric_type}",
        ttl=ttl,
        tags=[f"metrics", f"entity:{entity_id}"]
    )


def cache_search_result(query_type: str, ttl: int = 300):
    """Cache decorator for search results."""
    return cache_service.cache_result(
        prefix=f"search:{query_type}",
        ttl=ttl,
        tags=["search", "results"]
    )


def cache_dashboard_data(role: str, ttl: int = 600):
    """Cache decorator for dashboard data."""
    return cache_service.cache_result(
        prefix=f"dashboard:{role}",
        ttl=ttl,
        tags=["dashboard", f"role:{role}"]
    )

