import cocotb
from cocotb_bus.monitors import BusMonitor
from cocotb.triggers import RisingEdge, Timer

class SlaveMonitor(BusMonitor):
    
    def __init__(self, entity, clock,
                 name = '',
                 bus_separator='_',
                 signals = ['tvalid', 'tdata', 'tready']):
        
        self.dut = entity
        self._signals = signals
        BusMonitor.__init__(self, entity, name, clock, bus_separator = bus_separator, callback = None)
        self.clock = clock
        self.tvalid = getattr(self.bus,list(filter(lambda x: 'tvalid' in x, self._signals))[0])
        self.tready = getattr(self.bus,list(filter(lambda x: 'tready' in x, self._signals))[0])
        self.tdata  = getattr(self.bus,list(filter(lambda x: 'tdata' in x, self._signals))[0])

        
    @cocotb.coroutine
    def _monitor_recv(self):
        
        while True:
            yield RisingEdge(self.clock)
            if self.tvalid.value == 1:

                self.log.info(f"{self.name} tvalid {int(self.tvalid)}")
                self.log.info(f"{self.name} tready {int(self.tready)}")
                self.log.info(f"{self.name} tdata {int(self.tdata)}")
                
class MasterMonitor(BusMonitor):
    
    

    def __init__(self, entity, clock,
                 name = '',
                 bus_separator='_',
                 signals = ['tvalid', 'tdata', 'tready']):
        
        self.dut = entity
        self._signals = signals
        BusMonitor.__init__(self, entity, name, clock, bus_separator = bus_separator, callback = None)
        self.clock = clock
        self.tvalid = getattr(self.bus,list(filter(lambda x: 'tvalid' in x, self._signals))[0])
        self.tready = getattr(self.bus,list(filter(lambda x: 'tready' in x, self._signals))[0])
        self.tdata  = getattr(self.bus,list(filter(lambda x: 'tdata' in x, self._signals))[0])
        
        self.counter = 0
        
    @cocotb.coroutine
    def _monitor_recv(self):
        
        while True:
            yield RisingEdge(self.clock)
            if self.tvalid.value == 1:
                self.log.info(f"{self.name} tvalid {int(self.tvalid)}")
                self.log.info(f"{self.name} tready {int(self.tready)}")
                self.log.info(f"{self.name} tdata {hex(int(self.tdata))}")
                # assert Wx(int(self.entity.axis_s_tdata.value)) == int(self.entity.axis_m_tdata.value), f"{Wx(int(self.entity.axis_s_tdata.value))} {int(self.entity.axis_m_tdata.value)}"
        
