# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux1"""
    select =13
    inp13= 2
    inp12= 3
    dut.sel.value=select
    dut.inp13.value=inp13
    dut.inp12.value=inp12
    await Timer(2, units='ns')
    assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp13"
@cocotb.test()
async def test_mux2(dut):
    """Test for mux2"""
    select =10
    inp10=2
    dut.sel.value=select
    dut.inp10.value=inp10
    await Timer(4, units='ns')
    assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp10"
@cocotb.test()
async def test_mux3(dut):
    """Test for mux3"""
    select =12
    inp13= 2
    inp12= 3
    dut.sel.value=select
    dut.inp13.value=inp13
    dut.inp12.value=inp12
    await Timer(6, units='ns')
    assert dut.out.value == 3, f"mux result is incorrect: {dut.out.value} != inp12"
@cocotb.test()
async def test_mux4(dut):
    """Test for mux4"""
    select =20
    inp20= 3
    dut.sel.value=select
    dut.inp20.value=inp20
    await Timer(8, units='ns')
    assert dut.out.value == 3, f"mux result is incorrect: {dut.out.value} != inp20"
@cocotb.test()
async def test_mux5(dut):
    """Test for mux5"""
    select =30
    inp30=1
    dut.sel.value=select
    dut.inp30.value=inp30
    await Timer(10, units='ns')
    assert dut.out.value == 1, f"mux result is incorrect: {dut.out.value} != inp30"