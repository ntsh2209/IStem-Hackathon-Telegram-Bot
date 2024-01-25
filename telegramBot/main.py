from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final='6328869836:AAHp1n8c0BFJsfzNJ9Pdr0WFJImFhcjToLM'
BOT_USERNAME: Final='@istem_career_buddy_bot'

#Command
async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, Thanks for chatting with me , I am your career buddy')
    
async def help_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, Type something to respond')
    
async def custom_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, This is custom command')
    
#Responses
def handle_response(text:str)->str:
    processed: str=text.lower()
    if 'hello' in processed:
        return 'hey there'
    if 'how are you' in processed:
        return 'I am good'
    if 'hi' in processed:
        return 'hi, I am your career buddy'
    return 'I didnt understand your response.'


async def handle_message(update: Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str=update.message.chat.type
    text: str=update.message.text
    
    print(f'User({update.message.chat.id}) in  {message_type}: "{text}"')
    
    if message_type=='group':
        if BOT_USERNAME in text:
            new_text:str=text.replace(BOT_USERNAME,'').strip()
            response:str=handle_response(new_text)
        else:
            return
        
    else:
        response: str=handle_response(text)
        
    print('Bot:',response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__=='__main__':
    print('Starting bot...')
    app=Application.builder().token(TOKEN).build()
    
    #command
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    #Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Error
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=3)
            
            