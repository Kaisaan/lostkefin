.include "strings.asm", "UTF8"

Offset equ 0xFFF80

// Ys 3 Music Pointers

.orga 0x23B100

.dw @L2C1C70+Offset :: .skip 8
.dw @L2C1C80+Offset :: .skip 8
.dw @L2C1C98+Offset :: .skip 8
.dw @L2C1CB0+Offset :: .skip 8
.dw @L2C1CD0+Offset :: .skip 8
.dw @L2C1CE0+Offset :: .skip 8
.dw @L2C1D00+Offset :: .skip 8
.dw @L2C1D20+Offset :: .skip 8
.dw @L2C1D40+Offset :: .skip 8
.dw @L2C1D50+Offset :: .skip 8
.dw @L2C1D70+Offset :: .skip 8
.dw @L2C1D90+Offset :: .skip 8
.dw @L2C1DA8+Offset :: .skip 8
.dw @L2C1DC0+Offset :: .skip 8
.dw @L2C1DE0+Offset :: .skip 8
.dw @L2C1E00+Offset :: .skip 8
.dw @L2C1E20+Offset :: .skip 8
.dw @L2C1E40+Offset :: .skip 8
.dw @L2C1E58+Offset :: .skip 8
.dw @L2C1E70+Offset :: .skip 8
.dw @L2C1E88+Offset :: .skip 8
.dw @L2C1EA0+Offset :: .skip 8
.dw @L2C1EB8+Offset :: .skip 8
.dw @L2C1ED0+Offset :: .skip 8
.dw @L2C1EF0+Offset :: .skip 8
.dw @L2C1F08+Offset :: .skip 8

// Ys 3 Gallery Pointers

.orga 0x23B340

.dw @L2C1F10+Offset :: .skip 8
.dw @L2C1F20+Offset :: .skip 8
.dw @L2C1F40+Offset :: .skip 8
.dw @L2C1F60+Offset :: .skip 8
.dw @L2C1F80+Offset :: .skip 8
.dw @L2C1FA0+Offset :: .skip 8
.dw @L2C1FC0+Offset :: .skip 8
.dw @L2C1FE0+Offset :: .skip 8
.dw @L2C2000+Offset :: .skip 8
.dw @L2C2020+Offset :: .skip 8
.dw @L2C2040+Offset :: .skip 8
.dw @L2C2060+Offset :: .skip 8
.dw @L2C2080+Offset :: .skip 8
.dw @L2C20A0+Offset :: .skip 8
.dw @L2C20C0+Offset :: .skip 8
.dw @L2C20E0+Offset :: .skip 8
.dw @L2C2100+Offset :: .skip 8
.dw @L2C2120+Offset :: .skip 8
.dw @L2C2148+Offset :: .skip 8

.dw @LGallery1+offset
.dw 0x00
.dw 0x00
.dw @L2C1F08+Offset

// Ys 4 Music Pointers

.orga 0x23B580

.dw @L2C1C70+Offset :: .skip 8
.dw @L2C2158+Offset :: .skip 8
.dw @L2C2170+Offset :: .skip 8
.dw @L2C2190+Offset :: .skip 8
.dw @L2C21A8+Offset :: .skip 8
.dw @L2C21C0+Offset :: .skip 8
.dw @L2C21E0+Offset :: .skip 8
.dw @L2C21F8+Offset :: .skip 8
.dw @L2C2210+Offset :: .skip 8
.dw @L2C2228+Offset :: .skip 8
.dw @L2C2240+Offset :: .skip 8
.dw @L2C2260+Offset :: .skip 8
.dw @L2C2280+Offset :: .skip 8
.dw @L2C2298+Offset :: .skip 8
.dw @L2C22A8+Offset :: .skip 8
.dw @L2C22C0+Offset :: .skip 8
.dw @L2C22E0+Offset :: .skip 8
.dw @L2C2310+Offset :: .skip 8
.dw @L2C2328+Offset :: .skip 8
.dw @L2C2340+Offset :: .skip 8
.dw @L2C2358+Offset :: .skip 8
.dw @L2C2370+Offset :: .skip 8
.dw @L2C2390+Offset :: .skip 8
.dw @L2C23B0+Offset :: .skip 8
.dw @L2C23D0+Offset :: .skip 8
.dw @L2C23E8+Offset :: .skip 8
.dw @L2C23F8+Offset :: .skip 8
.dw @L2C2410+Offset :: .skip 8
.dw @L2C2430+Offset :: .skip 8
.dw @L2C2450+Offset :: .skip 8
.dw @L2C2470+Offset :: .skip 8
.dw @L2C1F08+Offset :: .skip 8

// Ys 4 Gallery Pointers

.orga 0x23B7C0

.dw @L2C1F10+Offset :: .skip 8
.dw @L2C2488+Offset :: .skip 8
.dw @L2C24A0+Offset :: .skip 8
.dw @L2C24C0+Offset :: .skip 8
.dw @L2C24E0+Offset :: .skip 8
.dw @L2C2500+Offset :: .skip 8
.dw @L2C2520+Offset :: .skip 8
.dw @L2C2540+Offset :: .skip 8
.dw @L2C2560+Offset :: .skip 8
.dw @L2C2580+Offset :: .skip 8
.dw @L2C25A0+Offset :: .skip 8
.dw @L2C25C0+Offset :: .skip 8
.dw @L2C25E0+Offset :: .skip 8
.dw @L2C2610+Offset :: .skip 8
.dw @L2C2630+Offset :: .skip 8
.dw @L2C2650+Offset :: .skip 8
.dw @L2C2670+Offset :: .skip 8
.dw @L2C26A0+Offset :: .skip 8
.dw @L2C26D0+Offset :: .skip 8
.dw @L2C26F8+Offset :: .skip 8

.dw @LGallery2+offset
.dw 0x01
.dw 0x00
.dw @L2C1F08+Offset

// Ys 5 Music Pointers

.orga 0x23BA00

.dw @L2C1C70+Offset :: .skip 8
.dw @L2C2708+Offset :: .skip 8
.dw @L2C2718+Offset :: .skip 8
.dw @L2C2728+Offset :: .skip 8
.dw @L2C2740+Offset :: .skip 8
.dw @L2C2750+Offset :: .skip 8
.dw @L2C2768+Offset :: .skip 8
.dw @L2C2780+Offset :: .skip 8
.dw @L2C2798+Offset :: .skip 8
.dw @L2C27B0+Offset :: .skip 8
.dw @L2C27D0+Offset :: .skip 8
.dw @L2C27F0+Offset :: .skip 8
.dw @L2C2810+Offset :: .skip 8
.dw @L2C2828+Offset :: .skip 8
.dw @L2C2840+Offset :: .skip 8
.dw @L2C2860+Offset :: .skip 8
.dw @L2C2880+Offset :: .skip 8
.dw @L2C2898+Offset :: .skip 8
.dw @L2C28B0+Offset :: .skip 8
.dw @L2C28D0+Offset :: .skip 8
.dw @L2C28F0+Offset :: .skip 8
.dw @L2C2910+Offset :: .skip 8
.dw @L2C2930+Offset :: .skip 8
.dw @L2C2950+Offset :: .skip 8
.dw @L2C2968+Offset :: .skip 8
.dw @L2C2980+Offset :: .skip 8
.dw @L2C29A0+Offset :: .skip 8
.dw @L2C29C0+Offset :: .skip 8
.dw @L2C29E0+Offset :: .skip 8
.dw @L2C2A00+Offset :: .skip 8
.dw @L2C2A20+Offset :: .skip 8
.dw @L2C2A40+Offset :: .skip 8
.dw @L2C2A60+Offset :: .skip 8
.dw @L2C2A80+Offset :: .skip 8
.dw @L2C2AA0+Offset :: .skip 8
.dw @L2C2AB8+Offset :: .skip 8
.dw @L2C2AD0+Offset :: .skip 8
.dw @L2C2AF0+Offset :: .skip 8
.dw @L2C2B10+Offset :: .skip 8
.dw @L2C2B30+Offset :: .skip 8
.dw @L2C2B50+Offset :: .skip 8
.dw @L2C2B70+Offset :: .skip 8
.dw @L2C1F08+Offset :: .skip 8

// Ys 5 Gallery Pointers

.orga 0x23BC40

