 # MULTIPLEXER DESIGN VERIFICATION
 
 The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
 
 Gitpod link of the environment: [Gitpod environment](https://vyomasystem-challengesr-z0ps2j7cguv.ws-us54.gitpod.io/)

![LEVEL1_DESIGN MUX](https://user-images.githubusercontent.com/89691159/181091264-b288a867-0342-46c4-af39-9afe314d9049.JPG)

## VERIFICATION ENVIRONMENT
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drive inputs to Design Under Test(DUT)(Multiplexer) which has 31 two bit inputs inp0 to inp30 with a 5 bit select input to select from those 31 inputs to give a 2 bit output.

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

## DESIGN BUG

## DESIGN FIX

## VERIFICATION STRATEGY

## IS THE VERIFICATION COMPLETE?
