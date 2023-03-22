import cocotb
from cocotb_bus.monitors import BusMonitor
from cocotb.triggers import RisingEdge
from test_drivers import parity_calculator

class SlaveMonitor(BusMonitor):
    
    def __init__(self, entity, clock,
                 name = '',
                 bus_separator='_',
                 signals = ['tvalid', 'tdata', 'tready', 'tlast']):
        
        self.dut = entity
        self._signals = signals
        BusMonitor.__init__(self, entity, name, clock, bus_separator = bus_separator, callback = None)
        self.clock = clock
        self.tvalid = getattr(self.bus,list(filter(lambda x: 'tvalid' in x, self._signals))[0])
        self.tready = getattr(self.bus,list(filter(lambda x: 'tready' in x, self._signals))[0])
        self.tdata  = getattr(self.bus,list(filter(lambda x: 'tdata' in x, self._signals))[0])
        self.tlast  = getattr(self.bus,list(filter(lambda x: 'tlast' in x, self._signals))[0])

        
    @cocotb.coroutine
    def _monitor_recv(self):
        
        while True:
            yield RisingEdge(self.clock)
            if self.tvalid.value == 1 or self.tlast.value == 1:

                self.log.info(f"{self.name} tvalid {int(self.tvalid)}")
                self.log.info(f"{self.name} tready {int(self.tready)}")
                self.log.info(f"{self.name} tdata {int(self.tdata)}")
                self.log.info(f"{self.name} tlast {int(self.tlast)}")
                
class MasterMonitor(BusMonitor):
    
    

    def __init__(self, entity, clock,
                 name = '',
                 bus_separator='_',
                 signals = ['tvalid', 'tdata', 'tready', 'tlast']):
        
        self.dut = entity
        self._signals = signals
        BusMonitor.__init__(self, entity, name, clock, bus_separator = bus_separator, callback = None)
        self.clock = clock
        self.tvalid = getattr(self.bus,list(filter(lambda x: 'tvalid' in x, self._signals))[0])
        self.tready = getattr(self.bus,list(filter(lambda x: 'tready' in x, self._signals))[0])
        self.tdata  = getattr(self.bus,list(filter(lambda x: 'tdata' in x, self._signals))[0])
        self.tlast  = getattr(self.bus,list(filter(lambda x: 'tlast' in x, self._signals))[0])

    @cocotb.coroutine
    def _monitor_recv(self):

        data_transferred_to_DUT = []
        data_from_DUT = []

        while True:
            
            yield RisingEdge(self.clock)

            if self.entity.axis_s_tvalid.value == 1:
                data_transferred_to_DUT += [int(self.entity.axis_s_tdata.value)]

            if self.tvalid.value == 1:

                data_from_DUT += [int(self.tdata)]

                if len(data_from_DUT) == 3:
                    
                    self.log.info(f"{self.name} tdata {[hex(i) for i in data_from_DUT]}")
                    assert data_from_DUT == parity_calculator(data_transferred_to_DUT), f"Data from DUT {data_from_DUT}, expected data {parity_calculator(data_transferred_to_DUT)}"

                    data_from_DUT = []
                    data_transferred_to_DUT = []

                if len(data_from_DUT) == 1 and data_from_DUT[0] != 0xab:
                    
                    self.log.info(f"{self.name} tdata {[hex(i) for i in data_from_DUT]}")
                    assert data_from_DUT == parity_calculator(data_transferred_to_DUT), f"Data from DUT {data_from_DUT}, expected data {parity_calculator(data_transferred_to_DUT)}"

                    data_from_DUT = []
                    data_transferred_to_DUT = []
