import pygame
import sys
import random
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
BUTTON_COLOR = ("#4CAF50")
BUTTON_HOVER_COLOR = ("#45a049")
BUTTON_TEXT_COLOR = WHITE
ERROR_COLOR = (255, 50, 50)
INFO_COLOR = (255, 255, 0)

# Margins
MARGIN = 5

# Game state variables
dice_rolled = False
current_dice_values = [0, 0]  # Store current dice values
available_moves = []  # Store available moves for current turn
selected_point = None  # Currently selected point for movement
current_message = ""  # Message to display to player
message_color = INFO_COLOR  # Color of the current message
has_valid_moves = True  # Flag to check if there are valid moves
skip_turn_button = None  # Button to skip turn when no moves available
used_dice_values = []  # Track which dice values have been used
black_player_name = ""  # Store black player's name
white_player_name = ""  # Store white player's name

class Button:
    def __init__(self, x, y, width, height, text, color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.visible = True
        
    def draw(self, surface):
        if not self.visible:
            return
            
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)
        
        font = pygame.font.SysFont('Arial', 20, bold=True)
        text_surface = font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        if not self.visible:
            self.is_hovered = False
            return
        self.is_hovered = self.rect.collidepoint(pos)
        
    def is_clicked(self, pos, event):
        if not self.visible:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

# Create buttons
roll_button_black = Button(0, 0, 150, 40, "ROLL DICE")
roll_button_white = Button(0, 0, 150, 40, "ROLL DICE")
skip_turn_button = Button(0, 0, 150, 40, "SKIP TURN", color=(200, 100, 50), hover_color=(180, 80, 40))

