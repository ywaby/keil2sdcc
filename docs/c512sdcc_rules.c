// sfr B = 0xF0;
__sfr __at (0xF0) B;

// sbit CY    = PSW^7;      
__sbit __at (0xD0+7) CY;

// sbit WDT_IO=WDTCN^3;
__sbit __at (WDTCN+3) WDT_IO;

// sbit WDT_IO=P0^3;
__sbit __at (0xF0+3) WDT_IO;

// bit
// typedef bit BOOLEAN; 
typedef __bit BOOLEAN; 

// bit done_flag = 0;
__bit done_flag = 0;

// int xdata numtab;
__xdata int numtab; 
// same code data __idata far pdata

// int xdata * p;
__xdata unsigned int * __data p;

// at
// int xdata i _at_ 0x80ff
__xdata __at (0x80ff) int i;


// void timer0 (void) interrupt 1 using 1  {}
void timer0 (void) __interrupt (1) __using (1) {}

//int calc(char I,int b) reentrant  {}
int calc(char I,int b) __reentrant  {}

// #pragma asm
//   JMP   $  ; endless loop
//   ADDC  R1  ; endless loop
// #pragma endasm
__asm__ (
    ”JMP   $  ; endless loop\n”
    ”ADDC  R1  ; endless loop\n”
);

// small, compact, large  -> ""

