# BIT MANIPULATION COPROCESSOR DESIGN VERIFICATION
 
 The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
 
 Gitpod link of the environment: [Gitpod environment](https://vyomasystem-challengesr-z0ps2j7cguv.ws-us54.gitpod.io/)

![gitpod environment](https://user-images.githubusercontent.com/89691159/181111599-38a3bd40-93c2-4650-bd4b-7c43b21a9362.JPG)

## VERIFICATION ENVIRONMENT
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drive inputs to Design Under Test(DUT)(Bit manipulation Coprocessor) which takes in 3 inputs CLK,RST_N and EN_mav_putvalue and four 32 bit inputs mav_putvalue_src1 , mav_putvalue_src2 , mav_putvalue_src3 , mav_putvalue_instr to give mav_putvalue as an 33 bit output.  

Values are assigned using
    
    dut.RST_N.value = 1
    
    dut.EN_mav_putvalue.value = 1
    
    mav_putvalue_src1 = 0x5
    
    mav_putvalue_src2 = 0x7
    
    mav_putvalue_src3 = 0x3
    
    mav_putvalue_instr = 0x401040B3
    
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    
    dut.mav_putvalue_instr.value = mav_putvalue_instr 
 
Clk is generated using couroutine(generator) imported from cocotb

    from cocotb.decorators import coroutine
    
    @cocotb.coroutine
    def clock_gen(signal):
          while True:
            signal.value <= 0
            yield Timer(1) 
            signal.value <= 1
            yield Timer(1) 
    
     cocotb.fork(clock_gen(dut.CLK))
    
It waits for a specific time for tasks to complete using falling edge of clock imported from cocotb.triggers as the reference
    
    from cocotb.triggers import Timer
   
    yield Timer(1)
    
Reference python model is called by

    from model_mkbitmanip import *
    
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    
The assert statement is used for comparing the bit manipulation coprocessor's output to the expected value from python program.

The following error is seen:

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 
     
## TEST SCENARIO

### TEST SCENARIO 1

- Test Inputs: RST_N = 0,1 , EN_mav_putvalue= 1 , mav_putvalue_src1= 0x5 , mav_putvalue_src2= 0x7 , mav_putvalue_src3= 0x3 , mav_putvalue_instr= 0x401070B3
- Expected Output: mav_putvalue= 0x1
- Observed Output in the DUT: dut.mav_putvalue= 0xb

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 2

- Test Inputs: RST_N = 0,1 , EN_mav_putvalue= 1 , mav_putvalue_src1= 0x5 , mav_putvalue_src2= 0x7 , mav_putvalue_src3= 0x3 , mav_putvalue_instr= 0x401040B3
- Expected Output: mav_putvalue= 0x1ffffffffb
- Observed Output in the DUT: dut.mav_putvalue= 0x1fffffffb

Output mismatches for the above inputs proving that this case has passed

![level 2 result1](https://user-images.githubusercontent.com/89691159/181140171-2b3e0adc-061e-43a4-b29c-4db80ae9761c.JPG)
![level 2 result2](https://user-images.githubusercontent.com/89691159/181140199-70443421-23cc-4c2e-b52d-070d7c67d549.JPG)

## DESIGN BUGS AND EXPLANATION

### BUG1

For test scenario 1 , bug is found .

ANDN operation with its func7 value = 0100000 , opcode value = 0110011 , func3 value= 111 has its output value different from its expected value from bug free python model causing a design bug

## VERIFICATION STRATEGY

Functional verification using software simulation has been created using directed test cases for specific scenarios where DUT could fail, to identify the bugs in the design . These directed test cases are chosen after thorough analysis of HDL design to understand its functionality and comparing it with the bug free python program to find corner cases for functional analysis. After analysing both HDL and python designs , directed test cases for specific  mav_putvalue_instr values have been included along with the other passing case.

## IS THE VERIFICATION COMPLETE?

Functional Verification is complete and fault coverage is done as all the bugs have been found in the design using test scenarios by comparing it with bug free python program
