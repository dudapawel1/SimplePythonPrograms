# from playsound import playsound
import time
import pygame


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarmSound.mp3")
    pygame.mixer.music.play()


def alarm(seconds):
    time_elaspsed = 0

    print(CLEAR)
    while time_elaspsed < seconds:
        time_left = seconds - time_elaspsed
        seconds_left = int(time_left % 60)
        minutes_left = int(time_left // 60)
        print(
            f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d} minutes {seconds_left:02d} seconds")
        time.sleep(1)
        time_elaspsed += 1

    play_sound()
    # playsound("alarmSound.mp3")


minutes = int(input("Enter the number of minutes for the alarm: "))
seconds = int(input("Enter the number of seconds for the alarm: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
