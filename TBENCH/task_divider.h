task set_divider;
input [7:0] in1;
begin
    i1 = in1; 
    @(posedge CLK) #DELAY;
        i1 = 8'bz; 
end
endtask
