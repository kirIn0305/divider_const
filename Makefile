TBENCH = ./TBENCH/tbench.v
VERILOG = ./HDL/divider_10_11.v

all:
	iverilog -o ./test.vpp $(TBENCH) $(VERILOG)
	./test.vpp
	gtkwave ./test.vcd
