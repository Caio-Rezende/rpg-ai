---
name: dice-roller
description: Use this skill whenever the user wants to roll dice using standard dice notation.
---

# Dice Roller Skill

This skill allows the agent to roll dice using a CLI tool. It replaces the previous MCP server implementation which was restricted by admin policies. If the user requests a roll without specifying notation, ask them to clarify: "What dice would you like to roll? Please use standard notation like 2d6 or 1d20."

## Usage

To roll dice, use the `run_in_terminal` tool to execute `python /Users/caioar/Documents/GitHub/rpg-ai/mcp-server/dice_cli.py`.

### Command Pattern
```zsh
python3 /Users/caioar/Documents/GitHub/rpg-ai/mcp-server/dice_cli.py <notation> [notation...]
```

### Dice Notation
- `NdS`: Roll `N` dice with `S` sides.
- Example: `4d6` rolls four 6-sided dice.
- Example: `1d20` rolls one 20-sided die.
- If `N` is omitted (e.g., `d20`), it defaults to 1.

## Implementation Details
The script `/Users/caioar/Documents/GitHub/rpg-ai/mcp-server/dice_cli.py` handles the parsing of dice notation and returns the individual results along with the total sum for each roll.

## Example Execution
**Input:** `python /Users/caioar/Documents/GitHub/rpg-ai/mcp-server/dice_cli.py 2d6 1d10`
**Output:** After running the command, relay the results to the user in a natural, readable format, e.g.: "You rolled 2d6: 3 and 5 (Total: 8), and 1d10: 7 (Total: 7)."

```
2d6: [3, 5] (Total: 8)
1d10: [7] (Total: 7)
```