.dw @L2C1F10+Offset :: .skip 8
.dw @L2C2B88+Offset :: .skip 8
.dw @L2C2BA0+Offset :: .skip 8
.dw @L2C2BC0+Offset :: .skip 8
.dw @L2C2BD0+Offset :: .skip 8
.dw @L2C2BF0+Offset :: .skip 8
.dw @L2C2C10+Offset :: .skip 8
.dw @L2C2C30+Offset :: .skip 8
.dw @L2C2C50+Offset :: .skip 8
.dw @L2C2C70+Offset :: .skip 8
.dw @L2C2C88+Offset :: .skip 8
.dw @L2C2CA0+Offset :: .skip 8
.dw @L2C2CB8+Offset :: .skip 8
.dw @L2C2CD0+Offset :: .skip 8
.dw @L2C2CF0+Offset :: .skip 8
.dw @L2C2D10+Offset :: .skip 8
.dw @L2C2D30+Offset :: .skip 8
.dw @L2C2D40+Offset :: .skip 8
.dw @L2C2D60+Offset :: .skip 8
.dw @L2C2D80+Offset :: .skip 8
.dw @L2C2DA0+Offset :: .skip 8
.dw @L2C2DC0+Offset :: .skip 8
.dw @L2C2DE0+Offset :: .skip 8
.dw @L2C2E00+Offset :: .skip 8
.dw @L2C2E20+Offset :: .skip 8
.dw @L2C2E40+Offset :: .skip 8
.dw @L2C2E60+Offset :: .skip 8
.dw @L2C2E80+Offset :: .skip 8
.dw @L2C2EA0+Offset :: .skip 8
.dw @L2C2EC0+Offset :: .skip 8
.dw @L2C2EE0+Offset :: .skip 8
.dw @L2C2F00+Offset :: .skip 8
.dw @L2C2F20+Offset :: .skip 8
.dw @L2C2F40+Offset :: .skip 8

.dw @LGallery3+offset
.dw 0x02
.dw 0x00
.dw @L2C1F08+Offset


// Ys 3 Music Text

.orga 0x2C1C70

@L2C1F08: .str L2C1F08
@L2C1C70: .str L2C1C70
@L2C1C80: .str L2C1C80
@L2C1C98: .str L2C1C98
@L2C1CB0: .str L2C1CB0
@L2C1CD0: .str L2C1CD0
@L2C1CE0: .str L2C1CE0
@L2C1D00: .str L2C1D00
@L2C1D20: .str L2C1D20
@L2C1D40: .str L2C1D40
@L2C1D50: .str L2C1D50
@L2C1D70: .str L2C1D70
@L2C1D90: .str L2C1D90
@L2C1DA8: .str L2C1DA8
@L2C1DC0: .str L2C1DC0
@L2C1DE0: .str L2C1DE0
@L2C1E00: .str L2C1E00
@L2C1E20: .str L2C1E20
@L2C1E40: .str L2C1E40
@L2C1E58: .str L2C1E58
@L2C1E70: .str L2C1E70
@L2C1E88: .str L2C1E88
@L2C1EA0: .str L2C1EA0
@L2C1EB8: .str L2C1EB8
@L2C1ED0: .str L2C1ED0
@L2C1EF0: .str L2C1EF0

// Ys 3 Gallery Text

@L2C1F10: .str L2C1F10
@L2C1F20: .str L2C1F20
@L2C1F40: .str L2C1F40
@L2C1F60: .str L2C1F60
@L2C1F80: .str L2C1F80
@L2C1FA0: .str L2C1FA0
@L2C1FC0: .str L2C1FC0
@L2C1FE0: .str L2C1FE0
@L2C2000: .str L2C2000
@L2C2020: .str L2C2020
@L2C2040: .str L2C2040
@L2C2060: .str L2C2060
@L2C2080: .str L2C2080
@L2C20A0: .str L2C20A0
@L2C20C0: .str L2C20C0
@L2C20E0: .str L2C20E0
@L2C2100: .str L2C2100
@L2C2120: .str L2C2120
@L2C2148: .str L2C2148

// Ys 4 Music Text

@L2C2158: .str L2C2158
@L2C2170: .str L2C2170
@L2C2190: .str L2C2190
@L2C21A8: .str L2C21A8
@L2C21C0: .str L2C21C0
@L2C21E0: .str L2C21E0
@L2C21F8: .str L2C21F8
@L2C2210: .str L2C2210
@L2C2228: .str L2C2228
@L2C2240: .str L2C2240
@L2C2260: .str L2C2260
@L2C2280: .str L2C2280
@L2C2298: .str L2C2298
@L2C22A8: .str L2C22A8
@L2C22C0: .str L2C22C0
@L2C22E0: .str L2C22E0
@L2C2310: .str L2C2310
@L2C2328: .str L2C2328
@L2C2340: .str L2C2340
@L2C2358: .str L2C2358
@L2C2370: .str L2C2370
@L2C2390: .str L2C2390
@L2C23B0: .str L2C23B0
@L2C23D0: .str L2C23D0
@L2C23E8: .str L2C23E8
@L2C23F8: .str L2C23F8
@L2C2410: .str L2C2410
@L2C2430: .str L2C2430
@L2C2450: .str L2C2450
@L2C2470: .str L2C2470

// Ys 4 Gallery text

@L2C2488: .str L2C2488
@L2C24A0: .str L2C24A0
@L2C24C0: .str L2C24C0
@L2C24E0: .str L2C24E0
@L2C2500: .str L2C2500
@L2C2520: .str L2C2520
@L2C2540: .str L2C2540
@L2C2560: .str L2C2560
@L2C2580: .str L2C2580
@L2C25A0: .str L2C25A0
@L2C25C0: .str L2C25C0
@L2C25E0: .str L2C25E0
@L2C2610: .str L2C2610
@L2C2630: .str L2C2630
@L2C2650: .str L2C2650
@L2C2670: .str L2C2670
@L2C26A0: .str L2C26A0
@L2C26D0: .str L2C26D0
@L2C26F8: .str L2C26F8

// Ys 5 Music Text

@L2C2708: .str L2C2708
@L2C2718: .str L2C2718
@L2C2728: .str L2C2728
@L2C2740: .str L2C2740
@L2C2750: .str L2C2750
@L2C2768: .str L2C2768
@L2C2780: .str L2C2780
@L2C2798: .str L2C2798
@L2C27B0: .str L2C27B0
@L2C27D0: .str L2C27D0
@L2C27F0: .str L2C27F0
@L2C2810: .str L2C2810
@L2C2828: .str L2C2828
@L2C2840: .str L2C2840
@L2C2860: .str L2C2860
@L2C2880: .str L2C2880
@L2C2898: .str L2C2898
@L2C28B0: .str L2C28B0
@L2C28D0: .str L2C28D0
@L2C28F0: .str L2C28F0
@L2C2910: .str L2C2910
@L2C2930: .str L2C2930
@L2C2950: .str L2C2950
@L2C2968: .str L2C2968
@L2C2980: .str L2C2980
@L2C29A0: .str L2C29A0
@L2C29C0: .str L2C29C0
@L2C29E0: .str L2C29E0
@L2C2A00: .str L2C2A00
@L2C2A20: .str L2C2A20
@L2C2A40: .str L2C2A40
@L2C2A60: .str L2C2A60
@L2C2A80: .str L2C2A80
@L2C2AA0: .str L2C2AA0
@L2C2AB8: .str L2C2AB8
@L2C2AD0: .str L2C2AD0
@L2C2AF0: .str L2C2AF0
@L2C2B10: .str L2C2B10
@L2C2B30: .str L2C2B30
@L2C2B50: .str L2C2B50
@L2C2B70: .str L2C2B70

// Ys 5 Gallery Text

@L2C2B88: .str L2C2B88
@L2C2BA0: .str L2C2BA0
@L2C2BC0: .str L2C2BC0
@L2C2BD0: .str L2C2BD0
@L2C2BF0: .str L2C2BF0
@L2C2C10: .str L2C2C10
@L2C2C30: .str L2C2C30
@L2C2C50: .str L2C2C50
@L2C2C70: .str L2C2C70
@L2C2C88: .str L2C2C88
@L2C2CA0: .str L2C2CA0
@L2C2CB8: .str L2C2CB8
@L2C2CD0: .str L2C2CD0
@L2C2CF0: .str L2C2CF0
@L2C2D10: .str L2C2D10
@L2C2D30: .str L2C2D30
@L2C2D40: .str L2C2D40
@L2C2D60: .str L2C2D60
@L2C2D80: .str L2C2D80
@L2C2DA0: .str L2C2DA0
@L2C2DC0: .str L2C2DC0
@L2C2DE0: .str L2C2DE0
@L2C2E00: .str L2C2E00
@L2C2E20: .str L2C2E20
@L2C2E40: .str L2C2E40
@L2C2E60: .str L2C2E60
@L2C2E80: .str L2C2E80
@L2C2EA0: .str L2C2EA0
@L2C2EC0: .str L2C2EC0
@L2C2EE0: .str L2C2EE0
@L2C2F00: .str L2C2F00
@L2C2F20: .str L2C2F20
@L2C2F40: .str L2C2F40

// VNText Name Pointers

.orga 0x2298E0

