// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(KBDLOOP)
        @R2
        M = 0
        @KBD
        D = M
        @BLACKLOOP
        D;JGT
        @KBD
        D = M
        @WHITELOOP
        D;JEQ
        @KBDLOOP
        0;JMP

(BLACKLOOP)
        // Get current counter
        @R2
        D = M
        
        // Blacken register
        @SCREEN
        A = A + D
        M = -1
        
        // Increment register counter
        @R2
        M = M + 1
        D = M

        @SCREEN
        D = A - D
        @8192
        D = D - A

        @BLACKLOOP
        D;JGT

        // Exit BLACKLOOP
        @KBDLOOP
        0;JMP

(WHITELOOP)
        // Get current counter
        @R2
        D = M
        
        // Whiten register
        @SCREEN
        A = A + D
        M = 0
        
        // Increment register counter
        @R2
        M = M + 1
        D = M

        @SCREEN
        D = A - D
        @8192
        D = D - A

        @WHITELOOP
        D;JGT

        // Exit WHITELOOP
        @KBDLOOP
        0;JMP
        