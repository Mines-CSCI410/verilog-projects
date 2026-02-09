// The intent is for you to use 16 bits to form a register, but when we
// get to the 16k ram there will be so many components to link that it
// will timeout the autograder, so you can use a 16-bit dff instead to fix
// this.
// Just understand that this component is supposed to be 16 bits.
//
// A 16 bit dff can be instantiated using the parameter N. Read the section of
// the verilog primer for details on parameterization.

module student_register (input [15:0] in, input load, output [15:0] out);
endmodule
