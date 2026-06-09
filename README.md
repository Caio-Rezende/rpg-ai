## RPG AI Agentic Project

This repository contains the structure and content for an AI-driven tabletop RPG experience. The goal is to create a chat-based game where the user acts as the Dungeon Master (DM), describing the scenario and prompting the AI characters to take actions.

### Project Structure

- **`content/`**: Contains templates for core game elements:
    - `characters/`: Character templates.
    - `locations/`: Location templates.
    - `encounters/`: Encounter templates.
- **`rules/`**: Contains the core ruleset for the game.
- **`agents/`**: Contains the logic and prompts for the AI agents that control the characters.
- **`README.md`**: This file.

### Game Flow

1.  **DM Input**: The user (DM) describes the scene and the characters present.
2.  **Core Agent Clarification**: The core agent evaluates the input. If details are missing, it asks the DM for clarification before proceeding.
3.  **Character Actions & Dice Preparation**: Characters use the provided context (location, encounter, DM details, and their own profile) to state their actions, what they intend to do, and why. Each action includes a dice set required for an MCP call (e.g., `[4, 6, 6, 20]`).
4.  **DM Difficulty Check**: The DM specifies the difficulty check (DC) or requirements for success.
5.  **Consequences & Loop**: The system summarizes the consequences of the actions, and the DM returns to step 1 to advance the narrative.

### Getting Started

To begin, please review the templates in `content/` and the core rules in `rules/`. The AI agents will be configured in the `agents/` directory.

**Next Steps:**
1.  Define the core ruleset in `rules/core_rules.md`.
2.  Develop the agent prompts in `agents/` to guide AI behavior.
3.  Create an MCP server with a dice-rolling function (e.g., `roll_dice(dice_set: list[int]) -> list[int]`).
4.  Test the flow by running a scenario.

---
*Last updated: 2026-06-09*
