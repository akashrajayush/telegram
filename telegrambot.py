from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6343317349:AAH9JxKZrPbScNPSnaLFKAFGlXAmygv_2CA'
BOT_USERNAME: Final = '@chait24_bot'


#commands

async def start_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, how are you')

async def help_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am chaitanya, please type something so that i can respond!')

async def custom_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom text')


#responces
    
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'how are you ?'
    
    if 'i am fine' in processed:
        return 'how was are day ?'
    
    if 'fine' in processed:
        return 'nice to hear that'
    
    return 'samajh nahi aaya :('

#checking if the bot is in the grp chat or in the pvt chat

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
        
    else:
        response: str = handle_response(text)

    print('bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if name == 'main':
    print('starting bot.....')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #error
    app.add_error_handler(error)

    #update
    print('polling...')
    app.run_polling(poll_interval=5)