.dw @L2638D8+Offset
.dw @L2638E0+Offset
.dw @L2638E8+Offset
.dw @L2638F0+Offset
.dw @L2638F8+Offset
.dw @L263908+Offset
.dw @L263910+Offset
.dw @L263920+Offset
.dw @L263928+Offset
.dw @L263938+Offset
.dw @L263940+Offset
.dw @L263950+Offset
.dw @L263958+Offset
.dw @L263968+Offset
.dw @L263978+Offset
.dw @L263988+Offset
.dw @L263998+Offset
.dw @L2639A8+Offset
.dw @L2639B8+Offset
.dw @L2639C0+Offset
.dw @L2639C8+Offset
.dw @L2639D8+Offset
.dw @L2639E0+Offset
.dw @L2639E8+Offset
.dw @L2639F0+Offset
.dw @L2639F8+Offset
.dw @L263A08+Offset
.dw @L263A10+Offset
.dw @L263A20+Offset
.dw @L263A30+Offset
.dw @L263A38+Offset
.dw @L263A40+Offset
.dw @L263A50+Offset
.dw @L263A60+Offset
.dw @L263A70+Offset
.dw @L263A78+Offset
.dw @L263A88+Offset
.dw @L263A98+Offset
.dw @L263AA8+Offset
.dw @L263AB8+Offset
.dw @L263AC8+Offset
.dw @L263AD8+Offset
.dw @L263AE8+Offset
.dw @L263AF8+Offset
.dw @L263B08+Offset
.dw @L263B18+Offset
.dw @L263B28+Offset
.dw @L263B38+Offset
.dw @L263B48+Offset
.dw @L263B50+Offset
.dw @L263B58+Offset
.dw @L263B60+Offset
.dw @L263B68+Offset
.dw @L263B78+Offset
.dw @L263B88+Offset
.dw @L263B98+Offset
.dw @L263BA8+Offset
.dw @L263BB8+Offset
.dw @L263BC0+Offset
.dw @L263BD0+Offset
.dw @L263BE0+Offset

.skip 12

.dw @L263BF8+Offset
.dw @L263C08+Offset
.dw @L263C10+Offset
.dw @L263C20+Offset
.dw @L263C30+Offset
.dw @L263C38+Offset
.dw @L263C40+Offset
.dw @L263B38+Offset

.skip 8

// Shop Block 1 Pointers

.dw @L263C50+Offset :: .skip 36
.dw @L263C70+Offset :: .skip 36
.dw @L263C90+Offset :: .skip 36
.dw @L263CC0+Offset :: .skip 36
.dw @L263CE0+Offset :: .skip 36
.dw @L263D00+Offset :: .skip 36
.dw @L263D20+Offset :: .skip 36
.dw @L263D40+Offset :: .skip 36
.dw @L263D70+Offset :: .skip 36
.dw @L263DA0+Offset :: .skip 36
.dw @L263DC0+Offset :: .skip 36

// Unknown Block 1 Pointers

.orga 0x22B808

.dw @L263DE0+Offset :: .skip 36
.dw @L2645F0+Offset :: .skip 36
.dw @L264620+Offset :: .skip 36
.dw @L264650+Offset :: .skip 36
.dw @L264670+Offset :: .skip 36
.dw @L2646A0+Offset :: .skip 36
.dw @L2646C0+Offset :: .skip 36

// Unknown Block 2 Pointers

.orga 0x22B308

.dw @L2644C0+Offset :: .skip 36
.dw @L2644F0+Offset :: .skip 36
.dw @L264510+Offset :: .skip 36
.dw @L264530+Offset :: .skip 36
.dw @L264550+Offset :: .skip 36
.dw @L264580+Offset :: .skip 36
.dw @L2645B0+Offset :: .skip 36
.dw @L2645D0+Offset :: .skip 36

// Locations Pointers
.orga 0x22CC00

.dw @L2648F0+Offset
.dw @L264900+Offset
.dw @L264910+Offset
.dw @L264920+Offset
.dw @L264930+Offset
.dw @L264940+Offset
.dw @L264948+Offset
.dw @L264958+Offset
.dw @L264968+Offset
.dw @L264978+Offset
.dw @L264990+Offset
.dw @L2649A8+Offset
.dw @L2649B8+Offset
.dw @L2649C8+Offset
.dw @L2649D8+Offset
.dw @L2649F0+Offset
.dw @L264A08+Offset
.dw @L264A18+Offset
.dw @L264A28+Offset
.dw @L264A38+Offset
.dw @L264A48+Offset
.dw @L264A58+Offset
.dw @L264A68+Offset
.dw @L264A70+Offset
.dw @L264A80+Offset
.dw @L264A90+Offset
.dw @L264AA0+Offset
.dw @L264AB0+Offset
.dw @L264AD0+Offset
.dw @L264AF0+Offset
.dw @L264B08+Offset
.dw @L264B18+Offset
.dw @L264B28+Offset
.dw @L264B38+Offset
.dw @L264B48+Offset
.dw @L2649B8+Offset
.dw @L2649B8+Offset
.dw @L2649D8+Offset
.dw @L264A38+Offset
.dw @L264A38+Offset
.dw @L264A38+Offset
.dw @L264A38+Offset
.dw @L264A38+Offset
.dw @L264A68+Offset
.dw @L264A68+Offset
.dw @L264A68+Offset
.dw @L264A68+Offset
.dw @L264A68+Offset
.dw @L264A68+Offset
.dw @L264AB0+Offset
.dw @L264AB0+Offset
.dw @L264AB0+Offset
.dw @L264AD0+Offset
.dw @L264AD0+Offset
.dw @L264AD0+Offset
.dw @L264AF0+Offset
.dw @L264AF0+Offset
.dw @L264AF0+Offset
.dw @L264AF0+Offset
.dw @L264AF0+Offset
.dw @L264AF0+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B48+Offset
.dw @L264B58+Offset
.dw @L264B60+Offset

.skip 20

// Credits Block 1 Pointers

.dw @L264B68+Offset :: .skip 20
.dw @L264B70+Offset :: .skip 20
.dw @L2638E0+Offset :: .skip 20
.dw @L264B90+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2638E8+Offset :: .skip 20
.dw @L264BA0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2638F0+Offset :: .skip 20
.dw @L264BB0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2638F8+Offset :: .skip 20
.dw @L264BC0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263908+Offset :: .skip 20
.dw @L264BD0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263920+Offset :: .skip 20
.dw @L264BE0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263950+Offset :: .skip 20
.dw @L264BF0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263958+Offset :: .skip 20
.dw @L264C00+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263968+Offset :: .skip 20
.dw @L264C10+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263910+Offset :: .skip 20
.dw @L264C20+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263938+Offset :: .skip 20
.dw @L264C30+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263998+Offset :: .skip 20
.dw @L264C40+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264C50+Offset :: .skip 20
.dw @L264C60+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263978+Offset :: .skip 20
.dw @L264C70+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264C80+Offset :: .skip 20
.dw @L264C90+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263940+Offset :: .skip 20
.dw @L264CA0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263928+Offset :: .skip 20
.dw @L264C70+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2639B8+Offset :: .skip 20
.dw @L264BC0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2639C8+Offset :: .skip 20
.dw @L264CB0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2639C0+Offset :: .skip 20
.dw @L264CC0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L263988+Offset :: .skip 20
.dw @L264CD0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264CE0+Offset :: .skip 20
.dw @L264D00+Offset :: .skip 20
.dw @L264D20+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264D30+Offset :: .skip 20
.dw @L264D40+Offset :: .skip 20
.dw @L264D50+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264D60+Offset :: .skip 20
.dw @L264D70+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264D80+Offset :: .skip 20
.dw @L264D90+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264DA0+Offset :: .skip 20
.dw @L264DA8+Offset :: .skip 20
.dw @L264DB8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264DC8+Offset :: .skip 20
.dw @L264DD0+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264DE0+Offset :: .skip 20
.dw @L264DF0+Offset :: .skip 20
.dw @L264E00+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264E10+Offset :: .skip 20
.dw @L264E20+Offset :: .skip 20
.dw @L264E30+Offset :: .skip 20
.dw @L264E40+Offset :: .skip 20
.dw @L264E48+Offset :: .skip 20
.dw @L264E58+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264E70+Offset :: .skip 20
.dw @L264E90+Offset :: .skip 20
.dw @L264EA8+Offset :: .skip 20
.dw @L264EB8+Offset :: .skip 20
.dw @L264EC8+Offset :: .skip 20
.dw @L264ED8+Offset :: .skip 20
.dw @L264EE8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264EF8+Offset :: .skip 20
.dw @L264F08+Offset :: .skip 20
.dw @L264F10+Offset :: .skip 20
.dw @L264F20+Offset :: .skip 20
.dw @L264F30+Offset :: .skip 20
.dw @L264F40+Offset :: .skip 20
.dw @L264F50+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264F68+Offset :: .skip 20
.dw @L264F78+Offset :: .skip 20
.dw @L264F88+Offset :: .skip 20
.dw @L264F98+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264FB0+Offset :: .skip 20
.dw @L264FC8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264FE0+Offset :: .skip 20
.dw @L265000+Offset :: .skip 20
.dw @L265020+Offset :: .skip 20
.dw @L265040+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L265070+Offset :: .skip 20
.dw @L265080+Offset :: .skip 20
.dw @L2650A0+Offset :: .skip 20
.dw @L2650B8+Offset :: .skip 20
.dw @L2650C8+Offset :: .skip 20
.dw @L2650D8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2650E8+Offset :: .skip 20
.dw @L2650F8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L265108+Offset :: .skip 20
.dw @L265118+Offset :: .skip 20
.dw @L265128+Offset :: .skip 20
.dw @L265138+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L265150+Offset :: .skip 20
.dw @L265168+Offset :: .skip 20
.dw @L265180+Offset :: .skip 20
.dw @L265198+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2651A8+Offset :: .skip 20
.dw @L2651B8+Offset :: .skip 20
.dw @L2651C8+Offset :: .skip 20
.dw @L2651D8+Offset :: .skip 20
.dw @L2651E8+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L2651F8+Offset :: .skip 20
.dw @L265210+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L265228+Offset :: .skip 20
.dw @L265230+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L265248+Offset :: .skip 20
.dw @L265250+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 20
.dw @L264B68+Offset :: .skip 8
.dw @L265268+Offset

