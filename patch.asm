.erroronwarning on
.ps2

.loadtable "kefin.tbl", "SJIS"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

// Fix halfwidth characters not updating textbox size correctly
.orga 0x0004CF38
addiu	t7, t7, 0x0A

.orga 0x0004CF44
addiu	a0, a0, 0x01

// System Text ------------------------------------------------

.orga 0x0025FBF0
.str "Ys Ⅳ save data has been found.\nWould you like to link it?"

.orga 0x25FC30
.str "Data loaded successfully. #Re○#Wh"

.orga 0x25FC60
.str "Failed to load data. #Re○#Wh"

.orga 0x25FC90
.str "Loading…\nDo not turn off or reset the PlayStation 2 console\nor remove any Memory Cards or controllers."

.orga 0x25FD30
.str "Checking…\nDo not turn off or reset the PlayStation 2 console\nor remove any Memory Cards or controllers."

.orga 0x25FDD0
.str "No Memory Card (8MB) (for PlayStation 2) inserted in Memory Card slot 1.\n(#Bl×#Wh to Cancel)"

.orga 0x25FE40
.str "Ys Ⅳ data not found. #Re○#Wh"

.orga 0x0025FE70
.str "Ys Ⅲ save data has been found.\nWould you like to link it?"

.orga 0x0025FEB0
.str "Ys Ⅲ data not found. #Re○#Wh"

.orga 0x25FEE0
.str "No Memory Card (8MB) (for PlayStation 2) inserted in Memory Card slot 1.\nTo save your game data, at least 300KB of free space is required.\nStart the game anyway?"

.orga 0x25FF90
.str "Not enough free space on the Memory Card (8MB) (for PlayStation 2) in Memory Card slot 1.\nTo save your game data, at least 300KB of free space is required.\nIf you start the game now, you will not be able to save your progress.\nStart the game anyway?"

.orga 0x260090
.str "Ys Ⅴ System Data loaded successfully."

.orga 0x2600D0
.str "Failed to load Ys Ⅴ System Data."

.orga 0x260110
.str "Loading System Data…\nDo not turn off or reset the PlayStation 2 console, or remove any Memory Cards (8MB) (for PlayStation 2) or controllers."

.orga 0x2601B0
.str "Overwrite the System Data?\nThe previous System Data will be lost. Are you sure?"

.orga 0x260210
.str "System Data saved. #Re○#Wh"

.orga 0x260240
.str "Not enough free space on the Memory Card (8MB) (for PlayStation 2) in Memory Card slot 1.\nTo save Ys Ⅴ data, at least 300KB of free space is required. #Re○#Wh"

.orga 0x2602F0
.str "Failed to save System Data. #Re○#Wh"

.orga 0x260320
.str "Saving System Data…\nDo not turn off or reset the PlayStation 2 console, or remove any Memory Cards (8MB) (for PlayStation 2) or controllers."

.orga 0x2603C0
.str "Load System Data?"

.orga 0x2603F0
.str "System Data loaded successfully. #Re○#Wh"

.orga 0x260420
.str "Failed to load System Data. #Re○#Wh"

.orga 0x260450
.str "The Memory Card (8MB) (for PlayStation 2) in Memory Card slot 1 is not formatted.\nWould you like to format it now?"

.orga 0x2604D0
.str "Formatting…\nDo not turn off or reset the PlayStation 2 console, or remove any Memory Cards (8MB) (for PlayStation 2) or controllers."

.orga 0x260570
.str "Failed to format. #Re○#Wh"

.orga 0x2605A0
.str "Create System Data?"

.orga 0x2605D0
.str "No data exists. #Re○#Wh"

.orga 0x260670
.str "No Memory Card (8MB) (for PlayStation 2) inserted in Memory Card slot 1."

.orga 0x260740
.str "Overwrite existing data?\nThe previous data will be lost."

.orga 0x260790
.str "Data saved. #Re○#Wh"

.orga 0x2607C0
.str "Failed to save data. #Re○#Wh"

.orga 0x2607F0
.str "Create new data?"

.orga 0x260820
.str "Saving…\nDo not turn off or reset the PlayStation 2 console, or remove any Memory Cards (8MB) (for PlayStation 2) or controllers."

.orga 0x002608C0
.str "Load data?"

.orga 0x00260B70
.str "Ys 3 Data search"

// Names ------------------------------------------------------

.orga 0x2638D8
.str "Adol"

.orga 0x2638E0
.str "Dogi"

.orga 0x2638E8
.str "Niena"

.orga 0x2638F0
.str "Terra"

.orga 0x2638F8
.str "Massea"

.orga 0x263908
.str "Stein"

.orga 0x263910
.str "Dorman"

.orga 0x263920
.str "Rizze"

.orga 0x263928
.str "Jabir"

.orga 0x263938
.str "Effie"

.orga 0x263940
.str "King of Kefin"

.orga 0x263950
.str "Alga"

.orga 0x263958
.str "Dios"

.orga 0x263968
.str "Nottis"

.orga 0x263978
.str "Chase"

.orga 0x263988
.str "Aisha"

.orga 0x263998
.str "Willy"

.orga 0x2639A8
.str "Muhaba"

.orga 0x2639B8
.str "Balck"

.orga 0x2639C0
.str "Abyss"

.orga 0x2639C8
.str "Karion"

//.orga 0x2639D8
//.str "Blacksmith"

.orga 0x2639E0
.str "Sailor"

.orga 0x2639E8
.str "Butler"

.orga 0x2639F0
.str "Maid"

//.orga 0x2639F8
//.str "Lower Ranking Soldier"

.orga 0x263A08
.str "Soldier"

//.orga 0x263A10
//.str "Adventurer A"
//
//.orga 0x263A20
//.str "Adventurer B"
//
//.orga 0x263A30
//.str "Merchant A"
//
//.orga 0x263A38
//.str "Merchant B"

.orga 0x263A40
.str "Kobold"

