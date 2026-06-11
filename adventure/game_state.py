#!/usr/bin/env python3
"""Session state tracker for RPG adventures."""

import argparse
import json
import os
from datetime import datetime

DEFAULT_STATE_DIR = "adventure/state"
DEFAULT_SESSION_FILE = os.path.join(DEFAULT_STATE_DIR, "session.json")


def _now():
    return datetime.now().isoformat()


def load_characters_simple(heroes_dir):
    from character_loader import load_party
    chars = {}
    for c in load_party(heroes_dir):
        chars[c["name"]] = {
             "hp_current": c["combat"]["hp_current"],
             "hp_max": c["combat"]["hp_max"],
             "spell_slots": dict(c.get("spells", {}).get("spell_slots", {})),
             "conditions": [],
             "notes": "",
         }
    return chars


def new_session(session_id, scene_name, heroes_dir="adventure/heroes/",
                state_file=DEFAULT_SESSION_FILE):
    chars = load_characters_simple(heroes_dir)
    state = {
         "session_id": session_id,
         "started_at": _now(),
         "last_updated": _now(),
         "scene": {
             "name": scene_name,
             "phase": "exploration",
             "description": "",
         },
         "characters": chars,
         "combat": {"active": False, "initiative_order": [], "current_turn": 0, "enemies": []},
         "turn_log": [],
     }
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    save_session(state, state_file)
    return state


def load_session(state_file=DEFAULT_SESSION_FILE):
    if not os.path.exists(state_file):
        return None
    with open(state_file, "r") as f:
        return json.load(f)


def save_session(state, state_file=DEFAULT_SESSION_FILE):
    state["last_updated"] = _now()
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def update_hp(state, updates, state_file=DEFAULT_SESSION_FILE):
    if "characters" not in state:
        state = load_session(state_file) or {}
    for entry in updates:
        name, val = entry.split("=")
        name = name.strip()
        new_hp = int(val.strip())
        chars = state.get("characters", {})
        if name in chars:
            chars[name]["hp_current"] = max(0, min(new_hp, chars[name].get("hp_max", 99)))
    save_session(state, state_file)
    return state


def update_spell_slots(state, updates, state_file=DEFAULT_SESSION_FILE):
    if "characters" not in state:
        state = load_session(state_file) or {}
    for entry in updates:
        name, val = entry.split("=")
        name = name.strip()
        level, count = val.strip().split("/")
        chars = state.get("characters", {})
        if name in chars:
            chars[name].setdefault("spell_slots", {})[level] = int(count)
    save_session(state, state_file)
    return state


def update_conditions(state, updates, state_file=DEFAULT_SESSION_FILE):
    if "characters" not in state:
        state = load_session(state_file) or {}
    for entry in updates:
        name, conds = entry.split(":", 1)
        name = name.strip()
        condition_list = [c.strip() for c in conds.split(",") if c.strip()]
        chars = state.get("characters", {})
        if name in chars:
            chars[name]["conditions"] = condition_list
    save_session(state, state_file)
    return state


def set_scene(state, scene_name, phase="exploration",
              description="", state_file=DEFAULT_SESSION_FILE):
    if "scene" not in state:
        state = load_session(state_file) or {}
    state.setdefault("scene", {})["name"] = scene_name
    state["scene"]["phase"] = phase
    state["scene"]["description"] = description
    save_session(state, state_file)
    return state


def add_log_entry(state, event, rolls=None, state_file=DEFAULT_SESSION_FILE):
    if "turn_log" not in state:
        state = load_session(state_file) or {}
    state.setdefault("turn_log", []).append({
         "turn": len(state.get("turn_log", [])) + 1,
         "event": event,
         "rolls": rolls or [],
     })
    save_session(state, state_file)
    return state


def main():
    parser = argparse.ArgumentParser(description="Manage RPG session state")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--new-session", nargs=2, metavar=("ID", "SCENE"),
                       help="Create new session: ID SCENE_NAME")
    group.add_argument("--update", action="store_true", help="Update existing session state")
    group.add_argument("--load", nargs="?", const=DEFAULT_SESSION_FILE, metavar="FILE",
                       help="Load and print session state")
    group.add_argument("--set-scene", nargs=3, metavar=("NAME", "PHASE", "DESC"),
                       help="Update scene info")

    parser.add_argument("--heroes-dir", default="adventure/heroes/",
                        help="Directory with character markdown files")
    parser.add_argument("--state-file", default=DEFAULT_SESSION_FILE,
                        help="Session state JSON file path")
    parser.add_argument("--hp", nargs="+", metavar="NAME=HP", help="Set HP for characters")
    parser.add_argument("--spell-slots", nargs="+", metavar="NAME/LEVEL=COUNT",
                        help="Set remaining spell slots")
    parser.add_argument("--conditions", nargs="+", metavar="NAME:COND,...",
                        help="Set conditions for characters")
    parser.add_argument("--log-event", nargs="?", const="", metavar="EVENT",
                        help="Add a turn log entry")

    args = parser.parse_args()

    if args.new_session:
        sid, scene = args.new_session
        state = new_session(sid, scene, heroes_dir=args.heroes_dir,
                            state_file=args.state_file)
        print(json.dumps(state, indent=2))

    elif args.load:
        state = load_session(args.load)
        if state is None:
            print(f"No session found at {args.load}")
            return
        print(json.dumps(state, indent=2))

    elif args.set_scene:
        name, phase, desc = args.set_scene
        state = load_session(args.state_file) or {}
        set_scene(state, name, phase, desc, state_file=args.state_file)
        print(json.dumps(state, indent=2))

    elif args.update:
        state = load_session(args.state_file) or {}
        if args.hp:
            update_hp(state, args.hp, state_file=args.state_file)
        if args.spell_slots:
            update_spell_slots(state, args.spell_slots, state_file=args.state_file)
        if args.conditions:
            update_conditions(state, args.conditions, state_file=args.state_file)
        if args.log_event is not None:
            add_log_entry(state, args.log_event or "", state_file=args.state_file)
        print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
