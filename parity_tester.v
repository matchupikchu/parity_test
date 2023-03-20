module parity_tester(
    in_clock, 
    // master
    axis_m_tvalid,
    axis_m_tdata,
    axis_m_tready,
    axis_m_tlast,
    // slave
    axis_s_tvalid,
    axis_s_tdata,
    axis_s_tready,
    axis_s_tlast);


input in_clock;

output reg		 axis_m_tvalid;
output reg [7:0] axis_m_tdata;
input 			 axis_m_tready;
output reg		 axis_m_tlast;

input             axis_s_tvalid;
input      [7:0]  axis_s_tdata;
output 			  axis_s_tready;
input 			  axis_s_tlast;

wire parity = 0;
reg [7:0] r_data;

reg [3:0] FSM_state;


localparam FSM_first = 1;
localparam FSM_second = 2;
localparam FSM_third = 3;



always @(posedge in_clock)
begin

    if(axis_s_tvalid)
        r_data <= axis_s_tdata;

    if(axis_s_tlast)
        if(parity)
        begin
            axis_m_tdata <= 8'hff;
            axis_m_tvalid <= 1;
            axis_m_tlast <= 1;
            // parity <= 0;
        end else begin
            FSM_state <= FSM_first;
            axis_m_tdata <= 8'hab;
            axis_m_tvalid <= 1;
            axis_m_tlast <= 0;
        end

end

assign parity = parity ^ r_data[7] ^ r_data[6] ^ r_data[5] ^ r_data[4] ^ r_data[3] ^ r_data[2] ^ r_data[1] ^ r_data[0];


endmodule