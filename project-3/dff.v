// Licensed under CC-BY-SA from Icarus Verilog Wiki
module dff(input in, input clock, input reset, output reg out);
    // On clock edge, check for reset and latch data
   always @(posedge clock or negedge reset) begin
       if (!reset)
           out <= 0;    // Reset the output to 0
       else
           out <= in;   // Latch the input data
   end
endmodule
