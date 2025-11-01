"""
Command Handler Module
Handles all bot commands like /start, /help, /list, etc.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /start command
    Sent when user first starts the bot or sends /start
    """
    user = update.effective_user
    chat_type = update.effective_chat.type
    
    logger.info(f'User {user.id} ({user.username}) sent /start in {chat_type} chat')
    
    welcome_message = f"""
🤖 <b>Welcome {user.first_name}!</b>

I'm your Telegram bot assistant.
Use /help to see what I can do for you.
"""
    
    await update.message.reply_text(welcome_message, parse_mode='HTML')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /help command
    Shows list of available commands
    """
    user = update.effective_user
    chat_type = update.effective_chat.type
    
    logger.info(f'User {user.id} ({user.username}) sent /help in {chat_type} chat')
    
    help_text = """
📋 <b>Available Commands:</b>

/start - Start the bot and see welcome message
/help - Show this help message
/status - Check if bot is online and operational
/list - Get a list of available features
/echo <text> - Echo your message back
/info - Get your chat and user information

<i>More commands coming soon!</i>
"""
    
    await update.message.reply_text(help_text, parse_mode='HTML')


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /status command
    Shows bot operational status
    """
    user = update.effective_user
    logger.info(f'User {user.id} ({user.username}) sent /status')
    
    await update.message.reply_text('✅ <b>Bot Status:</b> Online and operational!', parse_mode='HTML')


async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /list command
    This is where you can add your custom list functionality
    """
    user = update.effective_user
    chat_type = update.effective_chat.type
    
    logger.info(f'User {user.id} ({user.username}) sent /list in {chat_type} chat')
    
    # TODO: Add your custom list logic here
    # Example: listing items, users, data, etc.
    
    list_message = """
📝 <b>Available Items:</b>

1. Feature A
2. Feature B
3. Feature C

<i>This is a placeholder. Add your custom list logic in handlers/command_handler.py</i>
"""
    
    await update.message.reply_text(list_message, parse_mode='HTML')


async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /echo command
    Echoes back the user's message
    """
    user = update.effective_user
    logger.info(f'User {user.id} ({user.username}) sent /echo')
    
    if context.args:
        message = ' '.join(context.args)
        await update.message.reply_text(f'🔊 You said: <b>{message}</b>', parse_mode='HTML')
    else:
        await update.message.reply_text(
            '⚠️ Please provide a message to echo.\n\n'
            '<b>Usage:</b> /echo <i>your message here</i>',
            parse_mode='HTML'
        )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /info command
    Shows user and chat information
    """
    user = update.effective_user
    chat = update.effective_chat
    
    logger.info(f'User {user.id} ({user.username}) sent /info')
    
    info_message = f"""
ℹ️ <b>Your Information:</b>

<b>User ID:</b> <code>{user.id}</code>
<b>Username:</b> @{user.username if user.username else 'Not set'}
<b>First Name:</b> {user.first_name}
<b>Last Name:</b> {user.last_name if user.last_name else 'Not set'}

<b>Chat Type:</b> {chat.type}
<b>Chat ID:</b> <code>{chat.id}</code>
"""
    
    await update.message.reply_text(info_message, parse_mode='HTML')