.skip 4

// Credits Block 2 Pointers

.dw @L2638E0+Offset
.dw @L264B90+Offset :: .skip 8
.dw @L2638E8+Offset
.dw @L264BA0+Offset :: .skip 8
.dw @L2638F0+Offset
.dw @L264BB0+Offset :: .skip 8
.dw @L2638F8+Offset
.dw @L264BC0+Offset :: .skip 8
.dw @L263908+Offset
.dw @L264BD0+Offset :: .skip 8
.dw @L263920+Offset
.dw @L264BE0+Offset :: .skip 8
.dw @L263950+Offset
.dw @L264BF0+Offset :: .skip 8
.dw @L263958+Offset
.dw @L264C00+Offset :: .skip 8
.dw @L263968+Offset
.dw @L264C10+Offset :: .skip 8
.dw @L263910+Offset
.dw @L264C20+Offset :: .skip 8
.dw @L263938+Offset
.dw @L264C30+Offset :: .skip 8
.dw @L263998+Offset
.dw @L264C40+Offset :: .skip 8
.dw @L264C50+Offset
.dw @L264C60+Offset :: .skip 8
.dw @L263978+Offset
.dw @L264C70+Offset :: .skip 8
.dw @L264C80+Offset
.dw @L264C90+Offset :: .skip 8
.dw @L263940+Offset
.dw @L264CA0+Offset :: .skip 8
.dw @L263928+Offset
.dw @L264C70+Offset :: .skip 8
.dw @L2639B8+Offset
.dw @L264BC0+Offset :: .skip 8
.dw @L2639C8+Offset
.dw @L264CB0+Offset :: .skip 8
.dw @L2639C0+Offset
.dw @L264CC0+Offset :: .skip 8
.dw @L263988+Offset
.dw @L264CD0+Offset :: .skip 8

.skip 4

// Credits Block 3 Pointers

.dw @L265278+Offset :: .skip 4
.dw @L264D00+Offset
.dw @L264D20+Offset :: .skip 8
.dw @L264D30+Offset
.dw @L264D40+Offset
.dw @L264D50+Offset :: .skip 8
.dw @L264D60+Offset
.dw @L264D70+Offset :: .skip 8
.dw @L264D80+Offset
.dw @L264D90+Offset :: .skip 8
.dw @L264DA0+Offset
.dw @L264DA8+Offset
.dw @L264DB8+Offset :: .skip 8
.dw @L264DC8+Offset
.dw @L264DD0+Offset :: .skip 8
.dw @L264DE0+Offset
.dw @L264DF0+Offset
.dw @L264E00+Offset :: .skip 8
.dw @L264E10+Offset
.dw @L264E20+Offset
.dw @L264E30+Offset
.dw @L264E40+Offset
.dw @L264E48+Offset
.dw @L264E58+Offset :: .skip 8
.dw @L264E70+Offset
.dw @L264E90+Offset
.dw @L264EA8+Offset
.dw @L264EB8+Offset
.dw @L264EC8+Offset
.dw @L264ED8+Offset
.dw @L264EE8+Offset :: .skip 8
.dw @L264EF8+Offset
.dw @L264F08+Offset
.dw @L264F10+Offset
.dw @L264F20+Offset
.dw @L264F30+Offset
.dw @L264F40+Offset
.dw @L264F50+Offset :: .skip 8
.dw @L264F68+Offset
.dw @L264F78+Offset
.dw @L264F88+Offset
.dw @L264F98+Offset :: .skip 8
.dw @L264FB0+Offset
.dw @L264FC8+Offset :: .skip 8
.dw @L264FE0+Offset
.dw @L265000+Offset
.dw @L265020+Offset
.dw @L265040+Offset :: .skip 8
.dw @L265070+Offset
.dw @L265080+Offset
.dw @L2650A0+Offset
.dw @L2650B8+Offset
.dw @L2650C8+Offset
.dw @L2650D8+Offset :: .skip 8
.dw @L2650E8+Offset
.dw @L2650F8+Offset :: .skip 8
.dw @L265108+Offset
.dw @L265118+Offset
.dw @L265128+Offset
.dw @L265138+Offset :: .skip 8
.dw @L265150+Offset
.dw @L265168+Offset
.dw @L265180+Offset
.dw @L265198+Offset :: .skip 8
.dw @L2651A8+Offset
.dw @L2651B8+Offset
.dw @L2651C8+Offset
.dw @L2651D8+Offset
.dw @L2651E8+Offset :: .skip 8
.dw @L2651F8+Offset
.dw @L265210+Offset :: .skip 8
.dw @L265228+Offset
.dw @L265230+Offset :: .skip 8
.dw @L265248+Offset
.dw @L265250+Offset :: .skip 56
.dw @L265288+Offset :: .skip 12
.dw @L265290+Offset
.dw @L2652C0+Offset :: .skip 4
.dw @L2652E0+Offset
.dw @L265310+Offset :: .skip 4
.dw @L265340+Offset :: .skip 4
.dw @L265360+Offset :: .skip 4
.dw @L265380+Offset :: .skip 4
.dw @L2653A0+Offset
.dw @Lcredits1+Offset
.dw 0x00
.dw @L2653D0+Offset
.dw @L265400+Offset
.dw @L265420+Offset
.dw @L265450+Offset :: .skip 12
.dw @L265470+Offset :: .skip 56
.dw @L265288+Offset

.skip 16

// Item Names Pointers

.orga 0x22E56C

.dw @L265490+Offset :: .skip 152
.dw @L2654A8+Offset :: .skip 152
.dw @L2654B8+Offset :: .skip 152
.dw @L2654C8+Offset :: .skip 152
.dw @L2654E0+Offset :: .skip 152
.dw @L2654F8+Offset :: .skip 152
.dw @L265508+Offset :: .skip 152
.dw @L265518+Offset :: .skip 152
.dw @L265528+Offset :: .skip 152
.dw @L265538+Offset :: .skip 152
.dw @L265550+Offset :: .skip 152
.dw @L265570+Offset :: .skip 152
.dw @L265588+Offset :: .skip 152
.dw @L265598+Offset :: .skip 152
.dw @L2655A8+Offset :: .skip 152
.dw @L2655B8+Offset :: .skip 152
.dw @L2655C8+Offset :: .skip 152
.dw @L2655D8+Offset :: .skip 152
.dw @L2655F0+Offset :: .skip 152
.dw @L265608+Offset :: .skip 152
.dw @L265618+Offset :: .skip 152
.dw @L265630+Offset :: .skip 152
.dw @L265648+Offset :: .skip 152
.dw @L265658+Offset :: .skip 152
.dw @L265668+Offset :: .skip 152
.dw @L265678+Offset :: .skip 152
.dw @L265688+Offset :: .skip 152
.dw @L265698+Offset :: .skip 152
.dw @L2656B0+Offset :: .skip 152
.dw @L2656C8+Offset :: .skip 152
.dw @L2656D8+Offset :: .skip 152
.dw @L2656E0+Offset :: .skip 152
.dw @L2656F0+Offset :: .skip 152
.dw @L265700+Offset :: .skip 152
.dw @L265718+Offset :: .skip 152
.dw @L265728+Offset :: .skip 152
.dw @L265738+Offset :: .skip 152
.dw @L265748+Offset :: .skip 152
.dw @L265758+Offset :: .skip 152
.dw @L265768+Offset :: .skip 152
.dw @L265778+Offset :: .skip 152
.dw @L265788+Offset :: .skip 152
.dw @L265798+Offset :: .skip 152
.dw @L2657A0+Offset :: .skip 152
.dw @L2657B0+Offset :: .skip 152
.dw @L2657C0+Offset :: .skip 152
.dw @L2657D0+Offset :: .skip 152
.dw @L2657D8+Offset :: .skip 152
.dw @L2657E8+Offset :: .skip 152
.dw @L2657F8+Offset :: .skip 152
.dw @L265810+Offset :: .skip 152
.dw @L265830+Offset :: .skip 152
.dw @L265850+Offset :: .skip 152
.dw @L265870+Offset :: .skip 152
.dw @L265890+Offset :: .skip 152
.dw @L2658A8+Offset :: .skip 152
.dw @L2658B8+Offset :: .skip 152
.dw @L2658C8+Offset :: .skip 152
.dw @L2658E0+Offset :: .skip 152
.dw @L2658F8+Offset :: .skip 152
.dw @L265910+Offset :: .skip 152
.dw @L265928+Offset :: .skip 152
.dw @L2657F8+Offset :: .skip 152
.dw @L265810+Offset :: .skip 152
.dw @L265830+Offset :: .skip 152
.dw @L265850+Offset :: .skip 152
.dw @L265870+Offset :: .skip 152
.dw @L265890+Offset :: .skip 152
.dw @L2658A8+Offset :: .skip 152
.dw @L2658B8+Offset :: .skip 152
.dw @L2658C8+Offset :: .skip 152
.dw @L2658E0+Offset :: .skip 152
.dw @L2658F8+Offset :: .skip 152
.dw @L265910+Offset :: .skip 152
.dw @L265928+Offset :: .skip 152
.dw @L265938+Offset :: .skip 152
.dw @L265948+Offset :: .skip 152
.dw @L265958+Offset :: .skip 152
.dw @L265968+Offset :: .skip 152
.dw @L265978+Offset :: .skip 152
.dw @L265990+Offset :: .skip 152
.dw @L2659A8+Offset :: .skip 152
.dw @L2659B0+Offset :: .skip 152
.dw @L2659C0+Offset :: .skip 152
.dw @L2659D8+Offset :: .skip 152
.dw @L2659E8+Offset :: .skip 152

