# Mob Template

## 📝 Overview

This template defines enemies and creatures for encounters. Each creature entry should be compact but include enough detail for the AI to run dynamic combat. Creatures are organized by type and scaled by party level.

See individual creature type files in this directory for complete entries.

## 🧩 Fields

*   **Name:** [Creature name] — a recognizable identifier (e.g., *Goblin Scout*, *Shadow Mite*)
*   **Type:** [Aberration | Animal | Construct | Undead | Celestial | Demoniac | Animated | Treelike | Humanoid]
*   **CR (Challenge Rating):** [Level this creature is appropriate for, 1-20]
*   **Group Size:** [Average number that appear together: Solo | 1-2 | 3-4 | 5+ ]
*   **AC:** [Armor Class value]
*   **HP:** [Hit Points, scaled by CR]
*   **Speed:** [Movement speed, e.g., 30 ft.]

## 🎨 Description

A short visual description (1-2 sentences). What does the creature look like? Include size (Tiny/Small/Medium/Large). Keep it vivid but concise — the AI uses this for scene-setting.

```
[Description text]
```

## ⚔️ Attacks

One or two attack entries. Combine melee with ranged/spell when the creature has both to keep entries compact.

*   **[Attack Name]:** [Bonus] to hit, [Range], [Damage] [Damage type]. [Optional effect.]
*   **[Second Attack]:** [Same format, if applicable.]

### Attack Examples

```
Claws: +4 to hit, Melee (5 ft.), 1d6+2 slashing. On a hit, target must succeed on a DC 12 CON save or be Poisoned for 1 round.
Dark Bolt: +3 to hit, Ranged (60 ft.), 2d4 necrotic. Ignores cover.
```

## 🧠 Behavior

How the creature acts in combat and social encounters. This guides AI decision-making.

*   **Temperament:** [Aggressive | Defensive | Cunning | Neutral | Fleeing]
*   **Target Priority:** [Who they attack first: e.g., "casts on healers", "goes for the biggest threat", "attacks randomly"]
*   **Tactics:** [Combat style: e.g., "ambush from hiding", "flank with pack mates", "kite with ranged attacks"]
*   **Morale:** [When they break: e.g., "flees at 50% HP", "fights to the death", "rars when 25% of group dies"]
*   **Special Behavior:** [Any unique actions: ambush, sneak, intimidate, use environment, etc.]

### Behavior Examples

```
Temperament: Cunning
Target Priority: Isolates stragglers; targets casters first to deny healing
Tactics: Ambushes from trees; uses pack coordination to surround prey
Morale: Leader fights to death; minions flee when leader falls
Special Behavior: Can hide in forest terrain (DC 15 Persuasion to detect)
```

## 📏 Type Traits

Each creature type has inherent traits that affect how they interact with spells and items. Use these as a reference when writing creatures of each type.

| Type       | Common Traits                                      | Spell Vulnerabilities          | Spell Resistances      |
|------------|----------------------------------------------------|-------------------------------|------------------------|
| Aberration | Mind-based, alien thinking                         | Charm, Fear                   | None typical           |
| Animal     | Beast instincts, no reason                         | Charm, Calm Animals           | Necrotic (half)        |
| Construct  | No biology, immune to mind effects                 | Poison, Disease               | Lightning, Thunder     |
| Undead     | No soul, dark presence                             | Radiant, Holy                 | Necrotic (immune)      |
| Celestial  | Good-aligned, may spare defeated foes              | Radiant resistance            | None                   |
| Demoniac   | Evil, corrupting aura                              | Fire, Holy                    | Radiant (half)         |
| Animated   | No mind, driven by spell that animates             | Intelligence-based.           | None                   |
| Treelike   | Part plant, slow but durable                       | Cold, Frost, Fire             | Poison (immune)        |
| Humanoid     | Sentient race, can be reasoned with              | Charm (low CR), Fear            | None                     |

## 📐 Scaling by Level

Use these guidelines to scale creatures for the party's level:

| Party Level | HP Range    | AC Range | Attack Bonus | Damage Output | Group Size     |
|-------------|-------------|----------|--------------|---------------|----------------|
| 1-2         | 5-20        | 10-13    | +1 to +2     | 1d4-1d8       | 3-5 weak mobs  |
| 3-4         | 20-45       | 13-15    | +2 to +3     | 1d6-2d6       | 2-4 medium mobs|
| 5-6         | 45-80       | 15-17    | +3 to +4     | 2d6-3d6       | 1-3 tough mobs |
| 7-9         | 80-150      | 17-18    | +4 to +5     | 3d6-4d8       | Solo or 1-2    |
| 10+         | 150+        | 18+      | +5 to +7     | 4d8+          | Solo bosses    |

## 📄 Example Entry

**Name:** Gloom Spider
**Type:** Animal
**CR:** 2
**Group Size:** 3-4
**AC:** 12
**HP:** 15
**Speed:** 40 ft. (climbing 60 ft.)

**Description:** Small. A pale, emaciated spider the size of a large dog, with jagged legs and a web-slicked carapace that glistens in darkness. Drips acidic venom from fanged mandibles.

**Attacks:**
*   **Bite:** +3 to hit, Melee (5 ft.), 1d8 piercing. Target must succeed on a DC 11 CON save or take 1d4 poison damage and be Slowed for 1 round.
*   **Web:** +2 to hit, Ranged (30 ft.). Target is Restrained (DC 11 STR to break). Web burns away (1d6 fire) at the start of the creature's next turn.

**Behavior:**
*   **Temperament:** Cunning
*   **Target Priority:** Pins down isolated targets; avoids engaging the whole group at once
*   **Tactics:** Ambushes from ceiling or walls; uses web to separate prey before striking
*   **Morale:** Flees if more than 2 party members are engaged or drops below 25% HP
*   **Special Behavior:** Can hide in darkness (DC 13 Perception). Immune to charm and fear.

---
*Last updated: 2026-06-10*
