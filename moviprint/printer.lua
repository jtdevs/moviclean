print("Se cambiara a comuniacion con la impresora, adios!")
zero = 0
--printer connection setup
-- Rx -> GPIO13 -> D7
-- Tx -> GPIO15 -> D8
tmr.delay(500)
uart.alt(1)
tmr.delay(500)
-- printer baudrate: 19200 according to datasheet
uart.setup(0, 19200, 8, uart.PARITY_NONE, uart.STOPBITS_1, 0)
tmr.delay(500)
--printer init command
uart.write(0, 27)
uart.write(0, 64)
--printer wake command
uart.write(0, 27)
uart.write(0, 61)
uart.write(0, 1)
--printer print density = 15 and break time = 15
--n= density<<4 | time = 255
uart.write(0, 18)
uart.write(0, 35)
uart.write(0, 255)

uart.write(0, "READY TO PRINT!")
uart.write(0, 10)
uart.write(0, 10)
uart.write(0, 10)
tmr.delay(500)
--1 minute timeout on TCP_Server
TCP_Server=net.createServer(net.TCP, 60)
-- TCP_port 40 -> unassigned according to: en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
TCP_Server:listen(40, function(TCP_Port)
	TCP_Port:on("receive", function(socket,incoming)
		if incoming == "mayus\n" or incoming == "mayus" then
			uart.write(0, 29)
			uart.write(0, 33)
			uart.write(0, 255)
			--uart.write(0, "Changed to mayus")
		elseif incoming == "minus\n" or incoming == "minus" then
			uart.write(0, 29)
			uart.write(0, 33)
			uart.write(0, zero)
			--uart.write(0, "Changed to minus")
		elseif incoming == "lf\n" or incoming == "lf" then
			uart.write(0, 10)
			--uart.write(0, "linefeed")
		else
			uart.write(0, incoming)
		end
	end)
end)
