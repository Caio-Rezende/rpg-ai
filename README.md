## RPG AI Agentic Project

This repository contains the structure and content for an AI-driven tabletop RPG experience. The goal is to create a chat-based game where the user acts as the Dungeon Master (DM), describing the scenario and prompting the AI characters to take actions.

### Project Structure

- **`content/`**: Contains templates for core game elements:
    - `characters/`: Character templates.
    - `locations/`: Location templates.
    - `encounters/`: Encounter templates.
- **`adventure/`**: Contains the current campaign data:
    - `summary.md`: Overview of the adventure and party members.
    - `heroes/`: Detailed profiles for each character in the party.
- **`rules/`**: Contains the core ruleset for the game.
- **`agents/`**: Contains the logic and prompts for the AI agents that control the characters.
- **`README.md`**: This file.

### Game Flow

1.  **DM Input**: The user (DM) describes the scene and the characters present.
2.  **Core Agent Clarification**: The GM Agent evaluates the input. If details are missing, it asks the DM for clarification before proceeding.
3.  **Character Actions & Dice Preparation**: Characters use the provided context (location, encounter, DM details, and their own profile) to state their actions, what they intend to do, and why. Each action includes a dice set required for an MCP call (e.g., `[4, 6, 6, 20]`).
4.  **DM Difficulty Check**: The DM specifies the difficulty check (DC) or requirements for success.
5.  **Consequences & Loop**: The system summarizes the consequences of the actions, and the DM returns to step 1 to advance the narrative.

### Agent Architecture

To maintain a clear distinction between game mechanics and character performance, we use two distinct layers of agency:

#### 1. The Game Master (GM) Agent
The **GM Agent** is the primary interface for the user (DM). It understands the `rules/core_rules.md` and manages the high-level state of the game.
*   **Responsibilities:** Evaluating skill checks, managing combat turns, tracking environmental changes, and ensuring all actions adhere to the core rules.
*   **Context:** Uses the `adventure-1/summary.md`, current location, encounter details, and global game state.

#### 2. The Character (Sub-Agent) Layer
When a character needs to act or speak, the GM Agent invokes a **Character Sub-Agent**. This limits the context to prevent "hallucinating" knowledge from other characters or the wider world that they shouldn't know.
*   **Responsibilities:** Generating dialogue, expressing unique personality traits, and stating intentions based on their specific goals.
*   **Context:** Uses only their individual profile (e.g., `adventure-1/heroes/bram.md`) and the immediate scene description provided by the GM.

### Getting Started

To begin, please review the templates in `content/` and the core rules in `rules/`. The AI agents will be configured in the `agents/` directory.

**Next Steps:**
1.  Define the core ruleset in `rules/core_rules.md`.
2.  Develop the agent prompts in `agents/` to guide AI behavior.
3.  Create an MCP server with a dice-rolling function (e.g., `roll_dice(dice_set: list[int]) -> list[int]`).
4.  Test the flow by running a scenario.

---
*Last updated: 2026-06-09*
