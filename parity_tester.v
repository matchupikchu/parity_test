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

output reg    	 axis_m_tvalid;
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
reg r_s_tready;
reg r_tvalid_p;


localparam FSM_first = 1;
localparam FSM_second = 2;
localparam FSM_third = 3;
localparam FSM_fourth = 4;



always @(posedge a_clk)
begin
    if(axis_aresetn)
    begin
        r_data <= 0;
        r_parity <= 0;
        axis_m_tdata <= 0;
    end

    if(axis_s_tlast)
    begin
        FSM_state <= FSM_first;
    end
end

always @(posedge a_clk)
begin

    case(FSM_state)

        FSM_first   :   begin
                        if(r_parity)
                            begin
                                axis_m_tdata <= 8'hff;
                                axis_m_tvalid <= 1;
                                FSM_state <= FSM_fourth;
                            end
                        else 
                            begin
                                FSM_state <= FSM_second;
                                axis_m_tdata <= 8'hab;
                                axis_m_tvalid <= 1;
                            end
                        end
        FSM_second  :   begin
                            FSM_state <= FSM_third;
                            axis_m_tdata <= 8'h12;
                            axis_m_tvalid <= 1;
                        end
        FSM_third   :   begin
                            FSM_state <= FSM_fourth;
                            axis_m_tdata <= 8'hde;
                            axis_m_tvalid <= 1;
                            axis_m_tlast <= 0;
                        end
        FSM_fourth  :   begin
                            FSM_state <= 0;
                            axis_m_tdata <= 8'h00;
                            axis_m_tvalid <= 0;
                            axis_m_tlast <= 1;
                            axis_s_tready <= 1;
                        end

        default :       begin
                            axis_m_tdata <= 8'h00;
                            axis_m_tvalid <= 0;
                            axis_m_tlast <= 0;
                        end

    endcase

    if((axis_s_tvalid == 1) && (axis_m_tready == 1))
    begin     
        r_data <= axis_s_tdata;
        axis_s_tready <= 0;
    end

    r_parity <= r_parity ^ w_parity;
end


assign w_parity = axis_s_tdata[7] ^ axis_s_tdata[6] ^ axis_s_tdata[5] ^ axis_s_tdata[4] ^ axis_s_tdata[3] ^ axis_s_tdata[2] ^ axis_s_tdata[1] ^ axis_s_tdata[0];


endmodule