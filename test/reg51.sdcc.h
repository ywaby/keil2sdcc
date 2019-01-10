/* After is STC additional SFR */

/* sfr  AUXR  = 0x8e; */
/* sfr  AUXR1 = 0xa2; */
/* sfr  IPH   = 0xb7; */

__sfr __at (0xe8) P4;
__sbit __at (0xe8+3) P43;
__sbit __at (0xe8+2) P42;
__sbit __at (0xe8+1) P41;
__sbit __at (0xe8+0) P40;

__sfr __at (0xc0) XICON;

__sfr __at (0xe1) WDT_CONTR;

__sfr __at (0xe2) ISP_DATA;
__sfr __at (0xe3) ISP_ADDRH;
__sfr __at (0xe4) ISP_ADDRL;
__sfr __at (0xe5) ISP_CMD;
__sfr __at (0xe6) ISP_TRIG;
__sfr __at (0xe7) ISP_CONTR;

/* Above is STC additional SFR */

/*--------------------------------------------------------------------------
REG51F.H

Header file for 8xC31/51, 80C51Fx, 80C51Rx+
Copyright (c) 1988-1999 Keil Elektronik GmbH and Keil Software, Inc.
All rights reserved.

Modification according to DataSheet from April 1999
 - SFR's AUXR and AUXR1 added for 80C51Rx+ derivatives
--------------------------------------------------------------------------*/

/*  BYTE Registers  */
__sfr __at (0x80) P0;
__sfr __at (0x90) P1;
__sfr __at (0xA0) P2;
__sfr __at (0xB0) P3;
__sfr __at (0xD0) PSW;
__sfr __at (0xE0) ACC;
__sfr __at (0xF0) B;
__sfr __at (0x81) SP;
__sfr __at (0x82) DPL;
__sfr __at (0x83) DPH;
__sfr __at (0x87) PCON;
__sfr __at (0x88) TCON;
__sfr __at (0x89) TMOD;
__sfr __at (0x8A) TL0;
__sfr __at (0x8B) TL1;
__sfr __at (0x8C) TH0;
__sfr __at (0x8D) TH1;
__sfr __at (0xA8) IE;
__sfr __at (0xB8) IP;
__sfr __at (0x98) SCON;
__sfr __at (0x99) SBUF;

/*  80C51Fx/Rx Extensions  */
__sfr __at (0x8E) AUXR;
__sfr __at (0xA2) AUXR1;
__sfr __at (0xA9) SADDR;
__sfr __at (0xB7) IPH;
__sfr __at (0xB9) SADEN;
__sfr __at (0xC8) T2CON;
__sfr __at (0xC9) T2MOD;
__sfr __at (0xCA) RCAP2L;
__sfr __at (0xCB) RCAP2H;
__sfr __at (0xCC) TL2;
__sfr __at (0xCD) TH2;

/* PCA SFR
sfr CCON   = 0xD8;
sfr CMOD   = 0xD9;
sfr CCAPM0 = 0xDA;
sfr CCAPM1 = 0xDB;
sfr CCAPM2 = 0xDC;
sfr CCAPM3 = 0xDD;
sfr CCAPM4 = 0xDE;
sfr CL     = 0xE9;
sfr CCAP0L = 0xEA;
sfr CCAP1L = 0xEB;
sfr CCAP2L = 0xEC;
sfr CCAP3L = 0xED;
sfr CCAP4L = 0xEE;
sfr CH     = 0xF9;
sfr CCAP0H = 0xFA;
sfr CCAP1H = 0xFB;
sfr CCAP2H = 0xFC;
sfr CCAP3H = 0xFD;
sfr CCAP4H = 0xFE;
*/

/*  BIT Registers  */
/*  PSW   */
__sbit __at (0xD0+7) CY;
__sbit __at (0xD0+6) AC;
__sbit __at (0xD0+5) F0;
__sbit __at (0xD0+4) RS1;
__sbit __at (0xD0+3) RS0;
__sbit __at (0xD0+2) OV;
__sbit __at (0xD0+0) P;

/*  TCON  */
__sbit __at (0x88+7) TF1;
__sbit __at (0x88+6) TR1;
__sbit __at (0x88+5) TF0;
__sbit __at (0x88+4) TR0;
__sbit __at (0x88+3) IE1;
__sbit __at (0x88+2) IT1;
__sbit __at (0x88+1) IE0;
__sbit __at (0x88+0) IT0;

/*  IE   */
__sbit __at (0xA8+7) EA;
__sbit __at (0xA8+6) EC;
__sbit __at (0xA8+5) ET2;
__sbit __at (0xA8+4) ES;
__sbit __at (0xA8+3) ET1;
__sbit __at (0xA8+2) EX1;
__sbit __at (0xA8+1) ET0;
__sbit __at (0xA8+0) EX0;

/*  IP   */ 
/*  sbit PPC  = IP^6;*/
__sbit __at (0xB8+5) PT2;
__sbit __at (0xB8+4) PS;
__sbit __at (0xB8+3) PT1;
__sbit __at (0xB8+2) PX1;
__sbit __at (0xB8+1) PT0;
__sbit __at (0xB8+0) PX0;

/*  P3  */
__sbit __at (0xB0+7) RD;
__sbit __at (0xB0+6) WR;
__sbit __at (0xB0+5) T1;
__sbit __at (0xB0+4) T0;
__sbit __at (0xB0+3) INT1;
__sbit __at (0xB0+2) INT0;
__sbit __at (0xB0+1) TXD;
__sbit __at (0xB0+0) RXD;

/*  SCON  */
__sbit __at (0x98+7) SM0;// alternatively "FE"
__sbit __at (0x98+7) FE;
__sbit __at (0x98+6) SM1;
__sbit __at (0x98+5) SM2;
__sbit __at (0x98+4) REN;
__sbit __at (0x98+3) TB8;
__sbit __at (0x98+2) RB8;
__sbit __at (0x98+1) TI;
__sbit __at (0x98+0) RI;
             
/*  P1  */
/* PCA
sbit CEX4 = P1^7;
sbit CEX3 = P1^6;
sbit CEX2 = P1^5;
sbit CEX1 = P1^4;
sbit CEX0 = P1^3;
sbit ECI  = P1^2;
*/

__sbit __at (0x90+1) T2EX;
__sbit __at (0x90+0) T2;

/*  T2CON  */
__sbit __at (0xC8+7) TF2;
__sbit __at (0xC8+6) EXF2;
__sbit __at (0xC8+5) RCLK;
__sbit __at (0xC8+4) TCLK;
__sbit __at (0xC8+3) EXEN2;
__sbit __at (0xC8+2) TR2;
__sbit __at (0xC8+1) C_T2;
__sbit __at (0xC8+0) CP_RL2;

/*  CCON  */
/*  PCA
sbit CF    = CCON^7;
sbit CR    = CCON^6;

sbit CCF4  = CCON^4;
sbit CCF3  = CCON^3;
sbit CCF2  = CCON^2;
sbit CCF1  = CCON^1;
sbit CCF0  = CCON^0;
*/

