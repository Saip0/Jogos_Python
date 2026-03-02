import pygame
from random import randint
from time import sleep
telas = {
    'NORMAL' : (800,800),
}

tamanho_tela = telas['NORMAL']
cores = {
    'preto' : (0,0,0),
    'verde' : (0,255,0),
    'vermelho' : (255,0,0),
    'cinza' : (128,128,128),
}
pygame.init()

tela = pygame.display.set_mode(telas['NORMAL'])
pygame.display.set_caption('DesvBlocks')

inicio_jogo = True
fim_do_jogo = False

#tamanho do jogador = 5% do tamanho da tela
tamanho_jogador = ((tamanho_tela[0])//100*5, (tamanho_tela[1])//100*5)
jogador = pygame.Rect(400,750,tamanho_jogador[0],tamanho_jogador[1])
velocidade_jogador = [5,5]

#blocos
tamanho_bloco = ((tamanho_tela[0]//100*5),(tamanho_tela[1]//100*5))
velocidade_bloco = [10,10]
quantidade_blocos = 40

def desenhar_jogo(bloco):
    tela.fill(cores['cinza'])
    pygame.draw.rect(tela, cores['preto'], jogador)
    for i in range(quantidade_blocos):
        pygame.draw.rect(tela, cores['vermelho'], bloco[i])

def armazenar_blocos():
    blocos = []
    for i in range(quantidade_blocos):
        posicao_blocox = randint(1,tamanho_tela[0]- tamanho_tela[0]//100*10)

        bloco = pygame.Rect(posicao_blocox, 0, tamanho_bloco[0], tamanho_bloco[1])
        blocos.append(bloco)

    return blocos

def cair_blocos(blocos):
    #1/17 proporção 1 velocidade 17 tempo
    tempo_de_queda = (tamanho_tela[1]*1.7)#estimativa de 3.4 para cada 5 de velocidade
    for i in range(1,quantidade_blocos):#Tempo De Queda = 3 segundos
        if pygame.time.get_ticks()//tempo_de_queda == i:
            blocos[i].y += velocidade_bloco[1]

            #if jogador.colliderect(blocos[i]):
             #   fim_do_jogo = True

            #if blocos[i].y > tamanho_tela[1]:
            #    blocos.remove(blocos[i])

def movimentos_jogador():
    teclado = pygame.key.get_pressed()
    if teclado[pygame.K_a] and jogador.x > 0:
        jogador.x -= velocidade_jogador[0]
    if teclado[pygame.K_d] and jogador.x < tamanho_tela[0] - tamanho_jogador[0]:
        jogador.x += velocidade_jogador[0]

blocos = armazenar_blocos()
clock = pygame.time.Clock()

while not fim_do_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_do_jogo = True

    for i in range(quantidade_blocos):
        if jogador.colliderect(blocos[i]):
            fim_do_jogo = True

    desenhar_jogo(blocos)
    cair_blocos(blocos)
    movimentos_jogador()

    clock.tick(60)
    pygame.display.flip()


    #for i in range(quantidade_blocos):
     #   if pygame.time.get_ticks()//1000 == i:
      #      print(i)
pygame.quit()
print("Fim De Jogo")
sleep(10)