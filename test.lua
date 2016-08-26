uart.alt(1)
uart.setup(0,19200,8, uart.PARITY_NONE, uart.STOPBITS_1, 0)
--printer init command
uart.write(0, 27)
uart.write(0, 64)
--printer wake command
uart.write(0,27)
uart.write(0,61)
uart.write(0,1)
--printer print density = 15 and break time = 15
--n= density<<4 | time = 255
uart.write(0, 18)
uart.write(0, 35)
uart.write(0, 255)

uart.write(0, 10)
uart.write(0, 10)
uart.write(0, 10)
uart.write(0, "Hola Mundo!")
