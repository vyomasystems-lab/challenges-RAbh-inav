# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    assert dut.current_state.value == 0, f"sequence detector result is incorrect: {dut.current_state.value} != IDLE"
@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 0
    dut.inp_bit.value=1
    cocotb.log.info(dut.current_state.value)
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    cocotb.log.info(dut.current_state.value)
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    cocotb.log.info(dut.current_state.value)
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    cocotb.log.info(dut.current_state.value)
    await FallingEdge(dut.clk)
    assert dut.seq_seen.value == 1, f"sequence detector result is incorrect: {dut.next_state.value} != 1011"

