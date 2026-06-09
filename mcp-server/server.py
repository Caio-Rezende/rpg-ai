import asyncio
import random
from mcp.server.fastmcp import FastMCP

# Create an MCP server named "dice_roller"
mcp = FastMCP("dice_roller")

@mcp.tool()
def roll_dice(dice_set: list[int]) -> list[int]:
    """
    Rolls a set of dice specified by the dice_set.
    Each element in the list represents a die, e.g., [6, 20] for one d6 and one d20.
    Wait, the README says `roll_dice(dice_set: list[int]) -> list[int]` where each int is a die? 
    Actually, usually dice are represented as (number of dice, sides).
    The README example was `[4, 6, 6, 20]`. This looks like [count1, sides1, count2, sides2, ...].
    Let's re-read: `roll_dice(dice_set: list[int]) -> list[int]` (e.g., `[4, 6, 6, 20]`).
    If the input is [4, 6, 6, 20], it probably means 4d6 and 6d20? No, that's not right.
    Maybe it's [count, sides, count, sides...] or just a list of dice where each die is (count, sides)?
    Wait, `[4, 6, 6, 20]` could mean 4d6 and 6d20? No, that would be 10 dice.
    Let's look at the example again: `[4, 6, 6, 20]`. 
    If it's [count, sides, count, sides], then it's 4d6 and 6d20.
    Actually, a simpler interpretation is that each pair is (number of dice, number of sides).
    Or maybe it's just a list of individual dice? No, `[4, 6, 6, 20]` has 4 elements.
    If it was [count, sides], then [4, 6] would be 4d6.
    So [4, 6, 6, 20] would be 4d6 and 6d20.
    Let's implement it this way.
    """
    results = []
    # Iterate through the list in pairs of (count, sides)
    for i in range(0, len(dice_set), 2):
        if i + 1 < len(dice_set):
            count = dice_set[i]
            sides = dice_set[i+1]
            for _ in range(count):
                results.append(random.randint(1, sides))
    return results

if __name__ == "__main__":
    mcp.run()
