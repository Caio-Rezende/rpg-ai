# 🤖 RPG-AI Agentic Orchestration Framework

This document defines the hierarchical agent architecture and the deterministic loop used to power the RPG-AI experience. The system is designed to move from ambiguous natural language (DM input) to deterministic tool execution (MCP dice rolling) through a multi-stage agentic pipeline.

## 🏗️ Hierarchical Architecture

The system employs a "Hub-and-Spoke" orchestration pattern to ensure narrative consistency and mechanical accuracy.

### 1. Core Clarification Agent (The Orchestrator)
**Role:** The primary interface between the Dungeon Master (DM) and the simulation.
**Responsibility:** 
- **Context Validation:** Analyzes the DM's input to ensure all necessary variables are present (Who is acting? Where are they? What is the objective?).
- **Gap Analysis:** If the input is ambiguous (e.g., "The fight starts" without specifying who is fighting), the agent halts the loop and requests specific clarification from the DM.
- **Context Assembly:** Once validated, it gathers relevant data from `/content/characters`, `/content/locations`, and `/content/encounters` to create a "Turn Brief" for the Actor Agents.

### 2. Character Agents (The Actors)
**Role:** High-fidelity personas representing NPCs or PCs.
**Responsibility:**
- **Persona-Driven Decision Making:** Uses the Turn Brief and the character's specific attributes/motivations to determine the most authentic action.
- **Mechanical Intent:** Translates narrative intent into a mechanical request. Instead of "rolling a die," the agent specifies the *exact dice set* required for the action based on the `rules/core_rules.md`.
- **Output Structure:** Every Character Agent must output in the following format:
    - **Internal Monologue:** (Hidden from DM) The reasoning behind the choice.
    - **Narrative Action:** The descriptive text of what the character does.
    - **Mechanical Request:** The precise MCP tool call: `roll_dice([count, sides, ...])`.

---

## 🔄 The Agentic Loop (Deterministic Flow)

To maintain a "Staff-level" engineering signal, the system follows a strict state machine:

1.  **INPUT STATE**: DM provides a narrative prompt.
2.  **CLARIFICATION STATE**: 
    - `Core Clarification Agent` $\rightarrow$ Validates Context.
    - If $\text{Invalid} \rightarrow$ Request Clarification $\rightarrow$ Return to **INPUT STATE**.
    - If $\text{Valid} \rightarrow$ Generate Turn Brief $\rightarrow$ Proceed to **ACTION STATE**.
3.  **ACTION STATE**: 
    - `Character Agents` $\rightarrow$ Process Turn Brief $\rightarrow$ Generate Narrative Action + Dice Set.
4.  **EXECUTION STATE**: 
    - The system invokes the `dice_roller` MCP server with the provided `dice_set`.
    - Results are returned to the DM.
5.  **RESOLUTION STATE**: 
    - DM evaluates results against Difficulty Class (DC) $\rightarrow$ Describes consequences $\rightarrow$ Return to **INPUT STATE**.

## 🛠️ Integration Points

- **MCP Server**: The `roll_dice` tool provides the only source of truth for randomness, preventing "AI hallucinations" of success or failure.
- **Content Templates**: Character and Location templates provide the "ground truth" state that agents must adhere to, ensuring characters don't suddenly change personalities or locations.
