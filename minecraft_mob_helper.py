#!/usr/bin/env python3
"""
Minecraft Mob Helper Tool
A fun interactive tool to learn about Minecraft mobs!
"""

import sys

# Comprehensive Mob Database
MOBS = {
    "zombie": {
        "name": "Zombie",
        "type": "hostile",
        "health": 20,
        "damage": {"easy": 2.5, "normal": 3, "hard": 4.5},
        "xp": 5,
        "drops": ["Rotten Flesh (common)", "Iron Ingot (rare)", "Carrot (rare)", "Potato (rare)", "Armor/Weapons if equipped"],
        "spawn": "Dark areas (light level 0), Overworld surface at night",
        "tips": "Burns in sunlight. Can pick up items and wear armor. Baby zombies are faster!"
    },
    "creeper": {
        "name": "Creeper",
        "type": "hostile",
        "health": 20,
        "damage": {"easy": "Varies (explosion)", "normal": "Up to 49 (point blank)", "hard": "Up to 73 (point blank)"},
        "xp": 5,
        "drops": ["Gunpowder (common)", "Music Disc (if killed by skeleton)"],
        "spawn": "Dark areas (light level 0), Overworld",
        "tips": "Explodes when close! Run away or use a shield. Cats scare them away."
    },
    "skeleton": {
        "name": "Skeleton",
        "type": "hostile",
        "health": 20,
        "damage": {"easy": 2, "normal": 3, "hard": 4},
        "xp": 5,
        "drops": ["Arrow (common)", "Bone (common)", "Bow (rare)"],
        "spawn": "Dark areas (light level 0), Overworld",
        "tips": "Burns in sunlight. Attacks from range. Use shield to block arrows!"
    },
    "spider": {
        "name": "Spider",
        "type": "hostile",
        "health": 16,
        "damage": {"easy": 2, "normal": 2, "hard": 3},
        "xp": 5,
        "drops": ["String (common)", "Spider Eye (common)"],
        "spawn": "Dark areas (light level 0), can spawn with skeleton rider",
        "tips": "Neutral in daylight (unless attacked). Can climb walls!"
    },
    "enderman": {
        "name": "Enderman",
        "type": "neutral",
        "health": 40,
        "damage": {"easy": 4.5, "normal": 7, "hard": 10.5},
        "xp": 5,
        "drops": ["Ender Pearl (common)"],
        "spawn": "Overworld at night, The End, Nether (rare)",
        "tips": "Don't look at them! Teleports away from projectiles. Weak to water."
    },
    "pig": {
        "name": "Pig",
        "type": "passive",
        "health": 10,
        "damage": {"easy": 0, "normal": 0, "hard": 0},
        "xp": 3,
        "drops": ["Raw Porkchop (1-3)", "Cooked Porkchop if killed by fire"],
        "spawn": "Grassy areas with light level 9+",
        "tips": "Can be ridden with saddle! Carrot on a stick controls direction."
    },
    "cow": {
        "name": "Cow",
        "type": "passive",
        "health": 10,
        "damage": {"easy": 0, "normal": 0, "hard": 0},
        "xp": 3,
        "drops": ["Raw Beef (1-3)", "Leather (0-2)", "Cooked Beef if killed by fire"],
        "spawn": "Grassy areas with light level 9+",
        "tips": "Use bucket to get milk. Breed with wheat."
    },
    "sheep": {
        "name": "Sheep",
        "type": "passive",
        "health": 8,
        "damage": {"easy": 0, "normal": 0, "hard": 0},
        "xp": 3,
        "drops": ["Wool (1)", "Raw Mutton (1-2)", "Cooked Mutton if killed by fire"],
        "spawn": "Grassy areas with light level 9+",
        "tips": "Shear for wool without killing! Comes in many colors."
    },
    "chicken": {
        "name": "Chicken",
        "type": "passive",
        "health": 4,
        "damage": {"easy": 0, "normal": 0, "hard": 0},
        "xp": 3,
        "drops": ["Raw Chicken (1)", "Feather (0-2)", "Cooked Chicken if killed by fire"],
        "spawn": "Grassy areas with light level 9+",
        "tips": "Lays eggs every 5-10 minutes. Falls slowly (like feather falling)."
    },
    "wolf": {
        "name": "Wolf",
        "type": "neutral",
        "health": 8,
        "damage": {"easy": 3, "normal": 4, "hard": 6},
        "xp": 3,
        "drops": ["Nothing"],
        "spawn": "Forest and taiga biomes",
        "tips": "Tame with bones! Becomes your loyal companion. Attack as pack."
    },
    "blaze": {
        "name": "Blaze",
        "type": "hostile",
        "health": 20,
        "damage": {"easy": 4, "normal": 6, "hard": 9},
        "xp": 10,
        "drops": ["Blaze Rod (0-1)"],
        "spawn": "Nether Fortresses only",
        "tips": "Shoots fireballs! Weak to snowballs. Need blaze rods for brewing!"
    },
    "ghast": {
        "name": "Ghast",
        "type": "hostile",
        "health": 10,
        "damage": {"easy": 9, "normal": 17, "hard": 25},
        "xp": 5,
        "drops": ["Ghast Tear (0-1)", "Gunpowder (0-2)"],
        "spawn": "Open areas in the Nether",
        "tips": "Shoots explosive fireballs! Hit them back for achievement. Cries are creepy!"
    },
    "piglin": {
        "name": "Piglin",
        "type": "neutral",
        "health": 16,
        "damage": {"easy": 4, "normal": 5, "hard": 8},
        "xp": 5,
        "drops": ["Raw Porkchop", "Gold items if equipped"],
        "spawn": "Nether (except Basalt Deltas)",
        "tips": "Wear gold armor to avoid attack! Trade gold ingots for items. Afraid of soul fire."
    },
    "wither_skeleton": {
        "name": "Wither Skeleton",
        "type": "hostile",
        "health": 20,
        "damage": {"easy": 5, "normal": 8, "hard": 12},
        "xp": 5,
        "drops": ["Coal (0-1)", "Bone (0-2)", "Wither Skeleton Skull (2.5% chance)"],
        "spawn": "Nether Fortresses",
        "tips": "Gives Wither effect! Immune to fire. Need 3 skulls to summon Wither boss."
    },
    "ender_dragon": {
        "name": "Ender Dragon",
        "type": "boss",
        "health": 200,
        "damage": {"easy": 6, "normal": 10, "hard": 15},
        "xp": 12000,
        "drops": ["Dragon Egg (one time)", "Lots of XP"],
        "spawn": "The End (main island)",
        "tips": "Final boss! Destroy End Crystals first. Breathes dragon breath. Respawnable!"
    },
    "wither": {
        "name": "Wither",
        "type": "boss",
        "health": 300,
        "damage": {"easy": 5, "normal": 8, "hard": 12},
        "xp": 50,
        "drops": ["Nether Star (1)"],
        "spawn": "Player-summoned (soul sand + 3 wither skulls)",
        "tips": "Extremely dangerous! Causes Wither effect. Explodes at half health. Build underground!"
    },
    "iron_golem": {
        "name": "Iron Golem",
        "type": "neutral",
        "health": 100,
        "damage": {"easy": 4.75, "normal": 7.5, "hard": 11.25},
        "xp": 5,
        "drops": ["Iron Ingot (3-5)", "Poppy (0-2)"],
        "spawn": "Villages (naturally) or player-crafted",
        "tips": "Protects villagers! Don't attack unless you want a fight. Very strong!"
    },
    "villager": {
        "name": "Villager",
        "type": "passive",
        "health": 20,
        "damage": {"easy": 0, "normal": 0, "hard": 0},
        "xp": 0,
        "drops": ["Nothing"],
        "spawn": "Villages",
        "tips": "Trade for emeralds! Different professions offer different trades. Breed with food!"
    },
    "slime": {
        "name": "Slime",
        "type": "hostile",
        "health": "Varies (big: 16, medium: 4, small: 1)",
        "damage": {"easy": "Varies by size", "normal": "Big: 4, Med: 2, Small: 0", "hard": "Varies by size"},
        "xp": "Big: 4, Medium: 2, Small: 1",
        "drops": ["Slimeball (0-2, only small slimes)"],
        "spawn": "Swamps at night, Slime chunks below Y=40",
        "tips": "Splits into smaller slimes when killed! Needed for sticky pistons and leads."
    },
    "guardian": {
        "name": "Guardian",
        "type": "hostile",
        "health": 30,
        "damage": {"easy": 4, "normal": 6, "hard": 9},
        "xp": 10,
        "drops": ["Prismarine Shard", "Prismarine Crystal (rare)", "Raw Cod"],
        "spawn": "Ocean Monuments",
        "tips": "Laser attack! Moves fast in water. Use sword underwater or trident."
    }
}

