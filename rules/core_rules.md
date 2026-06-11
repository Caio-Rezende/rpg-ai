# Core Game Ruleset

## 📜 Overview

This document contains the foundational rules for the TTRPG. All character actions, combat resolutions, and skill checks must be evaluated against these rules.

## 🎲 Core Mechanics

### Skill Modifiers
Skill modifiers are derived from the relevant attribute score using the standard formula:

*    **Formula:** `Modifier = (Attribute // 2) - 10`
*    **Clamping:** All modifiers are clamped between **-3** (terrible) and **+5** (masterful).

| Attribute | Modifier | Attribute | Modifier |
|-----------|----------|-----------|----------|
| 8-9       | -1       | 14-15     | +2       |
| 10-11     | +0       | 16        | +3       |

*Example:* STR 15 → (15 // 2) - 10 = 7 - 10 = **-3**, clamped to **-3**.  
*Example:* DEX 16 → (16 // 2) - 10 = 8 - 10 = **-2**.

### Skill Checks
A skill check is resolved by rolling a d20 and adding the relevant skill modifier. The result must meet or exceed a Difficulty Class (DC) set by the DM.
*    **Formula:** `d20 + Skill Modifier ≥ DC`
*   **Modifiers:** Skills are rated from -3 (terrible) to +5 (masterful).

### Combat
Combat is turn-based and proceeds through distinct phases:
1.  **Initiative:** Determined by a roll (d20 + Agility Modifier).
2.  **Action Phase:** Each character gets one action (Attack, Skill Use, Item Use).
3.  **Movement Phase:** Characters move up to their speed limit.
4.  **End Turn:** The character passes initiative to the next person.

### Damage
Damage is calculated by summing the weapon's base damage and any relevant modifiers. Damage types (Slashing, Piercing, Bludgeoning) must be tracked.

## ❤️ Hit Points (HP)

Hit Points represent a character's ability to withstand injury. When HP reaches 0, the character falls unconscious and begins dying.

### Starting HP
At level 1, a character's HP is determined the max number on their class hit die then adding their Constitution modifier (only if positive):

*     **Formula:** `Starting HP = (MAX of Hit Die) + MAX(0, CON Modifier)`

### Class Hit Dice

| Class          | Hit Die | Example              |
|----------------|---------|----------------------|
| Paladin        | d10     | Roll 1d10 + CON      |
| Rogue          | d8      | Roll 1d8 + CON       |
| Cleric         | d8      | Roll 1d8 + CON       |
| Fighter        | d10     | Roll 1d10 + CON      |
| Wizard         | d6      | Roll 1d6 + CON       |
| Barbarian      | d12     | Roll 1d12 + CON      |

### Level-Up HP
When a character gains a level, they roll their hit die again and add their CON modifier.

*     **Formula:** `New HP = Current HP + Roll(Hit Die) + CON Modifier`

### Healing
Characters can recover HP through rest, healing magic, or consumable items. Maximum HP cannot be exceeded unless specified by a special ability or spell.

## �️ Armor Class (AC)

Armor Class determines how hard it is to hit a character in combat. Attackers must meet or exceed the target's AC with their attack roll (d20 + attack modifier).

### Starting AC
AC is calculated based on armor worn and Dexterity modifier:

*     **Formula:** `AC = Armor Base + MAX(0, DEX Modifier)` (unless armor prohibits DEX bonus)

### Armor Reference
For the complete list of armor types, shields, and equipment, see [`content/items/items_catalog.md`](content/items/items_catalog.md).

### Character Sheet Requirement
Every character sheet must explicitly list their Armor Class under Combat Stats.

## �👤 Character Creation

### Attributes
Characters have six core attributes: Strength (STR), Dexterity (DEX), Constitution (CON), Intelligence (INT), Wisdom (WIS), and Charisma (CHA).

*   **Attribute Generation:** Each attribute is determined by rolling a d20.
*   **Clamping:** All individual attribute scores must be clamped between a minimum of 8 and a maximum of 16.
*   **Minimum Attribute Sum Rule:** To ensure characters are sufficiently capable, the sum of all six attributes must be at least 65. If the total sum is less than 65, all attributes for that character must be rerolled until this condition is met.

### Agentic Roleplay Rules
To maintain immersion and character consistency, use a subagent when acting as or responding for a specific character. The subagent should be provided with the character's full profile (including Traits and Goals) as its primary context to ensure they act according to their unique personality and motivations.

### Enemies & Encounters Reference
For enemies in combat, see content/enemies/mob_template.md. For encounter scenarios, see content/encounters/encounter_template.md. Creatures are organized by type (aberration, animal, construct, undead, celestial, demoniac, animated, treelike) and each has inherent traits that affect spell interactions and combat behavior.

---
*Last updated: 2026-06-09*