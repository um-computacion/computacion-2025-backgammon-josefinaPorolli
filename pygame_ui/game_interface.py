import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.backgammon_game import BackgammonGame

game = BackgammonGame() # Define the game
game.set_default_checkers() # Set the default positions of the checkers

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

def create_point_mapping(board_inner_rect, point_width, point_height):
    """Crea un diccionario que mapea puntos del board a coordenadas visuales"""
    point_mapping = {}
    board_inner = board_inner_rect
    
    # Puntos 13-18 (superior izquierda)
    for i in range(6):
        point_number = 13 + i
        point_mapping[str(point_number)] = {
            "rect": pygame.Rect(
                board_inner.left + i * point_width,
                board_inner.top,
                point_width,
                point_height
            ),
            "direction": "down"
        }
    
    # Puntos 19-24 (superior derecha)
    for i in range(6):
        point_number = 19 + i
        point_mapping[str(point_number)] = {
            "rect": pygame.Rect(
                board_inner.left + board_inner.width // 2 + i * point_width,
                board_inner.top,
                point_width,
                point_height
            ),
            "direction": "down"
        }
    
    # Puntos 12-7 (inferior izquierda)
    for i in range(6):
        point_number = 12 - i
        point_mapping[str(point_number)] = {
            "rect": pygame.Rect(
                board_inner.left + i * point_width,
                board_inner.top + board_inner.height // 2,
                point_width,
                point_height
            ),
            "direction": "up"
        }
    
    # Puntos 6-1 (inferior derecha)
    for i in range(6):
        point_number = 6 - i
        point_mapping[str(point_number)] = {
            "rect": pygame.Rect(
                board_inner.left + board_inner.width // 2 + i * point_width,
                board_inner.top + board_inner.height // 2,
                point_width,
                point_height
            ),
            "direction": "up"
        }
    
    return point_mapping

def draw_checkers_on_point(screen, point_data, checkers, max_display=5):
    """Draws all the checkers in a specific point"""
    point_rect = point_data["rect"]
    direction = point_data["direction"]
    
    checker_radius = min(point_rect.width, 20)
    spacing = checker_radius * 2
    
    # Determine direction (will start up in the upper squares and down in the lower ones)
    if direction == "down":
        start_y = point_rect.top + checker_radius
        step = spacing
    else:  # up
        start_y = point_rect.bottom - checker_radius
        step = -spacing
    
    # Draw checkers according to the max display
    for i, checker in enumerate(checkers[:max_display]):
        color = BLACK_CHECKER_COLOR if checker.get_colour() == "Black" else WHITE_CHECKER_COLOR
        y_pos = start_y + i * step
        
        pygame.draw.circle(screen, color, (point_rect.centerx, y_pos), checker_radius)
        # Borders
        border_color = WHITE if checker.get_colour() == "Black" else BLACK
        pygame.draw.circle(screen, border_color, (point_rect.centerx, y_pos), checker_radius, 1)
    
    # Show counter if necessary
    if len(checkers) > max_display:
        font = pygame.font.SysFont('Arial', 20, bold=True)
        count_text = font.render(f"+{len(checkers) - max_display}", True, WHITE)
        text_rect = count_text.get_rect(center=(point_rect.centerx, start_y + max_display * step))
        screen.blit(count_text, text_rect)

def draw_checkers_in_area(screen, area, checkers):
    """Draws the checkers in the House and Eaten fields"""
    if not checkers:
        return
    
    checker_radius = min(area.height // 2 - 2, 10)
    overlap_offset = checker_radius
    
    # Calculate the max number of checkers that fit
    effective_width = checker_radius * 2 - overlap_offset
    max_per_row = max(1, (area.width - checker_radius) // effective_width)
    
    for i, checker in enumerate(checkers):
        row = i // max_per_row
        col = i % max_per_row
        
        # Overlap
        x = area.left + checker_radius + col * effective_width
        y = area.top + area.height // 2
        y += row * (checker_radius // 2)
        
        # Make sure it does not go off the area
        if y + checker_radius > area.bottom:
            # If it does not fit, make them smaller
            checker_radius = 8
            effective_width = checker_radius * 2 - overlap_offset
            max_per_row = max(1, (area.width - checker_radius) // effective_width)
            # Recalculate with new size
            row = i // max_per_row
            col = i % max_per_row
            x = area.left + checker_radius + col * effective_width
            y = area.top + area.height // 2 + row * (checker_radius // 2)
            
        color = BLACK_CHECKER_COLOR if checker.get_colour() == "Black" else WHITE_CHECKER_COLOR
        pygame.draw.circle(screen, color, (int(x), int(y)), checker_radius)
        border_color = WHITE if checker.get_colour() == "Black" else BLACK
        pygame.draw.circle(screen, border_color, (int(x), int(y)), checker_radius, 1)

def draw_general_interface():
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

    # Map all the points in the board related to __board__ points
    point_mapping = create_point_mapping(board_inner, point_width, point_height)

    # Draw the checkers
    board_state = game.__board__.get_board()

    for point_num, point_data in point_mapping.items():
        checkers_in_point = board_state.get(point_num, [])
        if checkers_in_point:
            draw_checkers_on_point(screen, point_data, checkers_in_point)

    # Areas for Black player
    black_eaten_area = pygame.Rect(
        black_player_control.left + 220,
        black_player_control.top + 60,
        black_player_control.width - 250,
        30
    )

    black_house_area = pygame.Rect(
        black_player_control.left + 220,
        black_player_control.top + 100,
        black_player_control.width - 250,
        30
    )

    # Areas for black player  
    white_eaten_area = pygame.Rect(
        white_player_control.left + 220,
        white_player_control.top + 60,
        white_player_control.width - 250,
        30
    )

    white_house_area = pygame.Rect(
        white_player_control.left + 220,
        white_player_control.top + 100,
        white_player_control.width - 250,
        30
    )

    # Draw special areas (Eaten and House)
    pygame.draw.rect(screen, (50, 50, 50), black_eaten_area, 2)
    pygame.draw.rect(screen, (50, 50, 50), black_house_area, 2)
    pygame.draw.rect(screen, (50, 50, 50), white_eaten_area, 2)  
    pygame.draw.rect(screen, (50, 50, 50), white_house_area, 2)

    # Draw checkers in special areas.
    draw_checkers_in_area(screen, black_eaten_area, board_state.get("BEaten", []))
    draw_checkers_in_area(screen, black_house_area, board_state.get("BHouse", []))
    draw_checkers_in_area(screen, white_eaten_area, board_state.get("WEaten", []))
    draw_checkers_in_area(screen, white_house_area, board_state.get("WHouse", []))

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
    
    draw_general_interface()

    # Update the screen
    pygame.display.flip()

# Exit Pygame
pygame.quit()
sys.exit()