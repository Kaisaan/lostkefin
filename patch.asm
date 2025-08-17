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

.orga 0x2608C0
.str "Load Data?"

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

.close
