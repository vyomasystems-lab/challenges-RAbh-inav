# SEQUENCE_DETECTOR_1011 DESIGN VERIFICATION
 
 The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
 
 Gitpod link of the environment: [Gitpod environment](https://vyomasystem-challengesr-z0ps2j7cguv.ws-us54.gitpod.io/)

![gitpod environment](https://user-images.githubusercontent.com/89691159/181111599-38a3bd40-93c2-4650-bd4b-7c43b21a9362.JPG)

## VERIFICATION ENVIRONMENT
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drive inputs to Design Under Test(DUT)(Sequence detector) which takes in 3 inputs clk,reset and inp_bit to give seq_seen as output.  

Values are assigned using
    
    dut.reset.value = 1
    
    dut.inp_bit.value=1
    
Clk is generated using clock imported from cocotb

    from cocotb.clock import Clock

    clock = Clock(dut.clk, 10, units="ns") 
    
    cocotb.start_soon(clock.start())   
    
It waits for a specific time for tasks to complete using falling edge of clock imported from cocotb.triggers as the reference
    
    from cocotb.triggers import FallingEdge
   
    await FallingEdge(dut.clk)
    
The assert statement is used for comparing the sequence detector's output to the expected value.

The following error is seen:

     assert dut.seq_seen.value == 1, f"sequence detector result is incorrect: {dut.seq_seen.value} != 1"
     
## TEST SCENARIO

### TEST SCENARIO 1

- Test Inputs: reset= 1,0 ; inp_bit= 1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=1

Output matches for the above inputs proving that this cas has passed

### TEST SCENARIO 2

- Test Inputs: reset= 1,0 ; inp_bit= 1,1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 3

- Test Inputs: reset= 1,0 ; inp_bit= 1,0,1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 4

- Test Inputs: reset= 1,0 ; inp_bit= 1,0,1,1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 5

- Test Inputs: reset= 1,0 ; inp_bit= 1,0,1,1,1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 6

- Test Inputs: reset= 1,0, inp_bit= 1,0,0,1,0,1,1
- Expected Output: seq_seen=1
- Observed Output in the DUT: dut.seq_seen=1

Output matches for the above inputs proving that this case has passed

![level 1 1011 seq detector result 1](https://user-images.githubusercontent.com/89691159/181119836-eb83e7eb-50f5-45ad-9e35-e6161a44556d.JPG)
![level 1 1011 seq detector result 2](https://user-images.githubusercontent.com/89691159/181119858-221fde6d-f7c7-4127-9f33-c46f76c1c831.JPG)

## DESIGN BUGS AND EXPLANATION

### BUG1
For test scenario 2 , bug is found in these lines

![level 1 1011 seq detector error](https://user-images.githubusercontent.com/89691159/181120440-6afd860e-610f-4128-b6f3-c9aa7387dbd2.JPG)

 When inp_bit is 1 in this case value, next_state must be SEQ_1 not IDLE leading to this bug.

### BUG2

For test scenario 3, bug is found in these lines

![level 1 1011 seq detector error 2 a](https://user-images.githubusercontent.com/89691159/181120639-122553f6-1358-4573-85af-08b9e288dcb7.JPG)

when inp_bit is not 1 in this case value, next_state must be SEQ_10 not IDLE leading to this bug.

### BUG3

For test scenarios 4 and 5, bug is found in these lines

![level 1 1011 seq detector error 2 b](https://user-images.githubusercontent.com/89691159/181120655-223a5b08-2847-4a4f-a233-0165f9533167.JPG)

When inp_bit is 1 in this case value, next_state must be SEQ_1 and when inp_bit is not 1, next_state must be SEQ_10 instead of IDLE for all inp_bit values leading to this bug.

## DESIGN FIX

- For Bug 1 , next_state is SEQ_1 when inp_bit= 1 for that case value.
- For Bug 2 , next_state is SEQ_10 when inp_bit!= 1 for that case value.
- For Bug 3, next_state is SEQ_1 when inp_bit= 1 for that case value and next_state is SEQ_1 when inp_bit!= 1 for that case value.

![level 1 1011 seq detector error free result ](https://user-images.githubusercontent.com/89691159/181120265-19ec2355-f10a-4484-b27c-85f3909586f4.JPG)


 Now all the bugs are fixed and after the design update all the tests have passed.
 
## VERIFICATION STRATEGY

Functional verification using software simulation has been created using directed test cases for specific inputs where scenarios where DUT could fail to identify the bugs in the design . These directed test cases are chosen after thorough analysis of HDL design to understand its functionality and finding corner cases for functional analysis. After analysing this HDL design , directed test cases for faulty transitions between states have been included along with other passing cases.

## IS THE VERIFICATION COMPLETE?

 Functional Verification is complete and fault coverage is done as all the bugs have been found in the design using test scenarios 

