module student_dmux (input in, input sel, output a, b);
    /*
    * Develop your solution here.
    * You can use NAND (nand_gate) or any gate you've already created
    * (student_xyz).
    * Please don't use built-in versions of the gate you are modeling.
    */
endmodule

/*
 * Using your solution above, create a version that has four outputs.
 */
module student_dmux4way (input in, input [1:0] sel, output a, b, c, d);
    // Your solution here
endmodule

/*
 * Using your four-way solution above, create a version that has eight outputs.
 */
module student_dmux8way (input in, input [2:0] sel, output a, b, c, d, e, f, g, h);
    // Your solution here
endmodule
