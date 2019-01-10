    sfr B = 0xF0; 
	//commet
//commet
/**
* https://opensource.org/licenses/MIT
*
* @file     FD612.h
* @brief     FD612 drive
* @version     1.1
* @author      ywabygl@gmail.com
* @date     2017-04-26
* @copyright Copyright (c) 2017 ywabygl@gmail.com
*
* This software is released under the MIT License.
* https://opensource.org/licenses/MIT
*/
#ifndef _FD612_H_
#define	_FD612_H_
#include "reg52.h" 

#ifdef __cplusplus
extern "C" {
#endif
	/*comment ^*/
sfr B = 0xF0; 
    sfr B = 0xF0; 	/*comment ^*/
sfr B = 0xF0; 		
sfr PSW    = 0xD0;          	//comment	/*comment ^*/
	sbit CY    = PSW^7;      	//comment
  
sfr P0 = 0xF0; 
sbit WDT_IO=P0^3;
sbit WDT_IO=WDTCN^3;
      

/****************************************
 *            a
 *         -------
 *        |       |
 *      f |       | b
 *         ---g---
 *      e |       | c
 *        |       |
 *         ---d---   dp
 ****************************************/
 
/*------------ comment -------------*/

	sbit AC    = PSW^6;       		/*comment  ^*///comment
	sbit F0    = PSW^5;       	/*comment  ^*/	//comment
xdata char x_var _at_ 0x34; pdata char p_var _at_ 0x34;	/*multi statements test  ^*/
  sbit F0=PSW^5;       	/*comment  ^*/
/** @addtogroup  UserChange  comment
  @{
*/
#define FD612_DEBUG_EN          0   ///<comment
#define	FD612_DECODE_TAB_EN     1   ///<comment
#define	FD612_DISP_BUFF_EN      1   ///<comment

#define FD612_SW1  	0x00000008  ///<comment
#define FD612_SW2  	0x00000004  ///<comment 
#define FD612_SW3  	0x00000002  ///<comment
#define FD612_SW4  	0x00000001  ///<comment
#define FD612_SW_NONE 0X00    ///<comment
typedef bit BOOLEAN;          ///<comment
typedef unsigned char INT8U;  ///<comment
typedef unsigned long INT32U; ///<comment

#include "FD612.h"

void main(){
  INT8U brightness = 0;
  FD612_Init();
  FD612_DispStr(0, "abcd");
  while (1) {
    switch (FD612_RdKey())  ///<comment
    {
    case FD612_SW1: { ///<comment
      FD612_dispBuff.state = (~FD612_dispBuff.state & 0x08) |
                                 (FD612_dispBuff.state & 0xf7);
      FD612_WAIT_SW_FREE;
      break;
      /** @addtogroup  UserChange  comment
  @{
*/
    }
    case FD612_SW2: {   // @addtogroup  UserChange  comment
      if (brightness == 0x07) 
        brightness = 0x00;
      else
        brightness++  
      FD612_dispBuff.state = FD612_dispBuff.state & 0xf8 | brightness;
      FD612_WAIT_SW_FREE;
      break;
    }
    default:
      break;
    }
    FD612_Update();
  }
}

