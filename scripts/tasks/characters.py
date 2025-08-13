"""
Character names mapping from the game script format.
Index corresponds to the hexadecimal values ($0-$47) used in the script files.
"""

CHARACTERS = [
    "Adol",                    # $0
    "Dogi",                    # $1
    "Niena",                   # $2
    "Terra",                   # $3
    "Massea",                  # $4
    "Stein",                   # $5
    "Doman",                   # $6
    "Rizze",                   # $7
    "Jabir",                   # $8
    "Effey",                   # $9
    "King Kefin",              # $A
    "Alga",                    # $B
    "Dios",                    # $C
    "Nottis",                  # $D
    "Chase",                   # $E
    "Aisha",                   # $F
    "Willy",                   # $10
    "Mubaja",                  # $11
    "Baruq",                   # $12
    "Abyss",                   # $13
    "Karion",                  # $14
    "Blacksmith",              # $15
    "Sailor",                  # $16
    "Butler",                  # $17
    "Maid",                    # $18
    "Foot Soldier",            # $19
    "Soldier",                 # $1A
    "Adventurer A",            # $1B
    "Adventurer B",            # $1C
    "Merchant A",              # $1D
    "Merchant B",              # $1E
    "Kobold",                  # $1F
    "Desert Old Woman",        # $20
    "Desert Old Man",          # $21
    "Desert Woman",            # $22
    "Desert Man A",            # $23
    "Desert Man B",            # $24
    "Desert Girl",             # $25
    "Desert Boy",              # $26
    "Kefin Man A",             # $27
    "Kefin Man B",             # $28
    "Kefin Woman A",           # $29
    "Kefin Woman B",           # $2A
    "Rebel A",                 # $2B
    "Rebel B",                 # $2C
    "Man A",                   # $2D
    "Man B",                   # $2E
    "Woman",                   # $2F
    "Villager Man A",          # $30
    "Villager Man B",          # $31
    "Villager Girl A",         # $32
    "Villager Girl B",         # $33
    "Old Woman",               # $34
    "Old Man",                 # $35
    "Boy A",                   # $36
    "Boy B",                   # $37
    "Girl A",                  # $38
    "Dog",                     # $39
    "Girl B",                  # $3A
    "Kidnapped Stein",         # $3B
    "Noties & Deios",          # $3C
    None,                      # $3D (missing in table)
    None,                      # $3E (missing in table)
    None,                      # $3F (missing in table)
    "Beautiful Woman",         # $40
    "Girl",                    # $41
    "Thug A",                  # $42
    "Thug B",                  # $43
    "Mysterious Voice",        # $44
    "Mysterious Man",          # $45
    "Big Man",                 # $46
    "Woman",                   # $47
]


def get_character_name(index):
    if isinstance(index, str):
        try:
            index = int(index, 16)
        except ValueError:
            return None
    
    if 0 <= index < len(CHARACTERS):
        return CHARACTERS[index]
    return None


def get_character_index(name):
    if "Narrator" in name:
        return 0x1c6
    if "Mailman" in name:
        return 0x1c7
    if "Previous" in name:
        return 0x1c5

    index = CHARACTERS.index(name)
    return index
