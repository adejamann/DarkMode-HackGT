import pygame

import random

pygame.init()
compScore = 0
playerScore = 0


screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Rock Paper Scissor ")

background_image = pygame.image.load('blue.png').convert()
font = pygame.font.Font('SunnyspellsRegular.otf', 33)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 235, 193))
play_message2 = font.render("Pick you Weapon to start playing", True, (255, 235, 193))

score_font = pygame.font.Font('SunnyspellsRegular.otf', 25)
user_score_message = score_font.render("Your Score:" + str(playerScore), True, (255, 235, 193))
comp_score_message = score_font.render("Comp Score:" + str(compScore), True, (255, 235, 193))


button_rock = pygame.image.load('button_rock.png')
button_paper = pygame.image.load('button_paper.png')
button_scissor = pygame.image.load('button_scissor.png')

rock_rect = button_rock.get_rect(topleft=(25, 350))
paper_rect = button_rock.get_rect(topleft=(235, 350))
scissor_rect = button_rock.get_rect(topleft=(475, 350))

rock = pygame.image.load('rock.png')
paper = pygame.image.load('paper.png')
scissor = pygame.image.load('scissor.png')
weapon_choices = [rock, paper, scissor]



is_start = False
user_weapon = None
comp_weapon = None
defeats = None
is_user_weapon = False

is_show_weapon = False


def pick_weapon(user_weapon_index):
    global is_start, user_weapon, comp_weapon, is_user_weapon, is_show_weapon, defeats
    is_start = True
    user_weapon = weapon_choices[user_weapon_index]
    is_user_weapon = True
    is_show_weapon = False
    comp_weapon_index = random.randint(0, 2)
    comp_weapon = weapon_choices[comp_weapon_index]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if rock_rect.collidepoint(event.pos):
                pick_weapon(0)
                if comp_weapon == user_weapon:
                    playerScore+=0
                    compScore+=0
                elif comp_weapon == paper :
                    playerScore+=0
                    compScore+=1
                elif comp_weapon == scissor :
                    playerScore+=1
                    compScore+=0

            elif paper_rect.collidepoint(event.pos):
                pick_weapon(1)
                if comp_weapon == user_weapon:
                    playerScore+=0
                    compScore+=0
                elif comp_weapon == rock:
                    playerScore+=1
                    compScore+=0
                elif comp_weapon == scissor :
                    playerScore+=0
                    compScore+=1

            elif scissor_rect.collidepoint(event.pos):
                pick_weapon(2)
                if comp_weapon == user_weapon:
                    playerScore+=0
                    compScore+=0
                elif comp_weapon == paper :
                    playerScore+=1
                    compScore+=0
                elif comp_weapon == rock:
                    playerScore+=0
                    compScore+=1

    score_font = pygame.font.Font('SunnyspellsRegular.otf', 25)
    user_score_message = score_font.render("Your Score:" + str(playerScore), True, (255, 235, 193))
    comp_score_message = score_font.render("Comp Score:" + str(compScore), True, (255, 235, 193))

        

    screen.blit(background_image, (0, 0))
    screen.blit(user_score_message, (130, 20))
    screen.blit(comp_score_message, (500, 20))

    if is_start is False:
        screen.blit(play_message, (180, 170))
        screen.blit(play_message2, (200, 200))

    if is_show_weapon:
        screen.blit(user_weapon, (120, 90))
        screen.blit(comp_weapon, (420, 90))

    if is_user_weapon:
        is_show_weapon = True

    screen.blit(button_rock, rock_rect)
    screen.blit(button_paper, paper_rect)
    screen.blit(button_scissor, scissor_rect)
    # if playerScore == 3:
    #     is_show_weapon = False
    #     win_message = font.render("You Win!", True, (255, 235, 193))
    #     screen.blit(win_message, (250, 170))
    #     playerScore = 0
    #     compScore = 0
    # elif compScore == 3:
    #     is_show_weapon = False
    #     lose_message = font.render("You Lose!", True, (255, 235, 193))
    #     screen.blit(lose_message, (250, 170))
    #     playerScore = 0
    #     compScore = 0


    pygame.display.update()