def get_player_names():
    """Obtains the players' names at the beginning of the game"""
    # Fonts
    title_font = pygame.font.SysFont('Arial', 48, bold=True)
    input_font = pygame.font.SysFont('Arial', 36)
    prompt_font = pygame.font.SysFont('Arial', 32)
    
    black_name = ""
    white_name = ""
    current_input = "black"  # 'black' or 'white'
    
    input_active = True
    while input_active:
        screen.fill(BACKGROUND_COLOR)
        
        # Title
        title_text = title_font.render("BACKGAMMON", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH//2, 100))
        screen.blit(title_text, title_rect)
        
        # Instructions
        if current_input == "black":
            prompt_text = prompt_font.render("Player with BLACK checkers, enter your name:", True, WHITE)
        else:
            prompt_text = prompt_font.render("Player with WHITE checkers, enter your name:", True, WHITE)
        
        prompt_rect = prompt_text.get_rect(center=(WIDTH//2, 250))
        screen.blit(prompt_text, prompt_rect)
        
        # Show names
        black_display = f"BLACK: {black_name}" if black_name else "BLACK: "
        white_display = f"WHITE: {white_name}" if white_name else "WHITE: "
        
        black_text = input_font.render(black_display, True, WHITE)
        white_text = input_font.render(white_display, True, WHITE)
        
        screen.blit(black_text, (WIDTH//2 - 200, 320))
        screen.blit(white_text, (WIDTH//2 - 200, 370))
        
        # Current input
        current_name = black_name if current_input == "black" else white_name
        input_text = input_font.render(current_name + "|", True, (255, 255, 0))  # Yellow cursor
        input_rect = input_text.get_rect(center=(WIDTH//2, 450))
        screen.blit(input_text, input_rect)
        
        # Instructions
        inst_text = prompt_font.render("Press ENTER to confirm, ESC to exit", True, (200, 200, 200))
        inst_rect = inst_text.get_rect(center=(WIDTH//2, 550))
        screen.blit(inst_text, inst_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    if current_input == "black" and black_name.strip():
                        current_input = "white"
                    elif current_input == "white" and white_name.strip():
                        input_active = False
                    elif current_input == "white" and not white_name.strip():
                        # No permitir nombre vacío
                        continue
                elif event.key == pygame.K_BACKSPACE:
                    if current_input == "black":
                        black_name = black_name[:-1]
                    else:
                        white_name = white_name[:-1]
                else:
                    # Solo permitir caracteres alfanuméricos y espacios
                    if event.unicode.isprintable() and len(event.unicode.strip()) > 0:
                        if current_input == "black":
                            black_name += event.unicode
                        else:
                            white_name += event.unicode
    
    return black_name, white_name

def draw_dice(screen, rect, value, is_selected=False, is_used=False):
    """Draws the dice with optional selection highlight and used state"""
    # Background with selection highlight
    if is_selected:
        pygame.draw.rect(screen, (255, 255, 100), rect.inflate(8, 8), border_radius=14)
    
    # Use gray background for used dice
    background_color = (180, 180, 180) if is_used else WHITE
    pygame.draw.rect(screen, background_color, rect, border_radius=12)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=12)
    
    dot_radius = rect.width // 15
    dot_color = (100, 100, 100) if is_used else BLACK  # Lighter dots for used dice
    
    # Realtive positions
    center_x, center_y = rect.center
    third_x = rect.width // 3
    third_y = rect.height // 3
    
    # Possible positions
    positions = {
        1: [(center_x, center_y)],
        2: [(rect.left + third_x, rect.top + third_y), 
            (rect.right - third_x, rect.bottom - third_y)],
        3: [(rect.left + third_x, rect.top + third_y),
            (center_x, center_y),
            (rect.right - third_x, rect.bottom - third_y)],
        4: [(rect.left + third_x, rect.top + third_y),
            (rect.right - third_x, rect.top + third_y),
            (rect.left + third_x, rect.bottom - third_y),
            (rect.right - third_x, rect.bottom - third_y)],
        5: [(rect.left + third_x, rect.top + third_y),
            (rect.right - third_x, rect.top + third_y),
            (center_x, center_y),
            (rect.left + third_x, rect.bottom - third_y),
            (rect.right - third_x, rect.bottom - third_y)],
        6: [(rect.left + third_x, rect.top + third_y),
            (rect.right - third_x, rect.top + third_y),
            (rect.left + third_x, center_y),
            (rect.right - third_x, center_y),
            (rect.left + third_x, rect.bottom - third_y),
            (rect.right - third_x, rect.bottom - third_y)]
    }
    
    # Draw the points
    for pos in positions[value]:
        pygame.draw.circle(screen, dot_color, pos, dot_radius)

def determine_first_turn(black_name, white_name):
    """Creates a window for setting the first turn"""
    temp_game = BackgammonGame()
    
    # Fonts
    title_font = pygame.font.SysFont('Arial', 48, bold=True)
    name_font = pygame.font.SysFont('Arial', 32, bold=True)
    result_font = pygame.font.SysFont('Arial', 36, bold=True)
    info_font = pygame.font.SysFont('Arial', 24)
    
    # Dice areas
    dice_size = 120
    black_dice_area = pygame.Rect(WIDTH//2 - dice_size - 50, 250, dice_size, dice_size)
    white_dice_area = pygame.Rect(WIDTH//2 + 50, 250, dice_size, dice_size)

    # Animation
    animation_frames = 25
    for frame in range(animation_frames):
        screen.fill(BACKGROUND_COLOR)
        
        title_text = title_font.render("DETERMINING FIRST TURN", True, (255, 215, 0))
        title_rect = title_text.get_rect(center=(WIDTH//2, 80))
        screen.blit(title_text, title_rect)
        
        # Names
        black_name_text = name_font.render(f"{black_name}", True, (200, 200, 200))
        white_name_text = name_font.render(f"{white_name}", True, (200, 200, 200))
        screen.blit(black_name_text, (WIDTH//2 - 300, 150))
        screen.blit(white_name_text, (WIDTH//2 + 100, 150))
        
        # Animated dice
        anim_black_val = random.randint(1, 6)
        anim_white_val = random.randint(1, 6)
        
        draw_dice(screen, black_dice_area, anim_black_val)
        draw_dice(screen, white_dice_area, anim_white_val)
        
        # Animated text
        roll_text = info_font.render("Rolling dice..." + "." * (frame % 4), True, (255, 255, 0))
        roll_rect = roll_text.get_rect(center=(WIDTH//2, 400))
        screen.blit(roll_text, roll_rect)
        
        pygame.display.flip()
        pygame.time.delay(20)
    
    # Use the real method after the timeout
    temp_game.set_first_turn()
    
    # Obtain values
    final_black = temp_game.__dice1__.get_number()
    final_white = temp_game.__dice2__.get_number()
    first_turn = temp_game.get_turn()
    
    # Show final result
    screen.fill(BACKGROUND_COLOR)
    
    title_text = title_font.render("FIRST TURN RESULT", True, (255, 215, 0))
    title_rect = title_text.get_rect(center=(WIDTH//2, 80))
    screen.blit(title_text, title_rect)
    
    # Names
    black_name_text = name_font.render(f"{black_name}", True, (200, 200, 200))
    white_name_text = name_font.render(f"{white_name}", True, (200, 200, 200))
    screen.blit(black_name_text, (WIDTH//2 - 300, 150))
    screen.blit(white_name_text, (WIDTH//2 + 100, 150))
    
    # Final dice
    draw_dice(screen, black_dice_area, final_black)
    draw_dice(screen, white_dice_area, final_white)
    
    # Numbers
    value_font = pygame.font.SysFont('Arial', 28, bold=True)
    black_value_text = value_font.render(f"Value: {final_black}", True, WHITE)
    white_value_text = value_font.render(f"Value: {final_white}", True, WHITE)
    screen.blit(black_value_text, (black_dice_area.centerx - 50, black_dice_area.bottom + 10))
    screen.blit(white_value_text, (white_dice_area.centerx - 50, white_dice_area.bottom + 10))
    
    # Result
    first_player = black_name if first_turn == "Black" else white_name
    result_text = result_font.render(f"{first_player} ({first_turn}) goes first!", True, (0, 255, 0))
    result_rect = result_text.get_rect(center=(WIDTH//2, 450))
    screen.blit(result_text, result_rect)
    
    # Instruction (press any key to start)
    continue_text = info_font.render("Press any key to start...", True, (255, 255, 0))
    continue_rect = continue_text.get_rect(center=(WIDTH//2, 520))
    screen.blit(continue_text, continue_rect)
    
    pygame.display.flip()
    
    # Wait for input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                waiting = False
    
    return first_turn

def create_point_mapping(board_inner_rect, point_width, point_height):
    """Creates a dictionary mapping board points to visual coordinates"""
    point_mapping = {}
    board_inner = board_inner_rect
    
    # Points 13-18 (top left)
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
    
    # Points 19-24 (top right)
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
    
    # Points 12-7 (bottom left)
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
    
    # Points 6-1 (bottom right)
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
    
    # Add beaten areas from player controls
    # Black player control area (top)
    black_control_left = MARGIN + (WIDTH - 2*MARGIN) * 2 // 3  # Inicio del panel de control
    point_mapping["BEaten"] = {
        "rect": pygame.Rect(
            black_control_left + 220,  # Posición X absoluta
            MARGIN + 60,  # Posición Y absoluta para el panel negro (black_player_control.top + 60)
            (WIDTH - 2*MARGIN) // 3 - 250,  # Ancho
            30  # Alto
        ),
        "direction": "none"
    }

    # Compute same layout values used in draw_general_interface so coordinates match
    message_area_height = 80
    HEIGHT_player_control = (HEIGHT - 2*MARGIN - message_area_height) // 2

    # White player control area (bottom) - align with draw_general_interface
    white_control_top = MARGIN + HEIGHT_player_control + message_area_height
    point_mapping["WEaten"] = {
        "rect": pygame.Rect(
            black_control_left + 220,  # Misma X que el negro
            white_control_top + 60,  # Posición Y absoluta para el panel blanco (white_player_control.top + 60)
            (WIDTH - 2*MARGIN) // 3 - 250,  # Ancho
            30  # Alto
        ),
        "direction": "none"
    }
    
    return point_mapping

def draw_checkers_on_point(screen, point_data, checkers, max_display=5, is_selected=False):
    """Draws all the checkers in a specific point with selection highlight"""
    point_rect = point_data["rect"]
    direction = point_data["direction"]
    
    # Draw selection highlight
    if is_selected:
        pygame.draw.rect(screen, (200, 200, 200), point_rect.inflate(6, 6), border_radius=4)
    
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

def roll_dice():
    """Roll the dice and update game state"""
    global dice_rolled, current_dice_values, available_moves, selected_point, current_message, has_valid_moves, used_dice_values
    
    # Roll the dice
    dice1_val = game.__dice1__.roll()
    dice2_val = game.__dice2__.roll()
    
    current_dice_values = [dice1_val, dice2_val]
    dice_rolled = True
    selected_point = None
    current_message = ""
    used_dice_values = []  # Reset used dice values
    
    # Initialize available moves list
    available_moves = []
    
    if dice1_val == dice2_val:
        # Doubles - 4 moves with the same value
        available_moves = [dice1_val, dice1_val, dice1_val, dice1_val]
    else:
        # Normal roll - 2 different moves
        available_moves = [dice1_val, dice2_val]
    
    # Check if there are any valid moves
    check_valid_moves()

def check_valid_moves():
    """Check if there are any valid moves available with current dice"""
    global has_valid_moves, current_message
    
    has_valid_moves = False
    board_state = game.__board__.get_board()
    current_color = game.get_turn()
    
    # Check each available move
    for move in set(available_moves):
        # Check all points including special areas
        for point in board_state.keys():
            checkers = board_state[point]
            # Check if point has checkers of current player
            if checkers and checkers[0].get_colour() == current_color:
                if game.check_move(point, move):
                    has_valid_moves = True
                    return
    
    # If no valid moves found
    if not has_valid_moves:
        current_message = "No valid moves available. Click SKIP TURN to continue."
        print("No valid moves available")

def draw_dice_section(screen, player_control_rect, dice_values, is_doubles=False, selected_dice=None):
    """Draw dice section for a specific player with clickable dice"""
    global used_dice_values
    dice_size = 50
    spacing = 10
    
    # Calculate total width needed
    if is_doubles:
        total_width = (dice_size * 4) + (spacing * 3)
    else:
        total_width = (dice_size * 2) + spacing
    
    start_x = player_control_rect.centerx - (total_width // 2)
    y_pos = player_control_rect.centery + 30
    
    # Draw dice
    if is_doubles:
        # Draw 4 dice for doubles
        remaining_moves = available_moves.count(dice_values[0])  # Count remaining moves for doubles
        for i in range(4):
            dice_rect = pygame.Rect(
                start_x + i * (dice_size + spacing),
                y_pos,
                dice_size,
                dice_size
            )
            is_selected = (selected_dice == dice_values[0])
            is_used = (i >= remaining_moves)  # Mark as used if we've used this many moves
            draw_dice(screen, dice_rect, dice_values[0], is_selected, is_used)
    else:
        # Draw 2 dice for normal roll
        for i in range(2):
            dice_rect = pygame.Rect(
                start_x + i * (dice_size + spacing),
                y_pos,
                dice_size,
                dice_size
            )
            is_selected = (selected_dice == dice_values[i])
            is_used = dice_values[i] not in available_moves  # Check if this value has been used
            draw_dice(screen, dice_rect, dice_values[i], is_selected, is_used)

def get_clicked_dice(mouse_pos, player_control_rect, dice_values, is_doubles=False):
    """Check if a dice was clicked and return its value"""
    dice_size = 50
    spacing = 10
    
    # Calculate total width needed
    if is_doubles:
        total_width = (dice_size * 4) + (spacing * 3)
    else:
        total_width = (dice_size * 2) + spacing
    
    start_x = player_control_rect.centerx - (total_width // 2)
    y_pos = player_control_rect.centery + 30
    
    # Check dice clicks
    if is_doubles:
        # Check 4 dice for doubles
        for i in range(4):
            dice_rect = pygame.Rect(
                start_x + i * (dice_size + spacing),
                y_pos,
                dice_size,
                dice_size
            )
            if dice_rect.collidepoint(mouse_pos):
                return dice_values[0]  # All same value for doubles
    else:
        # Check 2 dice for normal roll
        for i in range(2):
            dice_rect = pygame.Rect(
                start_x + i * (dice_size + spacing),
                y_pos,
                dice_size,
                dice_size
            )
            if dice_rect.collidepoint(mouse_pos):
                return dice_values[i]
    
    return None

def execute_move(origin_point, dice_value):
    """Execute a move with the given origin point and dice value"""
    global available_moves, selected_point, current_message, dice_rolled
    
    # Validate the move
    if not game.check_move(origin_point, dice_value):
        current_message = "Invalid move! Please try again."
        message_color = ERROR_COLOR
        return False
    
    # Execute the move
    try:
        game.move_checker(origin_point, dice_value)
        
        # Remove the used move from available moves
        if dice_value in available_moves:
            available_moves.remove(dice_value)
            current_message = f"Move executed! {len(available_moves)} moves remaining."
        
        # Reset selection
        selected_point = None
        
        # Check for winner
        winner = game.check_winner()
        if winner != "None":
            winner_name = black_player_name if winner == "Black" else white_player_name
            current_message = f"{winner_name} ({winner}) WINS THE GAME!"
            dice_rolled = False  # Prevent further moves
            game.set_turn("None")  # Set turn to None to prevent further rolls
            return True
        
        # If no moves left, end turn
        if not available_moves:
            current_message = "All moves completed! Switching turn..."
            switch_turn()
            return True
        
        # Check if remaining moves are still valid
        check_valid_moves()
        if not has_valid_moves:
            current_message = "No more valid moves available. Switching turn..."
            switch_turn()
            return True
            
        return True
        
    except Exception as e:
        current_message = f"Error executing move: {str(e)}"
        message_color = ERROR_COLOR
        return False

def switch_turn():
    """Switch to the next player's turn"""
    global dice_rolled, selected_point, current_message, available_moves
    
    # Reset game state for next turn
    dice_rolled = False
    selected_point = None
    available_moves = []
    
    # Switch turn
    next_color = "White" if game.get_turn() == "Black" else "Black"
    game.set_turn(next_color)
    
    current_message = f"{next_color}'s turn. Click ROLL DICE to start."

def draw_general_interface(black_player_name, white_player_name):
    global dice_rolled, current_dice_values, selected_point, current_message, has_valid_moves
    
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

    # Define message area height
    message_area_height = 80  # Altura para el área de mensajes
    
    # Adjust player control heights to accommodate message area
    HEIGHT_player_control = (HEIGHT - 2*MARGIN - message_area_height) // 2
    
    # Mini superior square for black player control
    black_player_control = pygame.Rect(
        MARGIN + left_width, 
        MARGIN, 
        right_width, 
        HEIGHT_player_control
    )
    
    # Message area in the middle
    message_area = pygame.Rect(
        MARGIN + left_width,
        MARGIN + HEIGHT_player_control,
        right_width,
        message_area_height
    )
    
    # Mini inferior square for white player control
    white_player_control = pygame.Rect(
        MARGIN + left_width, 
        MARGIN + HEIGHT_player_control + message_area_height, 
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
    board_margin = 20  # Internal board margin
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

    # In control section
    font = pygame.font.SysFont('Arial', 26, bold=True)

    # Black player control
    black_text = font.render(f"BLACK: {black_player_name}", True, WHITE)
    black_text_rect = black_text.get_rect(centerx=black_player_control.centerx, top=black_player_control.top + 10)
    screen.blit(black_text, black_text_rect)

    # White player control 
    white_text = font.render(f"WHITE: {white_player_name}", True, WHITE)
    white_text_rect = white_text.get_rect(centerx=white_player_control.centerx, top=white_player_control.top + 10)
    screen.blit(white_text, white_text_rect)

    font = pygame.font.SysFont('Arial', 20, bold=True) # Set the font

    black_eaten_text = font.render("EATEN CHECKERS: ", True, WHITE)
    black_eaten_text_rect = black_eaten_text.get_rect(centerx=black_player_control.left + 120, top=black_player_control.top + 60)
    screen.blit(black_eaten_text, black_eaten_text_rect)

    black_eaten_text = font.render("HOUSE: ", True, WHITE)
    black_eaten_text_rect = black_eaten_text.get_rect(centerx=black_player_control.left + 120, top=black_player_control.top + 100)
    screen.blit(black_eaten_text, black_eaten_text_rect)

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
        if point_num in board_state and point_num not in ["BEaten", "WEaten"]:  # Skip BEaten/WEaten here
            checkers_in_point = board_state.get(point_num, [])
            is_selected = (selected_point == point_num)
            if checkers_in_point:
                draw_checkers_on_point(screen, point_data, checkers_in_point, is_selected=is_selected)

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

    # Draw special areas (Eaten and House) with selection highlight
    current_turn = game.get_turn()
    
    # Draw eaten areas with highlight if they have checkers or are selected
    board_state = game.__board__.get_board()
    black_has_eaten = len(board_state.get("BEaten", [])) > 0
    white_has_eaten = len(board_state.get("WEaten", [])) > 0
    
    # Highlight for black eaten area
    if black_has_eaten and current_turn == "Black":
        pygame.draw.rect(screen, (80, 80, 80), black_eaten_area)  # Fondo más oscuro
    if selected_point == "BEaten":
        pygame.draw.rect(screen, (100, 255, 100), black_eaten_area, 3)  # Borde verde más grueso
    
    # Highlight for white eaten area
    if white_has_eaten and current_turn == "White":
        pygame.draw.rect(screen, (80, 80, 80), white_eaten_area)  # Fondo más oscuro
    if selected_point == "WEaten":
        pygame.draw.rect(screen, (100, 255, 100), white_eaten_area, 3)  # Borde verde más grueso
    
    # Draw borders for all areas
    pygame.draw.rect(screen, (50, 50, 50), black_eaten_area, 2)
    pygame.draw.rect(screen, (50, 50, 50), black_house_area, 2)
    pygame.draw.rect(screen, (50, 50, 50), white_eaten_area, 2)  
    pygame.draw.rect(screen, (50, 50, 50), white_house_area, 2)
    
    # Draw checkers in special areas
    draw_checkers_in_area(screen, black_eaten_area, board_state.get("BEaten", []))
    draw_checkers_in_area(screen, black_house_area, board_state.get("BHouse", []))
    draw_checkers_in_area(screen, white_eaten_area, board_state.get("WEaten", []))
    draw_checkers_in_area(screen, white_house_area, board_state.get("WHouse", []))

    # Position buttons for rolling dice
    roll_button_black.rect.centerx = black_player_control.centerx
    roll_button_black.rect.centery = black_player_control.centery + 40
    
    roll_button_white.rect.centerx = white_player_control.centerx
    roll_button_white.rect.centery = white_player_control.centery + 40
    
    # Position skip turn button
    skip_turn_button.rect.centerx = black_player_control.centerx if game.get_turn() == "Black" else white_player_control.centerx
    skip_turn_button.rect.centery = (black_player_control.centery if game.get_turn() == "Black" else white_player_control.centery) + 100

    # Draw dice and buttons based on current turn
    current_turn = game.get_turn()
    mouse_pos = pygame.mouse.get_pos()
    
    # Show current turn
    turn_font = pygame.font.SysFont('Arial', 24, bold=True)
    
    # Show game message in the dedicated message area
    if current_message:
        message_font = pygame.font.SysFont('Arial', 18, bold=True)
        
        # Dividir el mensaje en líneas si es muy largo
        words = current_message.split()
        lines = []
        current_line = words[0]
        for word in words[1:]:
            test_line = current_line + " " + word
            test_surface = message_font.render(test_line, True, WHITE)
            if test_surface.get_width() < right_width - 20:  # Margen de 10px a cada lado
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        # Dibujar fondo semi-transparente para el mensaje
        message_background = pygame.Surface((message_area.width, message_area.height))
        message_background.set_alpha(128)
        message_background.fill((30, 30, 30))  # Un poco más oscuro para mejor contraste
        screen.blit(message_background, message_area)
        
        # Dibujar borde del área de mensajes
        pygame.draw.rect(screen, (50, 50, 50), message_area, 1)
        
        # Dibujar cada línea del mensaje
        y_offset = message_area.centery - (len(lines) * 22 // 2)  # Reducido el espaciado vertical
        for line in lines:
            text_surface = message_font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center=(message_area.centerx, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 22  # Reducido el espaciado entre líneas
    
    if dice_rolled:
        # Show dice only for the current player
        is_doubles = current_dice_values[0] == current_dice_values[1]
        
        if current_turn == "Black":
            draw_dice_section(screen, black_player_control, current_dice_values, is_doubles, selected_point)
        else:
            draw_dice_section(screen, white_player_control, current_dice_values, is_doubles, selected_point)
            
        # Show doubles message if applicable
        if is_doubles:
            doubles_font = pygame.font.SysFont('Arial', 16, bold=True)
            doubles_text = doubles_font.render("DOUBLES! 4 moves available", True, (255, 255, 0))
            if current_turn == "Black":
                doubles_rect = doubles_text.get_rect(center=(black_player_control.centerx, black_player_control.centery + 90))
            else:
                doubles_rect = doubles_text.get_rect(center=(white_player_control.centerx, white_player_control.centery + 90))
            screen.blit(doubles_text, doubles_rect)
            
        # Show skip turn button if no valid moves
        if not has_valid_moves:
            skip_turn_button.visible = True
            skip_turn_button.check_hover(mouse_pos)
            skip_turn_button.draw(screen)
        else:
            skip_turn_button.visible = False
            
    else:
        # Show roll button only for the current player and if there's no winner
        if current_turn != "None":  # Si no hay ganador
            if current_turn == "Black":
                roll_button_black.visible = True
                roll_button_black.check_hover(mouse_pos)
                roll_button_black.draw(screen)
                roll_button_white.visible = False
            else:
                roll_button_white.visible = True
                roll_button_white.check_hover(mouse_pos)
                roll_button_white.draw(screen)
                roll_button_black.visible = False
        else:
            roll_button_black.visible = False
            roll_button_white.visible = False
            
        skip_turn_button.visible = False

    pygame.display.flip()

def handle_point_click(mouse_pos):
    """Handle clicks on board points"""
    global selected_point, current_message
    
    # Calculate board area
    board_square = pygame.Rect(MARGIN, MARGIN, (WIDTH - 2*MARGIN) * 2 // 3, HEIGHT - 2*MARGIN)
    board_margin = 20
    board_inner = pygame.Rect(
        board_square.left + board_margin,
        board_square.top + board_margin,
        board_square.width - 2 * board_margin,
        board_square.height - 2 * board_margin
    )
    
    point_width = board_inner.width // 12
    point_height = board_inner.height // 2
    
    # Create temporary point mapping for click detection
    point_mapping = create_point_mapping(board_inner, point_width, point_height)
    
    # Check if any point was clicked
    for point_num, point_data in point_mapping.items():
        if point_data["rect"].collidepoint(mouse_pos):
            # Check if point has checkers of current player
            board_state = game.__board__.get_board()
            checkers = board_state.get(point_num, [])
            current_color = game.get_turn()
            
            if checkers and checkers[0].get_colour() == current_color:
                selected_point = point_num
                current_message = f"Selected point {point_num}. Now click a dice to move."
                return True
            elif checkers:
                current_message = "You can only move your own checkers!"
                return False
            else:
                current_message = "No checkers in this point!"
                return False
    
    return False

def main():
    global dice_rolled, current_dice_values, selected_point, current_message, has_valid_moves
    
    # Get player names
    global black_player_name, white_player_name
    black_player_name, white_player_name = get_player_names()
    
    # Determine first turn
    first_turn = determine_first_turn(black_player_name, white_player_name)
    game.set_turn(first_turn)
    
    # Initialize game message
    current_message = f"{first_turn}'s turn. Click ROLL DICE to start."
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Handle button clicks
            current_turn = game.get_turn()
            
            if not dice_rolled:
                # Roll dice button
                if current_turn == "Black":
                    if roll_button_black.is_clicked(mouse_pos, event):
                        roll_dice()
                else:
                    if roll_button_white.is_clicked(mouse_pos, event):
                        roll_dice()
            else:
                # Skip turn button (when no valid moves)
                if skip_turn_button.is_clicked(mouse_pos, event) and not has_valid_moves:
                    current_message = "Skipping turn..."
                    switch_turn()
                
                # Handle point selection
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check if a point was clicked
                    if handle_point_click(mouse_pos):
                        continue
                    
                    # Check if a dice was clicked (if a point is already selected)
                    if selected_point:
                        player_control = None
                        # Use the same player control areas as in draw_general_interface
                        message_area_height = 80
                        HEIGHT_player_control = (HEIGHT - 2*MARGIN - message_area_height) // 2
                        
                        if current_turn == "Black":
                            player_control = pygame.Rect(
                                MARGIN + (WIDTH - 2*MARGIN) * 2 // 3, 
                                MARGIN, 
                                (WIDTH - 2*MARGIN) // 3,
                                HEIGHT_player_control
                            )
                        else:
                            player_control = pygame.Rect(
                                MARGIN + (WIDTH - 2*MARGIN) * 2 // 3, 
                                MARGIN + HEIGHT_player_control + message_area_height, 
                                (WIDTH - 2*MARGIN) // 3,
                                HEIGHT_player_control
                            )
                        
                        is_doubles = current_dice_values[0] == current_dice_values[1]
                        clicked_dice = get_clicked_dice(mouse_pos, player_control, current_dice_values, is_doubles)
                        
                        if clicked_dice and clicked_dice in available_moves:
                            # Try to execute the move
                            if execute_move(selected_point, clicked_dice):
                                # Move successful
                                pass
                            else:
                                # Move failed - keep selection for retry
                                pass
                        elif clicked_dice:
                            current_message = "This dice value is not available or already used!"
        
        # Draw the interface
        draw_general_interface(black_player_name, white_player_name)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()