//.orga 0x263A50
//.str "Desert Grandma"
//
//.orga 0x263A60
//.str "Desert Grandpa"
//
//.orga 0x263A70
//.str "Desert Lady"
//
//.orga 0x263A78
//.str "Desert Man A"
//
//.orga 0x263A98
//.str "Desert Man B"
//
//.orga 0x263A98
//.str "Desert Girl"
//
//.orga 0x263AA8
//.str "Desert Boy"
//
//.orga 0x263AB8
//.str "Kefin Man A"
//
//.orga 0x263AC8
//.str "Kefin Man B"
//
//.orga 0x263AD8
//.str "Kefin Lady A"
//
//.orga 0x263AE8
//.str "Kefin Lady B"
//
//.orga 0x263AF8
//.str "Resistance A"
//
//.orga 0x263B08
//.str "Resistance B"
//
//.orga 0x263B18
//.str "Grandpa A"
//
//.orga 0x263B28
//.str "Grandpa B"
//
//.orga 0x263B38
//.str "Grandma"
//
//.orga 0x263B48
//.str "Townsman A"
//
//.orga 0x263B50
//.str "Townsman B"
//
//.orga 0x263B58
//.str "Townslady A"
//
//.orga 0x263B60
//.str "Townslady B"
//
//.orga 0x263B68
//.str "Grandma"
//
//.orga 0x263B78
//.str "Grandpa"
//
//.orga 0x263B88
//.str "Boy A"
//
//.orga 0x263B98
//.str "Boy B"
//
//.orga 0x263BA8
//.str "Girl A"

.orga 0x263BB8
.str "Dog"

//.orga 0x263BC0
//.str "Girl B"
//
//.orga 0x263BD0
//.str "Kidnapped Stein"
//
//.orga 0x263BE0
//.str "Nottis & Dios"
//
//.orga 0x263BF8
//.str "Beautiful Woman"
//
//.orga 0x263C08
//.str "Young Girl"
//
//.orga 0x263C10
//.str "Ruffian A"
//
//.orga 0x263C20
//.str "Ruffian B"
//
//.orga 0x263C30
//.str "Mysterious Voice"
//
//.orga 0x263C38
//.str "Mysterious Man"

.orga 0x263C40
.str "Burly Man"

// Load Menu ------------------------------------------------------

//Unused?
//.orga 0x2603C8
//.str "Would you like to load this file?"

//.orga 0x260B28
//.str "Yes"

//.orga 0x260B30
//.str "No"

// Shop Menu (Buy) ------------------------------------------------

.orga 0x263C50
.str "Buy or Sell?"

.orga 0x263C70
.str "Select an item to purchase."

.orga 0x263C90
.str "Use the D-Pad to select the quantity."

//.orga 0x263CC0
//.str "You cannot carry any more swords."

//.orga 0x263CE0
//.str "You cannot carry any more shields."

.orga 0x263D00
.str "You cannot carry any more armor."

.orga 0x263D20
.str "You cannot carry any more accessories."

//.orga 0x263D50
//.str "You cannot carry any more of that item."

.orga 0x263D70
.str "Purchase this item?   @0    @1@C1@0"

.orga 0x263DA0
.str "Not enough Gold!"

.orga 0x263DC0
.str "Purchased @b piece(s) of @a!"

// Shop Menu (Sell) ------------------------------------------------

.orga 0x263DE0
.str "Select a category."

.orga 0x263E00
.str "Select an item to sell."

.orga 0x263E20
.str "You have no items in this category."

.orga 0x263E50
.str "Use the D-Pad to select the quantity to sell."

.orga 0x263E80
.str "That item cannot be sold."

.orga 0x263EB0
.str "You cannot sell your last sword!"

.orga 0x263EE0
.str "Sell this item?       @0    @1@C1@o"

.orga 0x263F10
.str "Sold @b piece(s) of @a!"

// Refinery Menu) ------------------------------------------------

.orga 0x263F30
.str "Equipped items cannot be sold."

.orga 0x263F60
.str "Select a weapon to refine. 【#cy×#wh…Back】"

//.orga 0x263FA0
//.str "This weapon cannot be refined any further."

//.orga 0x263FC0
//.str "Equipped Alchemic Stones will be removed."

//.orga 0x263FE0
//.str "There is a risk the weapon may break."

.orga 0x264000
.str "Refine this weapon?   @0    @1@C1"

.orga 0x264030
.str "You do not have enough Parace."

.orga 0x264050
.str "This weapon cannot be refined, as you risk losing your last one."

.orga 0x264080
.str "Refinement successful!"

.orga 0x2640A0
.str "Refinement failed…"

// Alchemic Stone Menu ------------------------------------------------

.orga 0x2640C0
.str "Select an Alchemic Stone to create. 【#cy×#wh…Back】"

.orga 0x264100
.str "Create this Alchemic Stone? @0    @1@C1"

//.orga 0x264130
//.str "You cannot create any more of this Alchemic Stone."

//.orga 0x264150
//.str "You do not have enough Elementals."

.orga 0x264170
.str "Created @a!"

.orga 0x264190
.str "Select a slot to modify."

.orga 0x2641C0
.str "Remove all Alchemic Stones."

//.orga 0x2641E0
//.str "There are no available slots to set an Alchemic Stone."

//.orga 0x264200
//.str "You cannot place four or more of the same Alchemic Stone in a row."

.orga 0x264240
.str "Select an Alchemic Stone to set."

//.orga 0x264260
//.str "Remove the currently set Alchemic Stone."

// Alchemic Stone Descriptions ------------------------------------------------

//.orga 0x264280
//.str "Allows the user to shoot a ball of fire forward."

//.orga 0x2642A0
//.str "Allows the user to shoot a homing sphere of fire."

//.orga 0x2642D0
//.str "Momentarily wreathes the sword's blade in flame, increasing its attack power."

//.orga 0x264300
//.str "Causes blades of ice to erupt from the ground, piercing the enemy."

//.orga 0x264330
//.str "Traps an enemy in a sphere of water, draining its movement and health."

