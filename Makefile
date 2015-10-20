DIVIDEND_WIDTH = 10
DIVISOR = 5
TBENCH = ./TBENCH/tbench.v
VERILOG = ./HDL/divider_10_11.v

all:
	python3 ./make_divider.py 10 11
	iverilog -o ./test.vpp $(TBENCH) $(VERILOG)
	./test.vpp
	gtkwave ./test.vcd

create_hdl:
	python3 ./make_divider.py $(DIVIDEND_WIDTH) $(DIVISOR)

sim:
	iverilog -o ./test.vpp $(TBENCH) $(VERILOG)
	./test.vpp
	gtkwave ./test.vcd
