import pygame

from sys import exit
from os.path import join
from random import randrange, choice


# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Room")


LIGHT_GRAY = (200,200,200)

    # for input box

input_box = pygame.Rect(500, 650, 400, 100)
input_text = ""
input_active = False

def convert_mouse_pos_to_grid(mouse_pos, button_size=(50, 50)):
    x_pos = (mouse_pos[0] - mouse_pos[0] % button_size[0]) // button_size[0]
    y_pos = (mouse_pos[1] - mouse_pos[1] % button_size[1]) // button_size[1]
    return x_pos, y_pos


# function to display text
def display_text(text, font, color, pos):
    
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = pos
    screen.blit(text_surface, rect)


# display welcome message at opening of the game
def display_welcome(screen,fill_color):
    screen.fill(fill_color)
    WHITE = (255, 255, 255)
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 36)
    display_text(
        "Welcome to", font_large, WHITE, (screen_width // 2, screen_height // 2 - 50)
    )
    display_text(
        "Escape Room Game",
        font_medium,
        WHITE,
        (screen_width // 2,
        screen_height // 2 + 50),
    )
    display_text(
        "Press any key to Start",
        font_small,
        WHITE,
        (screen_width // 2,
        screen_height - 100),
    )



def stage1(mouse_grid_pos, level1_data, total_guesses):
    pillow_count = 5
    level_count = 1
    if level1_data is None:
        level1_data = {}
        tile_pos = [(5, 1), (7, 1), (5, 3), (7, 3)]
        vals = []
        while len(vals) != 3:
            random_number = randrange(2, 10)
            if random_number == pillow_count or random_number in vals:
                continue
            vals.append(random_number)
        vals.append(pillow_count)
        for pos in tile_pos:
            val = choice(vals)
            level1_data[pos] = str(val)
            vals.remove(val)
    click_val = level1_data.get(mouse_grid_pos)
    if click_val is not None:
        if click_val == str(pillow_count):
            print("player won")
            level_count = 2
        else:
            total_guesses -= 1
    if total_guesses < 0:
        print("You Lost")
        total_guesses = 0
        level1_data = None
    return level1_data, total_guesses,level_count


def stage2(input_text):
    
    questions = [
        "What is the capital of France?",
        "Which planet is known as the Red Planet?",
        "Who wrote 'Romeo and Juliet'?"
    ]
    correct_answers = [
        "Paris",
        "Mars",
        "William Shakespeare"
    ]
    
    for i, question in enumerate(questions):
        display_text(question,  pygame.font.Font(None, 36), (255,255,255), (300, 170 + i * 100))

    pygame.draw.rect(screen, LIGHT_GRAY, input_box, 2)
    display_text(input_text, pygame.font.Font(None, 36), (255,255,255), (input_box.x + 5, input_box.y + 5))
    

def draw( level_count, bg_image_data, level1_data, BLOCK_SIZE,input_data):
    screen.fill((0, 0, 0))


    if not level_count:
        display_welcome(screen, (139, 69, 19))
    else:
        screen.blit(bg_image_data[level_count], (0, 0)) 

    if level_count == 1 and level1_data is not None:
        for pos, val in level1_data.items():
            pos = pos[0] * BLOCK_SIZE[0], pos[1] * BLOCK_SIZE[1]
            rect = pygame.Rect(pos, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            display_text(
                val, pygame.font.Font(None, 36), (0, 0, 0), (pos[0] + 25, pos[1] + 25))
    elif level_count == 2:
        display_text("Solve the following questions to complete the game :-" ,   pygame.font.Font(None, 50) , (255,255,255),  (450,50))
        stage2(input_text)
        display_text(input_data[0],pygame.font.Font(None, 36), (255,255,255), input_data[2].topleft)
                  
    pygame.display.update()


def main(screen):
    screen_size = screen.get_size()

    clock = pygame.time.Clock()
    fps = 60

    # Background images
    image1 = pygame.image.load(join("Assets", "image1.jpg")).convert()
    image1 = pygame.transform.scale(image1, screen_size)
    image2 = pygame.image.load(join("Assets", "image.png")).convert()
    image2 = pygame.transform.scale(image2, screen_size)
    level_bg_data = {1: image1, 2: image2}
    

    BLOCK_SIZE = 50, 50
    level1_data = None
    total_guesses = 0
    level_count = 0
    run = True

    input_text = ""
    input_active = False
    input_data = [input_text,input_active,input_box]

    correct_answers = [
        "P",
        "M",
        "W"
    ]

    

    while run:
        mouse_grid_pos = -1, -1
        clock.tick(fps)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and not level_count:
                level_count += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_grid_pos = convert_mouse_pos_to_grid( pygame.mouse.get_pos(), BLOCK_SIZE)
                   
                   #check if mouse click is within input box
                if input_box.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN and level_count ==  2:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        # Check answer
                        if input_text.lower() in [answer.lower() for answer in correct_answers]:
                            print("Correct!")
                            # Handle correct answer logic (e.g., move to next stage)
                            level_count = 2
                        else:
                            print("Incorrect. Try again.")
                        input_text = ""  # Clear input box after submission
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]

                    else:
                        input_text += event.unicode
                    input_data[0] = input_text

        if level_count == 1:
            level1_data, total_guesses,level_count = stage1(
                mouse_grid_pos, level1_data, total_guesses
            )
        elif level_count == 2:
            stage2(input_text)
        print(input_text)
        draw( level_count, level_bg_data, level1_data, BLOCK_SIZE,input_data)
        
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
