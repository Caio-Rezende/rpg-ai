## RPG AI Agentic Project

This repository contains the structure and content for an AI-driven tabletop RPG experience. The goal is to create a chat-based game where the user acts as the Dungeon Master (DM), describing the scenario and prompting the AI characters to take actions.

### Project Structure

- **`content/`**: Contains templates and catalogs for core game elements:
      - `characters/`: Character templates (includes weapon & spell references).
      - `locations/`: Location templates.
      - `encounters/`: Encounter templates.
        - `enemies/`: Mob and creature templates organized by type (aberrations, animals, constructs, undead, etc).
      - `weapons/`: Complete weapons catalog with damage, range, and properties.
      - `spells/`: Spells & magic catalog organized by level and class.
      - `items/`: Items & equipment catalog (armor table, shields, gear, consumables).
- **`adventure/`**: Contains the current campaign data:
     - `summary.md`: Overview of the adventure and party members.
     - `heroes/`: Detailed profiles for each character in the party.
- **`rules/`**: Contains the core ruleset for the game.
- **`agents/`**: Contains the logic and prompts for the AI agents that control the characters.
- **`.agents/skills/adventure/SKILL.md`**: Orchestrator skill — the entry point for adventure sessions.
- **`README.md`**: This file.

### Game Flow

1. **DM Input**: The user (DM) describes the scene, an event, or asks "What does the party do?"
2. **Character Reactions**: The system spawns a Character Sub-Agent for each character (heroes and enemies) who would react. Each sub-agent receives only its character profile and the DM's scene — no knowledge of other characters' reactions.
3. **Actions Declared**: Character sub-agents return in-character dialogue, actions, and any skill checks they declare (`*Requires Skill (d20 + modifier)*`).
4. **DM Rules**: The DM sets the DC, authorizes rolls, and interprets outcomes narratively. The system presents raw numbers — the DM decides what they mean.
5. **Consequences & Loop**: The DM describes consequences. The system updates state (HP, spell slots, conditions). Back to step 1.

### Agent Architecture

To maintain a clear distinction between game mechanics and character performance, we use two distinct layers of agency:

#### 1. The Rules Assistant (GM Agent)
The **Rules Assistant** is the primary interface for the user (DM). It manages game state and coordinates character sub-agents — but it does not narrate the world or interpret outcomes.
*    **Responsibilities:** Spawning character sub-agents, declaring skill checks, rolling dice when the DM authorizes, tracking numerical state (HP, spell slots, conditions, turn order), looking up rules for the DM.
*    **Context:** Uses the `adventure/summary.md`, current location, encounter details, and global game state.

#### 2. The Character (Sub-Agent) Layer
When characters need to act or speak, the Rules Assistant spawns a **Character Sub-Agent** — one per character, running in parallel and isolated from each other.
*    **Responsibilities:** Generating dialogue, expressing unique personality traits, and stating intentions based on their specific goals and what they perceive in the scene.
*    **Context:** Uses only their individual profile (e.g., `adventure/heroes/bram.md`) and the immediate scene description provided by the DM. No knowledge of other characters' reactions or broader world state.
*    **Isolation:** Both heroes and enemies run as sub-agents. Enemy behavior comes from their enemy file (`content/enemies/...`).

### What the DM Does vs What the Agent Does

| DM (User) | Rules Assistant (Agent) |
|---|---|
| Narrates scenes and atmosphere | Spawns character sub-agents for reactions |
| Sets DCs and difficulty | Looks up modifiers, presents applicable rules |
| Interprets dice results narratively | Rolls dice, presents raw numbers |
| Controls enemy behavior in the world | Runs enemy sub-agents for tactical decisions |
| Decides outcomes and consequences | Tracks HP, spell slots, conditions, turn order |

**The agent never asks the DM to play as a character.** Every character — hero or enemy — is driven by a sub-agent.

### Getting Started

To begin, please review the templates in `content/` and the core rules in `rules/`. The AI agents are configured in the `agents/` directory. See `.agents/skills/adventure/SKILL.md` for the orchestrator logic.

**Next Steps:**
1.  Review the content catalogs in `content/` for weapons, spells, and items.
2.  Define the core ruleset in `rules/core_rules.md` (armor table moved to `content/items/`).
3.  Develop the agent prompts in `agents/` to guide AI behavior.
4.  Create an MCP server with a dice-rolling function (e.g., `roll_dice(dice_set: list[int]) -> list[int]`).
5.  Test the flow by running a scenario.

### Content Catalogs

| Catalog | Path | Description |
|---------|------|-------------|
| **Weapons** | `content/weapons/weapons_catalog.md` | All weapons with damage dice, damage type, range, and special properties (finesse, thrown, versatile, etc.). |
| **Spells & Magic** | `content/spells/spells_catalog.md` | Index file. Spell definitions in `shared/` (by level), class lists in `classes/` (Cleric, Paladin, Wizard, Rogue). |
| **Items & Equipment** | `content/items/items_catalog.md` | Armor table (from core rules), shields, adventuring gear, tools, consumables, and currency. |
| **Enemies & Mobs** | `content/enemies/mob_template.md` | Creature templates organized by type, with scaling tables, behavior guidance, and attack definitions for AI-driven combat. |

### Rules Reference
The core ruleset in `rules/core_rules.md` now references the content catalogs for detailed tables. Armor types, equipment, and weapons are defined in their respective catalogs under `content/`, keeping the rules document focused on mechanics and formulas.

---
*Last updated: 2026-06-11*
