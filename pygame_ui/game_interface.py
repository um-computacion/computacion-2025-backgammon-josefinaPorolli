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

    # Update the screen
    pygame.display.flip()

# Exit Pygame
pygame.quit()
sys.exit()