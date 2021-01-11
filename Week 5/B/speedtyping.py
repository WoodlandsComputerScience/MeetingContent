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
        text_rect = text.get_rect(center=(self.w//2, y))
        screen.blit(text, text_rect)
        pygame.display.update() # render (update) the window with the new text

    # Checks the "edit distance" of a word to see how accurate the entered word was
    def edit_distance(self, str1, str2, m, n):
        # Create a table to store results of subproblems
        # "Dynamic Programming"
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

        # Fill d[][] in bottom up manner
        for i in range(m + 1):
            for j in range(n + 1):
                if(i == 0):
                    dp[i][j] = j # Min. operations = j
                elif(j == 0):
                    dp[i][j] = i # Min. operations = i
                elif(str1[i-1] == str2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                # If last character are different, consider all
                # possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],   # Insert
                                       dp[i-1][j],   # Remove
                                       dp[i-1][j-1]) # Replace
        return dp[m][n]

    # Randomly selects a sentence from `sentences.txt`
    def get_sentence(self):
        f = open("sentences.txt").read()
        sentences = f.split('\n') # changes all the individual lines
                                  # of the file into a list of sentences
        sentence = random.choice(sentences)
        return sentence

    # Displays the results after the test is finished
    def show_results(self, screen):
        if(not self.end):
            # calculate time
            self.total_time = time.time() - self.time_start

            # calculate accuracy
            # count = 0 # correct letters?
            # for i, c in enumerate(self.word): # returns a list of pairs of each
            #                                   #   ie. [(0,self.word[0]),(1,self.word[1])]
            #     try:
            #         if(self.input_text[i] == c):
            #             count += 1
            #     except:
            #         pass
            # self.accuracy = count/len(self.word)*100 # calculates accuracy as a percentage

            # calculate wpm
            self.wpm = len(self.input_text)*60/(5*self.total_time) # NOTE: a "word" when calculating WPM is 5 strokes (Shift counts I think?/idk ask Max)
            self.end = True
            # Results text
            self.results = "Time: " + str(round(self.total_time, 2)) + " secs   Mistakes: " + str(self.edit_distance(
                self.word, self.input_text, len(self.word), len(self.input_text))) + "   WPM: " + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load("icon.png")
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.w//2 - 75, self.h - 140))
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
                self.time_start = time.time() # resets the clock if there is no input
            if(not self.end):
                pygame.draw.rect(self.screen, (0, 0, 0), (300, 301, 150, 30))
                self.draw_text(self.screen, str(
                    round(time.time() - self.time_start, 2)), 315, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if(event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        self.running = False
                if(event.type == pygame.MOUSEBUTTONUP): # sets the input box active
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
                # track all "KEYDOWN" events
                if(event.type == pygame.KEYDOWN):
                    if(self.active and not self.end):
                        if(event.key == pygame.K_RETURN): #K_RETURN is the ENTER key
                            print(self.input_text)
                            self.show_results(self.screen) # show the results of the test when you're done typing
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
