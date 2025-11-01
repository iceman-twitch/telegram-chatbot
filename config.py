"""
Configuration file for Telegram Bot
Load environment variables and bot settings
"""

import os
import sys
from dotenv import load_dotenv
from utils.helper import validate_bot_token

# Load environment variables from .env file
load_dotenv()

# ==================== REQUIRED SETTINGS ====================

# Bot Token from BotFather (REQUIRED)
# Get your token from: https://t.me/BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print('❌ ERROR: BOT_TOKEN not found in environment variables!')
    print('Please create a .env file with your bot token.')
    print('Example: BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz')
    sys.exit(1)

# Validate bot token format
if not validate_bot_token(BOT_TOKEN):
    print('❌ ERROR: Invalid BOT_TOKEN format!')
    print('Token should be in format: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz')
    sys.exit(1)

# ==================== OPTIONAL SETTINGS ====================

# Debug mode (shows more detailed logs)
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Admin user IDs (comma-separated list)
# Example: ADMIN_IDS=123456789,987654321
ADMIN_IDS_STR = os.getenv('ADMIN_IDS', '')
ADMIN_IDS = [int(id.strip()) for id in ADMIN_IDS_STR.split(',') if id.strip().isdigit()]

# Bot username (optional, will be auto-detected if not set)
BOT_USERNAME = os.getenv('BOT_USERNAME', '')

# ==================== API SETTINGS ====================

# Add your external API keys and endpoints here
# Example: Weather API, Database API, etc.

# Example API configurations
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))  # Timeout in seconds
API_RETRY_COUNT = int(os.getenv('API_RETRY_COUNT', '3'))  # Number of retries

# Custom API Key (if you need to integrate with external services)
CUSTOM_API_KEY = os.getenv('CUSTOM_API_KEY', '')

# Database URL (if using a database)
DATABASE_URL = os.getenv('DATABASE_URL', '')

# ==================== FEATURE FLAGS ====================

# Enable/disable specific features
ENABLE_GROUP_CHAT = os.getenv('ENABLE_GROUP_CHAT', 'True').lower() == 'true'
ENABLE_PRIVATE_CHAT = os.getenv('ENABLE_PRIVATE_CHAT', 'True').lower() == 'true'
ENABLE_PHOTO_HANDLING = os.getenv('ENABLE_PHOTO_HANDLING', 'True').lower() == 'true'
ENABLE_DOCUMENT_HANDLING = os.getenv('ENABLE_DOCUMENT_HANDLING', 'True').lower() == 'true'

# ==================== LOGGING SETTINGS ====================

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FILE = os.getenv('LOG_FILE', 'bot.log')

# ==================== MESSAGE SETTINGS ====================

# Maximum message length before truncation
MAX_MESSAGE_LENGTH = int(os.getenv('MAX_MESSAGE_LENGTH', '4096'))

# Command prefix (default is /)
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '/')

# ==================== CONFIGURATION SUMMARY ====================

def print_config_summary():
    """Print a summary of the current configuration"""
    print('\n' + '='*50)
    print('🤖 BOT CONFIGURATION SUMMARY')
    print('='*50)
    print(f'Bot Token: {"✅ Configured" if BOT_TOKEN else "❌ Not Set"}')
    print(f'Debug Mode: {"✅ Enabled" if DEBUG else "❌ Disabled"}')
    print(f'Admin Count: {len(ADMIN_IDS)}')
    print(f'Group Chat: {"✅ Enabled" if ENABLE_GROUP_CHAT else "❌ Disabled"}')
    print(f'Private Chat: {"✅ Enabled" if ENABLE_PRIVATE_CHAT else "❌ Disabled"}')
    print(f'Log Level: {LOG_LEVEL}')
    print('='*50 + '\n')


if DEBUG:
    print_config_summary()
