// Read the textbook on this one. Especially chapter 4.
//
// One particularly sticky bit is the 'a' bit for C-instructions indicates the
// source is the inM not ARegister, despite the letter seeming to indicate the
// opposite.

module student_cpu (
    input signed [15:0] inM,
    input [15:0] instruction,
    input reset,
    output signed [15:0] outM,
    output writeM,
    output [14:0] address, pc,
    output signed [15:0] ARegister, DRegister // used so test scripts can see what's going on
);
endmodule