//.orga 0x264360
//.str "Creates a vortex of water that slices through enemies."

//.orga 0x264380
//.str "Allows the user to shoot a piercing blade of wind."

//.orga 0x2643B0
//.str "Allows the user to fire a bolt of lightning that pierces through enemies."

//.orga 0x2643E0
//.str "Creates a vortex of wind around the caster, shredding enemies."

//.orga 0x264410
//.str "Allows the user to shoot a stone projectile forward."

//.orga 0x264430
//.str "Shakes the ground, damaging enemies."

.orga 0x264460
.str "Summons a boulder from the sky to crush enemies."

//.orga 0x264490
//.str "Invigorates the caster's life force to heal their wounds."

// Equipment Menu ------------------------------------------------

.orga 0x2644C0
.str "Select the equipment you wish to change."

.orga 0x2644F0
.str "Select a sword to equip."

.orga 0x264510
.str "Select a shield to equip."

.orga 0x264530
.str "Select an armor to equip."

.orga 0x264550
.str "Select an accessory to equip."

.orga 0x264580
.str "Select an item to equip."

.orga 0x2645B0
.str "Remove current equipment."

//.orga 0x2645D0
//.str "You have no equippable items in this category."

// Item Menu ------------------------------------------------

//.orga 0x2645F0
//.str "Use the #re○#wh button to use the selected item."

.orga 0x264620
.str "Select an item to inspect."

.orga 0x264650
.str "This item cannot be used."

.orga 0x264670
.str "This item cannot be used at this time."

.orga 0x2646A0
.str "You have no items."

.orga 0x2646C0
.str "Use this item?              @0    @1@C1"

.orga 0x2646F0
.str "You acquired\n%s!"

// System & Main Menu ------------------------------------------------

//.orga 0x264700
//.str "You will be returned to the location of your Quick Save."

.orga 0x264730
.str "The data will be loaded."

//.orga 0x264750
//.str "You will be returned to the title screen."

.orga 0x264770
.str "Load from Quick Save?           @0    @1@C1"

.orga 0x2647A0
.str "Load this data?                 @0    @1@C1"

.orga 0x2647D0
.str "Return to the title screen?     @0    @1@C1"

.orga 0x264800
.str "Perform a Quick Save."

.orga 0x264820
.str "Open the Equipment screen."

.orga 0x264840
.str "Open the Alchemic Stones screen."

.orga 0x264860
.str "Open the Item screen."

.orga 0x264880
.str "Open the Options screen."

.orga 0x2648A0
.str "Perform a Quick Save?         @0    @1@C1"

.orga 0x2648E0
.str "Quick Save complete!"

// Places ------------------------------------------------

//.orga 0x2648F5
//.str "Port Town of Xandria"

.orga 0x268900
.str "Xandria Plains"

.orga 0x264910
.str "Massea's House"

//Meretseger
//.orga 0x264920
//.str "Mersegera Forest"

//.orga 0x264930
//.str "Alchemist's House"
//
//.orga 0x264940
//.str "The Arena"

.orga 0x264948
.str "Foresta Village"

.orga 0x264958
.str "Nead Cave"

//.orga 0x264968
//.str "Chamber of the Crystal"

.orga 0x264978
.str "Ramzen Plains"

.orga 0x264990
.str "Trading City of Ramzen"

//Theban
//.orga 0x2649A8
//.str "Zeibe Plains"
//
//Theban
//.orga 0x2649B8
//.str "The Zeibe Ruins"
//
//.orga 0x2649C8
//.str "Ramzen Great Falls"

.orga 0x2649D8
.str "Ramzen Caverns"

.orga 0x2649F0
.str "Desert Town of Ferte"

//.orga 0x264A08
//.str "Ferte Wilderness"
//
//Sahala
//.orga 0x264A18
//.str "Safar Desert"

.orga 0x264A28
.str "The Oasis"

//.orga 0x264A38
//.str "The Ruined City of Kefin"
//
//.orga 0x264A48
//.str "Chamber of Rituals"
//
//.orga 0x264A58
//.str "The Capital of Sand, Kefin"
//
//.orga 0x264A68
//.str "South Tower"
//
//.orga 0x264A70
//.str "Underground Passage"
//
//.orga 0x264A80
//.str "Kefin East District"
//
//.orga 0x264A90
//.str "Kefin West District"

.orga 0x264AA0
.str "Secret Facility"

//Suspicious line of 00s.
//.orga 0x264AB0
//.str "Kefin Castle - West Wing"
//Suspicious line of 00s.
//.orga 0x264AD0
//.str "Kefin Castle - East Wing"
//
//.orga 0x264AF0
//.str "Kefin Castle - Central Area"

.orga 0x264B08
.str "Throne Room"

//.orga 0x264B18
//.str "Stage of the Sacred Festival"

.orga 0x264B28
.str "Spiral Staircase"

//.orga 0x264B38
//.str "Chamber of the Philosopher's Stone"

.orga 0x264B48
.str "Sekhet-Heter"

.orga 0x264B88
.str "Archives"

.orga 0x264B60
.str "Jail Cell"

// Weapons ------------------------------------------------

.orga 0x265490
.str "Isios Blade"

.orga 0x2654A8
.str "Battle Sword"

.orga 0x2654B8
.str "Rune Sword"

.orga 0x2654C8
.str "Broadsword"

//Enhanced
.orga 0x2654E0
.str "Enhance Sword"

.orga 0x2654F8
.str "Falchion"

.orga 0x265508
.str "Scimitar"

.orga 0x265518
.str "Longsword"

.orga 0x265528
.str "Sword of Heroes"

.orga 0x265538
.str "Flame Sword"

.orga 0x265550
.str "Hermes Blade"


// Armor ------------------------------------------------

.orga 0x265570
.str "Isios Armor"

.orga 0x265588
.str "Battle Armor"

.orga 0x265598
.str "Reflex"

.orga 0x2655A8
.str "Plate Mail"

