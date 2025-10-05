module half_adder_test;
  reg a, b;
  wire sum, car;

  student_half_adder dut (.a(a), .b(b), .sum(sum), .car(car));

  initial begin
    $display("|a|b|sum|car|");

    a = 0;
    b = 0;
    #1 $display("|%b|%b|%b|%b|", a, b, sum, car);

    a = 0;
    b = 1;
    #2 $display("|%b|%b|%b|%b|", a, b, sum, car);

    a = 1;
    b = 0;
    #3 $display("|%b|%b|%b|%b|", a, b, sum, car);

    a = 1;
    b = 1;
    #4 $display("|%b|%b|%b|%b|", a, b, sum, car);

    $finish;
  end
endmodule
