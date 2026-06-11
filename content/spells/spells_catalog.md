# Spells & Magic Catalog

## ✨ Overview

This catalog is organized into two parts:

1. **Shared Spell Definitions** — Complete spell stats (school, casting time, range, duration, description) grouped by level. These are the building blocks reused across classes.
2. **Class Spell Lists** — Which spells each class can prepare and cast, organized by subclass/domain/oath/tradition.

---

## 📖 Spellcasting Rules

* **Spell Slots:** Casters have a number of spell slots per level, recovered on a long rest.
* **Cantrips:** Level 0 spells that can be cast at will, without using a spell slot.
* **Spell Save DC:** `10 + Proficiency Bonus + Spellcasting Ability Modifier`
* **Spell Attack Bonus:** `Proficiency Bonus + Spellcasting Ability Modifier`

### Schools of Magic

| School | Description |
|--------|-------------|
| **Abjuration** | Defensive spells that protect or banish. |
| **Conjuration** | Spells that summon objects or creatures. |
| **Divination** | Spells that reveal information or the future. |
| **Enchantment** | Spells that influence or control minds. |
| **Evocation** | Spells that create energy or elemental effects. |
| **Illusion** | Spells that create false sensory perceptions. |
| **Necromancy** | Spells that manipulate life force or death. |
| **Transmutation** | Spells that alter the properties of objects or creatures. |

---

## 📚 Shared Spell Definitions

Browse spells by level — these are the full spell definitions reused across all class lists:

| Level | File |
|-------|------|
| **Cantrips** | [shared/cantrips.md](shared/cantrips.md) — 13 cantrips (Burning Hands, Guidance, Light, Sacred Flame, etc.) |
| **1st Level** | [shared/1st_level.md](shared/1st_level.md) — 29 first-level spells (Bless, Cure Wounds, Magic Missile, etc.) |
| **2nd Level** | [shared/2nd_level.md](shared/2nd_level.md) — 16 second-level spells (Lesser Restoration, Spirit Guardians, etc.) |
| **3rd Level** | [shared/3rd_level.md](shared/3rd_level.md) — 11 third-level spells (Beacon of Hope, Revivify, etc.) |

---

## 🧙 Class Spell Lists

Find which spells each class can cast, organized by subclass:

| Class | File | Subclasses |
|-------|------|------------|
| **Cleric** | [classes/cleric.md](classes/cleric.md) | Life Domain, Nature Domain, Knowledge Domain, Light Domain, Tempest Domain |
| **Paladin** | [classes/paladin.md](classes/paladin.md) | Oath of Devotion, Oath of the Ancients, Oath of Vengeance |
| **Wizard** | [classes/wizard.md](classes/wizard.md) | School of Abjuration, School of Evocation, School of Divination, School of Transmutation |
| **Rogue** | [classes/rogue.md](classes/rogue.md) | Arcane Trickster (level 3+) |

---

## 🔗 Adding New Spells

To add a spell to the catalog:

1. Add the spell definition to the appropriate `shared/` file (by level).
2. Reference the spell from any class list in `classes/` that can cast it.
3. Update this index if you create a new class or subclass file.

---

*Last updated: 2026-06-09*
