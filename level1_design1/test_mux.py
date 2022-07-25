# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    select =10
    dut.sel.value=select
    await Timer(2, units='ns')
    assert dut.out.value == inp10, f"mux result is incorrect: {dut.out.value} != inp10"