// Item Description Pointers

.orga 0x231A40

.dw @L265A00+Offset
.dw @L265A60+Offset
.dw @L265AA0+Offset
.dw @L265B00+Offset
.dw @L265B60+Offset
.dw @L265BC0+Offset
.dw @L265C20+Offset
.dw @L265C70+Offset
.dw @L265CD0+Offset
.dw @L265D30+Offset
.dw @L265D90+Offset
.dw @L265DF0+Offset
.dw @L265E50+Offset
.dw @L265EB0+Offset
.dw @L265F10+Offset
.dw @L265F60+Offset
.dw @L265FC0+Offset
.dw @L266020+Offset
.dw @L266070+Offset
.dw @L2660D0+Offset
.dw @L266130+Offset
.dw @L266190+Offset
.dw @L2661E0+Offset
.dw @L266230+Offset
.dw @L266290+Offset
.dw @L2662E0+Offset
.dw @L266320+Offset
.dw @L266360+Offset
.dw @L2663B0+Offset
.dw @L266400+Offset
.dw @L266450+Offset
.dw @L2664B0+Offset
.dw @L266500+Offset
.dw @L266550+Offset
.dw @L2665A0+Offset
.dw @L2665F0+Offset
.dw @L266640+Offset
.dw @L266680+Offset
.dw @L2666C0+Offset
.dw @L266720+Offset
.dw @L266780+Offset
.dw @L2667E0+Offset
.dw @L266830+Offset
.dw @L266890+Offset
.dw @L2668E0+Offset
.dw @L266920+Offset
.dw @L266980+Offset
.dw @L2669D0+Offset
.dw @L266A10+Offset
.dw @L266A60+Offset
.dw @L266AB0+Offset
.dw @L266B10+Offset
.dw @L266B70+Offset
.dw @L266BD0+Offset
.dw @L266C30+Offset
.dw @L266C80+Offset
.dw @L266CE0+Offset
.dw @L266D40+Offset
.dw @L266DA0+Offset
.dw @L266DF0+Offset
.dw @L266E50+Offset
.dw @L266EB0+Offset
.dw @L266A60+Offset
.dw @L266AB0+Offset
.dw @L266B10+Offset
.dw @L266B70+Offset
.dw @L266BD0+Offset
.dw @L266C30+Offset
.dw @L266C80+Offset
.dw @L266CE0+Offset
.dw @L266D40+Offset
.dw @L266DA0+Offset
.dw @L266DF0+Offset
.dw @L266E50+Offset
.dw @L266EB0+Offset
.dw @L266F10+Offset
.dw @L266F60+Offset
.dw @L266FD0+Offset
.dw @L267020+Offset
.dw @L267070+Offset
.dw @L2670D0+Offset
.dw @L267120+Offset
.dw @L267180+Offset
.dw @L2671D0+Offset
.dw @L267240+Offset
.dw @L267290+Offset


// VNText Name Text

.orga 0x2638D8

@L2638D8: .str L2638D8
@L2638E0: .str L2638E0
@L2638E8: .str L2638E8
@L2638F0: .str L2638F0
@L2638F8: .str L2638F8
@L263908: .str L263908
@L263910: .str L263910
@L263920: .str L263920
@L263928: .str L263928
@L263938: .str L263938
@L263940: .str L263940
@L263950: .str L263950
@L263958: .str L263958
@L263968: .str L263968
@L263978: .str L263978
@L263988: .str L263988
@L263998: .str L263998
@L2639A8: .str L2639A8
@L2639B8: .str L2639B8
@L2639C0: .str L2639C0
@L2639C8: .str L2639C8
@L2639D8: .str L2639D8
@L2639E0: .str L2639E0
@L2639E8: .str L2639E8
@L2639F0: .str L2639F0
@L2639F8: .str L2639F8
@L263A08: .str L263A08
@L263A10: .str L263A10
@L263A20: .str L263A20
@L263A30: .str L263A30
@L263A38: .str L263A38
@L263A40: .str L263A40
@L263A50: .str L263A50
@L263A60: .str L263A60
@L263A70: .str L263A70
@L263A78: .str L263A78
@L263A88: .str L263A88
@L263A98: .str L263A98
@L263AA8: .str L263AA8
@L263AB8: .str L263AB8
@L263AC8: .str L263AC8
@L263AD8: .str L263AD8
@L263AE8: .str L263AE8
@L263AF8: .str L263AF8
@L263B08: .str L263B08
@L263B18: .str L263B18
@L263B28: .str L263B28
@L263B38: .str L263B38
@L263B48: .str L263B48
@L263B50: .str L263B50
@L263B58: .str L263B58
@L263B60: .str L263B60
@L263B68: .str L263B68
@L263B78: .str L263B78
@L263B88: .str L263B88
@L263B98: .str L263B98
@L263BA8: .str L263BA8
@L263BB8: .str L263BB8
@L263BC0: .str L263BC0
@L263BD0: .str L263BD0
@L263BE0: .str L263BE0
@L263BF8: .str L263BF8
@L263C08: .str L263C08
@L263C10: .str L263C10
@L263C20: .str L263C20
@L263C30: .str L263C30
@L263C38: .str L263C38
@L263C40: .str L263C40

// Shop Block 1 Text

@L263C50: .str L263C50
@L263C70: .str L263C70
@L263C90: .str L263C90
@L263CC0: .str L263CC0
@L263CE0: .str L263CE0
@L263D00: .str L263D00
@L263D20: .str L263D20
@L263D40: .str L263D40
@L263D70: .str L263D70
@L263DA0: .str L263DA0
@L263DC0: .str L263DC0

// Shop Block 2 Text

@L263DE0: .str L263DE0


@L263E00: .str L263E00
@L263E20: .str L263E20
@L263E50: .str L263E50
@L263E80: .str L263E80
@L263EB0: .str L263EB0
@L263EE0: .str L263EE0

@L263F10: .str L263F10
@L263F30: .str L263F30

// Alchemy Text

@L263F60: .str L263F60
@L263FA0: .str L263FA0
@L263FC0: .str L263FC0
@L263FE0: .str L263FE0
@L264000: .str L264000
@L264030: .str L264030
@L264050: .str L264050
@L264080: .str L264080
@L2640A0: .str L2640A0
@L2640C0: .str L2640C0
@L264100: .str L264100
@L264130: .str L264130
@L264150: .str L264150
@L264170: .str L264170
@L264190: .str L264190
@L2641C0: .str L2641C0
@L2641E0: .str L2641E0
@L264200: .str L264200
@L264240: .str L264240
@L264260: .str L264260
@L264280: .str L264280
@L2642A0: .str L2642A0
@L2642D0: .str L2642D0
@L264300: .str L264300
@L264330: .str L264330
@L264360: .str L264360
@L264380: .str L264380
@L2643B0: .str L2643B0
@L2643E0: .str L2643E0
@L264410: .str L264410
@L264430: .str L264430
@L264460: .str L264460
@L264490: .str L264490

// Equipment Text

@L2644C0: .str L2644C0
@L2644F0: .str L2644F0
@L264510: .str L264510
@L264530: .str L264530
@L264550: .str L264550
@L264580: .str L264580
@L2645B0: .str L2645B0
@L2645D0: .str L2645D0


@L2645F0: .str L2645F0
@L264620: .str L264620
@L264650: .str L264650
@L264670: .str L264670
@L2646A0: .str L2646A0
@L2646C0: .str L2646C0


@L2646F0: .str L2646F0

// Menu Block 1 Text

@L264700: .str L264700
@L264730: .str L264730
@L264750: .str L264750
@L264770: .str L264770
@L2647A0: .str L2647A0
@L2647D0: .str L2647D0

