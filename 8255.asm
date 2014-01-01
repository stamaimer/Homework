	MOV  DX, 303H		;将端口C地址送入DX
	MOV  AL, 81H		;将方式字送入AL
	OUT  DX, AL			;将方式字送入端口C
	MOV  AL, 0FH		;端口C置位控制字
	OUT  DX, AL 		;PC7置位，STB选通无效
	LEA  SI, SRC		;写入数据地址
	MOV  CX, 1024		;写入数据计数
L:	MOV  DX, 302H		;将状态端口地址送入DX
	IN   AL, DX 		;从状态端口读入状态字
	AND  AL, 02H		;检测IBF信号是否为高
	JNZ  L 				;当CX=1时跳转
	MOV  DX, 300H		;将端口A地址送入DX
	MOV  AL, [SI]		;将数据送入AL
	OUT  DX, AL 		;将数据送入端口A
	MOV  DX, 303H		;将端口C地址送入DX
	MOV  AL, 0EH		;端口C复位控制字
	OUT  DX, AL 		;PC7复位，STB选通生效
	NOP					;STB信号延迟
	NOP					;STB信号延迟
	MOV  AL, 0FH		;端口C置位控制字
	OUT  DX, AL 		;PC7置位，STB选通无效
	INC  SI				;递增数据地址
	LOOP L 				;循环