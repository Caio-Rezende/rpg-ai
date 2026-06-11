#!/usr/bin/env python3
"""Load character and enemy markdown files into structured dicts."""

import argparse
import glob
import json
import os
import re


def compute_modifier(score):
    mod = (score // 2) - 10
    return max(-3, min(5, mod))


def parse_stats(text):
    stats = {}
    pattern = r'\*\s*\*\*(?:[A-Za-z]+ )?\((ST|STR|DE|DEX|CO|CON|IN|INT|WI|WIS|CH|CHA)\)[^:]*:\*\*\s*(\d+)'
    for line in text.split("\n"):
        m = re.search(pattern, line, re.IGNORECASE)
        if m:
            abbrev = m.group(1).upper()
            map_ = {"ST": "STR", "DE": "DEX", "CO": "CON", "IN": "INT",
                    "WI": "WIS", "CH": "CHA"}
            stats[map_.get(abbrev, abbrev)] = int(m.group(2))
    return stats


def parse_line(text, pattern):
    for line in text.split("\n"):
        m = re.search(r'\*\s*' + pattern + r':\*\*\s*(.+)', line)
        if m:
            return m.group(1).strip()
    return None


def parse_section(text, header):
    lines = text.split("\n")
    in_section = False
    section_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            if header.lower() in stripped.lower():
                in_section = True
                section_lines = []
                continue
            elif in_section:
                break
        if in_section:
            section_lines.append(line)
    return "\n".join(section_lines)


def parse_skills(section_text):
    skills = {}
    for line in section_text.split("\n"):
        m = re.search(r'\*\s*(?:\*\*)?Skills:\*\*\s*(.+)', line)
        if m:
            skill_str = m.group(1)
            for part in skill_str.split(","):
                sm = re.search(r'([A-Za-z ]+)\s*\((\+?\-?\d+)\)', part)
                if sm:
                    skills[sm.group(1).strip()] = int(sm.group(2))
    return skills


def parse_equipment(section_text):
    for line in section_text.split("\n"):
        m = re.search(r'\*\s*(?:\*\*)?Equipment:\*\*\s*(.+)', line)
        if m:
            items = [i.strip() for i in m.group(1).split(",")]
            return [i for i in items if i]
    return []


def parse_weapons(section_text):
    weapons = []
    for line in section_text.split("\n"):
        m = re.match(r'\s*\*\s*\*\*([^*]+)\*\*\s*[—–]\s*(.+)', line)
        if m:
            name = m.group(1).strip()
            detail = m.group(2).strip()
            weapon = {"name": name, "detail": detail}
            dmg_m = re.search(r'(\d+d\d+)(\s+\w+)?', detail)
            if dmg_m:
                weapon["damage"] = dmg_m.group(1)
                weapon["damage_type"] = dmg_m.group(2).strip() if dmg_m.group(2) else ""
            if "melee" in detail.lower():
                weapon["range"] = "melee"
            elif "ranged" in detail.lower() or "thrown" in detail.lower():
                weapon["range"] = "ranged"
            weapons.append(weapon)
    return weapons


def parse_spells(section_text):
    spells = {
        "spellcasting_ability": None,
        "spell_save_dc": None,
        "spell_attack_bonus": None,
        "cantrips": [],
        "level_1_spells": [],
        "spell_slots": {},
        "domain": None,
    }

    for line in section_text.split("\n"):
        dc_m = re.search(r'\*\s*(?:\*\*)?Spell Save DC:\*\*\s*(.+)', line)
        if dc_m:
            dm = re.search(r'(\d+)', dc_m.group(1))
            if dm:
                spells["spell_save_dc"] = int(dm.group(1))

        atk_m = re.search(r'\*\s*(?:\*\*)?Spell Attack Bonus:\*\*\s*(.+)', line)
        if atk_m:
            am = re.search(r'(\+?\-?\d+)', atk_m.group(1))
            if am:
                spells["spell_attack_bonus"] = int(am.group(1))

        abi_m = re.search(r'\*\s*(?:\*\*)?Spellcasting Ability:\*\*\s*(.+)', line)
        if abi_m:
            spells["spellcasting_ability"] = abi_m.group(1).strip()

        domain_m = re.search(r'\*\s*(?:\*\*)?Domain:\*\*\s*(.+)', line)
        if domain_m:
            spells["domain"] = domain_m.group(1).strip()

        cantrip_m = re.search(r'\*\s*(?:\*\*)?Cantrips Known:\*\*\s*(.+)', line)
        if cantrip_m:
            text = cantrip_m.group(1)
            if "None" in text or "none" in text:
                spells["cantrips"] = []
            else:
                spells["cantrips"] = [s.strip() for s in re.findall(r'\*([^*]+)\*', text)]

        l1_m = re.search(r'\*\s*(?:\*\*)?1st Level Spells:\*\*\s*(.+)', line)
        if l1_m:
            text = l1_m.group(1)
            spells["level_1_spells"] = [s.strip() for s in re.findall(r'\*([^*]+)\*', text)]

        slot_m = re.search(r'\*\s*(?:\*\*)?Spell Slots:\*\*\s*(\d+)\s*(?:1st|first)', line)
        if slot_m:
            spells["spell_slots"] = {"1st": int(slot_m.group(1))}

    return spells


def load_character(filepath):
    with open(filepath, "r") as f:
        raw = f.read()

    name = os.path.basename(filepath).replace(".md", "")
    for line in raw.split("\n"):
        m = re.match(r'^# (.+)$', line)
        if m:
            name = m.group(1).strip()
            break

    race_class = parse_line(raw, r'Race/Class') or ""
    level = 1
    rc_m = re.search(r'\(Level\s+(\d+)\)', race_class)
    if rc_m:
        level = int(rc_m.group(1))

    stats_text = parse_section(raw, "Core Stats")
    stats = parse_stats(stats_text)

    combat_text = parse_section(raw, "Combat")
    hp_str = parse_line(combat_text, r'Hit Points') or "0 / 0"
    hp_parts = hp_str.split("/")
    hp_current = int(hp_parts[0].strip()) if len(hp_parts) > 0 else 0
    hp_max = int(hp_parts[1].strip()) if len(hp_parts) > 1 else hp_current

    ac_str = parse_line(combat_text, r'Armor Class') or "10"
    ac_m = re.search(r'(\d+)', ac_str)
    ac = int(ac_m.group(1)) if ac_m else 10

    speed_str = parse_line(combat_text, r'Speed') or "30 ft."
    speed_m = re.search(r'(\d+)', speed_str)
    speed = int(speed_m.group(1)) if speed_m else 30

    hit_die = parse_line(combat_text, r'Hit Die') or "d8"

    skills_section = parse_section(raw, "Skills & Abilities")
    skills = parse_skills(skills_section)
    equipment = parse_equipment(skills_section)

    weapons = parse_weapons(parse_section(raw, "Weapons"))
    spells = parse_spells(parse_section(raw, "Spells & Magic"))

    traits_text = parse_section(raw, "Traits")
    appearance = parse_line(traits_text, r'Appearance') or ""
    personality = parse_line(traits_text, r'Personality') or ""

    goals_text = parse_section(raw, "Goals & Motivations")

    return {
        "name": name,
        "race_class": race_class,
        "level": level,
        "stats": stats,
        "modifiers": {k: compute_modifier(v) for k, v in stats.items()},
        "traits": {"appearance": appearance, "personality": personality},
        "goals": goals_text.strip(),
        "combat": {"hit_die": hit_die, "hp_current": hp_current, "hp_max": hp_max,
                    "ac": ac, "speed": speed},
        "weapons": weapons,
        "spells": spells,
        "skills": skills,
        "equipment": equipment,
        "raw_md": raw,
    }


def load_enemy(filepath):
    with open(filepath, "r") as f:
        raw = f.read()

    name = os.path.basename(filepath).replace(".md", "")
    for line in raw.split("\n"):
        m = re.match(r'^# (.+)$', line)
        if m:
            name = m.group(1).strip()
            break

    enemy = {"name": name, "type": "", "cr": 1, "group_size": 1,
             "ac": 10, "hp_current": 10, "hp_max": 10, "speed": 30,
             "size": "", "alignment": "", "attacks": [], "behavior": {},
             "raw_md": raw}

    for line in raw.split("\n"):
        type_m = re.search(r'\*\*Type:\*\*\s*(.+?)(?:\s*\|\s*$)', line)
        if type_m:
            enemy["type"] = type_m.group(1).strip()
        cr_m = re.search(r'\*\*CR:\*\*\s*(\d+)', line)
        if cr_m:
            enemy["cr"] = int(cr_m.group(1))
        gs_m = re.search(r'\*\*Group Size:\*\*\s*(.+?)(?:\s*\||$)', line)
        if gs_m:
            enemy["group_size"] = gs_m.group(1).strip()

        ac_m = re.search(r'\*\*AC:\*\*\s*(\d+)', line)
        if ac_m and "Armor" not in line:
            enemy["ac"] = int(ac_m.group(1))

        hp_m = re.search(r'\*\*HP:\*\*\s*(\d+)', line)
        if hp_m:
            val = int(hp_m.group(1))
            enemy["hp_max"] = val
            enemy["hp_current"] = val

        spd_m = re.search(r'\*\*Speed:\*\*\s*(\d+)', line)
        if spd_m:
            enemy["speed"] = int(spd_m.group(1))

        size_m = re.search(r'\*\*Size:\*\*\s*(.+?)(?:\s*\||$)', line)
        if size_m:
            enemy["size"] = size_m.group(1).strip()

    atk_section = parse_section(raw, "Attacks")
    for line in atk_section.split("\n"):
        am = re.match(r'\s*\*\s*\*\*([^*]+)\*\*\s*(.+)', line)
        if am:
            enemy["attacks"].append({"name": am.group(1).strip(),
                                     "detail": am.group(2).strip()})

    beh_section = parse_section(raw, "Behavior")
    for line in beh_section.split("\n"):
        bm = re.search(r'\*\s*(?:\*\*)?(\w+)\s*:\*\*\s*(.+)', line)
        if bm:
            enemy["behavior"][bm.group(1)] = bm.group(2).strip()

    return enemy


def load_party(heroes_dir):
    chars = []
    for fpath in sorted(glob.glob(os.path.join(heroes_dir, "*.md"))):
        chars.append(load_character(fpath))
    return chars


def party_summary(party):
    lines = []
    for c in party:
        hp = "{}\{}".format(c['combat']['hp_current'], c['combat']['hp_max'])
        lines.append("- **{}** ({}) — HP: {}, AC: {}".format(
            c['name'], c['race_class'], hp, c['combat']['ac']))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Load RPG character/enemy markdown files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--load-character", help="Load a single character file, output JSON")
    group.add_argument("--load-party", help="Load all characters in directory, output JSON")
    group.add_argument("--summary", help="Brief party summary (human-readable)")
    group.add_argument("--load-enemy", help="Load an enemy file, output JSON")
    args = parser.parse_args()

    if args.load_character:
        char = load_character(args.load_character)
        char.pop("raw_md", None)
        print(json.dumps(char, indent=2))

    elif args.load_party:
        party = load_party(args.load_party)
        for c in party:
            c.pop("raw_md", None)
        print(json.dumps(party, indent=2))

    elif args.summary:
        party = load_party(args.summary)
        print(f"Party ({len(party)} members):")
        print(party_summary(party))

    elif args.load_enemy:
        enemy = load_enemy(args.load_enemy)
        enemy.pop("raw_md", None)
        print(json.dumps(enemy, indent=2))


if __name__ == "__main__":
    main()