@L264800: .str L264800
@L264820: .str L264820
@L264840: .str L264840
@L264860: .str L264860
@L264880: .str L264880
@L2648A0: .str L2648A0
@L2648D0: .str L2648D0

// Locations Text

@L2648F0: .str L2648F0
@L264900: .str L264900
@L264910: .str L264910
@L264920: .str L264920
@L264930: .str L264930
@L264940: .str L264940
@L264948: .str L264948
@L264958: .str L264958
@L264968: .str L264968
@L264978: .str L264978
@L264990: .str L264990
@L2649A8: .str L2649A8
@L2649B8: .str L2649B8
@L2649C8: .str L2649C8
@L2649D8: .str L2649D8
@L2649F0: .str L2649F0
@L264A08: .str L264A08
@L264A18: .str L264A18
@L264A28: .str L264A28
@L264A38: .str L264A38
@L264A48: .str L264A48
@L264A58: .str L264A58
@L264A68: .str L264A68
@L264A70: .str L264A70
@L264A80: .str L264A80
@L264A90: .str L264A90
@L264AA0: .str L264AA0
@L264AB0: .str L264AB0
@L264AD0: .str L264AD0
@L264AF0: .str L264AF0
@L264B08: .str L264B08
@L264B18: .str L264B18
@L264B28: .str L264B28
@L264B38: .str L264B38
@L264B48: .str L264B48
@L264B58: .str L264B58
@L264B60: .str L264B60

// Credits Text

@L264B68: .str L264B68

@L264B70: .str L264B70
@L264B90: .str L264B90
@L264BA0: .str L264BA0
@L264BB0: .str L264BB0
@L264BC0: .str L264BC0
@L264BD0: .str L264BD0
@L264BE0: .str L264BE0
@L264BF0: .str L264BF0
@L264C00: .str L264C00
@L264C10: .str L264C10
@L264C20: .str L264C20
@L264C30: .str L264C30
@L264C40: .str L264C40
@L264C50: .str L264C50
@L264C60: .str L264C60
@L264C70: .str L264C70
@L264C80: .str L264C80
@L264C90: .str L264C90
@L264CA0: .str L264CA0
@L264CB0: .str L264CB0
@L264CC0: .str L264CC0
@L264CD0: .str L264CD0
@L264CE0: .str L264CE0
@L264D00: .str L264D00
@L264D20: .str L264D20
@L264D30: .str L264D30
@L264D40: .str L264D40
@L264D50: .str L264D50
@L264D60: .str L264D60
@L264D70: .str L264D70
@L264D80: .str L264D80
@L264D90: .str L264D90
@L264DA0: .str L264DA0
@L264DA8: .str L264DA8
@L264DB8: .str L264DB8
@L264DC8: .str L264DC8
@L264DD0: .str L264DD0
@L264DE0: .str L264DE0
@L264DF0: .str L264DF0
@L264E00: .str L264E00
@L264E10: .str L264E10
@L264E20: .str L264E20
@L264E30: .str L264E30
@L264E40: .str L264E40
@L264E48: .str L264E48
@L264E58: .str L264E58
@L264E70: .str L264E70
@L264E90: .str L264E90
@L264EA8: .str L264EA8
@L264EB8: .str L264EB8
@L264EC8: .str L264EC8
@L264ED8: .str L264ED8
@L264EE8: .str L264EE8
@L264EF8: .str L264EF8
@L264F08: .str L264F08
@L264F10: .str L264F10
@L264F20: .str L264F20
@L264F30: .str L264F30
@L264F40: .str L264F40
@L264F50: .str L264F50
@L264F68: .str L264F68
@L264F78: .str L264F78
@L264F88: .str L264F88
@L264F98: .str L264F98
@L264FB0: .str L264FB0
@L264FC8: .str L264FC8
@L264FE0: .str L264FE0
@L265000: .str L265000
@L265020: .str L265020
@L265040: .str L265040
@L265070: .str L265070
@L265080: .str L265080
@L2650A0: .str L2650A0
@L2650B8: .str L2650B8
@L2650C8: .str L2650C8
@L2650D8: .str L2650D8
@L2650E8: .str L2650E8
@L2650F8: .str L2650F8
@L265108: .str L265108
@L265118: .str L265118
@L265128: .str L265128
@L265138: .str L265138
@L265150: .str L265150
@L265168: .str L265168
@L265180: .str L265180
@L265198: .str L265198
@L2651A8: .str L2651A8
@L2651B8: .str L2651B8
@L2651C8: .str L2651C8
@L2651D8: .str L2651D8
@L2651E8: .str L2651E8
@L2651F8: .str L2651F8
@L265210: .str L265210
@L265228: .str L265228
@L265230: .str L265230
@L265248: .str L265248
@L265250: .str L265250
@L265268: .str L265268
@L265278: .str L265278

// Ending Text
@L265288: .str L265288

@L265290: .str L265290
@L2652C0: .str L2652C0
@L2652E0: .str L2652E0
@L265310: .str L265310
@L265340: .str L265340
@L265360: .str L265360
@L265380: .str L265380
@L2653A0: .str L2653A0
@Lcredits1: .str Lcredits1
@L2653D0: .str L2653D0
@L265400: .str L265400
@L265420: .str L265420
@L265450: .str L265450
@L265470: .str L265470

// Item Names Text

@L265490: .str L265490
@L2654A8: .str L2654A8
@L2654B8: .str L2654B8
@L2654C8: .str L2654C8
@L2654E0: .str L2654E0
@L2654F8: .str L2654F8
@L265508: .str L265508
@L265518: .str L265518
@L265528: .str L265528
@L265538: .str L265538
@L265550: .str L265550
@L265570: .str L265570
@L265588: .str L265588
@L265598: .str L265598
@L2655A8: .str L2655A8
@L2655B8: .str L2655B8
@L2655C8: .str L2655C8
@L2655D8: .str L2655D8
@L2655F0: .str L2655F0
@L265608: .str L265608
@L265618: .str L265618
@L265630: .str L265630
@L265648: .str L265648
@L265658: .str L265658
@L265668: .str L265668
@L265678: .str L265678
@L265688: .str L265688
@L265698: .str L265698
@L2656B0: .str L2656B0
@L2656C8: .str L2656C8
@L2656D8: .str L2656D8
@L2656E0: .str L2656E0
@L2656F0: .str L2656F0
@L265700: .str L265700
@L265718: .str L265718
@L265728: .str L265728
@L265738: .str L265738
@L265748: .str L265748
@L265758: .str L265758
@L265768: .str L265768
@L265778: .str L265778
@L265788: .str L265788
@L265798: .str L265798
@L2657A0: .str L2657A0
@L2657B0: .str L2657B0
@L2657C0: .str L2657C0
@L2657D0: .str L2657D0
@L2657D8: .str L2657D8
@L2657E8: .str L2657E8
@L2657F8: .str L2657F8
@L265810: .str L265810
@L265830: .str L265830
@L265850: .str L265850
@L265870: .str L265870
@L265890: .str L265890
@L2658A8: .str L2658A8
@L2658B8: .str L2658B8
@L2658C8: .str L2658C8
@L2658E0: .str L2658E0
@L2658F8: .str L2658F8
@L265910: .str L265910
@L265928: .str L265928
@L265938: .str L265938
@L265948: .str L265948
@L265958: .str L265958
@L265968: .str L265968
@L265978: .str L265978
@L265990: .str L265990
@L2659A8: .str L2659A8
@L2659B0: .str L2659B0
@L2659C0: .str L2659C0
@L2659D8: .str L2659D8
@L2659E8: .str L2659E8

// Item Description Text

@L265A00: .str L265A00
@L265A60: .str L265A60
@L265AA0: .str L265AA0
@L265B00: .str L265B00
@L265B60: .str L265B60
@L265BC0: .str L265BC0
@L265C20: .str L265C20
@L265C70: .str L265C70
@L265CD0: .str L265CD0
@L265D30: .str L265D30
@L265D90: .str L265D90
@L265DF0: .str L265DF0
@L265E50: .str L265E50
@L265EB0: .str L265EB0
@L265F10: .str L265F10
@L265F60: .str L265F60
@L265FC0: .str L265FC0
@L266020: .str L266020
@L266070: .str L266070
@L2660D0: .str L2660D0
@L266130: .str L266130
@L266190: .str L266190
@L2661E0: .str L2661E0
@L266230: .str L266230
@L266290: .str L266290
@L2662E0: .str L2662E0
@L266320: .str L266320
@L266360: .str L266360
@L2663B0: .str L2663B0
@L266400: .str L266400
@L266450: .str L266450
@L2664B0: .str L2664B0
@L266500: .str L266500
@L266550: .str L266550
@L2665A0: .str L2665A0
@L2665F0: .str L2665F0
@L266640: .str L266640
@L266680: .str L266680
@L2666C0: .str L2666C0
@L266720: .str L266720
@L266780: .str L266780
@L2667E0: .str L2667E0
@L266830: .str L266830
@L266890: .str L266890
@L2668E0: .str L2668E0
@L266920: .str L266920
@L266980: .str L266980
@L2669D0: .str L2669D0
@L266A10: .str L266A10
@L266A60: .str L266A60
@L266AB0: .str L266AB0
@L266B10: .str L266B10
@L266B70: .str L266B70
@L266BD0: .str L266BD0
@L266C30: .str L266C30
@L266C80: .str L266C80
@L266CE0: .str L266CE0
@L266D40: .str L266D40
@L266DA0: .str L266DA0
@L266DF0: .str L266DF0
@L266E50: .str L266E50
@L266EB0: .str L266EB0
@L266F10: .str L266F10
@L266F60: .str L266F60
@L266FD0: .str L266FD0
@L267020: .str L267020
@L267070: .str L267070
@L2670D0: .str L2670D0
@L267120: .str L267120
@L267180: .str L267180
@L2671D0: .str L2671D0
@L267240: .str L267240
@L267290: .str L267290

