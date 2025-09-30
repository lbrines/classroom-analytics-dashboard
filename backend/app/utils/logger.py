import logging
import sys
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

# Create logger instance
logger = logging.getLogger("educational_dashboard")

def get_logger(name: str = None):
    """Get logger instance."""
    if name:
        return logging.getLogger(f"educational_dashboard.{name}")
    return logger
