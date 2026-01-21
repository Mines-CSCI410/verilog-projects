module student_or (input a, b, output out);
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
module student_or16 (input [15:0] a, b, output [15:0] out);
    genvar i;
    generate
        for (i=0; i<16; i=i+1) begin
            // Use your student_or gate here for each bit in the vectors
        end
    endgenerate
endmodule

/*
 * Using your single-bit solution above, create gate that uses a vector of
 * booleans as an input.
 * If any of the bits of `in` are `1`, the output should be `1`.
 * 
 * There are several ways of approaching this, but I recommend using a for
 * loop in some way to reduce repeated code.
 */
module student_or8way (input [7:0] in, output out);
    genvar i;
    generate
        for (i=0; i<7; i=i+1) begin
            // Use your student_or gate here
            // This isn't the same as our 16-bit versions, this is 8-WAY.
        end
    endgenerate
endmodule
