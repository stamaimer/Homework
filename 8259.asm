MOV AL, 11H			;ICW1标志，边沿触发，多片级联，需要输出ICW4
OUT 20H, AL			;向8259A的偶地址端口写入ICW1
MOV AL, 08H			;中断类型号08H
OUT 21H, AL			;向8259A的奇地址端口写入ICW2
MOV AL, 24H			;主片IR2、IR5引脚级联从片
OUT 21H, AL			;向8259A的奇地址端口写入ICW3
MOV AL, 01H			;完全嵌套，非缓冲，非自动结束，8086
OUT 21H, AL			;向8259A的奇地址端口写入ICW4


MOV AL, 11H			;ICW1标志，边沿触发，多片级联，需要输出ICW4
OUT A0H, AL		  ;向8259A的偶地址端口写入ICW1
MOV AL, 70H			;中断类型号70H
OUT A1H, AL		  ;向8259A的奇地址端口写入ICW2
MOV AL, 02H			;级联主片IR2引脚
OUT A1H, AL		  ;向8259A的奇地址端口写入ICW3
MOV AL, 01H			;完全嵌套，非缓冲，非自动结束，8086
OUT A1H, AL		  ;向8259A的奇地址端口写入ICW4


MOV AL, 11H			;ICW1标志，边沿触发，多片级联，需要输出ICW4
OUT C0H, AL		  ;向8259A的偶地址端口写入ICW1
MOV AL, 90H			;中断类型号90H
OUT C1H, AL		  ;向8259A的奇地址端口写入ICW2
MOV AL, 05H			;级联主片IR5引脚
OUT C1H, AL		  ;向8259A的奇地址端口写入ICW3
MOV AL, 01H			;完全嵌套，非缓冲，非自动结束，8086
OUT C1H, AL		  ;向8259A的奇地址端口写入ICW4