.orga 0x2655B8
.str "Scale Mail"

.orga 0x2655C8
.str "Chain Mail"

.orga 0x2655D8
.str "Leather Armor"


// Shields ------------------------------------------------

.orga 0x2655F0
.str "Isios Shield"

.orga 0x265608
.str "Battle Shield"

.orga 0x265618
.str "Mirror Shield"

.orga 0x265630
.str "Heater Shield"

.orga 0x265648
.str "Large Shield"

.orga 0x265658
.str "Buckler"

.orga 0x265668
.str "Leather Shield"

// Accessories ------------------------------------------------

.orga 0x265678
.str "Power Ring"

.orga 0x265688
.str "Shield Ring"

.orga 0x265698
.str "Magic Ring"

.orga 0x2656B0
.str "Berserk Ring"

//.orga 0x2656C8
//.str "Alchemist's Watch"

//.orga 0x2656D8
//.str "Spirit Stone"

//.orga 0x2656E0
//.str "Thief's Gauntlets"

.orga 0x2656F0
.str "Scrub Brush"

.orga 0x265700
.str "Isios Scrub Brush"

//.orga 0x265718
//.str "Rival Shop Flyer"

.orga 0x265728
.str "Impa's Bracelet"

//.orga 0x265738
//.str "Sapan's Necklace"

//.orga 0x265748
//.str "Jewel of Patience"


// Consumables ------------------------------------------------

//.orga 0x265758
//.str "Celcetan Panacea"

.orga 0x265768
.str "Nead Panacea"

.orga 0x265778
.str "Hi-Potion"

.orga 0x265788
.str "Potion"

//.orga 0x265798
//.str "Dried Meat"

.orga 0x2657A0
.str "Maju Fruit"

.orga 0x2657B0
.str "Antidote Herb"

.orga 0x2657C0
.str "Elixir"

//.orga 0x2657D0
//.str "Seed of Power"

.orga 0x2657D8
.str "Seed of Defense"

.orga 0x2657E8
.str "Seed of Wisdom"

// Spells ------------------------------------------------

.orga 0x2657F8
.str "Heat Ball"

.orga 0x265810
.str "Fire Blast"

.orga 0x265830
.str "Fire Weapon"

.orga 0x265850
.str "Ice Crescent"

.orga 0x265870
.str "Water Lock"

.orga 0x265890
.str "Cyclone Water"

.orga 0x2658A8
.str "Air Cutter"

.orga 0x2658B0
.str "Spark Bolt"

.orga 0x2658C8
.str "Air Slash"

.orga 0x2658E0
.str "Shoot Stone"

.orga 0x2658F8
.str "Earth Shock"

.orga 0x265910
.str "Rock Crash"

.orga 0x265928
.str "Healing"


// Key Items ------------------------------------------------

.orga 0x265938
.str "Ocarina"

.orga 0x265948
.str "Surge Eye"

//.orga 0x265958
//.str "Water Crystal Pyui"

//.orga 0x265968
//.str "Fire Crystal Agni"

.orga 0x265978
.str "Earth Crystal Teru"

.orga 0x265
.str "Sylphid's Feather"

.orga 0x2659A8
.str "Medal"

.orga 0x265980
.str "Garam's Key"

.orga 0x2659C0
.str "Letter and Ingredients"

.orga 0x2659D8
.str "White Emelas"

.orga 0x2659E8
.str "Otherworld Key"


