from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import sys
import telebot
import uuid

# Запуск браузера
driver = webdriver.Firefox(executable_path='/home/alexandr/geckodriver')
driver.get('https://web.telegram.org/#/login')


# Функция поиска html-элемента по классу
def try_except_by_class(class_name):
    try:
        temp_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
    except:
        driver.quit()
        sys.exit()
    return temp_elem


# Инициализация данных
input_temp = input('Если залогинились, введите "ДА": ')
if input_temp != 'ДА':
    driver.quit()
    sys.exit()
public_nick = input('Введите название группы, которую заспамить: ')
with open('bots.txt', 'r') as f:
    bots = f.read().splitlines()

# Добавление ботов в введенную группу (~ секунд 40)
for b in bots:
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'im_dialogs_search_field'))
        )
    except:
        driver.quit()
        sys.exit()
    search_field[0].clear()
    search_field[0].send_keys(b)
    time.sleep(1)
    search_field[0].send_keys(Keys.ENTER)
    header = try_except_by_class('tg_head_peer_title')
    header.click()
    section_link = try_except_by_class('md_modal_section_link')
    section_link.click()
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'im_dialogs_search_field'))
        )
    except:
        driver.quit()
        sys.exit()
    search_field[1].clear()
    search_field[1].send_keys(public_nick)
    search_field[1].send_keys(Keys.ENTER)
    try:
        btn_ok = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-md-primary'))
        )
    except:
        driver.quit()
        sys.exit()
    btn_ok.click()
    modal_action = try_except_by_class('md_modal_action_close')
    modal_action.click()

# Переход в нужный диалог
dialog = driver.find_elements_by_css_selector('.im_dialog_peer span')
for d in dialog:
    if d.text == public_nick:
        d.click()
        break

# Отправка в диалог команды, запускающей боты
dialog_input = driver.find_element_by_class_name('composer_rich_textarea')
dialog_input.send_keys('/letsgo')
dialog_input.send_keys(Keys.ENTER)

# Инициализация 15 ботов
bot = telebot.TeleBot('810415763:AAHFCYhdkJ2MOGbhTWq_0SXX0JH_IKACumI')
bot1 = telebot.TeleBot('933180839:AAHS7mPltO7uMPs5eFaYLr72HLcLykjlbuE')
bot2 = telebot.TeleBot('964206245:AAHe3PxrsczqpIMeMnUmLhKGJcTUeO0dgko')
bot3 = telebot.TeleBot('961944767:AAFiJtrmXoK85otPRFPqRs3hIaftuCxNKCE')
bot4 = telebot.TeleBot('942754188:AAFoSHT2A3wq50N9yNBY0NFER8zj4F6Dhk0')
bot5 = telebot.TeleBot('913818086:AAHtKGjg-JakPs_v8Hqi-KCWLShJFyqclUM')
bot6 = telebot.TeleBot('941193765:AAFQZQ7zYOW8loqRnhPusU6GLXO4W0YJQLA')
bot7 = telebot.TeleBot('892581458:AAFI4hh0JHRUO8kszIkuThVfsKvzTvUllQE')
bot8 = telebot.TeleBot('943857918:AAFb5qP4SCM8_T4ZTop-TizB-I8y29vCiN4')
bot9 = telebot.TeleBot('950446599:AAFlZjMcfomrJ3GxwW-e66Juzdqhs0X2vLY')
bot10 = telebot.TeleBot('986097691:AAFJ33T4R9q3Ut2Td2wNzLLimJvTGOK41os')
bot11 = telebot.TeleBot('966300031:AAHtnrIUnZsS5E54JlmdQyjMnyErUG_NR08')
bot12 = telebot.TeleBot('818750285:AAHFlR3TXNcLd90AXlqSL12SiDHHZ7iOGiE')
bot13 = telebot.TeleBot('978585062:AAGOjHjdOJ8rCEIkQNbvQ5uPbriUzQh7OZc')
bot14 = telebot.TeleBot('903316279:AAEdid0yGMYCm1Qxy0c4bBWuJLoumufFgPA')


# Декоратор добавляющий действие на ивент введения "/letsgo"
@bot.message_handler(commands=['letsgo'])
@bot1.message_handler(commands=['letsgo'])
@bot2.message_handler(commands=['letsgo'])
@bot3.message_handler(commands=['letsgo'])
@bot4.message_handler(commands=['letsgo'])
@bot5.message_handler(commands=['letsgo'])
@bot6.message_handler(commands=['letsgo'])
@bot7.message_handler(commands=['letsgo'])
@bot8.message_handler(commands=['letsgo'])
@bot9.message_handler(commands=['letsgo'])
@bot10.message_handler(commands=['letsgo'])
@bot11.message_handler(commands=['letsgo'])
@bot12.message_handler(commands=['letsgo'])
@bot13.message_handler(commands=['letsgo'])
@bot14.message_handler(commands=['letsgo'])
def start_message(message):
    for _ in range(100000):
        bot.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot1.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot2.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot3.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot4.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot5.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot6.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot7.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot8.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot9.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot10.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot11.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot12.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot13.send_message(message.chat.id, str(uuid.uuid4())[:16])
        bot14.send_message(message.chat.id, str(uuid.uuid4())[:16])


# Запуск бота
bot.polling()
bot1.polling()
bot2.polling()
bot3.polling()
bot4.polling()
bot5.polling()
bot6.polling()
bot7.polling()
bot8.polling()
bot9.polling()
bot10.polling()
bot11.polling()
bot12.polling()
bot13.polling()
bot14.polling()
