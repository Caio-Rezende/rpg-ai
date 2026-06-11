# Agent Core Logic and Prompting

## Purpose

This file defines the core prompt structure and logic for the AI agents. It serves as the blueprint for how agents should behave, what information they need, and how they should structure their output to facilitate the DM's evaluation.

## Role Separation

**The user is the Dungeon Master (DM).** The agent is a rules assistant and character proxy — not a co-DM.

| DM (User) | Agent |
|---|---|
| Narrates scenes, atmosphere, world state | Presents character reactions in voice |
| Sets DCs and difficulty | Looks up modifiers, mechanics |
| Interprets dice results narratively | Rolls dice, presents raw numbers |
| Controls enemies and NPCs | Manages turn order, HP tracking |
| Decides outcomes | Tracks spell slots, conditions |

## Agent Roles

To maintain a clear distinction between game mechanics and character performance, we use two distinct layers of agency:

### 1. The Rules Assistant (Agent)
The **Rules Assistant** is the primary interface for the user (DM). It understands the `rules/core_rules.md` and manages mechanical state — HP, spell slots, conditions, turn order — but does not narrate the world or interpret outcomes.
*   **Responsibilities:** Presenting character reactions, declaring skill checks, rolling dice when asked, tracking numerical state, looking up rules for the DM.
*   **Context:** Uses the `summary.md`, current location, encounter details, and global game state.

### 2. The Character (Sub-Agent) Layer
When a character needs to act or speak, the Rules Assistant invokes a **Character Sub-Agent**. This limits the context to prevent characters from knowing information they shouldn't have.
*   **Responsibilities:** Generating dialogue, expressing unique personality traits, and stating intentions based on their specific goals and what they perceive in the scene.
*   **Context:** Uses only their individual profile (e.g., `heroes/bram.md`) and the immediate scene description provided by the DM. No knowledge of other characters' reactions, no meta-knowledge of the broader world.
*   **Isolation:** Each character sub-agent runs in an isolated context — spawned fresh with only their own profile and the scene. They do not see each other's outputs or the full game state.

## Prompting Guidelines

All prompts must include:
1.  **Context:** The current scene description from the DM.
2.  **Goal:** The agent's immediate objective (e.g., "React to this scene", "Declare your action").
3.  **Output Format:** Strict Markdown format for easy parsing by the DM.

---
*Last updated: 2026-06-11*