# Weapon damage database
WEAPONS = {
    "fist": 1,
    "wooden_sword": 4,
    "stone_sword": 5,
    "iron_sword": 6,
    "diamond_sword": 7,
    "netherite_sword": 8,
    "wooden_axe": 7,
    "stone_axe": 9,
    "iron_axe": 9,
    "diamond_axe": 9,
    "netherite_axe": 10,
    "trident": 9,
    "bow": 6,
    "crossbow": 9
}


def print_header():
    """Print a cool header"""
    print("\n" + "="*60)
    print("       ⚔️  MINECRAFT MOB HELPER TOOL  ⚔️")
    print("="*60 + "\n")


def print_mob_info(mob_key):
    """Display detailed information about a mob"""
    mob = MOBS.get(mob_key.lower().replace(" ", "_"))

    if not mob:
        print(f"\n❌ Mob '{mob_key}' not found! Try searching.\n")
        return

    # Determine emoji based on type
    type_emoji = {
        "hostile": "⚔️",
        "neutral": "⚠️",
        "passive": "💚",
        "boss": "👑"
    }

    emoji = type_emoji.get(mob["type"], "❓")

    print(f"\n{emoji} {mob['name'].upper()} {emoji}")
    print("-" * 60)
    print(f"Type: {mob['type'].upper()}")
    print(f"Health: ❤️  {mob['health']} HP ({mob['health']/2} hearts)")

    # Damage
    if isinstance(mob['damage']['normal'], str):
        print(f"Damage: {mob['damage']['normal']}")
    else:
        print(f"Damage: ⚔️  Easy: {mob['damage']['easy']} | Normal: {mob['damage']['normal']} | Hard: {mob['damage']['hard']}")

    print(f"XP Drop: ⭐ {mob['xp']} XP")

    print(f"\nDrops:")
    for drop in mob['drops']:
        print(f"  • {drop}")

    print(f"\nSpawn Location: 📍 {mob['spawn']}")
    print(f"\nTips: 💡 {mob['tips']}")
    print("-" * 60 + "\n")


