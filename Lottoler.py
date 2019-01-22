import copy
import pygame
import random

BALL_NAME = ["Ball1", "Ball2", "Ball3", "Ball4", "Ball5", "Ball6", "Ball7", "Ball8", "Ball9"]
WND_SIZE = (800, 600)
ballDict = {}

CHOSEN_BALL_DISPLAY_POSITION = \
    [
        [
            [0, 400], [80, 400], [160, 400], [240, 400], [320, 400], [400, 400], [480, 400], [560, 400], [640, 400], [720, 400]
        ],
        [
            [0, 500], [80, 500], [160, 500], [240, 500], [320, 500], [400, 500], [480, 500], [560, 500], [640, 500], [720, 500]
        ]
    ]

SMALL = 0
LARGE = 1

class Ball:
    def __init__(self, texture, identity):
        self.texture = texture  # ball is the number of the ball in the ball_list
        self.position = [0, 0]    # position is a list containing its x/y coordinate
        self.identity = identity  # identity is the number on the ball texture
        self.drawn = False
        self.stored_pos = [0, 0]


    def switch_pos(self):
        self.position = [random.randint(0, 720), random.randint(0, 446)]


    def label_number(self, font):
        label_surface = font.render(str(self.identity), True, (0, 0, 0))
        return label_surface


def initializeBalls(ball_list):        # Initialize the ball objects
    ballDict["Ball1"] = Ball(ball_list[0], 1)
    ballDict["Ball2"] = Ball(ball_list[1], 2)
    ballDict["Ball3"] = Ball(ball_list[2], 3)
    ballDict["Ball4"] = Ball(ball_list[3], 4)
    ballDict["Ball5"] = Ball(ball_list[4], 5)
    ballDict["Ball6"] = Ball(ball_list[5], 6)
    ballDict["Ball7"] = Ball(ball_list[6], 7)
    ballDict["Ball8"] = Ball(ball_list[7], 8)
    ballDict["Ball9"] = Ball(ball_list[8], 9)
    return ballDict


def choose_number(screen, cursor, ball_list, ballDict, label_font, label_font_small, chosen_number, chosen_ball):
    while True:
        ball_num = random.randint(0, 8)
        current_event = pygame.event.poll()
        while True:
            label = random.randint(1, 30)
            if not (label in chosen_number):
                if len(chosen_number) == 30:
                    print("All number has been chosen")
                    return 0
                break
        ballDict[BALL_NAME[ball_num]].identity = label
        refresh(screen, cursor, ball_list, ballDict, ballDict[BALL_NAME[ball_num]].label_number(label_font), ball_num)
        if current_event.type == pygame.KEYDOWN:
            chosen_number.append(label)
            current_ball_texture = [ballDict[BALL_NAME[ball_num]].texture[0].copy(), ballDict[BALL_NAME[ball_num]].texture[1].copy()]
            #if len(chosen_ball) > 20:  # auto shuffle if the threshold is full
                #chosen_ball = chosen_ball[-19:]
            chosen_ball.append(Ball(current_ball_texture, ballDict[BALL_NAME[ball_num]].identity))
            refresh_chosen_ball(screen, chosen_ball, label_font_small)
            print(chosen_number)
            break
        if current_event.type == pygame.QUIT:
            exit()


def createWnd(sizeTurple):
    screen_main = pygame.display.set_mode(sizeTurple, 0 ,32)
    screen_main.fill((0, 0, 0))
    return screen_main

def refresh(screen, cursor, ball_list, ballDict, text_surface, ball_number):
    screen.fill((0, 0, 0))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x -= cursor.get_width() / 2
    mouse_y -= cursor.get_height() / 2

    current_ball = ball_list[ball_number][1].copy()
    current_ball_label_pos = (ball_list[ball_number][1].get_width() /2 - text_surface.get_width() / 2, ball_list[ball_number][1].get_height() / 2 - text_surface.get_height() / 2)
    current_ball.blit(text_surface, current_ball_label_pos)
    screen.blit(current_ball, (WND_SIZE[0] / 2 - ball_list[ball_number][1].get_width() / 2, WND_SIZE[1] / 3 - ball_list[ball_number][1].get_height() / 2))

    pygame.display.update(pygame.rect.Rect((0, 0), (800, 400)))

    return 0


