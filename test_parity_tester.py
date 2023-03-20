import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
# from utilities import SlaveDriver, MasterDriver, SlaveMonitor, MasterMonitor, Polynomial, Wx

   

@cocotb.test()
def test_primitive(dut):

    clock = Clock(dut.in_clock, 10, units="ns")
    cocotb.start(clock.start())

    # expected_value = []
    yield RisingEdge(dut.in_clock)
    dut.axis_m_tready.value = 1
    dut.axis_s_tvalid.value = 1
    dut.axis_s_tdata.value = 8
    dut.axis_s_tlast.value = 1
    yield RisingEdge(dut.in_clock)
    yield RisingEdge(dut.in_clock)
    yield RisingEdge(dut.in_clock)
    
    

    # for _ in range(10):

        # x = random.randint(0, 2*16)
        
        # await slave_driver._driver_send(x)