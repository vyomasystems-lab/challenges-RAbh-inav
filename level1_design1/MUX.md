 # MULTIPLEXER DESIGN VERIFICATION
 
 The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
 
 Gitpod link of the environment: [Gitpod environment](https://vyomasystem-challengesr-z0ps2j7cguv.ws-us54.gitpod.io/)

![gitpod environment](https://user-images.githubusercontent.com/89691159/181111599-38a3bd40-93c2-4650-bd4b-7c43b21a9362.JPG)

## VERIFICATION ENVIRONMENT
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drive inputs to Design Under Test(DUT)(Multiplexer) which has 31 two bit inputs inp0 to inp30 with a 5 bit select input to select from those 31 inputs to give a 2 bit output out.

Values are assigned using
    
    select =13
    
    inp13=2
    
    dut.sel.value=select (for select input)
    
    dut.inp13.value=inp13 
    
It waits for a specific time for tasks to complete using a timer
    
    await Timer(2, units='ns')
    
The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:

     assert dut.out.value == 2, f"mux result is incorrect: {dut.out.value} != inp13"
     
## TEST SCENARIO

### TEST SCENARIO 1

- Test Inputs: select=13, inp12=3, inp13=2
- Expected Output: out=2
- Observed Output in the DUT: dut.out=3

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 2

- Test Inputs: select=10, inp10=2
- Expected Output: out=2
- Observed Output in the DUT: dut.out=2

Output matches for the above inputs proving that this case has passed

### TEST SCENARIO 3

- Test Inputs: select=12, inp12=3, inp13=2
- Expected Output: out=2
- Observed Output in the DUT: dut.out=0

Output mismatches for the above inputs proving that there is a design bug

### TEST SCENARIO 4

- Test Inputs: select=20, inp20=3
- Expected Output: out=3
- Observed Output in the DUT: dut.out=3

Output mismatches for the above inputs proving that this case has passed

### TEST SCENARIO 5

- Test Inputs: select=30, inp30=1
- Expected Output: out=1
- Observed Output in the DUT: dut.out=0

Output mismatches for the above inputs proving that there is a design bug

![level 1 mux  result 1](https://user-images.githubusercontent.com/89691159/181101384-5b691bd3-481c-4afc-87f4-bba4a8dd0dfe.JPG)
![level 1 mux  result 2](https://user-images.githubusercontent.com/89691159/181101414-fb881eba-0931-4856-a3ec-4009df5f0246.JPG)

## DESIGN BUG AND EXPLANATION

### BUG1
For test scenarios 1 and 3 , bug is found in these lines

![level 1 mux error](https://user-images.githubusercontent.com/89691159/181103417-4568274d-ad58-4cf4-9d3a-39fe3bcd368c.JPG)  

There must be a case for select value of 12 . Value of 13 has been repeated 2 times in case instead of a 12 and 13 leading to error for both select values of 12 and 13

### BUG2

For test scenario 2, bug is found in these lines

![level 1 mux error 2](https://user-images.githubusercontent.com/89691159/181104273-cd5c202c-8bd3-48ff-981e-d06d3ff0c537.JPG)

 There must be a case for the input inp30 also which is missing in the case statement .

## DESIGN FIX

- For Bug1 , separate cases for select inputs 12 and 13 are provided
- For Bug 2 , separate cases for select input 30 is provided

![level 1 mux error free result](https://user-images.githubusercontent.com/89691159/181108541-05c9d53c-6b9d-4b61-a489-6f7c012d5bb4.JPG)

 Now all the bugs are fixed and after the design update all the tests have passed.
 
## VERIFICATION STRATEGY

Functional verification using software simulation has been created using directed test cases for specific inputs where scenarios where DUT could fail to identify the bugs in the design . These directed test cases are chosen after thorough analysis of HDL design to understand its functionality and finding corner cases for functional analysis. After analysing this HDL design , test cases for select input of 12, 13 and 30 have been included along with other passing cases.

## IS THE VERIFICATION COMPLETE?

 Functional Verification is complete as all the bugs have been found in the design using test scenarios 
