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




def convert_mouse_pos_to_grid(mouse_pos, button_size=(50, 50)):
    x_pos = (mouse_pos[0] - mouse_pos[0] % button_size[0]) // button_size[0]
    y_pos = (mouse_pos[1] - mouse_pos[1] % button_size[1]) // button_size[1]
    return x_pos, y_pos


# function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = (x, y)
    screen.blit(text_surface, rect)


# display welcome message at opening of the game
def display_welcome(fill_color):
    screen.fill(fill_color)
    WHITE = (255, 255, 255)
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 36)
    display_text(
        "Welcome to", font_large, WHITE, screen_width // 2, screen_height // 2 - 50
    )
    display_text(
        "Escape Room Game",
        font_medium,
        WHITE,
        screen_width // 2,
        screen_height // 2 + 50,
    )
    display_text(
        "Press any key to Start",
        font_small,
        WHITE,
        screen_width // 2,
        screen_height - 100,
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
        total_guesses = 3
        level1_data = None
    return level1_data, total_guesses,level_count


def stage2(image2,x,y):
    
    display_text("Who are you?",font_small,WHITE,8,2)
    

def draw(screen, level_count, bg_image_data, level1_data, BLOCK_SIZE):
    screen.fill((0, 0, 0))
    if not level_count:
        display_welcome((139, 69, 19))
    else:
        screen.blit(bg_image_data[level_count], (0, 0))
    if level_count == 1 and level1_data is not None:
        for pos, val in level1_data.items():
            pos = pos[0] * BLOCK_SIZE[0], pos[1] * BLOCK_SIZE[1]
            rect = pygame.Rect(pos, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            display_text(
                val, pygame.font.Font(None, 36), (0, 0, 0), pos[0] + 25, pos[1] + 25
            )
    pygame.display.update()


def main(screen):
    screen_size = screen.get_size()

    clock = pygame.time.Clock()
    fps = 60

    # Background images
    image1 = pygame.image.load(join("Assets", "Image1.jpg")).convert()
    image1 = pygame.transform.scale(image1, screen_size)
    image2 = pygame.image.load(join("Assets", "BgImage.jpg")).convert()
    image2 = pygame.transform.scale(image2, screen_size)
    level_bg_data = {1: image1, 2: image2}
    

    BLOCK_SIZE = 50, 50
    level1_data = None
    total_guesses = 3
    x = y =0
    level_count = 0
    run = True
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
                mouse_grid_pos = convert_mouse_pos_to_grid(
                    pygame.mouse.get_pos(), BLOCK_SIZE
                )
        if level_count == 1:
            level1_data, total_guesses,level_count = stage1(
                mouse_grid_pos, level1_data, total_guesses
            )
        elif level_count == 2:
            stage2(image2,x,y)
        draw(screen, level_count, level_bg_data, level1_data, BLOCK_SIZE)
        
    pygame.quit()
    exit()


if __name__ == "__main__":
    main(screen)
