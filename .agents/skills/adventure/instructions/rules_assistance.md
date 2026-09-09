# Rules Assistance

This module provides guidance on looking up game rules and mechanics.

## Core Responsibilities

- Assist the DM in finding skill modifiers, weapon properties, spell details, and core rules.
- Provide clear citations for all rule lookups.

### Rule Lookup Commands & Resources

Help the DM look up rules:
- Skill modifiers: `python3 adventure/character_loader.py --load-character adventure/heroes/bram.md`
- Weapon damage/properties: `content/weapons/weapons_catalog.md`
- Spell details: `content/spells/shared/` and class-specific files
- Core mechanics: `rules/core_rules.md`

Always cite the source file when providing rules information.

### Skill Modifiers
To load a character's full profile for modifier lookup:
```bash
python3 adventure/character_loader.py --load-character adventure/heroes/bram.md
```

### Weapon Properties
Refer to the weapons catalog:
`content/weapons/weapons_catalog.md`

### Spell Details
Refer to the spells directory:
`content/spells/shared/` and class-specific files within `content/spells/classes/`.

### Core Rules
Refer to the core rules file:
`rules/core_rules.md`

**Always cite the source file when providing information.**
