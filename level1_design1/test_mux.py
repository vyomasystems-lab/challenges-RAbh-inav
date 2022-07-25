# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    select =30
    inp30= 2
    dut.sel.value=select
    dut.inp30.value=inp30
    await Timer(2, units='ns')
    assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp30"
