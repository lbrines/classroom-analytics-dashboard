import pytest
import time
import json
from app.services.cache_service import AdvancedCacheService, CacheEntry, CacheStats


class TestAdvancedCacheService:
    """Test suite for AdvancedCacheService following TDD methodology."""
    
    @pytest.fixture
    def cache_service(self):
        """Create an AdvancedCacheService instance for testing."""
        return AdvancedCacheService(max_size=100, default_ttl=60)
    
    def test_get_returns_none_for_missing_key(self, cache_service):
        """Test that get returns None for missing key."""
        result = cache_service.get("non_existent_key")
        assert result is None
    
    def test_set_and_get_stores_and_retrieves_value(self, cache_service):
        """Test that set stores value and get retrieves it."""
        key = "test_key"
        value = {"test": "data", "number": 42}
        
        # Set value
        success = cache_service.set(key, value)
        assert success is True
        
        # Get value
        result = cache_service.get(key)
        assert result == value
    
    def test_set_respects_ttl_parameter(self, cache_service):
        """Test that set respects custom TTL parameter."""
        key = "ttl_test_key"
        value = "test_value"
        custom_ttl = 1  # 1 second
        
        # Set with custom TTL
        cache_service.set(key, value, ttl=custom_ttl)
        
        # Should be available immediately
        result = cache_service.get(key)
        assert result == value
        
        # Wait for expiration
        time.sleep(1.1)
        
        # Should be expired now
        result = cache_service.get(key)
        assert result is None
    
    def test_set_respects_default_ttl(self, cache_service):
        """Test that set uses default TTL when none specified."""
        key = "default_ttl_key"
        value = "test_value"
        
        # Set without TTL (should use default)
        cache_service.set(key, value)
        
        # Should be available immediately
        result = cache_service.get(key)
        assert result == value
    
    def test_delete_removes_existing_entry(self, cache_service):
        """Test that delete removes existing entry."""
        key = "delete_test_key"
        value = "test_value"
        
        # Set value
        cache_service.set(key, value)
        assert cache_service.get(key) == value
        
        # Delete value
        success = cache_service.delete(key)
        assert success is True
        
        # Should be gone
        assert cache_service.get(key) is None
    
    def test_delete_returns_false_for_missing_key(self, cache_service):
        """Test that delete returns False for missing key."""
        success = cache_service.delete("non_existent_key")
        assert success is False
    
    def test_invalidate_by_tags_removes_matching_entries(self, cache_service):
        """Test that invalidate_by_tags removes entries with matching tags."""
        # Set entries with different tags
        cache_service.set("key1", "value1", tags=["tag1", "tag2"])
        cache_service.set("key2", "value2", tags=["tag2", "tag3"])
        cache_service.set("key3", "value3", tags=["tag3"])
        
        # Verify all are present
        assert cache_service.get("key1") == "value1"
        assert cache_service.get("key2") == "value2"
        assert cache_service.get("key3") == "value3"
        
        # Invalidate by tag2
        invalidated = cache_service.invalidate_by_tags(["tag2"])
        assert invalidated == 2  # key1 and key2 should be invalidated
        
        # Verify invalidation
        assert cache_service.get("key1") is None
        assert cache_service.get("key2") is None
        assert cache_service.get("key3") == "value3"  # Should still be there
    
    def test_clear_removes_all_entries(self, cache_service):
        """Test that clear removes all entries."""
        # Set multiple entries
        cache_service.set("key1", "value1")
        cache_service.set("key2", "value2")
        cache_service.set("key3", "value3")
        
        # Verify they exist
        assert cache_service.get("key1") == "value1"
        assert cache_service.get("key2") == "value2"
        assert cache_service.get("key3") == "value3"
        
        # Clear all
        cleared_count = cache_service.clear()
        assert cleared_count == 3
        
        # Verify all are gone
        assert cache_service.get("key1") is None
        assert cache_service.get("key2") is None
        assert cache_service.get("key3") is None
    
    def test_get_stats_returns_cache_statistics(self, cache_service):
        """Test that get_stats returns correct statistics."""
        # Initially empty
        stats = cache_service.get_stats()
        assert stats.total_entries == 0
        assert stats.hit_count == 0
        assert stats.miss_count == 0
        assert stats.hit_rate == 0.0
        
        # Set and get a value
        cache_service.set("test_key", "test_value")
        cache_service.get("test_key")  # Hit
        cache_service.get("missing_key")  # Miss
        
        # Check updated stats
        stats = cache_service.get_stats()
        assert stats.total_entries == 1
        assert stats.hit_count == 1
        assert stats.miss_count == 1
        assert stats.hit_rate == 0.5  # 1 hit out of 2 requests
    
    def test_cache_eviction_respects_max_size(self, cache_service):
        """Test that cache evicts entries when max size is reached."""
        # Set max_size to 2 for testing
        cache_service.max_size = 2
        
        # Fill cache to max size
        cache_service.set("key1", "value1")
        cache_service.set("key2", "value2")
        
        # Verify both are present
        assert cache_service.get("key1") == "value1"
        assert cache_service.get("key2") == "value2"
        
        # Add one more (should trigger eviction)
        cache_service.set("key3", "value3")
        
        # One of the original entries should be evicted
        # (implementation-dependent which one)
        stats = cache_service.get_stats()
        assert stats.total_entries <= 2
        assert stats.eviction_count > 0
    
    def test_cache_entry_access_records_usage(self, cache_service):
        """Test that cache entry access is recorded correctly."""
        key = "access_test_key"
        value = "test_value"
        
        # Set value
        cache_service.set(key, value)
        
        # Access multiple times
        cache_service.get(key)
        cache_service.get(key)
        cache_service.get(key)
        
        # Check that entry was accessed
        entry = cache_service._cache[key]
        assert entry.access_count == 3
        assert entry.last_accessed > entry.created_at
    
    def test_generate_key_creates_deterministic_keys(self, cache_service):
        """Test that _generate_key creates deterministic keys."""
        # Same arguments should generate same key
        key1 = cache_service._generate_key("prefix", "arg1", "arg2", param1="value1")
        key2 = cache_service._generate_key("prefix", "arg1", "arg2", param1="value1")
        assert key1 == key2
        
        # Different arguments should generate different keys
        key3 = cache_service._generate_key("prefix", "arg1", "arg3", param1="value1")
        assert key1 != key3
        
        # Different parameter order should generate same key (sorted)
        key4 = cache_service._generate_key("prefix", "arg1", "arg2", param2="value2", param1="value1")
        key5 = cache_service._generate_key("prefix", "arg1", "arg2", param1="value1", param2="value2")
        assert key4 == key5
    
    def test_cache_decorator_caches_function_results(self, cache_service):
        """Test that cache_result decorator caches function results."""
        call_count = 0
        
        @cache_service.cache_result("test_function", ttl=60)
        def test_function(x, y):
            nonlocal call_count
            call_count += 1
            return x + y
        
        # First call should execute function
        result1 = test_function(2, 3)
        assert result1 == 5
        assert call_count == 1
        
        # Second call with same arguments should use cache
        result2 = test_function(2, 3)
        assert result2 == 5
        assert call_count == 1  # Function not called again
        
        # Different arguments should execute function
        result3 = test_function(4, 5)
        assert result3 == 9
        assert call_count == 2
    
    def test_get_cache_info_returns_detailed_information(self, cache_service):
        """Test that get_cache_info returns detailed cache information."""
        # Set some test data
        cache_service.set("key1", "value1", tags=["tag1"])
        cache_service.set("key2", "value2", tags=["tag2"])
        
        # Get cache info
        info = cache_service.get_cache_info()
        
        assert "stats" in info
        assert "configuration" in info
        assert "entries" in info
        
        # Check configuration
        config = info["configuration"]
        assert config["max_size"] == 100
        assert config["default_ttl"] == 60
        assert config["current_size"] == 2
        
        # Check entries info
        entries = info["entries"]
        assert entries["total"] == 2
        assert entries["expired"] == 0  # Should be 0 for fresh entries
        assert entries["stale"] >= 0
    
    def test_cleanup_expired_removes_expired_entries(self, cache_service):
        """Test that cleanup_expired removes expired entries."""
        # Set entry with very short TTL
        cache_service.set("expired_key", "value", ttl=0.1)
        
        # Should be available immediately
        assert cache_service.get("expired_key") == "value"
        
        # Wait for expiration
        time.sleep(0.2)
        
        # Cleanup expired entries
        cache_service.cleanup_expired()
        
        # Entry should be gone
        assert cache_service.get("expired_key") is None


