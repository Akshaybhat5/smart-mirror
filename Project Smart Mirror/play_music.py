import pygame
from pygame import mixer


pygame.init()
mixer.init()
def play_audio(prompt = "Happy"):
    pygame.init()
    pygame.mixer.init()
    if prompt == "happy":
        pygame.mixer.music.load('/home/akshay/Desktop/practise/Project Smart Mirror/songs/these_are_the_days.mp3')
        pygame.mixer.music.play()
        
    elif prompt == "sad":
        pygame.mixer.music.load('/home/akshay/Desktop/practise/Project Smart Mirror/songs/sad_emotion_song.mp3')
        pygame.mixer.music.play()
        
    elif prompt == "angry":
        pygame.mixer.music.load('/home/akshay/Desktop/practise/Project Smart Mirror/songs/y2mate (mp3cut.net).mp3')
        pygame.mixer.music.play()
        
    elif prompt == "neutral":
        pygame.mixer.music.load('/home/akshay/Desktop/practise/Project Smart Mirror/songs/sabrina.mp3')
        pygame.mixer.music.play()
        
    elif prompt == "surprise":
        pygame.mixer.music.load('/home/akshay/Desktop/practise/Project Smart Mirror/songs/way_down_we_go.mp3')
        pygame.mixer.music.play()
             
    else:
        pygame.mixer.music.load( '/home/akshay/Desktop/practise/Project Smart Mirror/songs/Normal.mp3')
        pygame.mixer.music.play()
            
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
            # break
    
          
# play_audio()
pygame.mixer.quit()
pygame.quit()


