import pygame # type: ignore #biblioteca de jogo
#python -m pip install pygame
pygame.init()#para abrir o pygame
#aplicar a dimensão da janela
#dimensão do plano de fundo
window = pygame.display.set_mode([1280,720])
#aplicar o título da janela/display
pygame.display.set_caption("Futebol SENAI")
#criar variáveis para as imagens:
campo = pygame.image.load("img/campo.png")
jogador1 = pygame.image.load("img/player1.png")
jogador1_y = 310
jogador1_y_moveup = False
jogador1_y_movedown = False
jogador2 = pygame.image.load("img/player2.png")
jogador2_y = 310
bola = pygame.image.load("img/ball.png")
menu = pygame.image.load("img/bar.png")
score1 = 0
score1_img = pygame.image.load("img/0.png")
score2 = 0
score2_img = pygame.image.load("img/0.png")
#colocar a bolinha para rolar
bola_x = 617
bola_y = 337
bola_dir = -5
bola_dir_y = 1

def draw():
    #Carregar as imagens
    window.blit(campo,(0,0))
    window.blit(jogador1,(50, jogador1_y))
    window.blit(jogador2,(1150,jogador2_y))
    window.blit(bola,(bola_x,bola_y))
    window.blit(score1_img,(500,50))
    window.blit(score2_img,(710,50))


def move_bola():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    #Para mover a bola para a direita
    bola_x += bola_dir
    bola_y += bola_dir_y

    if bola_x < 123:
        if jogador1_y < bola_y + 23:
            if jogador1_y + 146> bola_y:
                bola_dir *= -1

    if bola_x > 1100:
        if jogador2_y < bola_y + 23:
            if jogador2_y + 146> bola_y:
                bola_dir *= -1

    if bola_y > 685:
        bola_dir_y *= -1
    elif bola_y <= 0:
        bola_dir_y *= -1

    if bola_x < -50: #se a bola sair da tela
        bola_x = 617
        bola_y = 337
        bola_dir *= -1
        bola_dir_y *= -1
    elif bola_x > 1320:
        bola_x = 617
        bola_y = 337
        bola_dir *= -1
        bola_dir_y *= -1


def move_jogador():
    global jogador1_y
    if jogador1_y_moveup:
        jogador1_y-=5
    else:
        jogador1_y_moveup
        jogador1_y+=0
    if jogador1_y_movedown:
        jogador1_y+=5
    else:
        jogador1_y_movedown
        jogador1_y+=0

    if jogador1_y<=0:
        jogador1_y = 0
    elif jogador1_y >= 575:
        jogador1_y = 575

def move_jogador2():
    global jogador2_y
    jogador2_y = bola_y
    
#para manter a janela aberta:
loop = True
while loop:
    for event in pygame.event.get():
        #se ele clicar em X irá fechar
        if event.type == pygame.QUIT:
            loop = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jogador1_y_moveup = True
            if event.key == pygame.K_s:
                jogador1_y_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                jogador1_y_moveup = False
            if event.key == pygame.K_s:
                jogador1_y_movedown = False
    draw()
    move_bola()
    move_jogador()
    move_jogador2()
    #quero que atualize sempre quando houver mudança
    pygame.display.update()
pygame.quit()#para fechar o pygame