//  Load Screen Text

.orga 0x25FBF0 :: @L25FBF0: .str L25FBF0
.orga 0x25FC30 :: @L25FC30: .str L25FC30
.orga 0x25FC60 :: @L25FC60: .str L25FC60
.orga 0x25FC90 :: @L25FC90: .str L25FC90
.orga 0x25FD30 :: @L25FD30: .str L25FD30
.orga 0x25FDD0 :: @L25FDD0: .str L25FDD0
.orga 0x25FE40 :: @L25FE40: .str L25FE40
.orga 0x25FE70 :: @L25FE70: .str L25FE70
.orga 0x25FEB0 :: @L25FEB0: .str L25FEB0
.orga 0x25FEE0 :: @L25FEE0: .str L25FEE0
.orga 0x25FF90 :: @L25FF90: .str L25FF90
.orga 0x260090 :: @L260090: .str L260090
.orga 0x2600D0 :: @L2600D0: .str L2600D0
.orga 0x260110 :: @L260110: .str L260110
.orga 0x2601B0 :: @L2601B0: .str L2601B0
.orga 0x260210 :: @L260210: .str L260210
.orga 0x260240 :: @L260240: .str L260240
.orga 0x2602F0 :: @L2602F0: .str L2602F0
.orga 0x260320 :: @L260320: .str L260320
.orga 0x2603C0 :: @L2603C0: .str L2603C0
.orga 0x2603F0 :: @L2603F0: .str L2603F0
.orga 0x260420 :: @L260420: .str L260420
.orga 0x260450 :: @L260450: .str L260450
.orga 0x2604D0 :: @L2604D0: .str L2604D0
.orga 0x260570 :: @L260570: .str L260570
.orga 0x2605A0 :: @L2605A0: .str L2605A0
.orga 0x2605D0 :: @L2605D0: .str L2605D0

.orga 0x260670 :: @L260670: .str L260670
.orga 0x260740 :: @L260740: .str L260740
.orga 0x260790 :: @L260790: .str L260790
.orga 0x2607C0 :: @L2607C0: .str L2607C0
.orga 0x2607F0 :: @L2607F0: .str L2607F0
.orga 0x260820 :: @L260820: .str L260820
.orga 0x2608C0 :: @L2608C0: .str L2608C0

.orga 0x260AD0 :: @L260AD0: .str L260AD0
.orga 0x260B00 :: @L260B00: .str L260B00
.orga 0x260B28 :: @L260B28: .str L260B28
.orga 0x260B40 :: @L260B40: .str L260B40
.orga 0x260B70 :: @L260B70: .str L260B70
.orga 0x260BB0 :: @L260BB0: .str L260BB0
.orga 0x260BE0 :: @L260BE0: .str L260BE0
.orga 0x260C20 :: @L260C20: .str L260C20

// Menu Block 2 Text

.orga 0x268B20 :: @L268B20: .str L268B20
.orga 0x268B50 :: @L268B50: .str L268B50
.orga 0x268B70 :: @L268B70: .str L268B70
.orga 0x268B90 :: @L268B90: .str L268B90
.orga 0x268BB0 :: @L268BB0: .str L268BB0
.orga 0x268BE0 :: @L268BE0: .str L268BE0
.orga 0x268C10 :: @L268C10: .str L268C10
.orga 0x268C40 :: @L268C40: .str L268C40
.orga 0x268C70 :: @L268C70: .str L268C70

// Menu Block 1 Pointers
.orga 0x22C708

.dw @L264800+Offset :: .skip 36
.dw @L264820+Offset :: .skip 36
.dw @L264840+Offset :: .skip 36
.dw @L264860+Offset :: .skip 36
.dw @L264880+Offset :: .skip 36
.dw @L264750+Offset :: .skip 36
.dw @L2648A0+Offset :: .skip 36
.dw @L2648D0+Offset :: .skip 36
.dw @L2647D0+Offset :: .skip 36

// Alchemy Pointers

.orga 0x22A408

.dw @L263F60+Offset :: .skip 36
.dw @L263FA0+Offset :: .skip 36
.dw @L263FC0+Offset :: .skip 36
.dw @L263FE0+Offset :: .skip 36
.dw @L264000+Offset :: .skip 36
.dw @L263FA0+Offset :: .skip 36
.dw @L264030+Offset :: .skip 36
.dw @L264050+Offset :: .skip 36
.dw @L264080+Offset :: .skip 36
.dw @L2640A0+Offset :: .skip 36

// Selling Pointers

.orga 0x229F08

.dw @L263DE0+Offset :: .skip 36
.dw @L263E00+Offset :: .skip 36
.dw @L263E20+Offset :: .skip 36
.dw @L263E50+Offset :: .skip 36
.dw @L263E80+Offset :: .skip 36
.dw @L263EB0+Offset :: .skip 36
.dw @L263EE0+Offset :: .skip 36
.dw @L263F10+Offset :: .skip 36
.dw @L263F30+Offset :: .skip 36

// Magic Stones Pointers 2

.orga 0x22AE08

.dw @L264190+Offset :: .skip 36
.dw @L2641C0+Offset :: .skip 36
.dw @L2641E0+Offset :: .skip 36
.dw @L264200+Offset :: .skip 36
.dw @L264240+Offset :: .skip 36
.dw @L264260+Offset :: .skip 36
.dw @L264200+Offset :: .skip 36
.dw @L264280+Offset :: .skip 36
.dw @L2642A0+Offset :: .skip 36
.dw @L2642D0+Offset :: .skip 36
.dw @L264300+Offset :: .skip 36
.dw @L264330+Offset :: .skip 36
.dw @L264360+Offset :: .skip 36
.dw @L264380+Offset :: .skip 36
.dw @L2643B0+Offset :: .skip 36
.dw @L2643E0+Offset :: .skip 36
.dw @L264410+Offset :: .skip 36
.dw @L264430+Offset :: .skip 36
.dw @L264460+Offset :: .skip 36
.dw @L264490+Offset :: .skip 36

// Menu Block Text

