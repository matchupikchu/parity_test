## Parity tester in Verilog 

This repo contains the project of parity tester project in Verilog. The interface is compatible with the AXI stream.

Axis interface was implemented with the use AMBA 4 AXI4-Stream Protocol Specification: 
<https://developer.arm.com/documentation/ihi0051/a/Introduction/About-the-AXI4-Stream-protocol>

The whole interface consists of such signals as:
- global signals:
  - a_clk - global clock,
  - axis_aresetn - global reset signal
- slave side:
  - axis_s_tvalid - slave valid signal,
  - axis_s_t_data - slave 8 bit wide data bus,
  - axis_s_t_ready - slave ready signal, 
  - axis_s_tlast - slave last signal,
- master side:
  - axis_m_tvalid - master valid signal,
  - axis_m_tdata - master bit wide data bus,
  - axis_m_tready - master ready signal,
  - axis_m_tlast - master last signal
  
## Requirements
  - Python 3.8.10 (or newer)
  - Cocotb 1.7.2
  - Icarus Verilog 10.3 

## Example waveform
![image](https://user-images.githubusercontent.com/56771910/232452856-bcdbb651-470a-4305-9f4f-897fa3d7fdc9.png)



