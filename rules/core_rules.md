# 📜 Core Game Ruleset: RPG-AI

This document serves as the authoritative mechanical reference for the RPG-AI simulation. All Character Agents must adhere to these rules when generating mechanical requests, and the DM must use these as the baseline for resolution.

## 🎲 1. The Core Resolution Engine

The system uses a **d20-based resolution engine**. Any action with an uncertain outcome is resolved via a Skill Check.

### 1.1 Skill Checks
A skill check determines whether a character succeeds in a specific task.
**Formula:** `d20 + Skill Modifier ≥ Difficulty Class (DC)`

- **Difficulty Class (DC)**: Set by the DM based on the task's complexity.
    - **Trivial**: DC 5
    - **Easy**: DC 10
    - **Moderate**: DC 15
    - **Hard**: DC 20
    - **Near Impossible**: DC 30
- **Modifiers**: Derived from the character's stats and skill proficiency.
    - **Terrible**: -3
    - **Poor**: -1
    - **Average**: +0
    - **Proficient**: +2
    - **Masterful**: +5

## ⚔️ 2. Combat Mechanics

Combat is a structured state that overrides standard narrative flow.

### 2.1 Initiative
At the start of combat, every participant rolls for Initiative to determine the turn order.
**Formula:** `d20 + Dexterity Modifier`

### 2.2 Action Economy
On their turn, a character may perform the following:
1.  **Standard Action**: Attack, use a skill, or interact with an object.
2.  **Move Action**: Move up to their defined speed limit.
3.  **Bonus Action**: (Optional) A quick action granted by specific abilities.

### 2.3 Attack & Damage
An attack is a skill check against the target's Armor Class (AC).
- **Hit**: If `d20 + Attack Modifier ≥ AC`, the attack hits.
- **Damage**: The damage is determined by the weapon's damage dice (e.g., 1d8 + Strength Modifier).

## 🛡️ 3. State & Condition Tracking

Characters can be affected by conditions that modify their rolls.
- **Advantage**: Roll two d20s and take the higher result.
- **Disadvantage**: Roll two d20s and take the lower result.
- **Prone**: Attacks against the character have Advantage; their own melee attacks have Disadvantage.

---
*Version 1.1.0 | Authority: Game Design Lead*
