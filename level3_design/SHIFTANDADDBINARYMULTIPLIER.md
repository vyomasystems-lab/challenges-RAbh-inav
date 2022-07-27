# SHIFT AND ADD BINARY MULTIPLIER DESIGN VERIFICATION
 
 The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
 
 Gitpod link of the environment: [Gitpod environment](https://vyomasystem-challengesr-z0ps2j7cguv.ws-us54.gitpod.io/)
 
 Link to licensed source code: [shift and add binary multiplier](https://github.com/RAbh-inav/Shift-and-add-binary-multiplier)

![gitpod environment](https://user-images.githubusercontent.com/89691159/181111599-38a3bd40-93c2-4650-bd4b-7c43b21a9362.JPG)

## VERIFICATION ENVIRONMENT
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drive inputs to Design Under Test(DUT)(Sequence detector) which takes in 4 inputs clk,rst and 8 bit inputs A and B to give C as an 8 bit output.  

Values are assigned using
    
    dut.rst.value = 1
    
    dut.A.value= 10
    
    dut.B.value= 12
    
Clk is generated using clock imported from cocotb

    from cocotb.clock import Clock

    clock = Clock(dut.clk, 10, units="ns") 
    
    cocotb.start_soon(clock.start())   
    
It waits for a specific time for tasks to complete using falling edge of clock imported from cocotb.triggers as the reference
    
    from cocotb.triggers import FallingEdge
   
    await FallingEdge(dut.clk)
    
The assert statement is used for comparing the sequence detector's output to the expected value.

The following error is seen:

    assert dut.C.value == 0, f"Multiplier result is incorrect: {dut.C.value} != 0"
     
## TEST SCENARIO

### TEST SCENARIO 1

- Test Inputs: rst= 1,0 ; A= 13,B=3
- Expected Output: C=39
- Observed Output in the DUT: dut.C=3

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 2

- Test Inputs: rst= 1 ; A=10,B=12
- Expected Output: C=0
- Observed Output in the DUT: dut.C=1

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 3

- Test Inputs: rst= 1,0 ; A=12,B=6
- Expected Output: C=72
- Observed Output in the DUT: dut.C=72

Output matches for the above inputs proving that this case has passed

### TEST SCENARIO 4

- Test Inputs: reset= 1,0 ; A=2,B=63
- Expected Output: C=126
- Observed Output in the DUT: dut.C=72

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 5

- Test Inputs: reset= 1,0 ; A=12,B=7
- Expected Output: C=84
- Observed Output in the DUT: dut.C=84

Output matches for the above inputs proving that this case has passed

 
![level 3 result 1](https://user-images.githubusercontent.com/89691159/181124234-7435e40e-fc26-46ed-a484-d1bc643c05ef.JPG)
![level 3 result 2](https://user-images.githubusercontent.com/89691159/181124256-fd783a25-770f-40d9-a284-3041b510c916.JPG)


## DESIGN BUGS AND EXPLANATION

### BUG1

For test scenario 2 , bug is found in these lines

![level 3 error1](https://user-images.githubusercontent.com/89691159/181124958-00b4e765-d438-4053-872d-2aecd7b0a787.JPG)

On rst= 1, C is 1 instead 0 causing a design bug

### BUG2

For test scenario 4, bug is found in these lines

![level 3 error2](https://user-images.githubusercontent.com/89691159/181125037-4363c935-3875-41d5-9439-64fbc4f2608d.JPG)

Condition B % 9!= 0 is given negating multiples of 9 as values of B causing a design bug

### BUG3

For test scenarios 1, bug is found in these lines

![level 3 error3](https://user-images.githubusercontent.com/89691159/181125100-fd0497e4-6cb1-43f6-aeff-b5fe7459099c.JPG)

Condition A1 <= 12 is given negating values of A (A1 is from A) greater than 12 causing a design bug

## DESIGN FIX

- For Bug 1 , C is set to 0 when rst= 1.
- For Bug 2 , Condition B % 9!= 0 is removed cancelling the negation.
- For Bug 3, Condition A1 <= 12 is removed cancelling the negation.

![level 3 bug free result ](https://user-images.githubusercontent.com/89691159/181125202-a38c34f0-5ae1-45a1-a587-3aad9856ad46.JPG)

 Now all the bugs are fixed and after the design update all the tests have passed.
 
## VERIFICATION STRATEGY

Functional verification using software simulation has been created using directed test cases for specific inputs where scenarios where DUT could fail to identify the bugs in the design . These directed test cases are chosen after thorough analysis of HDL design to understand its functionality and finding corner cases for functional analysis. After analysing this HDL design , directed test cases for specific rst, A and B values have been included along with other passing cases.

## IS THE VERIFICATION COMPLETE?

 Functional Verification is complete and fault coverage is done as all the bugs have been found in the design using test scenarios 