// Item Descriptions ------------------------------------------------
//Isios Blade
//.orga 0x265A00
//.str "A sword forged from an ultimate metal created via Alchemy.\nIt holds within it the finest sharpness and the greatest power of Alchemy."
//
////Enhanced
//Enhance Sword
//.orga 0x265A60
//.str "A sword with a long body and a thick, heavy blade.\nIt is lighter than it appears and very easy to wield."
//
//Falchion
//.orga 0x265AA0
//.str "A sword with special decorations applied to a scimitar.\nThese adornments have the effect of strengthening the power of Alchemy."
//
//Broadsword
//.orga 0x265B00
//.str "A sword of forged steel with enhanced strength and sharpness.\nIt makes use of its wide blade and excels in slashing combat."
//
//Rune Sword
//.orga 0x265B60
//.str "A slender sword that possesses a higher durability than its appearance would suggest.\nIt is suitable for thrusting and, in the right hands, can even pierce plate mail."
//
//Scimitar
//.orga 0x265BC0
//.str "A single-edged, wide-bladed sword crafted to be heavier at its tip.\nIt is designed less for stabbing and more for cleaving cuts."
//
//Battle Sword
//.orga 0x265C20
//.str "A thick-bladed sword with a curved edge.\nIt specializes in downward swings to slash through enemies."
//
//Longsword
//.orga 0x265C70
//.str "A sword of common iron, strengthened through quenching.\nIts blade is thick, but the core is not as hard, making it prone to bending."
//
//Sword of Heroes
//.orga 0x265CD0
//.str "A sword with a unique hilt decoration that emits a faint aura.\nIt is said to possess the power to heal its wounded master."
//
//Flame Sword
//.orga 0x265D30
//.str "A legendary sword from the land of Felghana with a blade wreathed in flame.\nIt is capable of casting the Heat Ball spell."
//
//Hermes Blade
//.orga 0x265D90
//.str "A sword said to have been created via Alchemy.\nHowever, as it was likely an experimental model, multiple copies have been confirmed to exist."
//
//Isios Armor
//.orga 0x265DF0
//.str "Armor forged from an ultimate metal created via Alchemy.\nIt boasts a perfect defense that cannot be pierced by any blade."
//
//Battle Armor
//.orga 0x265E50
//.str "Steel armor with ornate decorations on its surface.\nIt is constructed in a way that does not restrict movement when swinging a sword."
//
//Reflex
//.orga 0x265EB0
//.str "Iron armor with a surface polished like a mirror.\nIts finish also grants it the ability to defend against magical attacks."
//
//Plate Mail
//.orga 0x265F10
//.str "Iron armor crafted from hammered steel plates.\nIt is exceptionally heavy, but possesses outstanding defensive power."
//
//Scale Mail
//.orga 0x265F60
//.str "Armor made of small iron plates linked together like the scales of a fish.\nIt is equipped by many warriors as a general-purpose armor."
//
//Chain Mail
//.orga 0x265FC0
//.str "Armor made of interlocking iron chains, woven together with brass wire.\nFor its light weight, it provides sufficient defensive performance."
//
//Leather Armor
//.orga 0x266020
//.str "Armor made from hardened animal hides.\nIt is light and easy to move in, but its defensive capabilities are not to be relied upon."
//
//Isios Shield
//.orga 0x266070
//.str "A shield forged from an ultimate metal created via Alchemy.\nNo matter the blade, it cannot be pierced."
//
//Battle Shield
//.orga 0x2660D0
//.str "A large steel shield with ornate decorations on its surface.\nIt is designed so as not to get in the way when swinging a sword."
//
//Mirror Shield
//.orga 0x266130
//.str "A shield with a surface so polished by a special process that it resembles a mirror.\nThis finish also grants it properties that suppress magical attacks."
//
//Heater Shield
//.orga 0x266190
//.str "A finely-crafted, kite-shaped shield.\nA standard type of shield that is widely and commonly used."
//
//Large Shield
//.orga 0x2661E0
//.str "A large, unadorned shield made entirely of iron.\nIt has high defensive power, but is heavy and difficult to handle."
//
//Buckler
//.orga 0x266230
//.str "A round shield with a wooden body and an iron frame.\nIt is very light and can be used to quickly parry an opponent's blow."
//
//Leather Shield
//.orga 0x266290
//.str "A shield made from hardened leather.\nBeing made of hide, it is ultimately nothing more than a rudimentary tool."
//
//Power Ring
//.orga 0x2662E0
//.str "A ring adorned with a light-yellow jewel.\nIt is capable of raising attack power."
//
//Shield Ring
//.orga 0x266320
//.str "A ring adorned with a pale-blue jewel.\nIt is capable of raising defensive power."
//
//Magic Ring
//.orga 0x266360
//.str "A ring adorned with a deep-green jewel.\nIt is capable of raising both alchemic attack and defense power."
//
//Berserk Ring
//.orga 0x2663B0
//.str "A ring adorned with a crimson jewel.\nWhile it raises attack power, in exchange, defensive power is lowered."
//
//Alchemist's Watch
//.orga 0x266400
//.str "A pocket watch with a gorgeous silver finish.\nIt speeds up the charge time for Alchemic Stones."
//
//Spirit Stone
//.orga 0x266450
//.str "A brooch in the shape of a feather, adorned with a blue jewel.\nIt has the power to increase the amount of Elementals obtained."
//
//Thief's Gauntlets
//.orga 0x2664B0
//.str "Gauntlets made of tanned leather, decorated with the image of a wolf.\nIt has the power to increase the amount of money obtained."
//
//Scrub Brush
//.orga 0x266500
//.str "A common household scrubbing brush.\nIt allows the holder to gain more experience points than usual."
//
//Isios Scrub Brush
//.orga 0x266550
//.str "A special scrubbing brush that emits a blue aura.\nIt has the power to increase the number of hits per attack."
//
//Rival Shop Flyer
//.orga 0x2665A0
//.str "A flyer, written on parchment, listing another shop's prices.\nIt allows one to purchase items at a discount."
//
//Impa's Bracelet
//.orga 0x2665F0
//.str "A bracelet with a carving of Anubis.\nIt is capable of preventing all forms of poison."
//
//Sapan's Necklace
//.orga 0x266640
//.str "A necklace with a carving of Baal.\nIt is capable of preventing paralysis."
//
//Jewel of Patience
//.orga 0x266680
//.str "A jewel that shines with a rainbow luster.\nIt increases the life force of its owner."
//
//Celcetan Panacea
//.orga 0x2666C0
//.str "A blue medicine in a decorated glass bottle.\nIt is said to cure any and all bodily ailments."
//
//Nead Panacea
//.orga 0x266720
//.str "A green medicine in a decorated glass bottle.\nIt is made from a medicinal herb said to be found in Nead Cave."
//
//Hi-Potion
//.orga 0x266780
//.str "An orange medicine in a simple glass bottle.\nA blend of extracts from several special medicinal herbs."
//
//Potion
//.orga 0x2667E0
//.str "A red medicine in a simple glass bottle.\nA blend of extracts from several medicinal herbs."
//
//Dried Meat
//.orga 0x266830
//.str "Meat that has been dried to preserve it.\nAn essential food for travelers, but it is tasteless and unpleasant."
//
//Maju Fruit
//.orga 0x266890
//.str "A reddish-brown fruit that grows on the Maju tree.\nEating it fills the body with a mysterious power."
//
//Antidote Herb
//.orga 0x2668E0
//.str "A green herb that grows on the plains.\nIt possesses a strong poison-curing effect."
//
//Elixir
//.orga 0x266920
//.str "A yellow medicine in a lavishly decorated bottle.\nIt is said to be made with a lost art and can even revive the dead."
//
//Seed of Power
//.orga 0x266980
//.str "A seed filled with the power of the great trees.\nConsuming it grants the strength to withstand any disaster."
//
//Seed of Defense
//.orga 0x2669D0
//.str "A seed filled with the life of the great trees.\nConsuming it grants the vitality of nature itself."
//
//Seed of Wisdom
//.orga 0x266A10
//.str "A seed filled with the memory of the great trees.\nConsuming it grants a piece of a memory from ancient times."
//
//Heat Ball
//.orga 0x266A60
//.str "A round, red Alchemic Stone that unleashes power when set in a sword.\nAllows the user to shoot a ball of fire forward."
//
//Fire Blast
//.orga 0x266AB0
//.str "A triangular, red Alchemic Stone that unleashes power when set in a sword.\nAllows the user to shoot a homing sphere of fire."
//
//Fire Weapon
//.orga 0x266B10
//.str "A square, red Alchemic Stone that unleashes power when set in a sword.\nMomentarily wreathes the sword's blade in flame, increasing its attack power."
//
//Ice Crescent
//.orga 0x266B70
//.str "A round, blue Alchemic Stone that unleashes power when set in a sword.\nCauses blades of ice to erupt from the ground, piercing the enemy."
//
//Water Lock
//.orga 0x266BD0
//.str "A triangular, blue Alchemic Stone that unleashes power when set in a sword.\nTraps an enemy in a sphere of water, draining its movement and health."
//
//Cyclone Water
//.orga 0x266C30
//.str "A square, blue Alchemic Stone that unleashes power when set in a sword.\nCreates a vortex of water that slices through enemies."
//
//Air Cutter
//.orga 0x266C80
//.str "A round, green Alchemic Stone that unleashes power when set in a sword.\nAllows the user to shoot a piercing blade of wind."
//
//Spark Bolt
//.orga 0x266CE0
//.str "A triangular, green Alchemic Stone that unleashes power when set in a sword.\nAllows the user to fire a bolt of lightning that pierces through enemies."
//
//Air Slash
//.orga 0x266D40
//.str "A square, green Alchemic Stone that unleashes power when set in a sword.\nCreates a vortex of wind around the caster, shredding enemies."
//
//Shoot Stone
//.orga 0x266DA0
//.str "A round, yellow Alchemic Stone that unleashes power when set in a sword.\nAllows the user to shoot a stone projectile forward."
//
//Earth Shock
//.orga 0x266DF0
//.str "A triangular, yellow Alchemic Stone that unleashes power when set in a sword.\nShakes the ground, damaging enemies."
//
//Rock Crash
//.orga 0x266E50
//.str "A square, yellow Alchemic Stone that unleashes power when set in a sword.\nSummons a boulder from the sky to crush enemies."
//
//Healing
//.orga 0x266EB0
//.str "A round, white Alchemic Stone that unleashes power when set in a sword.\nInvigorates the caster's life force to heal their wounds."
//
//Ocarina
//.orga 0x266F10
//.str "The ocarina that Niena holds so dear.\nHer only possession from the time before she met her father."
//
//Surge Eye
//.orga 0x266F60
//.str "An amulet, passed down in the Safar Desert, that is shaped like a human eye.\nIt is said that one who holds it can cross the deadly desert."
//
//Water Crystal Pyui
//.orga 0x266FD0
//.str "A blue, glowing crystal.\nIt is said to be connected to the lost art of Alchemy."
//
//Fire Crystal Agni
//.orga 0x267020
//.str "A red, glowing crystal.\nIt is said to be connected to the lost art of Alchemy."
//
//Earth Crystal Teru
//.orga 0x267070
//.str "An ochre-colored, glowing crystal.\nIt is said to be connected to the lost art of Alchemy."
//
//Sylphid's Feather
//.orga 0x2670D0
//.str "A feather dropped by a wind spirit.\nIt allows the holder to instantly fly to a place that shares its same elemental wavelength."
//
//Medal
//.orga 0x267120
//.str "An old medal bearing the royal crest of Kefin.\nIt is said to guide its owner to the lost city."
//
//Garam's Key
//.orga 0x267180
////Theban
//.str "A small, decorated key.\nIt can open the door to a small room in the Zeibe Ruins."
//
//Letter and Ingredients
//.orga 0x2671D0
//.str "A letter from the merchant to Massea requesting a medicine blend, and the materials for it.\nMassea's house is past the Xandria Plains."
//
//White Emelas
//.orga 0x267240
//.str "A white fragment that possesses a mysterious power.\nThis enigmatic stone almost feels as if it were a living thing."
//
//Otherworld Key
//.orga 0x267290
//.str "A faintly glowing tome. Within is written: 'In the place\nwhere the sun rises, present the four elements.'"

