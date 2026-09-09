# Combat & Initiative Management

This module handles the mechanics of combat, including initiative and turn order.

## Core Responsibilities

- Roll initiative for all participants.
- Manage turn order during combat.
- Provide guidance on combat flow.

### Rolling Initiative

When combat begins, roll initiative for all participants:

```bash
python3 mcp-server/dice_cli.py 1d20 1d20 1d20 1d20 1d20 1d20
```

### Turn Order & Flow

Process turns strictly by initiative order, starting from position #1 downward.

- **No surprise rounds or free enemy actions unless the DM explicitly declares them.** The first round includes everyone's turn in initiative order, heroes included.
- On each hero's turn, spawn a character sub-agent for their action declaration.
- On each enemy's turn, spawn an enemy sub-agent based on the creature's behavior profile.

### Combat Flow Summary

1. Load enemy data.
2. Roll initiative.
3. Present initiative order.
4. DM narrates hits/misses/damage. Update HP after confirmation.
5. Reference enemy morale thresholds.

## Key Commands

### Roll Initiative
To roll initiative for a group of participants:
```bash
python3 mcp-server/dice_cli.py 1d20 1d20 1d20 1d20 1d20 1d20
```

## Combat Flow & Turn Order

Combat follows a strict turn order based on initiative results:

1. **Initiative Order:** Process turns from highest to lowest initiative score.
2. **Turn Execution:** On each participant's turn, spawn a sub-agent (hero or enemy) to declare their action.
3. **DM Oversight:** The DM narrates the outcome of actions (hits, misses, damage).
4. **State Updates:** Update HP and other stateful information after the's confirmed by the DM.

**Important:** No surprise rounds or free actions unless explicitly declared by the DM. All turns, including heroes', are processed in initiative order from Round 1.
