.erroronwarning on
.ps2

.loadtable "kefin.tbl", "SJIS"

.open "extracted/SLPM_663.60", "translated/SLPM_663.60", 0x0

// Fix halfwidth characters not updating textbox size correctly
.orga 0x0004CF38
addiu	t7, t7, 0x0A

.orga 0x0004CF44
addiu	a0, a0, 0x01

// Bootup Text ------------------------------------------------

.orga 0x0025FD45
.strn "KaisaanTest"

.orga 0x0025FE70
.strn "Ys 3 Data found"

.orga 0x0025FEB0
.strn "No Ys 3 Data"

.orga 0x00260B70
.strn "Ys 3 Data search"

// Names ------------------------------------------------------

.orga 0x2638D8
.strn "Adol", 0x00, 0x00

.orga 0x2638E0
.strn "Dogi"

.orga 0x2638E8
.strn "Niena", 0x00

.orga 0x2638F0
.strn "Terra"

.orga 0x2638F8
.strn "Massea", 0x00, 0x00

.orga 0x263908
.strn "Stein", 0x00

.orga 0x263910
.strn "Doman", 0x00, 0x00, 0x00

.orga 0x263920
.strn "Rizze", 0x00

.orga 0x263928
.strn "Javil", 0x00, 0x00, 0x00

.orga 0x263938
.strn "Effey", 0x00

.orga 0x263940
.strn "King Kefin"

.orga 0x263950
.strn "Alga", 0x00, 0x00

.orga 0x263958
.strn "Deios", 0x00, 0x00, 0x00

.orga 0x263968
.strn "Nottis", 0x00, 0x00

.orga 0x263978
.strn "Chase", 0x00, 0x00, 0x00

.orga 0x263988
.strn "Aisha", 0x00, 0x00, 0x00

.orga 0x263998
.strn "Willy", 0x00, 0x00, 0x00

.orga 0x2639A8
.strn "Mujaba", 0x00, 0x00, 0x00

.orga 0x2639B8
.strn "Balk", 0x00, 0x00

.orga 0x2639C0
.strn "Abyss", 0x00

.orga 0x2639C8
.strn "Carion", 0x00, 0x00

//Blacksmith
//.orga 0x2639D8
//.strn "鍛冶屋"

.orga 0x2639E0
.strn "Sailor"

.orga 0x2639E8
.strn "Butler"

.orga 0x2639F0
.strn "Maid", 0x00, 0x00

//Foot Soldier
//.orga 0x263
//.strn "下級兵士"

.orga 0x263A08
.strn "Soldier"

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
.strn "Would you like to load this file?", 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00

//Unused?
//.orga 0x2603C8
//.strn "Would you like to load this file?", 0x00, 0x00, 0x00, 0x00, 0x00, 0x00

.orga 0x2648F0
.strn "Xandria Port", 0x00, 0x00

//.orga 0x260B28
//.strn "Yes", 0x00

//.orga 0x260B30
//.strn "No", 0x00, 0x00, 0x00, 0x00

// ------------------------------------------------------------

.close

.open "extracted/DATA.BIN", "translated/DATA.BIN", 0x0

.orga 0x3B9A880
.db 0xFF

.close
