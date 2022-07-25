import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge,ClockCycles

@cocotb.test()
async def shift_and_add_multiplier_bug1(dut):
    """Test for bug in shift and add multiplier """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    dut.A.value=13
    dut.B.value=3
    await FallingEdge(dut.clk)
    assert dut.C.value == 39, f"Multiplier result is incorrect: {dut.C.value} != 39"

@cocotb.test()
async def shift_and_add_multiplier_bug2(dut):
    """Test for bug in shift and add multiplier """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)
    dut.A.value=10
    dut.B.value=12
    await FallingEdge(dut.clk)
    assert dut.C.value == 0, f"Multiplier result is incorrect: {dut.C.value} != 0"

@cocotb.test()
async def shift_and_add_multiplier_bug3(dut):
    """Test for bug in shift and add multiplier """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)    
    dut.A.value=12
    dut.B.value=6
    await FallingEdge(dut.clk)
    assert dut.C.value == 72, f"Multiplier result is incorrect: {dut.C.value} != 72"

@cocotb.test()
async def shift_and_add_multiplier_bug4(dut):
    """Test for bug in shift and add multiplier """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)    
    dut.A.value=2
    dut.B.value=63
    await FallingEdge(dut.clk)
    assert dut.C.value == 126, f"Multiplier result is incorrect: {dut.C.value} != 126"

@cocotb.test()
async def shift_and_add_multiplier_bug5(dut):
    """Test for bug in shift and add multiplier """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)    
    dut.A.value=12
    dut.B.value=7
    await FallingEdge(dut.clk)
    assert dut.C.value == 84, f"Multiplier result is incorrect: {dut.C.value} != 84"