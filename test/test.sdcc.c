    __sfr __at (0xF0) B;
    //累加器
//累加器
/**
* https://opensource.org/licenses/MIT
*
* @file FD612.h
* @brief FD612 drive
* @version 1.1
* @author ywaby@163.coom
* @date 2017-04-26
* @copyright Copyright (c) 2017 ywaby@163.com
*
* This software is released under the MIT License.
* https://opensource.org/licenses/MIT
*/
#ifndef _FD612_H_
#define _FD612_H_
#include "stc12c5a.h"

#ifdef __cplusplus
extern "C" {
#endif
    /*用户标志位0  ^*/
__sfr __at (0xF0) B;
    __sfr __at (0xF0) B;/*用户标志位0  ^*/
__sfr __at (0xF0) B;//B 寄存器
__sfr __at (0xD0) PSW;//程序状态字寄存器/*用户标志位0  ^*/
    __sbit __at (0xD0+7) CY;//进位标志位
  


      

/****************************************
 * a
 * -------
 * | |
 * f | | b
 * ---g---
 * e | | c
 * | |
 * ---d--- dp
 ****************************************/
 
/*------------ 系统管理特殊功能寄存器 -------------*/

    __sbit __at (0xD0+6) AC;/*用户标志位0  ^*///辅助进位标志位
    __sbit __at (0xD0+5) F0;/*用户标志位0  ^*/   //用户标志位0
__xdata __at (0x34) char nobu;/*用户标志位0  ^*/
  __sbit __at () F0=PSW^5;/*用户标志位0  ^*/
/** @addtogroup  UserChange  移植修改
  @{
*/
#define FD612_DEBUG_EN 0///<是否开启DEBUG功能 0为关闭
#define FD612_DECODE_TAB_EN 1///<是否开启FD612_decodeTab功能 0为关闭,关闭该功能可以省CODE
#define FD612_DISP_BUFF_EN 1///<是否开启FD612_dispBuff功能 0为关闭,关闭该功能可以省RAM

#define FD612_SW1 0x00000008///<FD612的按键定义
#define FD612_SW2 0x00000004///<FD612的按键定义 
#define FD612_SW3 0x00000002///<FD612的按键定义
#define FD612_SW4 0x00000001///<FD612的按键定义
#define FD612_SW_NONE 0X00///<FD612的无按键时的码值
typedef __bit BOOLEAN;///<定义布尔类型
typedef unsigned char INT8U;///<定义无符号8位数
typedef unsigned long INT32U;///<定义无符号32位数

#include "FD612.h"

void main(){
  INT8U brightness = 0;
  FD612_Init();
  FD612_DispStr(0, "abcd");
  while (1) {
    switch (FD612_RdKey())///<FD612的按键定义
    {
    case FD612_SW1: {///<FD612的按键定义
      FD612_dispBuff.state = (~FD612_dispBuff.state & 0x08) |
                                 (FD612_dispBuff.state & 0xf7);
      FD612_WAIT_SW_FREE;
      break;
      /** @addtogroup  UserChange  移植修改
  @{
*/
    }
    case FD612_SW2: {/** @addtogroup  UserChange  移植修改
      if (brightness == 0x07)/*用户标志位0  ^*/
        brightness = 0x00;
      else
        brightness++;/*用户标志位0  ^*/
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

