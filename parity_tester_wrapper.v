module parity_tester_wrapper(
    a_clk, 
    // master
    axis_aresetn,
    axis_m_tvalid,
    axis_m_tdata,
    axis_m_tready,
    axis_m_tlast,
    // slave
    axis_s_tvalid,
    axis_s_tdata,
    axis_s_tready,
    axis_s_tlast);

output reg a_clk;
input             axis_aresetn;

// master
output 			 axis_m_tvalid;
output     [7:0] axis_m_tdata;
input 			 axis_m_tready;
output      	 axis_m_tlast;

// slave
input             axis_s_tvalid;
input      [7:0]  axis_s_tdata;
output 			  axis_s_tready;
input 			  axis_s_tlast;

parity_tester dut(
    .a_clk(a_clk),
    .axis_aresetn(axis_aresetn),
    // master
    .axis_m_tvalid(axis_m_tvalid),
    .axis_m_tdata(axis_m_tdata),
    .axis_m_tready(axis_m_tready),
    .axis_m_tlast(axis_m_tlast),
    // slave
    .axis_s_tvalid(axis_s_tvalid),
    .axis_s_tdata(axis_s_tdata),
    .axis_s_tready(axis_s_tready),
    .axis_s_tlast(axis_s_tlast)
);

initial begin
    $dumpfile("parity_tester.vcd");
	  $dumpvars;
	  a_clk=0;
	  forever begin
		  #5 a_clk=~a_clk;
	  end
end



endmodule