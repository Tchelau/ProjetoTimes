import pygame
time = str(input("Qual time você torce? "))

pygame.mixer.init()
pygame.init()

if time == "Corinthians":
    pygame.mixer.music.load('corinthianstheme.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
elif time == "Palmeiras":
    pygame.mixer.music.load('palmeirastheme.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
elif time == "São Paulo":
    pygame.mixer.music.load('saopaulotheme.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
elif time == "Santos":
    pygame.mixer.music.load('santostheme.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print("Desculpe, ainda não temos o hino do seu time em nosso banco de dados ):")
