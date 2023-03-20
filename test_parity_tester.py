import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
# from utilities import SlaveDriver, MasterDriver, SlaveMonitor, MasterMonitor, Polynomial, Wx

   

@cocotb.test()
def test_primitive(dut):

    clock = Clock(dut.a_clk, 10, units="ns")
    cocotb.start(clock.start())

    # expected_value = []

    dut.axis_aresetn.value = 1
    yield RisingEdge(dut.a_clk)

    dut.axis_aresetn.value = 0
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 1
    dut.axis_s_tdata.value = 8
    dut.axis_s_tlast.value = 0
    yield RisingEdge(dut.a_clk)

    dut.axis_aresetn.value = 0
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 1
    dut.axis_s_tdata.value = 8
    dut.axis_s_tlast.value = 0
    yield RisingEdge(dut.a_clk)

    dut.axis_aresetn.value = 0
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 1
    dut.axis_s_tdata.value = 0xb
    dut.axis_s_tlast.value = 0
    yield RisingEdge(dut.a_clk)

    dut.axis_aresetn.value = 0
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 0
    dut.axis_s_tdata.value = 0
    dut.axis_s_tlast.value = 1
    yield RisingEdge(dut.a_clk)

    dut.axis_aresetn.value = 0
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 0
    dut.axis_s_tdata.value = 0
    dut.axis_s_tlast.value = 0
    yield RisingEdge(dut.a_clk)


    yield RisingEdge(dut.a_clk)
    yield RisingEdge(dut.a_clk)
    yield RisingEdge(dut.a_clk)
    yield RisingEdge(dut.a_clk)
    yield RisingEdge(dut.a_clk)
    yield RisingEdge(dut.a_clk)
    
    
    
    

    # for _ in range(10):

        # x = random.randint(0, 2*16)
        
        # await slave_driver._driver_send(x)