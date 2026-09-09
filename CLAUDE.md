# RPG AI — Agent Instructions

This is an AI-driven tabletop RPG where the **user is always the Dungeon Master** and the AI controls all characters. See [README.md](README.md) for full architecture details.

## Core Principle

> The DM narrates the world. The AI controls every character (heroes and enemies) and handles all mechanics.

Never ask the user to play as a character. Never narrate scenes. Never interpret dice results. See [.agents/skills/adventure/SKILL.md](.agents/skills/adventure/SKILL.md) for the full orchestration logic.

## Entry Points

| Task | Entry Point |
|------|-------------|
| Start/run an adventure session | `.agents/skills/adventure/SKILL.md` (the `/adventure` skill) |
| Session state (load/save/update) | `.agents/skills/adventure/instructions/session_management.md` |
| Character/enemy loading + sub-agent prompts | `.agents/skills/adventure/instructions/character_management.md` |
| Combat & initiative | `.agents/skills/adventure/instructions/combat_management.md` |
| Rules lookups | `.agents/skills/adventure/instructions/rules_assistance.md` |
| Character sub-agent prompt template | `agents/prompts/character_system_prompt.md` |
| Rules Assistant system prompt | `agents/prompts/gm_system_prompt.md` |

## Key Directories

| Path | Contents |
|------|----------|
| `adventure/heroes/` | Party character profiles (Bram, Pip, Sariel) |
| `adventure/state/session.json` | Live session state (HP, conditions, spell slots) |
| `adventure/summary.md` | Party backstory and dynamics |
| `content/enemies/` | Enemy files organized by type |
| `content/weapons/weapons_catalog.md` | Weapons table |
| `content/spells/` | Spells by level and class |
| `rules/core_rules.md` | Core mechanics reference |
| `mcp-server/dice_cli.py` | Dice roller CLI |

## CLI Commands

```bash
# Roll dice
python3 mcp-server/dice_cli.py 1d20 2d6

# Load session
python3 adventure/game_state.py --load adventure/state/session.json

# New session
python3 adventure/game_state.py --new-session "id" "Title" --heroes-dir adventure/heroes/

# Update state
python3 adventure/game_state.py --update --state-file adventure/state/session.json \
  --hp "Bram=12" "Pip=11" "Sariel=9" --spell-slots "Sariel/1st=2" \
  --conditions "Bram:" "Pip:" "Sariel:" --log-event "description"

# Load party summary
python3 adventure/character_loader.py --summary adventure/heroes/

# Load enemy
python3 adventure/character_loader.py --load-enemy content/enemies/humanoids/goblin.md
```

## Tests

```bash
cd mcp-server && python -m pytest test_dice.py
```

## Environment

- Python virtual environment: `.venv/` — activate with `source .venv/bin/activate`
- MCP server dependency: `mcp` (see `mcp-server/requirements.txt`)
- MCP server config: `.vscode/mcp.json`
