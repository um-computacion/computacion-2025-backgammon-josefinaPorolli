"""CLI module for Backgammon game"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.backgammon_game import BackgammonGame

class BackgammonCLI:
    """Command Line Interface for Backgammon game"""
    
    def __init__(self):
        self.game = BackgammonGame()
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_board(self):
        """Board display"""
        board = self.game.__board__.get_board()
        
        print("\n" + "="*80)
        print("BACKGAMMON BOARD".center(80))
        print("="*80)
        
        # Top numbers (13-24)
        print(" " * 10 + "13  14  15  16  17  18    19  20  21  22  23  24")
        print(" " * 10 + "┌───┌───┌───┌───┌───┌───┐  ┌───┌───┌───┌───┌───┌───┐")
        
        # Display checkers for top row
        for row in range(5):
            line = " " * 10
            for point in range(13, 25):
                checkers = board[str(point)]
                if len(checkers) > row:
                    color_char = '○' if checkers[row].get_colour() == "Black" else '●'
                    line += f"│ {color_char} "
                else:
                    line += "│   "
            line += "│"
            print(line)
        
        print(" " * 10 + "└───└───└───└───└───└───┘  └───└───└───└───└───└───┘")
        
        # Middle section with eaten checkers and houses
        print(f"BEaten:{len(board['BEaten']):2d} " + "─" * 40 + f" WEaten:{len(board['WEaten']):2d}")
        print(f"BHouse:{len(board['BHouse']):2d} " + "─" * 40 + f" WHouse:{len(board['WHouse']):2d}")
        
        # Bottom numbers (12-1)
        print(" " * 10 + "12  11  10   9   8   7     6   5   4   3   2   1")
        print(" " * 10 + "┌───┌───┌───┌───┌───┌───┐  ┌───┌───┌───┌───┌───┌───┐")
        
        # Display checkers for bottom row
        for row in range(4, -1, -1):
            line = " " * 10
            for point in range(12, 0, -1):
                checkers = board[str(point)]
                if len(checkers) > row:
                    color_char = '○' if checkers[row].get_colour() == "Black" else '●'
                    line += f"│ {color_char} "
                else:
                    line += "│   "
            line += "│"
            print(line)
        
        print(" " * 10 + "└───└───└───└───└───└───┘  └───└───└───└───└───└───┘")
        print("="*80)
        
    def get_player_names(self):
        """Get player names from input"""
        print("Welcome to Backgammon!")
        print("="*30)
        
        black_name = input("Player with black checkers, enter your name: ")
        white_name = input("Player with white checkers, enter your name: ")
        
        # Set names using the player objects
        self.game.__player1__.set_name(black_name)
        self.game.__player2__.set_name(white_name)
        
        return black_name, white_name
    
    def display_dice_roll(self):
        """Display dice roll results"""
        dice1 = self.game.__dice1__.get_number()
        dice2 = self.game.__dice2__.get_number()
        
        print(f"\nDice Roll: {dice1} and {dice2}")
        
        if dice1 == dice2:
            print("DOUBLES! You have 4 moves of the same value.")
    
    def get_player_move(self, player_name, color, available_moves):
        """Get a move from the player"""
        print(f"\n{player_name} ({color}), it's your turn!")
        
        while True:
            try:
                print("\nAvailable moves:", available_moves)
                origin = input("Enter origin point (or 'BEaten'/'WEaten' for eaten checkers): ").strip()
                steps = int(input("Enter number of steps: "))
                
                # Validate the move
                if self.game.check_move(origin, steps):
                    return origin, steps
                else:
                    print("Invalid move! Please try again.")
                    
            except ValueError:
                print("Please enter valid input!")
            except Exception as e:
                print(f"Error: {e}. Please try again.")
    
    def determine_first_turn(self):
        """Determine who goes first"""
        print("\nDetermining who goes first...")
        self.game.set_first_turn()
        
        dice1 = self.game.__dice1__.get_number()
        dice2 = self.game.__dice2__.get_number()
        first_player = self.game.get_turn()
        
        print(f"Black rolled: {dice1}, White rolled: {dice2}")
        print(f"{first_player} goes first!")
        
        input("\nPress Enter to continue...")
    
    def play_game(self):
        """Main game loop"""
        # Setup
        black_name, white_name = self.get_player_names()
        self.clear_screen()
        self.determine_first_turn()
        self.game.set_default_checkers()
        
        # Main game loop
        while True:
            self.clear_screen()
            self.display_board()
            
            # Check for winner
            winner = self.game.check_winner()
            if winner != "None":
                winner_name = black_name if winner == "Black" else white_name
                print(f"\n🎉 CONGRATULATIONS! {winner_name} ({winner}) WINS! 🎉")
                break
            
            # Get current player info
            current_color = self.game.get_turn()
            current_player = black_name if current_color == "Black" else white_name
            
            # Roll dice for current turn
            dice1_val = self.game.__dice1__.roll()
            dice2_val = self.game.__dice2__.roll()
            
            print(f"\n{current_player}'s turn ({current_color})")
            self.display_dice_roll()
            
            # Handle moves based on dice
            moves = []
            if dice1_val == dice2_val:
                # Doubles - 4 moves
                moves = [dice1_val] * 4
            else:
                moves = [dice1_val, dice2_val]
            
            # Execute moves
            for move_steps in moves:
                if move_steps == 0:  # Skip if move was already used
                    continue
                    
                self.display_board()
                print(f"\nRemaining moves: {moves}")
                
                origin, steps = self.get_player_move(current_player, current_color, moves)
                
                # Execute the move
                self.game.move_checker(origin, steps)
                
                # Remove this move from available moves
                if steps in moves:
                    moves[moves.index(steps)] = 0
            
            # Switch turn
            next_color = "White" if current_color == "Black" else "Black"
            self.game.set_turn(next_color)
            
            input("\nPress Enter to continue to next turn...")

def main():
    """Main function to start the game"""
    try:
        cli = BackgammonCLI()
        cli.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()