def refresh_chosen_ball(screen, chosen_ball_list, label_font):
    chosen_ball_rect = pygame.rect.Rect((0, 400), (800, 600))
    screen.fill((0, 0, 0), chosen_ball_rect)
    for chosen_ball_object in chosen_ball_list:
        if chosen_ball_object.drawn is not True:
            if (chosen_ball_list.index(chosen_ball_object) + 1) <= 10:
                x_pos = chosen_ball_list.index(chosen_ball_object)
            else:
                x_pos = (chosen_ball_list.index(chosen_ball_object) + 1) - (((chosen_ball_list.index(chosen_ball_object) + 1) // 10) * 10) - 1
            if chosen_ball_list.index(chosen_ball_object) == 0:
                y_pos = 0
            elif ((chosen_ball_list.index(chosen_ball_object)) // 10) % 2 == 1:
                y_pos = 1
            else:
                y_pos = 0

            chosen_ball_object.stored_pos = [x_pos, y_pos]

            text_surface = chosen_ball_object.label_number(label_font)

            current_ball_label_pos = (chosen_ball_object.texture[0].get_width() / 2 - text_surface.get_width() / 2,
                                      chosen_ball_object.texture[0].get_height() / 2 - text_surface.get_height() / 2)

            chosen_ball_object.texture[0].blit(text_surface, current_ball_label_pos)
            chosen_ball_object.drawn = True

        screen.blit(chosen_ball_object.texture[0], CHOSEN_BALL_DISPLAY_POSITION[chosen_ball_object.stored_pos[1]][chosen_ball_object.stored_pos[0]])

    pygame.display.update(chosen_ball_rect)

    return 0


def loadResource():
    machine = pygame.image.load("Texture/machine.png").convert_alpha()
    ball1_texture = pygame.image.load("Texture/ball1.png").convert_alpha()
    ball2_texture = pygame.image.load("Texture/ball2.png").convert_alpha()
    ball3_texture = pygame.image.load("Texture/ball3.png").convert_alpha()
    ball4_texture = pygame.image.load("Texture/ball4.png").convert_alpha()
    ball5_texture = pygame.image.load("Texture/ball5.png").convert_alpha()
    ball6_texture = pygame.image.load("Texture/ball6.png").convert_alpha()
    ball7_texture = pygame.image.load("Texture/ball7.png").convert_alpha()
    ball8_texture = pygame.image.load("Texture/ball8.png").convert_alpha()
    ball9_texture = pygame.image.load("Texture/ball9.png").convert_alpha()
    ball1_big_texture = pygame.image.load("Texture/ball1_big.png").convert_alpha()
    ball2_big_texture = pygame.image.load("Texture/ball2_big.png").convert_alpha()
    ball3_big_texture = pygame.image.load("Texture/ball3_big.png").convert_alpha()
    ball4_big_texture = pygame.image.load("Texture/ball4_big.png").convert_alpha()
    ball5_big_texture = pygame.image.load("Texture/ball5_big.png").convert_alpha()
    ball6_big_texture = pygame.image.load("Texture/ball6_big.png").convert_alpha()
    ball7_big_texture = pygame.image.load("Texture/ball7_big.png").convert_alpha()
    ball8_big_texture = pygame.image.load("Texture/ball8_big.png").convert_alpha()
    ball9_big_texture = pygame.image.load("Texture/ball9_big.png").convert_alpha()

    ball_list = [[ball1_texture, ball1_big_texture], [ball2_texture, ball2_big_texture], [ball3_texture, ball3_big_texture], [ball4_texture, ball4_big_texture], [ball5_texture, ball5_big_texture], [ball6_texture, ball6_big_texture], [ball7_texture, ball7_big_texture], [ball8_texture, ball8_big_texture], [ball9_texture,ball9_big_texture]]# List containing all texture of balls, for the sake of choosing
    cursor = pygame.image.load("Texture/cursor.png").convert_alpha()
    label_font = pygame.font.SysFont("Arial", 48)
    label_font_small = pygame.font.SysFont("Arial", 16)
    return machine, ball_list, cursor, label_font, label_font_small


def main():
    global ballDict

    pygame.init()

    screen_main = createWnd(WND_SIZE)

    chosen_number = []

    chosen_ball = []

    machine, ball_list, cursor, label_font, label_font_small = loadResource()

    initializeBalls(ball_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choose_number(screen_main, cursor, ball_list, ballDict, label_font, label_font_small, chosen_number, chosen_ball)


if __name__ == '__main__':
    main()
