import pygame
time = str(input("Qual time você torce? "))

pygame.mixer.init()
pygame.init()

def TitulosCorinthians():
    print("- 6 Campeonatos Brasileiro;")
    print("- 30 Campeonatos Paulista;")
    print("- 1 Libertadores da América;")
    print("- 2 Mundiais de Clubes da Fifa.")

def TitulosPalmeiras():
    print("- 5 Campeonatos Brasileiro;")
    print("- 23 Campeonatos Paulista;")
    print("- 3 Libertadores da América;")

def TitulosSaoPaulo():
    print("- 6 Campeonatos Brasileiro;")
    print("- 21 Campeonatos Paulista;")
    print("- 3 Libertadores da América;")
    print("- 3 Mundiais de Clubes da Fifa.")

def TitulosSantos():
    print("- 5 Campeonatos Brasileiro;")
    print("- 22 Campeonatos Paulista;")
    print("- 3 Libertadores da América;")





if time == "Corinthians":
    pygame.mixer.music.load('corinthianstheme.mp3')
    pygame.mixer.music.play()
    TitulosCorinthians()
    pygame.event.wait()
elif time == "Palmeiras":
    pygame.mixer.music.load('palmeirastheme.mp3')
    pygame.mixer.music.play()
    TitulosPalmeiras()
    pygame.event.wait()
elif time == "Sao Paulo":
    pygame.mixer.music.load('saopaulotheme.mp3')
    pygame.mixer.music.play()
    TitulosSaoPaulo()
    pygame.event.wait()
elif time == "Santos":
    pygame.mixer.music.load('santostheme.mp3')
    pygame.mixer.music.play()
    TitulosSantos()
    pygame.event.wait()
else:
    print("Desculpe, ainda não temos o hino do seu time em nosso banco de dados ):")