.orga 0x2634B0 :: @L2634B0: .str L2634B0
.orga 0x2634B8 :: @L2634B8: .str L2634B8
.orga 0x2634C0 :: @L2634C0: .str L2634C0
.orga 0x2634C8 :: @L2634C8: .str L2634C8
.orga 0x2634D0 :: @L2634D0: .str L2634D0
.orga 0x2634D8 :: @L2634D8: .str L2634D8
.orga 0x2634E0 :: @L2634E0: .str L2634E0
.orga 0x2634E8 :: @L2634E8: .str L2634E8
.orga 0x2634F0 :: @L2634F0: .str L2634F0
.orga 0x2634F8 :: @L2634F8: .str L2634F8
.orga 0x263500 :: @L263500: .str L263500
.orga 0x263508 :: @L263508: .str L263508
.orga 0x263510 :: @L263510: .str L263510
.orga 0x263518 :: @L263518: .str L263518
.orga 0x263520 :: @L263520: .str L263520
.orga 0x263528 :: @L263528: .str L263528
.orga 0x263530 :: @L263530: .str L263530
.orga 0x263538 :: @L263538: .str L263538
.orga 0x263540 :: @L263540: .str L263540
.orga 0x263548 :: @L263548: .str L263548
.orga 0x263550 :: @L263550: .str L263550
.orga 0x263558 :: @L263558: .str L263558
.orga 0x263560 :: @L263560: .str L263560
.orga 0x263568 :: @L263568: .str L263568
.orga 0x263570 :: @L263570: .str L263570
.orga 0x263578 :: @L263578: .str L263578
.orga 0x263580 :: @L263580: .str L263580
.orga 0x263588 :: @L263588: .str L263588
.orga 0x263590 :: @L263590: .str L263590
.orga 0x263598 :: @L263598: .str L263598
.orga 0x2635A8 :: @L2635A8: .str L2635A8
.orga 0x2635B8 :: @L2635B8: .str L2635B8
.orga 0x2635F8 :: @L2635F8: .str L2635F8
.orga 0x263608 :: @L263608: .str L263608
.orga 0x263610 :: @L263610: .str L263610
.orga 0x263658 :: @L263658: .str L263658
.orga 0x263660 :: @L263660: .str L263660
.orga 0x263668 :: @L263668: .str L263668
.orga 0x263670 :: @L263670: .str L263670
.orga 0x263678 :: @L263678: .str L263678
.orga 0x263680 :: @L263680: .str L263680
.orga 0x263688 :: @L263688: .str L263688
.orga 0x263690 :: @L263690: .str L263690
.orga 0x263698 :: @L263698: .str L263698
.orga 0x2636A0 :: @L2636A0: .str L2636A0
.orga 0x2636A8 :: @L2636A8: .str L2636A8
.orga 0x2636B0 :: @L2636B0: .str L2636B0
.orga 0x2636B8 :: @L2636B8: .str L2636B8
.orga 0x2636C0 :: @L2636C0: .str L2636C0
.orga 0x2636C8 :: @L2636C8: .str L2636C8
.orga 0x2636D0 :: @L2636D0: .str L2636D0
.orga 0x2636D8 :: @L2636D8: .str L2636D8
.orga 0x2636E0 :: @L2636E0: .str L2636E0
.orga 0x2636E8 :: @L2636E8: .str L2636E8
.orga 0x2636F0 :: @L2636F0: .str L2636F0
.orga 0x2636F8 :: @L2636F8: .str L2636F8
.orga 0x263700 :: @L263700: .str L263700
.orga 0x263708 :: @L263708: .str L263708
.orga 0x263710 :: @L263710: .str L263710
.orga 0x263718 :: @L263718: .str L263718
.orga 0x263720 :: @L263720: .str L263720
.orga 0x263728 :: @L263728: .str L263728
.orga 0x263730 :: @L263730: .str L263730
.orga 0x263738 :: @L263738: .str L263738
.orga 0x263740 :: @L263740: .str L263740
.orga 0x263748 :: @L263748: .str L263748
.orga 0x263778 :: @L263778: .str L263778
.orga 0x263790 :: @L263790: .str L263790
.orga 0x2637A0 :: @L2637A0: .str L2637A0
.orga 0x2637A8 :: @L2637A8: .str L2637A8
.orga 0x2637B8 :: @L2637B8: .str L2637B8
.orga 0x2637C8 :: @L2637C8: .str L2637C8
.orga 0x2637D8 :: @L2637D8: .str L2637D8
.orga 0x2637E8 :: @L2637E8: .str L2637E8
.orga 0x2637F8 :: @L2637F8: .str L2637F8
.orga 0x263808 :: @L263808: .str L263808
.orga 0x263820 :: @L263820: .str L263820
.orga 0x263830 :: @L263830: .str L263830
.orga 0x263840 :: @L263840: .str L263840
.orga 0x263850 :: @L263850: .str L263850
.orga 0x263860 :: @L263860: .str L263860
.orga 0x263878 :: @L263878: .str L263878
.orga 0x263888 :: @L263888: .str L263888
.orga 0x2638A0 :: @L2638A0: .str L2638A0
.orga 0x2638C0 :: @L2638C0: .str L2638C0

.orga 0x26DE98 :: @L26DE98: .str L26DE98
.orga 0x26DEA0 :: @L26DEA0: .str L26DEA0
.orga 0x26DEA8 :: @L26DEA8: .str L26DEA8
.orga 0x26DEB0 :: @L26DEB0: .str L26DEB0
.orga 0x26DEB8 :: @L26DEB8: .str L26DEB8
.orga 0x26DEC0 :: @L26DEC0: .str L26DEC0
.orga 0x26DEC8 :: @L26DEC8: .str L26DEC8
.orga 0x26DED0 :: @L26DED0: .str L26DED0
.orga 0x26DED8 :: @L26DED8: .str L26DED8
.orga 0x26DEE0 :: @L26DEE0: .str L26DEE0
.orga 0x26DEE8 :: @L26DEE8: .str L26DEE8
.orga 0x26DEF0 :: @L26DEF0: .str L26DEF0
.orga 0x26DEF8 :: @L26DEF8: .str L26DEF8
.orga 0x26DF00 :: @L26DF00: .str L26DF00
.orga 0x26DF08 :: @L26DF08: .str L26DF08
.orga 0x26DF10 :: @L26DF10: .str L26DF10
.orga 0x26DF18 :: @L26DF18: .str L26DF18
.orga 0x26DF20 :: @L26DF20: .str L26DF20
.orga 0x26DF28 :: @L26DF28: .str L26DF28
.orga 0x26DF30 :: @L26DF30: .str L26DF30
.orga 0x26DF38 :: @L26DF38: .str L26DF38
.orga 0x26DF40 :: @L26DF40: .str L26DF40
.orga 0x26DF48 :: @L26DF48: .str L26DF48
.orga 0x26DF50 :: @L26DF50: .str L26DF50
.orga 0x26DF58 :: @L26DF58: .str L26DF58
.orga 0x26DF60 :: @L26DF60: .str L26DF60
.orga 0x26DF68 :: @L26DF68: .str L26DF68
.orga 0x26DF70 :: @L26DF70: .str L26DF70
.orga 0x26DF80 :: @L26DF80: .str L26DF80
.orga 0x26DF88 :: @L26DF88: .str L26DF88
.orga 0x26DF90 :: @L26DF90: .str L26DF90
.orga 0x26DF98 :: @L26DF98: .str L26DF98
.orga 0x26DFB8 :: @L26DFB8: .str L26DFB8
.orga 0x26DFC8 :: @L26DFC8: .str L26DFC8
.orga 0x26DFD8 :: @L26DFD8: .str L26DFD8
.orga 0x26DFE8 :: @L26DFE8: .str L26DFE8
.orga 0x26E040 :: @L26E040: .str L26E040
.orga 0x26E048 :: @L26E048: .str L26E048
.orga 0x26E050 :: @L26E050: .str L26E050

.orga 0x2D2710 :: @L2D2710: .str L2D2710
.orga 0x2D2730 :: @L2D2730: .str L2D2730

// File Select Text Block

.orga 0x25F9C0 :: @L25F9C0: .str L25F9C0
.orga 0x25F9C8 :: @L25F9C8: .str L25F9C8
.orga 0x25F9D0 :: @L25F9D0: .str L25F9D0
.orga 0x25F9D8 :: @L25F9D8: .str L25F9D8
.orga 0x25F9E0 :: @L25F9E0: .str L25F9E0
.orga 0x25F9E8 :: @L25F9E8: .str L25F9E8
.orga 0x25F9F0 :: @L25F9F0: .str L25F9F0
.orga 0x25F9F8 :: @L25F9F8: .str L25F9F8
.orga 0x25FA00 :: @L25FA00: .str L25FA00
.orga 0x25FA08 :: @L25FA08: .str L25FA08
.orga 0x25FA10 :: @L25FA10: .str L25FA10
.orga 0x25FA18 :: @L25FA18: .str L25FA18
.orga 0x25FA20 :: @L25FA20: .str L25FA20
.orga 0x25FA28 :: @L25FA28: .str L25FA28
.orga 0x25FA30 :: @L25FA30: .str L25FA30
.orga 0x25FA38 :: @L25FA38: .str L25FA38
.orga 0x25FA40 :: @L25FA40: .str L25FA40
.orga 0x25FA48 :: @L25FA48: .str L25FA48
.orga 0x25FA50 :: @L25FA50: .str L25FA50
.orga 0x25FA58 :: @L25FA58: .str L25FA58
.orga 0x25FA60 :: @L25FA60: .str L25FA60
.orga 0x25FA68 :: @L25FA68: .str L25FA68
.orga 0x25FA70 :: @L25FA70: .str L25FA70
.orga 0x25FA78 :: @L25FA78: .str L25FA78
.orga 0x25FA80 :: @L25FA80: .str L25FA80
.orga 0x25FA88 :: @L25FA88: .str L25FA88
.orga 0x25FA90 :: @L25FA90: .str L25FA90
.orga 0x25FB40 :: @L25FB40: .str L25FB40
.orga 0x25FB48 :: @L25FB48: .str L25FB48
.orga 0x25FB50 :: @L25FB50: .str L25FB50
.orga 0x25FB60 :: @L25FB60: .str L25FB60
.orga 0x25FBA0 :: @L25FBA0: .str L25FBA0
.orga 0x25FBC0 :: @L25FBC0: .str L25FBC0

// Game Over Block Pointers

.orga 0x22C208

.dw @L264700+Offset :: .skip 36
.dw @L264730+Offset :: .skip 36
.dw @L264750+Offset :: .skip 36
.dw @L264770+Offset :: .skip 36
.dw @L2647A0+Offset :: .skip 36
.dw @L2647D0+Offset :: .skip 36

// Item Get Pointers

.orga 0x22BD08

.dw @L2646F0+Offset

// Stones Menu Pointers

.orga 0x22A908

.dw @L2640C0+Offset :: .skip 36
.dw @L264100+Offset :: .skip 36
.dw @L264130+Offset :: .skip 36
.dw @L264150+Offset :: .skip 36
.dw @L264170+Offset :: .skip 36