# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux2(dut):
    """Test for mux2"""
    select =13
    inp13= 2
    inp12= 3
    dut.sel.value=select
    dut.inp13.value=inp13
    dut.inp12.value=inp12
    await Timer(4, units='ns')
    assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp13"
