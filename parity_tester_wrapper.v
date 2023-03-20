module parity_tester_wrapper(
    in_clock, 
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

output reg in_clock;
output 			 axis_m_tvalid;
output     [7:0] axis_m_tdata;
input 			 axis_m_tready;
output      	 axis_m_tlast;

input             axis_aresetn;
input             axis_s_tvalid;
input      [7:0]  axis_s_tdata;
output 			  axis_s_tready;
input 			  axis_s_tlast;

parity_tester dut(
    .in_clock(in_clock),
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
	  in_clock=0;
	  forever begin
		  #5 in_clock=~in_clock;
	  end
end



endmodule