// BGM Names & Gallery Image Titles ------------------------------------------------

.orga 0x2C1C70
.str "BGM00: No BGM"

//.orga 0x02C1C80
//.str "BGM01: Dancing on the Road"
//
//.orga 0x02C1C98
//.str "BGM02: A Premonition"
//
//.orga 0x02C1CB0
//.str "BGM03: Trading Town of Redmont"
//
//.orga 0x02C1CD0
//.str "BGM04: A Quiet Moment"
//
//.orga 0x02C1CE0
//.str "BGM05: Welcome!!"
//
//.orga 0x02C1D00
//.str "BGM06: Prelude to the Adventure"
//
//.orga 0x02C1D20
//.str "BGM07: The Boy Who Had Wings"
//
//.orga 0x02C1D40
//.str "BGM08: Be Careful"
//
//.orga 0x02C1D50
//.str "BGM09: Beasts as Black as Night"
//
//.orga 0x02C1D70
//.str "BGM10: Illburns Ruins"
//
//.orga 0x02C1D90
//.str "BGM11: A Searing Struggle"
//
//.orga 0x02C1DA8
//.str "BGM12: Snare of Darkness"
//
//.orga 0x02C1DC0
//.str "BGM13: Death Blitz"
//
//.orga 0x02C1DE0
//.str "BGM14: Quickening Dream"
//
//.orga 0x02C1E00
//.str "BGM15: Steeling the Will to Fight"
//
//.orga 0x02C1E20
//.str "BGM16: Tearful Twilight"
//
//.orga 0x02C1E40
//.str "BGM17: Valestein Castle"
//
//.orga 0x02C1E58
//.str "BGM18: Seal of Time"
//
//.orga 0x02C1E70
//.str "BGM19: Beat of Destruction"
//
//.orga 0x02C1E88
//.str "BGM20: Tower of Fate"
//
//.orga 0x02C1E88
//.str "BGM20:運命の塔"
//
//.orga 0x02C1EA0
//.str "BGM21: Behold!!"
//
//.orga 0x02C1EB8
//.str "BGM22: The Strongest Foe"
//
//.orga 0x02C1ED0
//.str "BGM23: Morning of Departure"
//
//.orga 0x02C1EF0
//.str "BGM24: Wanderers from Ys"
//
//.orga 0x02C1F10
//.str "No.00: No Image"
//
//.orga 0x02C1F20
//.str "No.01: Prologue"
//
//.orga 0x02C1F40
//.str "No.02: Elena's Flashback"
//
//.orga 0x02C1F60
//.str "No.03: The Tablet of Destiny"
//
//.orga 0x02C1F80
//.str "No.04: The Decayed Village"
//
//.orga 0x02C1FA0
//.str "No.05: The Evil God Galbalan"
//
//.orga 0x02C1FC0
//.str "No.06: To Galbalan Island"
//
//.orga 0x02C1FE0
//.str "No.07: Morning of Departure"
//
//.orga 0x02C2000
//.str "No.08: In Those Eyes..."
//
//.orga 0x02C2020
//.str "No.09: The Collapse of Galbalan Island"
//
//.orga 0x02C2040
//.str "No.10: Portrait: Adol"
//
//.orga 0x02C2060
//.str "No.11: Portrait: Dogi"
//
//.orga 0x02C2080
//.str "No.12: Portrait: Elena"
//
//.orga 0x02C20A0
//.str "No.13: Portrait: Chester"
//
//.orga 0x02C20C0
//.str "No.14: Portrait: Edgar"
//
//.orga 0x02C20E0
//.str "No.15: Portrait: Pierre"
//
//.orga 0x02C2100
//.str "No.16: Portrait: Dogi's Master"
//
//.orga 0x02C2120
//.str "No.17: Portrait: Count McGuire"
//
//.orga 0x02C2148
//.str "No.18: Poster"
//
//.orga 0x02C2158
//.str "BGM01: Feena"
//
//.orga 0x02C2170
//.str "BGM02: Promalock"
//
//.orga 0x02C2190
//.str "BGM03: Romun Empire"
//
//.orga 0x02C21A8
//.str "BGM04: Crimson Wings"
//
//.orga 0x02C21C0
//.str "BGM05: The Great Forest of Celceta"
//
//.orga 0x02C21E0
//.str "BGM06: Want to be Kind"
//
//.orga 0x02C21F8
//.str "BGM07: Anxiety"
//
//.orga 0x02C2210
//.str "BGM08: Valley of Quicksand"
//
//.orga 0x02C2228
//.str "BGM09: Leeza"
//
//.orga 0x02C2240
//.str "BGM10: Field"
//
//.orga 0x02C2260
//.str "BGM11: Beyond Reminiscence"
//
//.orga 0x02C2280
//.str "BGM12: Bronze District"
//
//.orga 0x02C2298
//.str "BGM13: Burning Sword"
//
//.orga 0x02C22A8
//.str "BGM14: The Five Disciples"
//
//.orga 0x02C22C0
//.str "BGM15: Temple of the Sun"
//
//.orga 0x02C22E0
//.str "BGM16: Lava Zone ~ A Kiss for Eldeel"
//
//.orga 0x02C2310
//.str "BGM17: Harlequin's Temptation"
//
//.orga 0x02C2328
//.str "BGM18: Sanctuary"
//
//.orga 0x02C2340
//.str "BGM19: The Ancient City Surfaces"
//
//.orga 0x02C2358
//.str "BGM20: The Clan of Darkness
//
//.orga 0x02C2370
//.str "BGM21: Eldeel"
//
//.orga 0x02C2390
//.str "BGM22: Battle #58"
//
//.orga 0x02C23B0
//.str "BGM23: Walking the Path of Legend"
//
//.orga 0x02C23D0
//.str "BGM24: In the Fires of Ignition"
//
//.orga 0x02C23E8
//.str "BGM25: Karna"
//
//.orga 0x02C23F8
//.str "BGM26: The Final Decisive Battle"
//
//.orga 0x02C2410
//.str "BGM27: A New Beginning"
//
//.orga 0x02C2430
//.str "BGM28: Poem of the Blue Moon"
//
//.orga 0x02C2450
//.str "BGM29: Game Over"
//
//.orga 0x02C2470
//.str "BGM30: The Dawn of Ys"
//
//.orga 0x02C2488
//.str "No.01: The Relief"
//
//.orga 0x02C24A0
//.str "No.02: The Golden Castle Surfaces"
//
//.orga 0x02C24C0
//.str "No.03: Bird's-Eye View of the Golden Castle"
//
//.orga 0x02C24E0
//.str "No.04: World Map"
//
//.orga 0x02C2500
//.str "No.05: Portrait: Adol"
//
//.orga 0x02C2520
//.str "No.06: Portrait: Dogi"
//
//.orga 0x02C2540
//.str "No.07: Portrait: Karna"
//
//.orga 0x02C2560
//.str "No.08: Portrait: Leeza"
//
//.orga 0x02C2580
//.str "No.09: Portrait: Gruda"
//
//.orga 0x02C25A0
//.str "No.10: Portrait: Bami"
//
//.orga 0x02C25C0
//.str "No.11: Portrait: Gadis"
//
//.orga 0x02C25E0
//.str "No.12: Portrait: Eldeel"
//
//.orga 0x02C2610
//.str "No.13: Portrait: Bratos"
//
//.orga 0x02C2630
//.str "No.14: Portrait: Flair"
//
//.orga 0x02C2650
//.str "No.15: Portrait: Gazock"
//
//.orga 0x02C2670
//.str "No.16: Portrait: Elder of Komodo"
//
//.orga 0x02C26A0
//.str "No.17: Portrait: Elder of Highland"
//
//.orga 0x02C26D0
//.str "No.18: Portrait: Elder of Selray"
//
//.orga 0x02C26F8
//.str "No.19: Poster"
//
//.orga 0x02C2708
//.str "BGM01: Digest"
//
//.orga 0x02C2718
//.str "BGM02: Title"
//
//.orga 0x02C2728
//.str "BGM03: Continue"
//
//.orga 0x02C2740
//.str "BGM04: Port Town"
//
//.orga 0x02C2750
//.str "BGM05: In The Cradle"
//
//.orga 0x002C2768
//.str "BGM06:Shopping"
//
//.orga 0x02C2780
//.str "BGM07: Field of Gale"
//
//.orga 0x02C2798
//.str "BGM08: Massea"
//
//.orga 0x02C27B0
//.str "BGM09: Bad Species"
//
//.orga 0x02C27D0
//.str "BGM10: Woodside Village"
//
//.orga 0x02C27F0
//.str "BGM11: Warning!!"
//
//.orga 0x02C2810
//.str "BGM12: Sinister Shadow"
//
//.orga 0x02C2828
//.str "BGM14: The Five Disciples"
//
//.orga 0x02C2840
//.str "BGM14: Thieves of Brotherhood"
//
//.orga 0x02C2860
//.str "BGM15: Scheme The Madness"
//
//.orga 0x02C2880
//.str "BGM16: Niena's Melody"
//
//.orga 0x02C2898
//.str "BGM17: Niena"
//
//.orga 0x02C28B0
//.str "BGM18: Wind Knight"
//
//.orga 0x02C28D0
//.str "BGM19: Peace in The Street"
//
//.orga 0x02C28F0
//.str "BGM20: Sand Castle"
//
//.orga 0x02C2910
//.str "BGM21: Wilderness"
//
//.orga 0x02C2930
//.str "BGM22: Stormy Town"
//
//.orga 0x02C2950
//.str "BGM23: Desert Clime"
//
//.orga 0x02C2968
//.str "BGM24: Oasis"
//
//.orga 0x02C2980
//.str "BGM25: Scheme The Madness II"
//
//.orga 0x02C29A0
//.str "BGM26: Pain Maker"
//
//.orga 0x02C29C0
//.str "BGM27: Forgotten City"
//
//.orga 0x02C29E0
//.str "BGM28: Break into Territory"
//
//.orga 0x02C2A00
//.str "BGM29: Battle Against Fate"
//
//.orga 0x02C2A20
//.str "BGM30: Turning Death Spiral"
//
//.orga 0x02C2A40
//.str "BGM31: Theme of Kefin"
//
//.orga 0x02C2A60
//.str "BGM32: Theme of Kefin II"
//
//.orga 0x02C2A80
//.str "BGM33: Crime and Punishment"
//
//.orga 0x02C2AA0
//.str "BGM34: Wicked Pleasure"
//
//.orga 0x02C2AB8
//.str "BGM35: Crumble"
//
//.orga 0x02C2AD0
//.str "BGM36: Theme of Lovers"
//
//.orga 0x02C2AF0
//.str "BGM37: Vanishing World"
//
//.orga 0x02C2B10
//.str "BGM38: Theme of Adol"
//
//.orga 0x02C2B30
//.str "BGM39: The Secret Experience"
//
//.orga 0x02C2B50
//.str "BGM40: Quickening Dream"
//
//.orga 0x02C2B70
//.str "BGM41: Treasure Box"
//
//.orga 0x02C2B88
//.str "No.01: The Capital of Sand"
//
//.orga 0x02C2BA0
//.str "No.02: The Girl with the Winged Scar"
//
//.orga 0x02C2BC0
//.str "No.03: Tender Care"
//
//.orga 0x02C2BD0
//.str "No.04: Parting with Father"
//
//.orga 0x02C2BF0
//.str "No.05: Dogi's Letter"
//
//.orga 0x02C2C10
//.str "No.06: Breaking Through the Wall of Storms"
//
//.orga 0x02C2C30
//.str "No.07: The Resistance Purge"
//
//.orga 0x02C2C50
//.str "No.08: The Secret of the Scar"
//
//.orga 0x02C2C70
//.str "No.09: Melody of Memories"
//
//.orga 0x02C2C88
//.str "No.10: The Rescue"
//
//.orga 0x02C2CA0
//.str "No.11: Reunion with Mother"
//
//.orga 0x02C2CB8
//.str "No.12: The Sacred Festival"
//
//.orga 0x02C2CD0
//.str "No.13: Fusion with the Philosopher's Stone"
//
//.orga 0x002C2CF0
//.str "No.14:No.14: The Port of Departure"
//
//.orga 0x02C2D10
//.str "No.15: Adol on Deck"
//
//.orga 0x02C2D30
//.str "No.16: The Ocarina"
//
//.orga 0x02C2D40
//.str "No.17: Portrait: Adol"
//
//.orga 0x02C2D60
//.str "No.18: Portrait: Dogi"
//
//.orga 0x02C2D80
//.str "No.19: Portrait: Niena"
//
//.orga 0x02C2DA0
//.str "No.20: Portrait: Terra"
//
//.orga 0x02C2DC0
//.str "No.21: Portrait: Massea"
//
//.orga 0x02C2DE0
//.str "No.22: Portrait: Stein"
//
//.orga 0x02C2E00
//.str "No.23: Portrait: Dorman"
//
//.orga 0x02C2E20
//.str "No.24: Portrait: Rizze"
//
//.orga 0x02C2E40
//.str "No.25: Portrait: Effie"
//
//.orga 0x02C2E60
//.str "No.26: Portrait: King of Kefin"
//
//.orga 0x02C2E80
//.str "No.27: Portrait: Jabir"
//
//.orga 0x02C2EA0
//.str "No.28: Portrait: Aisha"
//
//.orga 0x02C2EC0
//.str "No.29: Portrait: Alga"
//
//.orga 0x02C2EE0
//.str "No.30: Portrait: Dios"
//
//.orga 0x02C2F00
//.str "No.31: Portrait: Nottis"
//
//.orga 0x02C2F20
//.str "No.32: Portrait: Chase"
//
//.orga 0x02C2F40
//.str "No.33: Key Visual"

.close
