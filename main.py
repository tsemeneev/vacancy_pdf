import pandas as pd
from telebot import TeleBot, StateMemoryStorage
from bot_keyboards import start_keyb
from src.make_pdf import create_html_file, del_html_pdf

storage = StateMemoryStorage()

bot = TeleBot(token="TOKEN", state_storage=storage)


@bot.message_handler(commands=["start"])
def start(message):
  text = "Привет 👋, я бот для поиска вакансий.\nНапиши мне название вакансии и я пришлю pdf файл с подходящими вакансиями.\n"
  text += "Также, я могу прислать файл со всеми вакансиями в excel или pdf формате.\n"
  text += "Нажми на кнопку ниже и выбери какой формат вам подходит"
  bot.send_message(message.chat.id, text, reply_markup=start_keyb())
  
@bot.callback_query_handler(func=lambda call: call.data == 'like_pdf')
def like_pdf(call):
  bot.send_document(call.message.chat.id, open('train_data.pdf', 'rb'))
  
@bot.callback_query_handler(func=lambda call: call.data == 'like_xlsx')
def like_xlsx(call):
  df = pd.read_excel('./xlsx/template.xlsx')
  df.sort_values(by='Категория', inplace=True)
  file_name_path = './xlsx/Актуальные вакансии(РаботаВахтой).xlsx'
  df.to_excel(file_name_path, index=False)
  bot.send_document(call.message.chat.id, open(file_name_path, 'rb'))
  
@bot.callback_query_handler(func=lambda call: call.data == 'like_vacancy')
def like_vacancy(call):
  bot.send_message(call.message.chat.id, "Отлично 👍 Напишите название вакансии")
  bot.set_state(call.from_user.id, 'vacancy', call.message.chat.id)
  
  
@bot.message_handler(func=lambda message: bot.get_state(message.from_user.id, message.chat.id) == 'vacancy', content_types=['text'])
def vacancy(message):
  bot.send_message(message.chat.id, 'Принято✅ Собираю вакансии...')
  id = message.chat.id
  vacancy = message.text
  created = create_html_file(vacancy=vacancy, id=id)
  if created:
    bot.send_document(message.chat.id, open(f'./pdf/{id}/Список вакансий (РаботаВахтой).pdf', 'rb'))
    del_html_pdf(id)
    bot.delete_state(message.from_user.id, message.chat.id)
  else:
    bot.send_message(message.chat.id, 'Не нашел вакансий по такому запросу')
    del_html_pdf(id)


