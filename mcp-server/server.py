from mcp.server.fastmcp import FastMCP
from dice_cli import roll_dice

# Create an MCP server named "dice_roller"
mcp = FastMCP("dice_roller")

@mcp.tool()
def roll_dice_tool(dice_notation: str) -> list[int]:
    """
    Rolls dice based on notation like '4d6', '1d20'.
    Example: '4d6' rolls four 6-sided dice.
    """
    return roll_dice(dice_notation)

if __name__ == "__main__":
    mcp.run()