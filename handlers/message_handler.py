"""
Message Handler Module
Handles all non-command messages (text, photos, documents, etc.)
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def handle_private_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle messages received in private chat (DM)
    This function processes all text messages that are not commands
    """
    user = update.effective_user
    message_text = update.message.text
    
    logger.info(f'Received private message from {user.id} ({user.username}): {message_text}')
    
    # TODO: Add your custom logic here for processing private messages
    # You can check for specific keywords, patterns, etc.
    
    # Example: Check for specific keywords
    if 'hello' in message_text.lower() or 'hi' in message_text.lower():
        await update.message.reply_text(
            f'Hello {user.first_name}! 👋\n'
            'How can I help you today?'
        )
    elif 'help' in message_text.lower():
        await update.message.reply_text(
            'You can use /help to see all available commands!'
        )
    else:
        # Default response for private messages
        await update.message.reply_text(
            f'I received your message: "{message_text}"\n\n'
            'Use /help to see available commands.'
        )


async def handle_group_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle messages received in group chats
    """
    user = update.effective_user
    message_text = update.message.text
    chat = update.effective_chat
    
    logger.info(f'Received group message from {user.id} ({user.username}) in chat {chat.id}: {message_text}')
    
    # TODO: Add your custom logic for group messages
    # For example: respond only when mentioned, moderate content, etc.
    
    # Example: Respond only if bot is mentioned
    if context.bot.username and f'@{context.bot.username}' in message_text:
        await update.message.reply_text(
            f'Hello {user.first_name}! You mentioned me in the group.'
        )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle photos sent to the bot
    """
    user = update.effective_user
    photo = update.message.photo[-1]  # Get highest resolution photo
    
    logger.info(f'Received photo from {user.id} ({user.username}), file_id: {photo.file_id}')
    
    # TODO: Add your custom logic for handling photos
    # You can download, process, or analyze images
    
    await update.message.reply_text(
        f'📸 Thanks for the photo, {user.first_name}!\n'
        f'Photo size: {photo.width}x{photo.height}\n'
        f'File size: {photo.file_size} bytes'
    )


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle documents/files sent to the bot
    """
    user = update.effective_user
    document = update.message.document
    
    logger.info(f'Received document from {user.id} ({user.username}): {document.file_name}')
    
    # TODO: Add your custom logic for handling documents
    
    await update.message.reply_text(
        f'📄 Received your file: <b>{document.file_name}</b>\n'
        f'Size: {document.file_size} bytes\n'
        f'Type: {document.mime_type}',
        parse_mode='HTML'
    )


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Main handler for text messages
    Routes to appropriate handler based on chat type
    """
    chat_type = update.effective_chat.type
    
    if chat_type == 'private':
        await handle_private_message(update, context)
    elif chat_type in ['group', 'supergroup']:
        await handle_group_message(update, context)
    else:
        logger.warning(f'Received message from unknown chat type: {chat_type}')
