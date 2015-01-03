	 	MOV  DX, 52H			;写入控制端口地址	
	 	MOV  AL, 40H			;工作命令字，IR=1，内部复位命令字
	 	OUT  DX, AL				;写入工作命令字
	 	MOV  AL, FAH			;方式命令字，异步，2停止位，偶校验，7位数据，波特率因子16
	 	OUT  DX, AL				;写入方式命令字
	 	MOV  AL, 37H			;工作命令字
	 	OUT  DX, AL				;写入工作命令字
	 	LEA  SI, SRC			;写入数据地址
	 	MOV  CX, 80				;写入数据计数
BRGIN:	MOV  DX, 52H			;写入状态端口地址
		IN   AL, DX			 	;读入状态字
		AND  AL, 01H			;是否发送
		JZ   BEGIN				;等待允许发送
		MOV  DX, 50H			;写入输出端口地址
		MOV  AL, [SI]			;将数据送入AL
		OUT  DX, AL 	 		;将数据送入输出端口
		INC  SI					;递增数据地址
		LOOP BEGIN				;循环