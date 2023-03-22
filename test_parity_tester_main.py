import random

import cocotb
from test_parity_tester import ParityTester

@cocotb.test()
def test(dut):
    
    tb = ParityTester(dut)
    
    tb.start_clock()

    for _ in range(10):
        x = random.sample(range(0, 256), 10)

        yield tb.axis_s_driver._driver_send(x)
    
    
    