# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    select =10
    inp10=2
    dut.sel.value=select
    dut.inp10.value=inp10
    await Timer(2, units='ns')
    assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp10"
