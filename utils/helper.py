"""
Helper Utilities
Common utility functions used throughout the bot
"""

import logging
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)


def format_timestamp(timestamp: Optional[datetime] = None) -> str:
    """
    Format a timestamp to a readable string
    
    Args:
        timestamp: datetime object, defaults to now if not provided
        
    Returns:
        Formatted timestamp string
    """
    if timestamp is None:
        timestamp = datetime.now()
    
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def is_admin(user_id: int, admin_list: list) -> bool:
    """
    Check if a user is an admin
    
    Args:
        user_id: The user's telegram ID
        admin_list: List of admin user IDs
        
    Returns:
        True if user is admin, False otherwise
    """
    return user_id in admin_list


def sanitize_text(text: str, max_length: int = 4096) -> str:
    """
    Sanitize and truncate text to fit Telegram's message length limit
    
    Args:
        text: Text to sanitize
        max_length: Maximum length (default 4096 for Telegram)
        
    Returns:
        Sanitized text
    """
    if len(text) > max_length:
        return text[:max_length - 3] + '...'
    return text


def parse_command_args(text: str, command: str) -> list:
    """
    Parse arguments from a command message
    
    Args:
        text: Full message text
        command: Command name (without /)
        
    Returns:
        List of arguments
    """
    # Remove the command from the text
    text = text.replace(f'/{command}', '').strip()
    
    # Split by spaces and return non-empty args
    return [arg for arg in text.split() if arg]


def build_menu(buttons: list, n_cols: int = 2) -> list:
    """
    Build a button menu layout
    
    Args:
        buttons: List of button objects
        n_cols: Number of columns (default 2)
        
    Returns:
        2D list representing the button layout
    """
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu


def log_user_action(user_id: int, username: str, action: str) -> None:
    """
    Log a user action for tracking
    
    Args:
        user_id: User's Telegram ID
        username: User's username
        action: Description of the action
    """
    timestamp = format_timestamp()
    logger.info(f'[{timestamp}] User {user_id} (@{username}): {action}')


def validate_bot_token(token: str) -> bool:
    """
    Basic validation for Telegram bot token format
    
    Args:
        token: Bot token string
        
    Returns:
        True if token format is valid, False otherwise
    """
    if not token or not isinstance(token, str):
        return False
    
    # Basic format check: should contain ':' and be reasonably long
    parts = token.split(':')
    if len(parts) != 2:
        return False
    
    # First part should be numeric (bot ID)
    if not parts[0].isdigit():
        return False
    
    # Second part should be alphanumeric
    if not parts[1].isalnum():
        return False
    
    return True
