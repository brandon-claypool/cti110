# ============================================================================
# Brandon Claypool
# CTI-110 Final Project
# Text-Based Tactical Mission Game - CLI of Duty - A Text Base Combat Thriller
# ============================================================================

import random
import time


# ----------------------------
# ROLE DEFINITIONS
# ----------------------------

ROLES = {
    "Team Leader": {"morale_bonus": 10, "success_bonus": 5},
    "Medic": {"casualty_reduction": 1},
    "RTO": {"intel_bonus": 5},
    "Scout": {"recon_bonus": 10},
    "Breacher": {"raid_bonus": 10},
    "Rifleman": {}
}


# ----------------------------
# INPUT HELPERS
# ----------------------------

def get_menu_choice(prompt, low, high):
    while True:
        choice = input(prompt).strip()
        if choice.isdigit():
            choice = int(choice)
            if low <= choice <= high:
                return choice
        print(f"Enter a number from {low} to {high}.")


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


# ----------------------------
# CHARACTER FUNCTIONS
# ----------------------------

def create_character():
    """Value-returning function to create a character."""

    name = input("Enter character name: ").strip()
    if name == "":
        name = f"Hero{random.randint(10, 99)}"

    def get_stat(prompt, low, high):
        while True:
            try:
                val = int(input(prompt))
                if low <= val <= high:
                    return val
                print(f"Enter a value from {low} to {high}.")
            except ValueError:
                print("Enter a whole number.")

    stamina = get_stat(f"{name}'s stamina (20–120): ", 20, 120)
    power = get_stat(f"{name}'s power (1–10): ", 1, 10)
    defense = get_stat(f"{name}'s defense (0–8): ", 0, 8)
    luck = get_stat(f"{name}'s luck (0–5): ", 0, 5)

    role = random.choice(list(ROLES.keys()))

    character = {
        "name": name,
        "role": role,
        "stamina": stamina,
        "power": power,
        "defense": defense,
        "luck": luck
    }

    print(f"{name} created as {role} ✅")
    return character


def auto_create_characters():
    """Auto-generate a team of 1–12 operators with roles."""

    callsigns = [
        "Viper", "Ghost", "Reaper", "Falcon", "Nomad", "Ranger",
        "Havoc", "Atlas", "Echo", "Titan", "Zero", "Mako"
    ]

    count = get_menu_choice("How many team members (1–12): ", 1, 12)
    team = []

    for _ in range(count):
        name = f"{random.choice(callsigns)}-{random.randint(10, 99)}"
        role = random.choice(list(ROLES.keys()))

        team.append({
            "name": name,
            "role": role,
            "stamina": random.randint(20, 120),
            "power": random.randint(1, 10),
            "defense": random.randint(0, 8),
            "luck": random.randint(0, 5)
        })

    print(f"\n✅ Auto-created {count} operators\n")
    return team


def display_characters(characters):
    """Non-value returning function to display characters."""

    if not characters:
        print("No characters created yet.\n")
        return

    print("\n🪖🪖🪖🪖🪖 TEAM ROSTER 🪖🪖🪖🪖🪖")
    for c in characters:
        print(
            f"{c['name']} | Role: {c['role']} | "
            f"Sta:{c['stamina']} Pow:{c['power']} "
            f"Def:{c['defense']} Luck:{c['luck']}"
        )
    print("🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖🪖\n")


# ----------------------------
# MISSION SYSTEM
# ----------------------------

def new_mission_state(characters):
    mission = {
        "success": 50.0,
        "morale": 100.0,
        "casualties": 0,
        "turns": 0,
        "recon_used": False,
        "intel_used": False,
        "patrol_base_used": False,
        "last_halt": 0.0,
        "team_size": len(characters)
    }

    for c in characters:
        role = c["role"]
        mission["success"] += ROLES.get(role, {}).get("success_bonus", 0)
        mission["morale"] += ROLES.get(role, {}).get("morale_bonus", 0)

    mission["success"] = clamp(mission["success"], 0, 100)
    mission["morale"] = clamp(mission["morale"], 0, 100)
    return mission


def show_mission_stats(m):
    print("\n=========== MISSION STATS ===========")
    print(f"Mission Success Probability: {m['success']:.1f}%")
    print(f"Unit Morale: {m['morale']:.1f}%")
    print(f"Unit Casualties: {m['casualties']} / {m['team_size']}")
    print(f"Turns Elapsed: {m['turns']}")
    print("====================================\n")


def resolve_turn(m, characters):
    m["turns"] += 1

    if m["morale"] < 60:
        m["success"] -= 5

    if m["success"] < 50 and m["turns"] % 2 == 0:
        medics = sum(1 for c in characters if c["role"] == "Medic")
        if medics > 0:
            print("🩺 Medic prevented a casualty.")
        else:
            m["casualties"] += 1
            print("⚠️ Casualty incurred.")

    m["success"] = clamp(m["success"], 0, 100)
    m["morale"] = clamp(m["morale"], 0, 100)


def mission_lost(m):
    if m["casualties"] > m["team_size"] / 2:
        print("❌ Mission failed: excessive casualties.")
        return True
    if m["success"] < 30:
        print("❌ Mission failed: probability too low.")
        return True
    if m["morale"] < 20:
        print("❌ Mission failed: morale collapsed.")
        return True
    return False


# ----------------------------
# MISSION ACTIONS
# ----------------------------

