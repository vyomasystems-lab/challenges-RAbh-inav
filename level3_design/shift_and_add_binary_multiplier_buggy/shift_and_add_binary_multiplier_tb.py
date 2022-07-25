# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

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
    dut.A.value=1
    dut.B.value=1
    await FallingEdge(dut.clk)
    assert dut.C.value == 1, f"sequence detector result is incorrect: {dut.C.value} != 1"