def search_mobs(query):
    """Search for mobs by name"""
    query = query.lower()
    matches = [key for key in MOBS.keys() if query in key or query in MOBS[key]['name'].lower()]

    if not matches:
        print(f"\n❌ No mobs found matching '{query}'\n")
        return []

    print(f"\n🔍 Found {len(matches)} mob(s):\n")
    for i, mob_key in enumerate(matches, 1):
        mob = MOBS[mob_key]
        emoji = {"hostile": "⚔️", "neutral": "⚠️", "passive": "💚", "boss": "👑"}.get(mob['type'], "❓")
        print(f"  {i}. {emoji} {mob['name']} ({mob['type']})")
    print()

    return matches


def list_all_mobs():
    """List all available mobs by category"""
    categories = {"hostile": [], "neutral": [], "passive": [], "boss": []}

    for key, mob in MOBS.items():
        categories[mob['type']].append(mob['name'])

    print("\n📋 ALL MOBS IN DATABASE\n")

    if categories['boss']:
        print("👑 BOSSES:")
        for name in sorted(categories['boss']):
            print(f"  • {name}")
        print()

    if categories['hostile']:
        print("⚔️  HOSTILE MOBS:")
        for name in sorted(categories['hostile']):
            print(f"  • {name}")
        print()

    if categories['neutral']:
        print("⚠️  NEUTRAL MOBS:")
        for name in sorted(categories['neutral']):
            print(f"  • {name}")
        print()

    if categories['passive']:
        print("💚 PASSIVE MOBS:")
        for name in sorted(categories['passive']):
            print(f"  • {name}")
        print()