def conduct_recon(m, team):
    if m["recon_used"]:
        print("Recon already conducted.")
        return
    bonus = 15 + sum(ROLES[c["role"]].get("recon_bonus", 0) for c in team)
    m["success"] += bonus
    m["morale"] -= 5
    m["recon_used"] = True
    print(f"Recon complete: +{bonus}% success, -5% morale")


def radio_for_intel(m, team):
    if m["intel_used"]:
        print("Intel already gathered.")
        return
    bonus = 10 + sum(ROLES[c["role"]].get("intel_bonus", 0) for c in team)
    m["success"] += bonus
    m["morale"] -= 2.5
    m["intel_used"] = True
    print(f"Intel received: +{bonus}% success, -2.5% morale")


def ambush_or_raid(m, team, label):
    if not m["recon_used"] and not m["intel_used"]:
        m["success"] -= 20
        print("⚠️ No recon/intel: -20% success")

    m["success"] = clamp(m["success"], 0, 100)

    roll = random.randint(1, 100)
    print(f"{label} roll: {roll} vs {int(m['success'])}")
    time.sleep(0.6)

    if roll <= m["success"]:
        m["morale"] += 20
        print(f"✅ {label} SUCCESS: +20% morale")
        return True
    else:
        m["morale"] -= 20
        m["casualties"] += 2
        print(f"❌ {label} FAILED: -20% morale, +2 casualties")
        return False


def short_halt(m):
    cooldown = 300  # 5 minutes in seconds
    now = time.time()
    elapsed = now - m["last_halt"]

    if elapsed < cooldown:
        remaining = int(cooldown - elapsed)
        print(f"Short halt unavailable for {remaining} seconds.")
        return

    m["morale"] += 1
    m["last_halt"] = now
    print("Short halt: +1% morale")


def long_halt(m):
    cooldown = 300  # 5 minutes in seconds
    now = time.time()
    elapsed = now - m["last_halt"]

    if elapsed < cooldown:
        remaining = int(cooldown - elapsed)
        print(f"Long halt unavailable for {remaining} seconds.")
        return

    m["morale"] += 2.5
    m["last_halt"] = now
    print("Long halt: +2.5% morale")



def setup_patrol_base(m):
    if m["patrol_base_used"]:
        print("Patrol base already established for this operation.")
        return

    m["success"] += 25
    m["morale"] -= 40
    m["patrol_base_used"] = True

    print("Patrol base established: +25% success, -40% morale")

def ask_play_again():
    while True:
        ans = input("🎖️🎖️🎖️ Mission WIN! 🎖️🎖️🎖️ Run another mission? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter y/yes or n/no.")

# ----------------------------
# COMBAT OPERATION MENU
# ----------------------------

def conduct_combat_operation(mission, team):
    while True:
        print("""
========= COMBAT OPERATION =========
1. Conduct Reconnaissance 🗺️
2. Conduct Ambush 🪖
3. Conduct Raid 🪖
4. Radio for Intel 🗺️
5. Short Halt
6. Long Halt
7. Setup Patrol Base 
8. Show Mission Stats
9. Return to Base
===================================
""")

        choice = get_menu_choice("Select action: ", 1, 9)

        if choice == 1:
            conduct_recon(mission, team)
            resolve_turn(mission, team)
        elif choice == 2:
            win = ambush_or_raid(mission, team, "AMBUSH")
            resolve_turn(mission, team)
            if win:
                return "WIN"
        elif choice == 3:
            win = ambush_or_raid(mission, team, "RAID")
            resolve_turn(mission, team)
            if win:
                return "WIN"
        elif choice == 4:
            radio_for_intel(mission, team)
            resolve_turn(mission, team)
        elif choice == 5:
            short_halt(mission)
            resolve_turn(mission, team)
        elif choice == 6:
            long_halt(mission)
            resolve_turn(mission, team)
        elif choice == 7:
            setup_patrol_base(mission)
            resolve_turn(mission, team)
        elif choice == 8:
            show_mission_stats(mission)
            continue
        elif choice == 9:
            confirm = input("Return to base and reset mission? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                return "RESET"
            else:
                continue

        if mission_lost(mission):
            return "LOSS"


# ----------------------------
# MAIN MENU
# ----------------------------

def main():
    characters = []
    mission = None

    while True:
        print("""
=========== MAIN MENU ===========
1. Create a character
2. Auto-create characters
3. Display characters
4. Conduct a Combat Operation
5. Exit Game
================================
""")

        choice = get_menu_choice("Select option: ", 1, 5)

        if choice == 1:
            characters.append(create_character())

        elif choice == 2:
            characters = auto_create_characters()
            mission = None   # team changed, reset mission

        elif choice == 3:
            display_characters(characters)

        elif choice == 4:
            if not characters:
                print("Create a team first.\n")
            else:
                if mission is None:
                    mission = new_mission_state(characters)

                result = conduct_combat_operation(mission, characters)
                
                if result == "WIN":
                    play_again = ask_play_again()
                    if play_again:
                        characters = []
                        mission = None
                        continue
                    else:
                        print("Exiting game. Goodbye!")
                        break

                elif result == "LOSS":
                    characters = []
                    mission = None
                    continue
                
                elif result == "RESET":
                    characters = []
                    mission = None 
                    continue

        elif choice == 5:
            print("Exiting game. Goodbye!")
            break


if __name__ == "__main__":
    main()
