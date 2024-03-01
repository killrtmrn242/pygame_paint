from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

cursor_image = pygame.image.load("cursor.png").convert_alpha()
sound = pygame.mixer.Sound('pencil-write-with-a-pencil.wav')
soundb = pygame.mixer.Sound('click-button.wav')

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel,
                             (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win, WHITE, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))
        for j in range(COLS+1):
            pygame.draw.line(win, WHITE, (j * PIXEL_SIZE, 0),
                             (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw_cursor(cursor_image):
    cursor_img_rect.center = pygame.mouse.get_pos()
    pygame.draw.circle(WIN, drawing_color, cursor_img_rect.center, BRUSH_SIZE)
    WIN.blit(cursor_image, cursor_img_rect)

def draw(win, grid, buttons, cursor_image):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    draw_cursor(cursor_image)

    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE



    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = RED

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 25, 50, BLACK),
    Button(40, button_y, 25, 50, RED),
    Button(70, button_y, 25, 50, GREEN),
    Button(100, button_y, 25, 50, BLUE),
    Button(130, button_y, 25, 50, LIGHT_BLUE),
    Button(160, button_y, 25, 50, ORANGE),
    Button(190, button_y, 25, 50, PURPLE),
    Button(220, button_y, 25, 50, YELLOW),
    Button(270, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(330, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(390, button_y, 50, 50, WHITE, "BG", BLACK),
    Button(450, button_y, 50, 50, WHITE, "Save", BLACK)
]

pygame.mouse.set_visible(False)
cursor_img_rect = cursor_image.get_rect()
grid_color = WHITE
soundb.set_volume(0.05)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
        if event.type == pygame.MOUSEBUTTONUP:
            sound.stop()
        elif event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if y < 600:
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
    if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            # try except block to define a drawble area
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    soundb.play()
                    if not button.clicked(pos):
                        continue

                    try:
                        if button.text == "Clear":
                            grid_color = BG_COLOR
                            grid = init_grid(ROWS, COLS, grid_color)
                            drawing_color = current_color
                        if button.text == "Erase":
                            drawing_color = grid_color
                        if button.text == "BG":
                            grid_color = current_color
                            grid = init_grid(ROWS, COLS, grid_color)
                        if button.text == "Save":
                            rect = pygame.Rect(0, 0, 600, 600)
                            sub = WIN.subsurface(rect)
                            pygame.image.save(sub, "screenshot.jpg")
                        elif button.text == None:
                            drawing_color = button.color
                            current_color = button.color
                    except NameError:
                        pass

    draw(WIN, grid, buttons, cursor_image)
pygame.quit()