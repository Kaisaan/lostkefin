"""
Character names mapping from the game script format.
Index corresponds to the hexadecimal values ($0-$47) used in the script files.
"""

CHARACTERS = [
    "Adol",  # $0
    "Dogi",  # $1
    "Niena",  # $2
    "Terra",  # $3
    "Massea",  # $4
    "Stein",  # $5
    "Dorman",  # $6
    "Rizze",  # $7
    "Jabir",  # $8
    "Effie",  # $9
    "King of Kefin",  # $A
    "Alga",  # $B
    "Dios",  # $C
    "Nottis",  # $D
    "Chase",  # $E
    "Aisha",  # $F
    "Willy",  # $10
    "Muhaba",  # $11
    "Balck",  # $12
    "Abyss",  # $13
    "Karion",  # $14
    "Blacksmith",  # $15
    "Sailor",  # $16
    "Butler",  # $17
    "Maid",  # $18
    "Lower Ranking Soldier",  # $19
    "Soldier",  # $1A
    "Adventurer A",  # $1B
    "Adventurer B",  # $1C
    "Merchant A",  # $1D
    "Merchant B",  # $1E
    "Kobold",  # $1F
    "Desert Grandma",  # $20
    "Desert Grandpa",  # $21
    "Desert Lady",  # $22
    "Desert Man A",  # $23
    "Desert Man B",  # $24
    "Desert Girl",  # $25
    "Desert Boy",  # $26
    "Kefin Man A",  # $27
    "Kefin Man B",  # $28
    "Kefin Lady A",  # $29
    "Kefin Lady B",  # $2A
    "Resistance A",  # $2B
    "Resistance B",  # $2C
    "Grandpa A",  # $2D
    "Grandpa B",  # $2E
    "Grandma",  # $2F
    "Townsman A",  # $30
    "Townsman B",  # $31
    "Townslady A",  # $32
    "Townslady B",  # $33
    "Grandma",  # $34
    "Grandpa",  # $35
    "Boy A",  # $36
    "Boy B",  # $37
    "Girl A",  # $38
    "Dog",  # $39
    "Girl B",  # $3A
    "Kidnapped Stein",  # $3B
    "Nottis & Dios",  # $3C
    None,  # $3D (missing in table)
    None,  # $3E (missing in table)
    None,  # $3F (missing in table)
    "Beautiful Woman",  # $40
    "Young Girl",  # $41
    "Ruffian A",  # $42
    "Ruffian B",  # $43
    "Mysterious Voice",  # $44
    "Mysterious Man",  # $45
    "Burly Man",  # $46
    "Woman",  # $47
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
        return 0x1C6
    if "Mailman" in name:
        return 0x1C7
    if "Previous" in name:
        return 0x1C5

    index = CHARACTERS.index(name)
    return index
