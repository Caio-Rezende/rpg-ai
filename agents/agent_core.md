# Agent Core Logic and Prompting

## 🤖 Purpose

This file defines the core prompt structure and logic for the AI agents. It serves as the blueprint for how agents should behave, what information they need, and how they should structure their output to facilitate the DM's evaluation.

## 🧠 Agent Roles

To maintain a clear distinction between game mechanics and character performance, we use two distinct layers of agency:

### 1. The Game Master (GM) Agent
The **GM Agent** is the primary interface for the user (DM). It understands the `rules/core_rules.md` and manages the high-level state of the game.
*   **Responsibilities:** Evaluating skill checks, managing combat turns, tracking environmental changes, and ensuring all actions adhere to the core rules.
*   **Context:** Uses the `summary.md`, current location, encounter details, and global game state.

### 2. The Character (Sub-Agent) Layer
When a character needs to act or speak, the GM Agent invokes a **Character Sub-Agent**. This limits the context to prevent "hallucinating" knowledge from other characters or the wider world that they shouldn't know.
*   **Responsibilities:** Generating dialogue, expressing unique personality traits, and stating intentions based on their specific goals.
*   **Context:** Uses only their individual profile (e.g., `heroes/bram.md`) and the immediate scene description provided by the GM.

## ⚙️ Prompting Guidelines

All prompts must include:
1.  **Context:** The current scene description and the actions of other characters.
2.  **Goal:** The agent's immediate objective (e.g., "Escape the room," "Gather information").
3.  **Output Format:** Strict Markdown format for easy parsing by the DM.

---
*Last updated: 2026-06-09*