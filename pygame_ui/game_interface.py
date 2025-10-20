import pygame
import sys
import os

# Añadir el directorio core al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.backgammon_game import BackgammonGame

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("¡BACKGAMMON!")

# Colores
BROWN = (139, 69, 19)
LIGHT_BROWN = (222, 184, 135)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Fuente
font = pygame.font.SysFont('Arial', 20)

# Crear instancia del juego
game = BackgammonGame()
game.set_default_checkers()
game.set_first_turn()

# Variables para el control del juego
selected_point = None
dice_rolled = False
dice_values = [0, 0]
available_moves = []

def draw_board():
    # Dibujar el tablero base
    screen.fill(BROWN)
    
    # Dibujar el área central
    pygame.draw.rect(screen, LIGHT_BROWN, (WIDTH//2 - 200, 50, 400, HEIGHT - 100))
    
    # Dibujar los puntos (triángulos)
    point_width = 30
    point_height = 200
    
    # Puntos del lado izquierdo (1-12)
    for i in range(12):
        x = WIDTH//2 - 200 + (i % 6) * (point_width + 10)
        y = 50 if i < 6 else HEIGHT - 50 - point_height
        
        # Determinar dirección del triángulo
        if i < 6:
            points = [(x, y), (x + point_width, y), (x + point_width//2, y + point_height)]
        else:
            points = [(x, y + point_height), (x + point_width, y + point_height), (x + point_width//2, y)]
        
        pygame.draw.polygon(screen, BROWN, points)
        pygame.draw.polygon(screen, BLACK, points, 1)
    
    # Puntos del lado derecho (13-24)
    for i in range(12):
        x = WIDTH//2 + 200 - point_width - (i % 6) * (point_width + 10)
        y = 50 if i < 6 else HEIGHT - 50 - point_height
        
        # Determinar dirección del triángulo
        if i < 6:
            points = [(x, y), (x + point_width, y), (x + point_width//2, y + point_height)]
        else:
            points = [(x, y + point_height), (x + point_width, y + point_height), (x + point_width//2, y)]
        
        pygame.draw.polygon(screen, BROWN, points)
        pygame.draw.polygon(screen, BLACK, points, 1)
    
    # Dibujar áreas de casas y comidas
    pygame.draw.rect(screen, LIGHT_BROWN, (WIDTH//2 - 250, 50, 50, HEIGHT - 100))
    pygame.draw.rect(screen, LIGHT_BROWN, (WIDTH//2 + 200, 50, 50, HEIGHT - 100))

def draw_checkers():
    board = game.__board__.get_board()
    
    # Dibujar fichas en los puntos
    for point in [str(i) for i in range(1, 25)]:
        checkers = board[point]
        if not checkers:
            continue
            
        # Determinar posición del punto
        point_idx = int(point) - 1
        if point_idx < 12:  # Puntos 1-12 (lado izquierdo)
            x = WIDTH//2 - 200 + (point_idx % 6) * 40 + 15
            direction = 1 if point_idx < 6 else -1
            y_start = 60 if point_idx < 6 else HEIGHT - 60
        else:  # Puntos 13-24 (lado derecho)
            x = WIDTH//2 + 200 - (point_idx % 6) * 40 - 45
            direction = 1 if point_idx < 18 else -1
            y_start = 60 if point_idx < 18 else HEIGHT - 60
        
        # Dibujar fichas
        for i, checker in enumerate(checkers):
            color = WHITE if checker.get_colour() == "White" else BLACK
            border_color = BLACK if checker.get_colour() == "White" else WHITE
            
            y = y_start + i * 20 * direction
            pygame.draw.circle(screen, color, (x, y), 15)
            pygame.draw.circle(screen, border_color, (x, y), 15, 2)
    
    # Dibujar fichas comidas
    for i, checker in enumerate(board["BEaten"]):
        x = WIDTH//2 - 225
        y = 100 + i * 30
        pygame.draw.circle(screen, BLACK, (x, y), 15)
        pygame.draw.circle(screen, WHITE, (x, y), 15, 2)
    
    for i, checker in enumerate(board["WEaten"]):
        x = WIDTH//2 + 225
        y = 100 + i * 30
        pygame.draw.circle(screen, WHITE, (x, y), 15)
        pygame.draw.circle(screen, BLACK, (x, y), 15, 2)
    
    # Dibujar fichas en casa
    for i, checker in enumerate(board["BHouse"]):
        x = WIDTH//2 - 275
        y = 100 + i * 30
        pygame.draw.circle(screen, BLACK, (x, y), 15)
        pygame.draw.circle(screen, WHITE, (x, y), 15, 2)
    
    for i, checker in enumerate(board["WHouse"]):
        x = WIDTH//2 + 275
        y = 100 + i * 30
        pygame.draw.circle(screen, WHITE, (x, y), 15)
        pygame.draw.circle(screen, BLACK, (x, y), 15, 2)

def draw_dice():
    # Dibujar dados
    dice1_x, dice2_x = WIDTH//2 - 50, WIDTH//2 + 20
    dice_y = HEIGHT - 80
    
    # Dibujar fondo de dados
    pygame.draw.rect(screen, WHITE, (dice1_x, dice_y, 40, 40))
    pygame.draw.rect(screen, WHITE, (dice2_x, dice_y, 40, 40))
    pygame.draw.rect(screen, BLACK, (dice1_x, dice_y, 40, 40), 2)
    pygame.draw.rect(screen, BLACK, (dice2_x, dice_y, 40, 40), 2)
    
    # Dibujar puntos en los dados
    if dice_values[0] > 0:
        draw_dice_points(dice1_x, dice_y, dice_values[0])
    if dice_values[1] > 0:
        draw_dice_points(dice2_x, dice_y, dice_values[1])
    
    # Dibujar botón para lanzar dados
    pygame.draw.rect(screen, GREEN, (WIDTH//2 - 60, dice_y - 60, 120, 40))
    roll_text = font.render("Lanzar Dados", True, BLACK)
    screen.blit(roll_text, (WIDTH//2 - 50, dice_y - 50))

def draw_dice_points(x, y, value):
    dot_radius = 4
    positions = {
        1: [(x + 20, y + 20)],
        2: [(x + 10, y + 10), (x + 30, y + 30)],
        3: [(x + 10, y + 10), (x + 20, y + 20), (x + 30, y + 30)],
        4: [(x + 10, y + 10), (x + 30, y + 10), (x + 10, y + 30), (x + 30, y + 30)],
        5: [(x + 10, y + 10), (x + 30, y + 10), (x + 20, y + 20), (x + 10, y + 30), (x + 30, y + 30)],
        6: [(x + 10, y + 10), (x + 10, y + 20), (x + 10, y + 30), 
            (x + 30, y + 10), (x + 30, y + 20), (x + 30, y + 30)]
    }
    
    for pos in positions[value]:
        pygame.draw.circle(screen, BLACK, pos, dot_radius)

def draw_game_info():
    # Dibujar información del juego
    turn_text = font.render(f"Turno: {game.get_turn()}", True, WHITE)
    screen.blit(turn_text, (20, 20))
    
    # Dibujar movimientos disponibles si hay un punto seleccionado
    if selected_point and available_moves:
        moves_text = font.render(f"Movimientos disponibles: {available_moves}", True, WHITE)
        screen.blit(moves_text, (20, 50))
    
    # Verificar si hay un ganador
    winner = game.check_winner()
    if winner != "None":
        winner_text = font.render(f"¡{winner} gana!", True, RED)
        screen.blit(winner_text, (WIDTH//2 - 100, 20))

def get_point_from_mouse(pos):
    x, y = pos
    
    # Verificar puntos del lado izquierdo (1-12)
    if WIDTH//2 - 200 <= x <= WIDTH//2 - 200 + 240:
        if 50 <= y <= 250:  # Puntos 1-6
            point_idx = (x - (WIDTH//2 - 200)) // 40
            return str(point_idx + 1)
        elif HEIGHT - 250 <= y <= HEIGHT - 50:  # Puntos 7-12
            point_idx = (x - (WIDTH//2 - 200)) // 40
            return str(point_idx + 7)
    
    # Verificar puntos del lado derecho (13-24)
    if WIDTH//2 + 200 - 240 <= x <= WIDTH//2 + 200:
        if 50 <= y <= 250:  # Puntos 13-18
            point_idx = 5 - (x - (WIDTH//2 + 200 - 240)) // 40
            return str(point_idx + 13)
        elif HEIGHT - 250 <= y <= HEIGHT - 50:  # Puntos 19-24
            point_idx = 5 - (x - (WIDTH//2 + 200 - 240)) // 40
            return str(point_idx + 19)
    
    # Verificar áreas especiales
    if WIDTH//2 - 250 <= x <= WIDTH//2 - 200:
        if game.get_turn() == "Black":
            return "BEaten"
        else:
            return "BHouse"
    
    if WIDTH//2 + 200 <= x <= WIDTH//2 + 250:
        if game.get_turn() == "White":
            return "WEaten"
        else:
            return "WHouse"
    
    return None

def roll_dice():
    global dice_rolled, dice_values
    dice_values = [game.__dice1__.roll(), game.__dice2__.roll()]
    dice_rolled = True

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Verificar si se hizo clic en el botón de lanzar dados
            if WIDTH//2 - 60 <= pos[0] <= WIDTH//2 + 60 and HEIGHT - 140 <= pos[1] <= HEIGHT - 100:
                if not dice_rolled and game.check_winner() == "None":
                    roll_dice()
            
            # Verificar si se hizo clic en un punto
            point = get_point_from_mouse(pos)
            if point:
                if dice_rolled:
                    if selected_point is None:
                        # Seleccionar un punto
                        selected_point = point
                        # Calcular movimientos disponibles
                        available_moves = []
                        for steps in dice_values:
                            if game.check_move(selected_point, steps):
                                available_moves.append(steps)
                    else:
                        # Intentar mover la ficha
                        if selected_point == point:
                            # Deseleccionar si se hace clic en el mismo punto
                            selected_point = None
                            available_moves = []
                        else:
                            # Calcular pasos basados en el punto de destino
                            # (Esta es una simplificación, en un juego real necesitarías
                            # una lógica más compleja para determinar los pasos)
                            if available_moves:
                                steps = available_moves[0]
                                if game.check_move(selected_point, steps):
                                    game.move_checker(selected_point, steps)
                                    # Eliminar el dado usado
                                    dice_values.remove(steps)
                                    if not dice_values:
                                        dice_rolled = False
                                        # Cambiar turno
                                        if game.get_turn() == "Black":
                                            game.set_turn("White")
                                        else:
                                            game.set_turn("Black")
                                selected_point = None
                                available_moves = []
    
    # Dibujar el juego
    draw_board()
    draw_checkers()
    draw_dice()
    draw_game_info()
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()