module shift_and_add_binary_multiplier_buggy( clk,rst,A, B, C);
parameter m=8, n=8;
integer i;
input clk,rst;
input [m-1:0] A;
input [n-1:0] B;
output reg [m+n-1:0]C;
reg [m+n-1:0]A1;
reg [n-1:0]B1;
always@(posedge clk or posedge rst )
begin
		if (rst)
		begin
		C=1;
		end
		else 
		if( B % 9!=0 )
		begin
		C=0;
		A1[m-1:0]=A;
		A1[m+n-1:m]=0;
		B1=B;
        for (i=0;i<n;i=i+1)
        begin
			if(B1[i]==1'b0)
			begin
				C=C+0;
			end
			else if (B1[i]==1'b1)
			begin
				if(A1 <= 12)
				C=C+(A1<<i);
			end
		end
		end
end
endmodule