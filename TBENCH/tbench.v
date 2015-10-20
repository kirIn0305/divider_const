`timescale 10ps/1ps

module tbench;

    `include "TBENCH/clk_common.h"
    `include "TBENCH/instance_0.h"
    `include "TBENCH/task_divider.h"

    initial begin
        $dumpfile("./test.vcd");
        $dumpvars(0,divider_10_11);

        CLK <= 0;
        @(posedge CLK) #DELAY;
            set_divider(10'h10);
        @(posedge CLK) #DELAY;
            set_divider(10'd22);
        @(posedge CLK) #DELAY;
            set_divider(10'd44);
        @(posedge CLK) #DELAY;
            set_divider(10'd88);
        @(posedge CLK) #DELAY;
            set_divider(10'd95);
        /* @(posedge CLK); */
        #(1000 * CYCLE)    $finish();
    end

endmodule
