module student_computer (
    input [(32768*16)-1:0] program, // equivalent to ROM
    input [((2**15)*16)-1:0] memory, // what to load into RAM
    input reload, // reload RAM from memory (some tests need to manipulate RAM)
    input reset, // reset PC
    output [14:0] pc,
    output [15:0] ARegister, DRegister,
    output [((2**15)*16)-1:0] mem_contents // used so test scripts can see what's going on
);
endmodule
