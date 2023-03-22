import random
import cocotb
from test_parity_tester import ParityTester
from schemdraw import logic

@cocotb.test()
def test(dut):
    
    tb = ParityTester(dut)
    
    tb.start_clock()

    for _ in range(10):
        n = random.randint(2, 100)
        x = random.sample(range(0, 256), n)

        yield tb.axis_s_driver._driver_send(x)
    
    
