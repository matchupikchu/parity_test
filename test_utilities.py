
import cocotb
from cocotb_bus.scoreboard import Scoreboard
from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, Timer


from test_drivers import MasterDriver, SlaveDriver
from test_monitors import MasterMonitor, SlaveMonitor

from numpy import sum


class TbParityTester(object):
    def __init__(self, dut):
        self.dut = dut
    
    def start_clock(self, clk_period = 10):
        self.dut._log.info("Running clock")
        cocotb.start_soon(Clock(self.dut.a_clk, clk_period,units='ns').start())


class ParityTester(TbParityTester):
    def __init__(self, dut):
        super(ParityTester, self).__init__(dut)

        self.expected_output = []
        self.dut.axis_s_tvalid.value = 0 
        self.dut.axis_m_tready.value = 1
        self.dut.axis_s_tdata.value = 0
        self.dut.axis_s_tlast.value = 0

        self.axis_s_driver = SlaveDriver(self.dut, "axis_s", dut.a_clk)
        self.axis_m_driver = MasterDriver(self.dut, "axis_m", dut.a_clk)

        self.axis_s_monitor = SlaveMonitor(self.dut, name = "axis_s",
                                           clock = dut.a_clk)

# print(parity_calculator([2,3,6]))