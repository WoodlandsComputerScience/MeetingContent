import pygame
from pygame.locals import *
import sys
import time
import random


class Game:
    def __init__(self):
        # set window dimensions
        self.w = 750
        self.h = 500
        # initialize varibles
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"
        self.results = "Time: 0 Accuracy: 0 % WPM: 0"
        self.wpm = 0
        self.end = False
        # set location of text
        self.HEAD_C = (0, 213, 0)
        self.TEXT_C = (0, 213, 0)
        self.RESULT_C = (125, 213, 125)

        # start pygame window
        pygame.init()
        self.open_img = pygame.image.load(
            "type-speed-open.png")  # background image
        self.open_img = pygame.transform.scale(
            self.open_img, (self.w, self.h))  # scale (resize) background image

        self.bg = pygame.image.load("background.jpg")
        self.bg = pygame.transform.scale(
            self.bg, (750, 500))  # (self.w,self.h)

        # set dimensions of window (display) using the varibles set above
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Typing Speed Test") # set window name

    # Draw text
    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize) # use default font and set it to
                                             # `fsize` (which is an argument from the function)
        text = font.render(msg, 1, color) # set colour of the text
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update() # render (update) the window with the new text

    # Checks the "edit distance" of a word to see how accurate the entered word was
    def edit_distance(self, str1, str2, m, n):
        if(m == 0):
            return n
        if(n == 0):
            return m
        if(str1[m-1] == str2[n-1]):
            return self.edit_distance(str1, str2, m-1, n-1)
        return 1 + min(
            self.edit_distance(str1, str2, m, n-1),
            self.edit_distance(str1, str2, m-1, n),
            self.edit_distance(str1, str2, m-1, n-1))

    # Randomly selects a sentence from `sentences.txt`
    def get_sentence(self):
        f = open("sentences.txt").read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    # Displays the results after the test is finished
    def show_results(self, screen):
        if(not self.end):
            # calculate time
            self.total_time = time.time() - self.time_start

            # calculate accuracy
            count = 0 # correct letters?
            for i, c in enumerate(self.word): # returns a list of pairs of each
                                              #   ie. [(0,self.word[0]),(1,self.word[1])]
                try:
                    if(self.input_text[i] == c):
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100 # calculates accuracy as a percentage

            # calculate wpm
            self.wpm = len(self.input_text)*60/(5*self.total_time) # NOTE: a "word" when calculating WPM is 5 strokes (Shift counts I think?/idk ask Max)
            self.end = True
            # Results text
            self.results = "Time: " + str(round(self.total_time, 2)) + " secs   Mistakes: " + str(self.edit_distance(
                self.word, self.input_text, len(self.word), len(self.input_text))) + "   WPM: " + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load("icon.png")
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.w/2 - 75, self.h - 140))
            # add "Reset" text
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

            pygame.display.update() # rerender window

    # Run Game
    def run(self):
        self.reset_game() # "reset" the state of the test/game

        self.running = True
        while(self.running):
            # Start timing when you start typing.
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text,
                           274, 26, (250, 250, 250))
            if(self.input_text == ''):
                self.time_start = time.time()
            if(not self.end):
                pygame.draw.rect(self.screen, (0, 0, 0), (300, 301, 150, 30))
                self.draw_text(self.screen, str(
                    round(time.time() - self.time_start, 2)), 315, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if(event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        self.running = False
                if(event.type == pygame.MOUSEBUTTONUP):
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if(x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                    # position of reset box
                    if(x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()
                if(event.type == pygame.KEYDOWN):
                    if(self.active and not self.end):
                        if(event.key == pygame.K_RETURN):
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(
                                self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True
                        elif(event.key == pygame.K_BACKSPACE):
                            self.input_text = self.input_text[:-1]
                        else:
                            if(self.input_text == 0):
                                self.time_start = time.time()
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)
        pygame.quit()

    # Reset state of the test/game
    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # get random sentence
        self.word = self.get_sentence()
        if(not self.word):
            self.reset_game()

        # draw heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        # draw the sentence string
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

        pygame.display.update()


Game().run()
