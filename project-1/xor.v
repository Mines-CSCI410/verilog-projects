module student_xor (input a, b, output out);
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
module student_xor16 (input [15:0] a, b, output [15:0] out);
    genvar i;
    generate
        for (i=0; i<16; i=i+1) begin
            // Use your student_xor gate here for each bit in the vectors
        end
    endgenerate
endmodule
