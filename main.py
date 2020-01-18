import telebot
from os import listdir
from os.path import isfile, join
import datetime
import time

TOKEN = '991120396:AAHnUOcjzCLs4s7V5yIcmdMGnQ-FurXGy60'
TORRENTS_DIRECTORY_PATH = 'F:\\torrent_test_folder'
CHANNEL_NAME = '-1001417096822'

TIME_DELTA = 5


_files = []
bot = telebot.TeleBot(TOKEN)

#telebot.apihelper.proxy = 'http://orbtl.s5.opennetwork.cc:999/'

def main():
    _files = get_files_list()

    while True:
        time.sleep(TIME_DELTA)
        files = get_files_list()
        print(files)
        newFiles = list(set(_files).symmetric_difference(set(files)))
        if len(newFiles) > 0:
            _files = files
            for file in newFiles:
                print(file)
                message = 'Файл ' + file + ' успешно добавлен!'
                bot.send_message(CHANNEL_NAME, message)
    return

def get_files_list():
    files = listdir(TORRENTS_DIRECTORY_PATH)
    for file in files:
        if not isfile(TORRENTS_DIRECTORY_PATH + "\\" + file):
            files.remove(file)
    return files

if __name__ == '__main__':
    main()