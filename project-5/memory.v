module student_memory #(parameter A = 15) (
  input [((2**A)*16)-1:0] data, // initial value to load into RAM
  input reload, // reload RAM from memory (some tests need to manipulate RAM)
  input [15:0] in,
  input load,
  input [A-1:0] address,
  output [15:0] out,
  output reg [((2**A)* 16)-1:0] mem_contents // used as an output so test scripts can see what's going on
);
endmodule
