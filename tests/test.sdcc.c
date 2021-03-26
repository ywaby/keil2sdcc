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
__sfr __at (0xF0) B;
#include "reg51.h"

#ifdef __cplusplus
extern "C"
{
#endif
  /*comment ^*/
  __sfr __at (0xF0) B;
  __sfr __at (0xD0) PSW;//comment/*comment ^*/
  __sbit __at (0xD0+7) CY;//comment

  __sbit __at (P0+3) WDT_IO;
  __sbit __at (WDTCN+3) WDT_IO;

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
  __sbit __at (0xD0+5) F0;/*comment  ^*/ //comment
  typedef __bit BOOLEAN;///<comment
  int __xdata *p;
  extern int __xdata __at (0x80ff) int i;
  void main()
  {
#pragma asm
    JMP $;
    endless loop
#pragma endasm
  }

  void timer0(void) interrupt 1 __using (1) {}
  int calc(char I, int b) __reentrant {}
