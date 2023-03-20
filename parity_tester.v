module parity_tester(
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


input a_clk;

input axis_aresetn;

output reg		 axis_m_tvalid;
output reg [7:0] axis_m_tdata;
input 			 axis_m_tready;
output reg		 axis_m_tlast;

input             axis_s_tvalid;
input      [7:0]  axis_s_tdata;
output reg		  axis_s_tready;
input 			  axis_s_tlast;

wire w_parity;
reg r_parity = 0;
reg [7:0] r_data;

reg [3:0] FSM_state;
reg s_tready;

localparam FSM_first = 1;
localparam FSM_second = 2;
localparam FSM_third = 3;



always @(posedge a_clk)
begin

    if(axis_aresetn)
    begin
        r_data <= 0;
        r_parity <= 0;
    end

end

always @(negedge a_clk)
begin

    if(axis_s_tvalid & axis_m_tready)
    begin     
        r_data <= axis_s_tdata;
        
    end

    r_parity <= r_parity ^ w_parity;
    s_tready <= 0;

end

assign w_parity = axis_s_tdata[7] ^ axis_s_tdata[6] ^ axis_s_tdata[5] ^ axis_s_tdata[4] ^ axis_s_tdata[3] ^ axis_s_tdata[2] ^ axis_s_tdata[1] ^ axis_s_tdata[0];


assign axis_s_tready = s_tready;


endmodule