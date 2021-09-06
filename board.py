import pygame

class Slot:
    def __init__(self, surface, x, y, size) -> None:
        self.surface = surface
        self.slot = pygame.Rect(x, y, size, size)

        self.default_color = (212, 212, 212)
        self.hover_color = (170, 170, 170)
        self.color = self.default_color
        
        self.color_red = (255, 121, 121)
        self.color_blue = (121, 121, 255)

        self.blue = False
        self.red = False

        self.clicked = False

    def hover(self):
        mx, my = pygame.mouse.get_pos()

        if self.slot.collidepoint(mx, my):
            self.color = self.hover_color
        else:
            self.color = self.default_color

    def pressed(self):
        mx, my = pygame.mouse.get_pos()
        if self.slot.collidepoint(mx, my) and pygame.mouse.get_pressed()[0] and not self.clicked:
            return True

    def change_color(self):
        if self.blue:
            self.color = self.color_blue
        if self.red:
            self.color = self.color_red

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.slot, 5)

    def update(self):
        self.draw()
        self.hover()
        self.change_color()

class Board:
    def __init__(self, surface, surface_w, surface_h) -> None:
        self.screen = surface
        self.screen_width = surface_w
        self.screen_height = surface_h

        self.slot_size = 90
        self.slot_offset = 50

        self.slot1 = Slot(self.screen, self.screen_width/2-self.slot_size-self.slot_offset, self.screen_height/2-self.slot_offset-self.slot_size, self.slot_size)
        self.slot2 = Slot(self.screen, self.screen_width/2-self.slot_size/2, self.screen_height/2-self.slot_offset-self.slot_size, self.slot_size)
        self.slot3 = Slot(self.screen, self.screen_width/2+self.slot_offset, self.screen_height/2-self.slot_offset-self.slot_size, self.slot_size)

        self.slot4 = Slot(self.screen, self.screen_width/2-self.slot_size-self.slot_offset, self.screen_height/2-self.slot_size/2, self.slot_size)
        self.slot5 = Slot(self.screen, self.screen_width/2-self.slot_size/2, self.screen_height/2-self.slot_size/2, self.slot_size)
        self.slot6 = Slot(self.screen, self.screen_width/2+self.slot_offset, self.screen_height/2-self.slot_size/2, self.slot_size)

        self.slot7 = Slot(self.screen, self.screen_width/2-self.slot_size-self.slot_offset, self.screen_height/2+self.slot_offset, self.slot_size)
        self.slot8 = Slot(self.screen, self.screen_width/2-self.slot_size/2, self.screen_height/2+self.slot_offset, self.slot_size)
        self.slot9 = Slot(self.screen, self.screen_width/2+self.slot_offset, self.screen_height/2+self.slot_offset, self.slot_size)

        self.turn_amount = 0
        self.player_turn = 'blue'

        self.font = pygame.font.Font('assets/misc/Roboto-Thin.ttf', 64)

        self.game_over = False

    def turn(self):
        if self.slot1.pressed():
            self.sound('click')
            self.slot1.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot1.blue = True
            if self.player_turn == 'red':
                self.slot1.red = True

        if self.slot2.pressed():
            self.sound('click')
            self.slot2.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot2.blue = True
            if self.player_turn == 'red':
                self.slot2.red = True

        if self.slot3.pressed():
            self.sound('click')
            self.slot3.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot3.blue = True
            if self.player_turn == 'red':
                self.slot3.red = True

        if self.slot4.pressed():
            self.sound('click')
            self.slot4.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot4.blue = True
            if self.player_turn == 'red':
                self.slot4.red = True

        if self.slot5.pressed():
            self.sound('click')
            self.slot5.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot5.blue = True
            if self.player_turn == 'red':
                self.slot5.red = True

        if self.slot6.pressed():
            self.sound('click')
            self.slot6.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot6.blue = True
            if self.player_turn == 'red':
                self.slot6.red = True

        if self.slot7.pressed():
            self.sound('click')
            self.slot7.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot7.blue = True
            if self.player_turn == 'red':
                self.slot7.red = True

        if self.slot8.pressed():
            self.sound('click')
            self.slot8.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot8.blue = True
            if self.player_turn == 'red':
                self.slot8.red = True

        if self.slot9.pressed():
            self.sound('click')
            self.slot9.clicked = True
            self.turn_amount += 1
            print(self.player_turn)
            if self.player_turn == 'blue':
                self.slot9.blue = True
            if self.player_turn == 'red':
                self.slot9.red = True

    def check_turn(self):
        if (self.turn_amount%2) == 0:
            self.player_turn = 'blue'
        else:
            self.player_turn = 'red'

    def slots(self):
        self.slot1.update()
        self.slot2.update()
        self.slot3.update()

        self.slot4.update()
        self.slot5.update()
        self.slot6.update()

        self.slot7.update()
        self.slot8.update()
        self.slot9.update()

    def check_board(self):
        # top row
        if self.slot1.blue and self.slot2.blue and self.slot3.blue:
            self.display_winner('blue')
        if self.slot1.red and self.slot2.red and self.slot3.red:
            self.display_winner('red')
        # left row
        if self.slot1.blue and self.slot4.blue and self.slot7.blue:
            self.display_winner('blue')
        if self.slot1.red and self.slot4.red and self.slot7.red:
            self.display_winner('red')
        # right row
        if self.slot3.blue and self.slot6.blue and self.slot9.blue:
            self.display_winner('blue')
        if self.slot3.red and self.slot6.red and self.slot9.red:
            self.display_winner('red')
        # bottom row
        if self.slot7.blue and self.slot8.blue and self.slot9.blue:
            self.display_winner('blue')
        if self.slot7.red and self.slot8.red and self.slot9.red:
            self.display_winner('red')
        # vertical middle row
        if self.slot2.blue and self.slot5.blue and self.slot8.blue:
            self.display_winner('blue')
        if self.slot2.red and self.slot5.red and self.slot8.red:
            self.display_winner('red')
        # horizontal middle row
        if self.slot4.blue and self.slot5.blue and self.slot6.blue:
            self.display_winner('blue')
        if self.slot4.red and self.slot5.red and self.slot6.red:
            self.display_winner('red')
        # left diagonal row
        if self.slot1.blue and self.slot5.blue and self.slot9.blue:
            self.display_winner('blue')
        if self.slot1.red and self.slot5.red and self.slot9.red:
            self.display_winner('red')
        # right diagonal row
        if self.slot3.blue and self.slot5.blue and self.slot7.blue:
            self.display_winner('blue')
        if self.slot3.red and self.slot5.red and self.slot7.red:
            self.display_winner('red')

    def reset_board(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.slot1.blue = False
            self.slot1.red = False
            self.slot1.clicked = False

            self.slot2.blue = False
            self.slot2.red = False
            self.slot2.clicked = False

            self.slot3.blue = False
            self.slot3.red = False
            self.slot3.clicked = False

            self.slot4.blue = False
            self.slot4.red = False
            self.slot4.clicked = False

            self.slot5.blue = False
            self.slot5.red = False
            self.slot5.clicked = False

            self.slot6.blue = False
            self.slot6.red = False
            self.slot6.clicked = False

            self.slot7.blue = False
            self.slot7.red = False
            self.slot7.clicked = False

            self.slot8.blue = False
            self.slot8.red = False
            self.slot8.clicked = False

            self.slot9.blue = False
            self.slot9.red = False
            self.slot9.clicked = False

            self.turn_amount = 0
    
    def display_winner(self, winner):
        if winner == 'blue':
            color_winner = self.slot1.color_blue
            winner = 'Blue'
        if winner == 'red':
            color_winner = self.slot2.color_red
            winner = 'Red'

        text = self.font.render((f'{winner} Wins'), True, color_winner)
        self.screen.blit(text, (70,-10))
        self.game_over = True
        
    def instructions(self):
        color = (170, 170, 170)
        font = pygame.font.Font('assets/misc/Roboto-Thin.ttf', 16)
        text = font.render(('--- Press SPACEBAR to Reset ---'), True, color)
        self.screen.blit(text, (self.screen_width/2-100-8, self.screen_height-32))

    def over(self):
        if self.game_over:
            self.slot1.clicked = True
            self.slot2.clicked = True
            self.slot3.clicked = True
            self.slot4.clicked = True
            self.slot5.clicked = True
            self.slot6.clicked = True
            self.slot7.clicked = True
            self.slot8.clicked = True
            self.slot9.clicked = True
            
            self.game_over = False

    def sound(self, sound):
        game_over = pygame.mixer.Sound('assets/audio/game_over.wav')
        click = pygame.mixer.Sound('assets/audio/click.wav')
        reset = pygame.mixer.Sound('assets/audio/reset.wav')

        if sound == 'game_over':
            game_over.play()
        if sound == 'click':
            click.play()
        if sound == 'reset':
            reset.play()

    def run(self):
        self.instructions()
        self.slots()
        self.turn()
        self.check_turn()
        self.check_board()
        self.reset_board()
        self.over()
