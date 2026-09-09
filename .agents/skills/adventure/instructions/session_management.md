# Session Management

This module handles loading, resuming, and updating the game session state.

## Core Responsibilities

- Load or resume an existing session from `adventure/state/session.json`.
- Create a new session if one does not exist.
- Update session state (HP, spell slots, conditions, event logs) after meaningful beats.

### Starting a Session

When a session is first started:

```bash
# Step 1: Load or resume session
python3 adventure/game_state.py --load adventure/state/session.json 2>/dev/null

# If no session exists, create one:
python3 adventure/game_state.py --new-session "adventure-1" "Fog on the Road" --heroes-dir adventure/heroes/
```

### Updating State

After the DM narrates consequences or meaningful beats, update the state:

```bash
python3 adventure/game_state.py --update --state-file adventure/state/session.json \
      --hp "Bram=12" "Pip=11" "Sariel=9" \
      --spell-slots "Sariel/1st=2" \
      --conditions "Bram:" "Pip:" "Sariel:" \
      --log-event "Fog appears, party reacts"
```

## Key Commands

### Initialize or Resume Session
```bash
python3 adventure/game_state.py --load adventure/state/session.json
```

If no session exists:
```bash
python3 adventure/game_state.py --new-session "adventure-1" "Fog on the Road" --heroes-dir adventure/heroes/
```

### Update Session State
After a meaningful beat, update the state with the following information:
```bash
python3 adventure/game_state.py --update --state-file adventure/state/session.json \
      --hp "Bram=12" "Pip=11" "Sariel=9" \
      --spell-slots "Sariel/1st=2" \
      --conditions "Bram:" "Pip:" "Sariel:" \
      --log-event "Fog appears, party reacts"
```

## State Schema Reference

The session state tracks:
- **Party HP**: Current health for each hero.
- **Spell Slots**: Remaining slots per character and level.
- **Conditions**: Active status effects on characters.
- **Event Log**: A history of significant events in the current session.
