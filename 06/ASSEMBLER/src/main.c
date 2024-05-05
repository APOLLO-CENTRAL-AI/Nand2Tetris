#include <stdio.h>

enum dest{
    NIL    = 0b000,
    M       = 0b001,
    D       = 0b010,
    DM      = 0b011,
    A       = 0b100,
    AM      = 0b101,
    AD      = 0b110,
    ADM     = 0b111
};

enum comp{
    // VAR_N         --> negated, i.e. !Var
    ZERO           = 0b101010,
    ONE            = 0b111111,
    D              = 0b001100,
    A              = 0b110000,
    D_N            = 0b001101,
    A_N            = 0b110011,
    MINUS_D        = 0b001111,
    MINUS_A        = 0b110011,
    D_PLUS_1       = 0b011111,
    A_PLUS_1       = 0b110111,
    D_MINUS_1      = 0b001110,
    A_MINUS_1      = 0b110010,
    D_PLUS_A       = 0b000010,
    D_MINUS_A      = 0b010011,
    A_MINUS_D      = 0b000111,
    D_AND_A        = 0b000000,
    D_OR_A         = 0b010101,
    M              = 0b110000,
    M_N            = 0b110001,
    M_PLUS_1       = 0b110111,
    M_MINUS_1      = 0b110010,
    D_PLUS_M       = 0b000010,
    D_MINUS_M      = 0b010011,
    M_MINUS_D      = 0b000111,
    D_AND_M        = 0b000000,
    D_OR_M         = 0b010101
};

enum jump{
    NIL     = 0b000,
    JGT     = 0b001,
    JEQ     = 0b010,
    JGE     = 0b011,
    JLT     = 0b100,
    JNE     = 0b101,
    JLE     = 0b110,
    JMP     = 0b111
};

int main(){
    printf("Hello. Test\n");
    return 0;
}

