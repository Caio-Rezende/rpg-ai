import random
from mcp.server.mcpserver import MCPServer
from logic import roll_dice

# Create an MCP server named "dice_roller"
mcp = MCPServer("dice_roller")

@mcp.tool()
def roll_dice_tool(dice_set: list[int]) -> list[int]:
    """
    Rolls multiple sets of dice and returns the individual results.

    Args:
        dice_set (list[int]): A list of integers where each pair represents (count, sides).
            Example: [4, 6, 1, 20] rolls 4d6 and 1d20.

    Returns:
        list[int]: A list containing the result of every individual die roll.

    Raises:
        ValueError: If the dice_set contains an odd number of elements or non-positive values.
    """
    return roll_dice(dice_set)

if __name__ == "__main__":
    mcp.run()