class TestCacheEntry:
    """Test suite for CacheEntry following TDD methodology."""
    
    def test_cache_entry_creation(self):
        """Test that CacheEntry is created with correct attributes."""
        now = time.time()
        entry = CacheEntry(
            key="test_key",
            value="test_value",
            created_at=now,
            expires_at=now + 60,
            tags=["tag1", "tag2"]
        )
        
        assert entry.key == "test_key"
        assert entry.value == "test_value"
        assert entry.created_at == now
        assert entry.expires_at == now + 60
        assert entry.access_count == 0
        assert entry.last_accessed == now
        assert entry.tags == ["tag1", "tag2"]
    
    def test_cache_entry_is_expired_checks_expiration(self):
        """Test that is_expired correctly checks expiration."""
        now = time.time()
        
        # Not expired entry
        entry1 = CacheEntry("key1", "value1", now, now + 60)
        assert not entry1.is_expired()
        
        # Expired entry
        entry2 = CacheEntry("key2", "value2", now - 120, now - 60)
        assert entry2.is_expired()
    
    def test_cache_entry_is_stale_checks_staleness(self):
        """Test that is_stale correctly checks staleness."""
        now = time.time()
        
        # Fresh entry
        entry1 = CacheEntry("key1", "value1", now - 10, now + 60)
        entry1.last_accessed = now - 10
        assert not entry1.is_stale(stale_threshold=300)
        
        # Stale entry
        entry2 = CacheEntry("key2", "value2", now - 400, now + 60)
        entry2.last_accessed = now - 400
        assert entry2.is_stale(stale_threshold=300)
    
    def test_cache_entry_access_updates_counters(self):
        """Test that access updates access count and last accessed time."""
        now = time.time()
        entry = CacheEntry("key", "value", now, now + 60)
        
        # Access entry
        entry.access()
        
        assert entry.access_count == 1
        assert entry.last_accessed >= now
        
        # Access again
        entry.access()
        
        assert entry.access_count == 2
        assert entry.last_accessed >= now

