module xor_test;
  reg a, b;
  wire out;

  student_xor dut (.a(a), .b(b), .out(out));

  initial begin
    $display("| a | b |out|");

    a = 0;
    b = 0;
    #1 $display("| %d | %d | %d |", a, b, out);

    a = 0;
    b = 1;
    #2 $display("| %d | %d | %d |", a, b, out);

    a = 1;
    b = 0;
    #3 $display("| %d | %d | %d |", a, b, out);

    a = 1;
    b = 1;
    #4 $display("| %d | %d | %d |", a, b, out);
    $finish;
  end
endmodule
