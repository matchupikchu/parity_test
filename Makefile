SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += parity_tester.v
VERILOG_SOURCES += parity_tester_wrapper.v


Wx:
	rm -rf sim_build
	$(MAKE) sim MODULE=test_parity_tester TOPLEVEL=parity_tester_wrapper

include $(shell cocotb-config --makefiles)/Makefile.sim
