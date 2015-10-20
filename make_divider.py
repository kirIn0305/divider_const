# -*- coding: utf-8 -*
import sys
from math import modf

class divider_const:

    def __init__(self, dividend_width, divisor):
        print("divider_const __init__")
        print("dividend_width : {0}".format(dividend_width))
        print("divisor : {0}".format(divisor))
        self.fname = "./HDL/divider_{0}_{1}.v".format(dividend_width, divisor)
        self.dividend_width = dividend_width
        self.divisor = divisor
        self.multiplier = 1.0 / divisor
        self.first_one_width = 0

    def calc_bin(self):
        print("     calc_bin start ...")
        self.reverse_binary = ""

        while True:
            self.multiplier *= 2.0
            if self.multiplier >= 1:
                self.reverse_binary += "1"
                self.first_one_width = len(self.reverse_binary)
                print("         first 1 bit found! : {0}".format(self.reverse_binary))
                decimal, integer = modf(self.multiplier)
                self.multiplier = decimal
                break
            else:
                self.reverse_binary += "0"

        for num in range(self.dividend_width):
            self.multiplier *= 2
            if self.multiplier >= 1:
                self.reverse_binary += "1"
            else:
                self.reverse_binary += "0"

            print("         update... : {0}".format(self.reverse_binary))
            decimal, integer = modf(self.multiplier)
            self.multiplier = decimal
        bin_LSBadd = int(self.reverse_binary, 2) + 1

        self.new_divisor = format(bin_LSBadd, 'b').rjust(int(self.first_one_width + self.dividend_width), '0')
        print("         new_divisor bit width : {0}".format(len(self.new_divisor)))
        print("         new_divisor           : {0}".format(self.new_divisor))

    def create_divider_hdl(self):
        try:
            wf = open(self.fname, 'w')
        except IOError:
            print("Usage : python {0}".format(sys.argv[0]))

        divider_hdl = """/*================================================================================
| Project name
|---------------------------------------------------------------------------------
| Block name  : divider_{0}_{1}
| Version     : 0.0.0
| Description : 
|     - const unsigned Integer value divider (if you want use signed, you should calculate abs)
|     - i1 / i2 = o1  (i1 = Integer value, i2 = const Integer value)
|     - convert calculation method from divider to multiplier
|     - reference LSI/FPGAの回路アーキテクチャ設計法 P289
|---------------------------------------------------------------------------------
| Created by kirIn : author's email address
\===============================================================================*/

module divider_{0}_{1}(i1, o1);

//================================================================================
// Constants
//================================================================================
    parameter  BWI1 = {0};
    parameter  BWI2 = {2};
    parameter  BWO1 = {0};
    parameter  CONST_MULTI = 'b{3};

//================================================================================
// Declare Input and Output Pins
//================================================================================
    input [BWI1-1:0] i1;
    output [BWO1-1:0] o1;

//================================================================================
// Declare Wires and Regs
//================================================================================
    wire [BWI2-1:0] i2;
    wire [BWI1+BWI2-1:0] o_tmp;

//================================================================================
// Divider (To tell the Truth -> Multipiler)
//================================================================================
    assign i2 = CONST_MULTI;
    assign o_tmp = i1 * i2;

    assign o1 = o_tmp[BWI1+BWI2-1 : BWI2];

endmodule""".format(self.dividend_width, self.divisor, len(self.new_divisor), self.new_divisor)
        wf.write(divider_hdl)
        wf.close()
        print("     success creating divider verilog file")

if __name__ == '__main__':
    test = divider_const(int(sys.argv[1]), int(sys.argv[2]))
    test.calc_bin()
    test.create_divider_hdl()

    
