# Character & Enemy Management

This module handles loading character profiles and managing sub-agent interactions.

## Core Responsibilities

- Load party data for reference at the start of a session.
- Load specific enemy data when combat begins.
- Provide context for spawning character sub-agents.

### Loading Party Data

At the beginning of a session, load the party summary:

```bash
python3 adventure/character_loader.py --summary adventure/heroes/
```

### Loading Enemy Data

When combat starts, load specific enemy data:

```bash
python3 adventure/character_loader.py --load-enemy content/enemies/humanoids/goblin.md
```

### Character Sub-Agent Context

Build each sub-agent's prompt from `agents/prompts/character_system_prompt.md`, substituting:
- `{CHARACTER_NAME}` — Character name
- `{RACE_CLASS}` — Their race/class (e.g., "Human Paladin")
- `{CHARACTER_RAW_MD}` — Full raw markdown of their hero file (`adventure/heroes/{name}.md`)
- `{IMMEDIATE_SCENE}` — The DM's exact words for this moment (no additions)
- `{CONDITIONS}` — Any active conditions from session state

## Key Commands

### Load Party Summary
To get an overview of all heroes in the party:
```bash
python3 adventure/character_loader.py --summary adventure/heroes/
```

### Load Individual Character Profile
To load a specific hero's full details (for skill checks or reference):
```bash
python3 adventure/character_loader.py --load-character adventure/heroes/bram.md
```

### Load Enemy Data
When combat starts, load the enemy profile:
```bash
python3 adventure/character_loader.py --load-enemy content/enemies/humanoids/goblin.md
```

## Sub-Agent Prompt Construction

When spawning a sub-agent, use `agents/prompts/character_system_prompt.md` and substitute the following:

- `{CHARACTER_NAME}`: The name of the character.
- `{RACE_CLASS}`: Their race and class (e.g., "Human Paladin").
- `{CHARACTER_RAW_MD}`: The full content of their profile file.
- `{IMMEDIATE_SCENE}`: The DM's exact input for this moment.
- `{CONDITIONS}`: Any active status effects from the session state.

**Note:** Sub-agents are isolated and only see their own profile and the current scene.
