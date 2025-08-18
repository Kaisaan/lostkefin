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
.str "Adol", 0x00, 0x00

.orga 0x2638E0
.str "Dogi"

.orga 0x2638E8
.str "Niena", 0x00

.orga 0x2638F0
.str "Terra"

.orga 0x2638F8
.str "Massea", 0x00, 0x00

.orga 0x263908
.str "Stein", 0x00

.orga 0x263910
.str "Dorman", 0x00, 0x00, 0x00

.orga 0x263920
.str "Rizze", 0x00

.orga 0x263928
.str "Jabil", 0x00, 0x00, 0x00

.orga 0x263938
.str "Effie", 0x00

.orga 0x263940
.str "King of Kefin"

.orga 0x263950
.str "Alga", 0x00, 0x00

.orga 0x263958
.str "Dios", 0x00, 0x00, 0x00

.orga 0x263968
.str "Nottis", 0x00, 0x00

.orga 0x263978
.str "Chase", 0x00, 0x00, 0x00

.orga 0x263988
.str "Aisha", 0x00, 0x00, 0x00

.orga 0x263998
.str "Willy", 0x00, 0x00, 0x00

.orga 0x2639A8
.str "Muhaba", 0x00, 0x00, 0x00

.orga 0x2639B8
.str "Balck", 0x00, 0x00

.orga 0x2639C0
.str "Abyss", 0x00

.orga 0x2639C8
.str "Karion", 0x00, 0x00

//Blacksmith
//.orga 0x2639D8
//.str "鍛冶屋"

.orga 0x2639E0
.str "Sailor"

.orga 0x2639E8
.str "Butler"

.orga 0x2639F0
.str "Maid", 0x00, 0x00

//Foot Soldier
//.orga 0x263
//.str "下級兵士"

.orga 0x263A08
.str "Soldier"

// TODO?
//Adventurer A
//Adventurer B
//Merchant A
//Merchant B
//Kobold
//Desert Old Woman
//Desert Old Man
//Desert Woman
//Desert Man A
//Desert Man B
//Desert Girl
//Desert Boy
//Kefin Man A
//Kefin Man B
//Kefin Woman A
//Kefin Woman B
//Rebel A
//Rebel B
//Man A
//Man B
//Woman
//Villager Man A
//Villager Man B
//Villager Girl A
//Villager Girl B
//Old Woman
//Old Man
//Boy A
//Boy B
//Girl A
//Dog
//Girl B
//Kidnapped Stein
//Noties & Deios
//Beautiful Woman
//Girl
//Thug A
//Thug B
//Mysterious Voice
//Mysterious Man
//Big Man
//Woman

// Load Menu --------------------------------------------

//Unused?
//.orga 0x2603C8
//.str "Would you like to load this file?", 0x00, 0x00, 0x00, 0x00, 0x00, 0x00

.orga 0x2648F0
.str "Xandria Port", 0x00, 0x00

//.orga 0x260B28
//.str "Yes", 0x00

//.orga 0x260B30
//.str "No", 0x00, 0x00, 0x00, 0x00

// ------------------------------------------------------------

.orga 0x263C50
.str "Buy or sell?"

.orga 0x263C70
.str "Select an item to purchase."

.orga 0x263C90
.str "Use the D-Pad to select the quantity."

.orga 0x263CC0
.str "You cannot carry any more swords."

.orga 0x263CE0
.str "You cannot carry any more shields."

.orga 0x263D00
.str "You cannot carry any more armor."


.orga 0x263D20
.str "You cannot carry any more accessories."

.orga 0x263D50
.str "You cannot carry any more of that item."

.orga 0x263D70
.str "Purchase this item?   @0    @1@C1@0"

.orga 0x263DA0
.str "Not enough Gold!"

.orga 0x263DC0
.str "Purchased @b piece(s) of @a!"

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

.orga 0x263F30
.str "Equipped items cannot be sold."

.orga 0x263F60
.str "Select a weapon to refine. 【#cy×#wh…Back】"

.orga 0x263FA0
.str "This weapon cannot be refined any further."

.orga 0x263FC0
.str "Equipped Alchemic Stones will be removed."

.orga 0x263FE0
.str "There is a risk the weapon may break."

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

.orga 0x2640C0
.str "Select an Alchemic Stone to create. 【#cy×#wh…Back】"

.orga 0x264100
.str "Create this Alchemic Stone? @0    @1@C1"

.orga 0x264130
.str "You cannot create any more of this Alchemic Stone."

.orga 0x264150
.str "You do not have enough Elementals."

.orga 0x264170
.str "Created @a!"

.orga 0x264190
.str "Select a slot to modify."

.orga 0x2641C0
.str "Remove all Alchemic Stones."

.orga 0x2641E0
.str "There are no available slots to set an Alchemic Stone."

.orga 0x264200
.str "You cannot place four or more of the same Alchemic Stone in a row."

.orga 0x264240
.str "Select an Alchemic Stone to set."

.orga 0x264260
.str "Remove the currently set Alchemic Stone."

.orga 0x264280
.str "Allows the user to shoot a ball of fire forward."

.orga 0x2642A0
.str "Allows the user to shoot a homing sphere of fire."

.orga 0x2642D0
.str "Momentarily wreathes the sword's blade in flame, increasing its attack power."

.orga 0x264300
.str "Causes blades of ice to erupt from the ground, piercing the enemy."

.orga 0x264330
.str "Traps an enemy in a sphere of water, draining its movement and health."

.orga 0x264360
.str "Creates a vortex of water that slices through enemies."

.orga 0x264380
.str "Allows the user to shoot a piercing blade of wind."

.orga 0x2643B0
.str "Allows the user to fire a bolt of lightning that pierces through enemies."

.orga 0x2643E0
.str "Creates a vortex of wind around the caster, shredding enemies."

.orga 0x264410
.str "Allows the user to shoot a stone projectile forward."

.orga 0x264430
.str "Shakes the ground, damaging enemies."

.orga 0x264460
.str "Summons a boulder from the sky to crush enemies."

.orga 0x264490
.str "Invigorates the caster's life force to heal their wounds."

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

.orga 0x2645D0
.str "You have no equippable items in this category."

.orga 0x2645F0
.str "Use the #re○#wh button to use the selected item."

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

.orga 0x264700
.str "You will be returned to the location of your Quick Save."

.orga 0x264730
.str "The data will be loaded."

.orga 0x264750
.str "You will be returned to the title screen."

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

.close
