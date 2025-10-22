import pygame
import sys

# Initialize Pygame
pygame.init()

# Define the resolution
WIDTH = 1280
HEIGHT = 720

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BACKGAMMON")

BACKGROUND_COLOR = ("#6F1A07")
BOARD_MAIN_COLOR = ("#F2D398")
POINT1_COLOR = ("#4C5760")
POINT2_COLOR = ("#A8763E")
BLACK_CHECKER_COLOR = ("#2B2118")
WHITE_CHECKER_COLOR = ("#F7F3E3")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Margins
MARGIN = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Exit also with esc
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Fill the background
    screen.fill(BACKGROUND_COLOR)
    
    # Calculate areas with margins
    total_area = pygame.Rect(MARGIN, MARGIN, WIDTH - 2*MARGIN, HEIGHT - 2*MARGIN)

    # Divide into left (2/3) and right (1/3)
    left_width = (WIDTH - 2*MARGIN) * 2 // 3
    right_width = (WIDTH - 2*MARGIN) - left_width

    # Left quadrant (2/3 of WIDTH)
    board_square = pygame.Rect(
        MARGIN, 
        MARGIN, 
        left_width, 
        HEIGHT - 2*MARGIN
    )

    # Right quadrant (1/3 of WIDTH)
    right_width = (WIDTH - 2*MARGIN) - left_width
    players_control_square = pygame.Rect(
        MARGIN + left_width, 
        MARGIN, 
        right_width,
        HEIGHT - 2*MARGIN
    )

    # Divide the right quadrant into 2 equal parts (top and bottom)
    HEIGHT_player_control = (HEIGHT - 2*MARGIN) // 2
    
    # Mini superior square for black player control
    black_player_control = pygame.Rect(
        MARGIN + left_width, 
        MARGIN, 
        right_width, 
        HEIGHT_player_control
    )
    
    # Mini inferior square for white player control
    white_player_control = pygame.Rect(
        MARGIN + left_width, 
        MARGIN + HEIGHT_player_control, 
        right_width, 
        HEIGHT_player_control
    )

    # Draw the quadrants with different colors for visualization
    pygame.draw.rect(screen, BOARD_MAIN_COLOR, board_square)
    pygame.draw.rect(screen, BACKGROUND_COLOR, black_player_control)
    pygame.draw.rect(screen, BACKGROUND_COLOR, white_player_control)

    # Draw borders for better visualization
    pygame.draw.rect(screen, BLACK, board_square, 2)
    pygame.draw.rect(screen, BLACK, black_player_control, 2)
    pygame.draw.rect(screen, BLACK, white_player_control, 2)

    # BACKGAMMON BOARD
    board_margin = 20  # Margen interno del tablero
    board_inner = pygame.Rect(
        board_square.left + board_margin,
        board_square.top + board_margin,
        board_square.width - 2 * board_margin,
        board_square.height - 2 * board_margin
    )

    # Divide the board in the middle to differ left and right squares
    board_center_x = board_inner.left + board_inner.width // 2
    
    # Create the 24 points (triangles)
    point_width = board_inner.width // 12  # Width
    point_height = board_inner.height // 2  # Height

    # Font for numbers of each point
    font = pygame.font.SysFont('Arial', 14, bold=True)

    # Draw points and numbers

    # Upper left quadrant (points 13-18) - pointing DOWN
    for i in range(6):
        point_number = 13 + i
        point_rect = pygame.Rect(
            board_inner.left + i * point_width,
            board_inner.top,
            point_width,
            point_height
        )
        color = POINT1_COLOR if i % 2 == 0 else POINT2_COLOR
        # Triangle pointing down
        pygame.draw.polygon(screen, color, [
            (point_rect.left, point_rect.top),
            (point_rect.right, point_rect.top),
            (point_rect.left + point_rect.width // 2, point_rect.bottom)
        ])
        # Numbers above the points
        number_text = font.render(str(point_number), True, BLACK)
        text_rect = number_text.get_rect(center=(point_rect.centerx, board_inner.top - 10))
        screen.blit(number_text, text_rect)

    # Upper right quadrant (points 19-24) - pointing DOWN
    for i in range(6):
        point_number = 19 + i
        point_rect = pygame.Rect(
            board_center_x + i * point_width,
            board_inner.top,
            point_width - 2,
            point_height
        )
        color = POINT1_COLOR if i % 2 == 0 else POINT2_COLOR
        # Triangle pointing down
        pygame.draw.polygon(screen, color, [
            (point_rect.left, point_rect.top),
            (point_rect.right, point_rect.top),
            (point_rect.left + point_rect.width // 2, point_rect.bottom)
        ])
        # Numbers above the points
        number_text = font.render(str(point_number), True, BLACK)
        text_rect = number_text.get_rect(center=(point_rect.centerx, board_inner.top - 10))
        screen.blit(number_text, text_rect)

    # Lower left quadrant (points 12-7) - pointing UP
    for i in range(6):
        point_number = 12 - i
        point_rect = pygame.Rect(
            board_inner.left + i * point_width,
            board_inner.top + board_inner.height // 2,
            point_width - 2,
            point_height
        )
        color = POINT2_COLOR if i % 2 == 0 else POINT1_COLOR
        # Triangle pointing UP
        pygame.draw.polygon(screen, color, [
            (point_rect.left, point_rect.bottom),
            (point_rect.right, point_rect.bottom),
            (point_rect.left + point_rect.width // 2, point_rect.top)
        ])
        # Numbers below the points
        number_text = font.render(str(point_number), True, BLACK)
        text_rect = number_text.get_rect(center=(point_rect.centerx, board_inner.bottom + 10))
        screen.blit(number_text, text_rect)

    # Lower right quadrant (points 6-1) - pointing UP
    for i in range(6):
        point_number = 6 - i
        point_rect = pygame.Rect(
            board_center_x + i * point_width,
            board_inner.top + board_inner.height // 2,
            point_width - 2,
            point_height
        )
        color = POINT2_COLOR if i % 2 == 0 else POINT1_COLOR
        # Triangle pointing UP
        pygame.draw.polygon(screen, color, [
            (point_rect.left, point_rect.bottom),
            (point_rect.right, point_rect.bottom),
            (point_rect.left + point_rect.width // 2, point_rect.top)
        ])
        # Numbers below the points
        number_text = font.render(str(point_number), True, BLACK)
        text_rect = number_text.get_rect(center=(point_rect.centerx, board_inner.bottom + 10))
        screen.blit(number_text, text_rect)

    # Soft center line
    pygame.draw.line(screen, BLACK, 
                    (board_center_x, board_inner.top), 
                    (board_center_x, board_inner.bottom), 2)

    # Inner board border
    pygame.draw.rect(screen, BLACK, board_inner, 1)

    # SQUARES FOR CONTROLS IN THE RIGHT SQUARE
    font = pygame.font.SysFont('Arial', 26, bold=True) # Set the font

    # Black player control
    black_text = font.render("BLACK PLAYER", True, WHITE)
    black_text_rect = black_text.get_rect(centerx=black_player_control.centerx, top=black_player_control.top + 10)
    screen.blit(black_text, black_text_rect)

    font = pygame.font.SysFont('Arial', 20, bold=True) # Set the font

    black_eaten_text = font.render("EATEN CHECKERS: ", True, WHITE)
    black_eaten_text_rect = black_eaten_text.get_rect(centerx=black_player_control.left + 120, top=black_player_control.top + 60)
    screen.blit(black_eaten_text, black_eaten_text_rect)

    black_eaten_text = font.render("HOUSE: ", True, WHITE)
    black_eaten_text_rect = black_eaten_text.get_rect(centerx=black_player_control.left + 120, top=black_player_control.top + 100)
    screen.blit(black_eaten_text, black_eaten_text_rect)

    font = pygame.font.SysFont('Arial', 26, bold=True) # Set the font
    
    # White player control
    white_text = font.render("WHITE PLAYER", True, WHITE)
    white_text_rect = white_text.get_rect(centerx=white_player_control.centerx, top=white_player_control.top + 10)
    screen.blit(white_text, white_text_rect)

    font = pygame.font.SysFont('Arial', 20, bold=True) # Set the font

    white_eaten_text = font.render("EATEN CHECKERS: ", True, WHITE)
    white_eaten_text_rect = white_eaten_text.get_rect(centerx=white_player_control.left + 120, top=white_player_control.top + 60)
    screen.blit(white_eaten_text, white_eaten_text_rect)

    white_house_text = font.render("HOUSE: ", True, WHITE)
    white_house_text_rect = white_house_text.get_rect(centerx=white_player_control.left + 120, top=white_player_control.top + 100)
    screen.blit(white_house_text, white_house_text_rect)

    # Update the screen
    pygame.display.flip()

# Exit Pygame
pygame.quit()
sys.exit()