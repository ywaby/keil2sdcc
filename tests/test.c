//commet
//// conment
///// conment
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
sfr B = 0xF0;
#include "reg51.h"

#ifdef __cplusplus
extern "C"
{
#endif
  /*comment ^*/
  sfr B = 0xF0;
  sfr PSW = 0xD0;    //comment	/*comment ^*/
  sbit CY = PSW^7; //comment

  sbit WDT_IO = P0^3;
  sbit WDT_IO = WDTCN^3;

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
  sbit F0 = PSW^5; /*comment  ^*/ //comment
  typedef bit BOOLEAN;        ///<comment
  int xdata *p;
  extern int xdata i _at_ 0x80ff;
  void main()
  {
#pragma asm
    JMP $;
    endless loop
#pragma endasm
  }

  void timer0(void) interrupt 1 using 1 {}
  int calc(char I, int b) reentrant {}