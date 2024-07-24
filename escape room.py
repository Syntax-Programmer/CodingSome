import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")

#colors
WHITE = (255,255,255)
BROWN = (139,69,19)
# Fonts
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None,50)
font_small = pygame.font.Font(None, 36)

# function to display text
def display_text(text,font,color,x,y):
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)
#display welcome message at opening of the game
def display_welcome():
    screen.fill(BROWN)
    display_text("Welcome to",font_large,WHITE, screen_width//2, screen_height//2 - 50)
    display_text("Escape Room Game",font_medium,WHITE, screen_width//2, screen_height//2 +50)
    display_text("Press any key to Start",font_small,WHITE, screen_width//2, screen_height - 100)
    pygame.display.update()
display_welcome()

fps = 60
# Background images 
image1 = pygame.image.load("image for afajf.jpg")
image2 = pygame.image.load("background.jpg")


def main(screen):
    CLOCK = pygame.time.Clock()
    run = True
    while run :
        CLOCK.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()


            
def stage1():
    CLOCK = pygame.time.Clock()
    pillow_count = 5
    guess = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.k_RETURN:
                    guess = input(" enter your guess about the no of pillows")
                    try:
                        guess = int(guess)
                        if guess == pillow_count:
                            print(" correct ! you have won the stage 1 ")
                            stage2()
                        else:
                            print(" incoreect try again!")
                    except ValueError:
                        print(" invalid input. Please enter a number")
            screen.fill(image1)

            #display instructions
            guess_text = font_small.render("Press enter to submit your guess.",True,WHITE)
            screen.blit(guess_text, (50, height - 50))
        
            # Update the display
            pygame.display.flip()
            clock.tick(30)
            
def stage2():
    screen.fill(image2)
    
if __name__ == "__main__":
    main(screen)
    








