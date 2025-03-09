from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7385946905:AAHGWwIl5iv9ogUokdhdY2DFpizBk8mvfew'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("MBBS 1st Year", callback_data='1st_year')],
        [InlineKeyboardButton("MBBS 2nd Year", callback_data='2nd_year')],
        [InlineKeyboardButton("MBBS 3rd Year", callback_data='3rd_year')],
        [InlineKeyboardButton("MBBS Final Year", callback_data='final_year')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select your MBBS Year:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data in ['1st_year', '2nd_year', '3rd_year', 'final_year']:
        keyboard = [
            [InlineKeyboardButton("Lectures", callback_data=f'{query.data}_lectures')],
            [InlineKeyboardButton("Notes", callback_data=f'{query.data}_notes')],
            [InlineKeyboardButton("Test Papers", callback_data=f'{query.data}_tests')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f'Select an option for {query.data.replace("_", " ").title()}:', reply_markup=reply_markup)

    elif '_lectures' in query.data or '_notes' in query.data or '_tests' in query.data:
        keyboard = [
            [InlineKeyboardButton("Marrow", url='https://www.marrow.com')],
            [InlineKeyboardButton("Prepladder", url='https://www.prepladder.com')],
            [InlineKeyboardButton("Egurukul", url='https://egurukul.com')],
            [InlineKeyboardButton("Cerebellum BTR & RR", url='https://cerebellum.com')],
            [InlineKeyboardButton("DAMS", url='https://damsdelhi.com')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f'Select a resource for {query.data.split("_")[1].title()} in {query.data.split("_")[0].replace("_", " ").title()}:', reply_markup=reply_markup)


if name == 'main':
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    application.run_polling()
