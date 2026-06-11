# Encounter Template

## ⚔️ Encounter Scenario

This template is used to structure a challenge or event that the party must face. It must provide enough detail for the AI to generate a dynamic scene.

## 🧩 Fields

*   **Title:** A catchy name for the encounter.
*   **Type:** (e.g., Combat, Social, Puzzle, Environmental).
*   **Setup:** The initial description and context for the encounter. This sets the scene.
*    **Participants:** List of NPCs or creatures involved. For enemies, use mob entries from [`content/enemies/`](content/enemies/) (e.g., *[Mob: Gloom Spider ×3]*). For NPCs, use character templates from [`content/characters/`](content/characters/). See [`content/enemies/mob_template.md`](content/enemies/mob_template.md) for creating new creatures.
*   **Goal/Challenge:** What the party must achieve or overcome. This is the core objective.
*   **Rules/Mechanics:** Specific rules from `rules/core_rules.md` that apply (e.g., "Requires a successful DC 15 Wisdom (Perception) check to spot").
*   **Resolution Options:** Potential outcomes based on player actions, including potential failure states.

## 💡 Example

**Title:** The Ambush at the Crossroads
**Type:** Combat
**Setup:** The party is traveling through a narrow mountain pass when three heavily armed bandits jump out from behind a rock formation.
**Participants:** 3 Bandits (Level 2), 1 Leader (Level 3).
**Goal/Challenge:** Defeat the bandits or negotiate passage.
**Rules/Mechanics:** Combat rules apply. Initiative is key.
**Resolution Options:** Combat (high difficulty), Stealth (requires successful checks), Diplomacy (requires high Charisma).

---
*Last updated: 2026-06-09*