import config
from pygame import mixer # Load the required library
import time
import logging
from mutagen.mp3 import MP3
import os
import datetime
from display_message import Displaying_message


# Getting the alarm length of the alarm mp3
def get_alarm_length():
    audio = MP3(config.MP3_LOCATION)
    alarm_length = audio.info.length
    return alarm_length

# Playing alarm
def play_alarm():
    logging.info("Alarm started at {}".format(os.times()))
    mixer.init()
    mixer.music.load(config.MP3_LOCATION)
    mixer.music.play()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    while True:
        # Getting the hour and minute so that we can know when to ring the alarm
        current_time_hour, current_time_minute = datetime.datetime.now().hour, datetime.datetime.now().minute
        logging.info("Current time is {}:{}".format(current_time_hour,current_time_minute))

        #print(type(current_time_hour), type(config.TIME_OF_ALARM.split(":")[0]), current_time_minute, config.TIME_OF_ALARM.split(":")[1])

        if current_time_hour is int(config.TIME_OF_ALARM.split(":")[0]) and current_time_minute is int(config.TIME_OF_ALARM.split(":")[1]):
            break

        time.sleep(30)

    # Getting the length of the mp3 file which is the alarm
    alarm_length = get_alarm_length()

    # Sounding the alarm
    play_alarm()

    # Displaying the message to be displayed
    displaying_message_obj = Displaying_message(config.MESSAGE_TO_DISPLAY)
    displaying_message_obj.start()



    # Playing the alarm
    time.sleep(alarm_length)
