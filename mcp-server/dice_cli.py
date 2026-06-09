import random
import sys
import re

def roll_dice(dice_notation):
    """
    Rolls dice based on notation like '4d6', '1d20'.
    Returns a list of results.
    """
    match = re.match(r'(\d*)d(\d+)', dice_notation.lower())
    if not match:
        raise ValueError(f"Invalid dice notation: {dice_notation}. Expected format like '4d6' or '1d20'.")
    
    count_str, sides_str = match.groups()
    count = int(count_str) if count_str else 1
    sides = int(sides_str)
    
    if sides < 1:
        raise ValueError("Number of sides must be at least 1.")
        
    return [random.randint(1, sides) for _ in range(count)]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dice_cli.py <notation> [notation...]")
        print("Example: python dice_cli.py 4d6 1d20")
        sys.exit(1)
        
    all_results = []
    for notation in sys.argv[1:]:
        try:
            res = roll_dice(notation)
            all_results.append((notation, res))
        except ValueError as e:
            print(f"Error rolling {notation}: {e}")
            
    for notation, res in all_results:
        print(f"{notation}: {res} (Total: {sum(res)})")
