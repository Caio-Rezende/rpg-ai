# Agent Core Logic and Prompting

## 🤖 Purpose

This file defines the core prompt structure and logic for the AI agents. It serves as the blueprint for how agents should behave, what information they need, and how they should structure their output to facilitate the DM's evaluation.

## 🧠 Agent Roles

*   **NPC Agent:** Responsible for generating actions, dialogue, and motivations for a specific NPC.
*   **Environment Agent:** Responsible for describing the immediate surroundings and reacting to actions.
*   **Narrative Agent:** Responsible for maintaining the overall tone and pacing of the scene.

## ⚙️ Prompting Guidelines

All prompts must include:
1.  **Context:** The current scene description and the actions of other characters.
2.  **Goal:** The agent's immediate objective (e.g., "Escape the room," "Gather information").
3.  **Output Format:** Strict Markdown format for easy parsing by the DM.

---
*Last updated: 2026-06-09*