def combat_calculator():
    """Calculate hits needed to kill a mob"""
    print("\n⚔️  COMBAT CALCULATOR\n")

    mob_name = input("Enter mob name: ").strip().lower().replace(" ", "_")
    mob = MOBS.get(mob_name)

    if not mob:
        print(f"❌ Mob not found!\n")
        return

    print(f"\nSelect weapon:")
    weapons_list = list(WEAPONS.keys())
    for i, weapon in enumerate(weapons_list, 1):
        print(f"  {i}. {weapon.replace('_', ' ').title()} (💥 {WEAPONS[weapon]} damage)")

    try:
        choice = int(input("\nEnter number: ").strip())
        weapon = weapons_list[choice - 1]
        damage = WEAPONS[weapon]
    except (ValueError, IndexError):
        print("❌ Invalid choice!\n")
        return

    health = mob['health']
    if isinstance(health, str):
        print(f"\n❌ {mob['name']} has variable health!\n")
        return

    hits_needed = (health + damage - 1) // damage  # Ceiling division

    print(f"\n🎯 COMBAT STATS:")
    print(f"Mob: {mob['name']} (❤️  {health} HP)")
    print(f"Weapon: {weapon.replace('_', ' ').title()} (💥 {damage} damage)")
    print(f"Hits needed: ⚔️  {hits_needed} hits")
    print(f"Total damage needed: 💥 {hits_needed * damage} damage\n")


def xp_calculator():
    """Calculate how many mobs needed for XP levels"""
    print("\n⭐ XP CALCULATOR\n")
    print("Popular XP farms:")
    print("  1. Zombie (5 XP each)")
    print("  2. Skeleton (5 XP each)")
    print("  3. Blaze (10 XP each)")
    print("  4. Enderman (5 XP each)")
    print()

    mob_name = input("Enter mob name: ").strip().lower().replace(" ", "_")
    mob = MOBS.get(mob_name)

    if not mob:
        print(f"❌ Mob not found!\n")
        return

    try:
        target_level = int(input("What level do you want to reach? ").strip())
    except ValueError:
        print("❌ Invalid number!\n")
        return

    # Simplified XP calculation (actual formula is more complex)
    if target_level <= 16:
        xp_needed = target_level ** 2 + 6 * target_level
    elif target_level <= 31:
        xp_needed = 2.5 * target_level ** 2 - 40.5 * target_level + 360
    else:
        xp_needed = 4.5 * target_level ** 2 - 162.5 * target_level + 2220

    xp_per_mob = mob['xp']
    mobs_needed = int(xp_needed / xp_per_mob) + 1

    print(f"\n📊 XP CALCULATION:")
    print(f"Target Level: {target_level}")
    print(f"XP Needed: ~{int(xp_needed)} XP")
    print(f"Mob: {mob['name']} ({xp_per_mob} XP each)")
    print(f"Mobs to kill: ~{mobs_needed} {mob['name']}s\n")


def main_menu():
    """Main interactive menu"""
    while True:
        print("\n📖 MAIN MENU")
        print("  1. Search for a mob")
        print("  2. List all mobs")
        print("  3. Combat Calculator")
        print("  4. XP Calculator")
        print("  5. Random mob facts")
        print("  6. Exit")

        choice = input("\nWhat would you like to do? (1-6): ").strip()

        if choice == "1":
            query = input("\nEnter mob name or search term: ").strip()
            matches = search_mobs(query)
            if matches:
                if len(matches) == 1:
                    print_mob_info(matches[0])
                else:
                    try:
                        num = int(input("Enter number to view details (or 0 to skip): ").strip())
                        if 1 <= num <= len(matches):
                            print_mob_info(matches[num - 1])
                    except (ValueError, IndexError):
                        pass

        elif choice == "2":
            list_all_mobs()
            mob_name = input("\nEnter mob name for details (or press Enter to skip): ").strip()
            if mob_name:
                print_mob_info(mob_name)

        elif choice == "3":
            combat_calculator()

        elif choice == "4":
            xp_calculator()

        elif choice == "5":
            import random
            mob_key = random.choice(list(MOBS.keys()))
            print("\n🎲 Random Mob Fact!")
            print_mob_info(mob_key)

        elif choice == "6":
            print("\n👋 Thanks for using Minecraft Mob Helper! Happy mining!\n")
            break

        else:
            print("\n❌ Invalid choice! Please enter 1-6.\n")


if __name__ == "__main__":
    print_header()

    # Check if command line argument provided
    if len(sys.argv) > 1:
        mob_name = " ".join(sys.argv[1:])
        print(f"Looking up: {mob_name}")
        print_mob_info(mob_name)
    else:
        main_menu()
