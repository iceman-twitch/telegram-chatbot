"""
Telegram Chatbot - Main Entry Point
A modular Telegram bot with organized command and message handlers
"""

import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Import configuration
import config

# Import handlers
from handlers import (
    start_command,
    help_command,
    status_command,
    list_command,
    echo_command,
    info_command,
    handle_text_message,
    handle_photo,
    handle_document
)

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, config.LOG_LEVEL),
    handlers=[
        logging.FileHandler(config.LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f'Update {update} caused error: {context.error}', exc_info=context.error)
    
    # Optionally notify user of error
    if update and update.effective_message:
        await update.effective_message.reply_text(
            '⚠️ An error occurred while processing your request.\n'
            'Please try again later or contact support.'
        )


def setup_handlers(application: Application) -> None:
    """
    Set up all command and message handlers
    """
    logger.info('Setting up handlers...')
    
    # ==================== COMMAND HANDLERS ====================
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(CommandHandler("echo", echo_command))
    application.add_handler(CommandHandler("info", info_command))
    
    # ==================== MESSAGE HANDLERS ====================
    
    # Handle text messages (non-commands)
    if config.ENABLE_PRIVATE_CHAT or config.ENABLE_GROUP_CHAT:
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message)
        )
    
    # Handle photos
    if config.ENABLE_PHOTO_HANDLING:
        application.add_handler(
            MessageHandler(filters.PHOTO, handle_photo)
        )
    
    # Handle documents
    if config.ENABLE_DOCUMENT_HANDLING:
        application.add_handler(
            MessageHandler(filters.Document.ALL, handle_document)
        )
    
    # ==================== ERROR HANDLER ====================
    application.add_error_handler(error_handler)
    
    logger.info('✅ All handlers set up successfully!')


def main() -> None:
    """
    Start the bot
    """
    logger.info('='*60)
    logger.info('🚀 Starting Telegram Bot...')
    logger.info('='*60)
    
    # Print configuration summary if debug mode is enabled
    if config.DEBUG:
        config.print_config_summary()
    
    try:
        # Create the Application
        application = Application.builder().token(config.BOT_TOKEN).build()
        
        # Set up all handlers
        setup_handlers(application)
        
        # Start the bot
        logger.info('✅ Bot is now running and listening for messages...')
        logger.info('Press Ctrl+C to stop the bot')
        logger.info('='*60)
        
        # Run the bot until stopped
        application.run_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True  # Ignore messages sent while bot was offline
        )
        
    except Exception as e:
        logger.error(f'❌ Fatal error occurred: {e}', exc_info=True)
        raise
    finally:
        logger.info('='*60)
        logger.info('🛑 Bot stopped')
        logger.info('='*60)


if __name__ == '__main__':
    main()
