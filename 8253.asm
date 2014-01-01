CLI					;关中断
MOV AL, 34H			;T0初始化，计数器0，先读低八位，后读高八位，方式2，二进制
OUT 43H, AL 		;写入方式字
MOV AL, 76H			;T1初始化，计数器1，先读低八位，后读高八位，方式3，二进制
OUT 43H, AL 		;写入方式字
MOV AX, 4E20H		;向T0写入计数值	
OUT 40H, AL			;送入低8位
MOV AL, AH 			;写入高8位
OUT 40H, AL 		;送入高8位
MOV AX, 07D0H		;向T1写入计数值
OUT 41H, AL 		;送入低8位
MOV AL, AH 			;写入高8位
OUT 41H, AL 		;送入高8位
STI					;开中断