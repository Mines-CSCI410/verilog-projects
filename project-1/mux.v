module student_mux (input a, b, input sel, output out);
    /*
    * Develop your solution here.
    * You can use NAND (nand_gate) or any gate you've already created
    * (student_xyz).
    * Please don't use built-in versions of the gate you are modeling.
    */
endmodule

/*
 * Using your single-bit solution above, create a 16-bit version here.
 */
module student_mux16 (input [15:0] a, b, input sel, output [15:0] out);
    genvar i;
    generate
        for (i=0; i<16; i=i+1) begin
            // Use your student_mux gate here for each bit in the vectors
        end
    endgenerate
endmodule

/*
 * Using your 16-bit solution above, create a version that accepts four inputs.
 */
module student_4way16 (input [15:0] a, b, c, d, input [1:0] sel, output [15:0] out);
    // Your solution here
endmodule

/*
 * Using your four-way solution above, create a version that accepts eight inputs.
 */
module student_mux8way16 (input [15:0] a, b, c, d, e, f, g, h, input [2:0] sel, output [15:0] out);
    // Your solution here
endmodule
