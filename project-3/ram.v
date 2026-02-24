// Read the section of the Verilog Primer (linked to on the Canvas page) about
// Muxlib. It will be helpful, though you can also use your multi-way
// multiplexers from project 1.

// If you use your student ram implementations for each of these your solution
// will probably time out. Instead, use the `fast_ram` parameterized module
// defined in the tests directory in place of your previous ram gate.
//
// For instance, in student_ram64, instead of creating 8 instances of
// student_ram8, create 8 instances of fast_ram #(8).

module student_ram8 (input [15:0] in, input load, input [2:0] address, output [15:0] out);
endmodule

module student_ram64 (input [15:0] in, input load, input [5:0] address, output [15:0] out);
endmodule

module student_ram512 (input [15:0] in, input load, input [8:0] address, output [15:0] out);
endmodule

module student_ram4k (input [15:0] in, input load, input [11:0] address, output [15:0] out);
endmodule

module student_ram16k (input [15:0] in, input load, input [13:0] address, output [15:0] out);
endmodule
