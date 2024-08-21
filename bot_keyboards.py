from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton('Все вакансии в PDF', callback_data='like_pdf'))
    kb.add(InlineKeyboardButton('Все вакансии в Excel', callback_data='like_xlsx'))
    kb.add(InlineKeyboardButton('Напишу название вакансии', callback_data='like_vacancy'))
    return kb