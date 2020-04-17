import ptbot
import os
from pytimeparse import parse

TOKEN = os.getenv("TOKEN")
CHAT_ID = '730219355'  # подставьте свой ID

def notify():
  bot.send_message(CHAT_ID, 'Время вышло')
  print('Время вышло')

def notify_progress(secs_left, new_text, time, new_time):
  new_text = bot.update_message(CHAT_ID, new_text, "Осталось секунд: " + str(secs_left))
  new_time = bot.update_message(CHAT_ID, new_time, render_progressbar(time, secs_left))

def reply(text):
  time = parse(text)
  start_message_id = bot.send_message(CHAT_ID, 'Таймер запущен на {0} секунд'.format(time))
  start_progress = bot.send_message(CHAT_ID, render_progressbar(time, time))
  bot.create_countdown(time, notify_progress, new_text = start_message_id, time = time, new_time = start_progress)
  bot.create_timer(time, notify)

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

bot = ptbot.Bot(TOKEN)
bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
bot.reply_on_message(reply)

bot.run_bot()