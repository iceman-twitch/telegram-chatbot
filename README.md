# Telegram Chatbot

A Python-based Telegram bot with extensible command handling.

## Setup Instructions

### 1. Create Virtual Environment
Run the following command to create a Python 3.9 virtual environment:
```bash
env.bat
```

### 2. Activate Environment and Install Dependencies
```bash
env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Bot Token
1. Copy `.env.example` to `.env`
2. Get your bot token from [@BotFather](https://t.me/BotFather) on Telegram
3. Add your token to the `.env` file:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   ```

### 4. Run the Bot
Use the test script which automatically activates the environment, runs the bot, and deactivates after:
```bash
test.bat
```

## Available Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Show available commands
- `/status` - Check if bot is running
- `/list` - Get a list of available features (customize this for your needs)
- `/echo <message>` - Echo your message back
- `/info` - Get your user and chat information

## Message Handling

The bot can handle:
- **Private messages** - Direct messages from users
- **Group messages** - Messages in group chats (responds when mentioned)
- **Photos** - Image files sent to the bot
- **Documents** - File uploads

All message handling can be customized in `handlers/message_handler.py`.

## Project Structure

```
telegram-chatbot/
├── handlers/                    # Message and command handlers
│   ├── __init__.py             # Handlers package initialization
│   ├── command_handler.py      # All bot commands (/start, /help, /list, etc.)
│   └── message_handler.py      # Text, photo, and document handlers
├── utils/                       # Utility functions
│   ├── __init__.py             # Utils package initialization
│   └── helper.py               # Helper functions (validation, formatting, etc.)
├── bot.py                       # Main bot entry point
├── config.py                    # Configuration and environment variables
├── requirements.txt             # Python dependencies
├── env.bat                      # Script to create virtual environment
├── test.bat                     # Script to run the bot
├── onefile.bat                  # Script to build standalone executable
├── .env.example                 # Example environment configuration
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Adding New Commands

To add a new command:

1. **Create the command handler** in `handlers/command_handler.py`:
```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /mycommand"""
    await update.message.reply_text('Response text')
```

2. **Export it** from `handlers/__init__.py`:
```python
from .command_handler import my_command
__all__ = [..., 'my_command']
```

3. **Register it** in `bot.py` inside the `setup_handlers()` function:
```python
application.add_handler(CommandHandler("mycommand", my_command))
```

## Customizing Message Handling

### For Private Messages
Edit `handle_private_message()` in `handlers/message_handler.py` to process messages received in private chats.

### For the /list Command
The `/list` command is ready for customization in `handlers/command_handler.py`. Add your custom logic there to display lists, menus, or data.

## Configuration Options

All configuration is managed through the `.env` file. Key settings include:

- `BOT_TOKEN` - Your Telegram bot token (required)
- `DEBUG` - Enable detailed logging
- `ADMIN_IDS` - Comma-separated list of admin user IDs
- `ENABLE_GROUP_CHAT` - Enable/disable group chat functionality
- `ENABLE_PRIVATE_CHAT` - Enable/disable private chat functionality
- `ENABLE_PHOTO_HANDLING` - Enable/disable photo processing
- `ENABLE_DOCUMENT_HANDLING` - Enable/disable document processing

See `.env.example` for all available options.

## Requirements

- Python 3.9
- python-telegram-bot 20.7
- python-dotenv 1.0.0

## License

See LICENSE file for details.
