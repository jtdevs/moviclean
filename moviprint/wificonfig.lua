print("Bienvenido a Moviprint")
print("V0.1")
print("Configurando red WiFi oculta")

--wifi connection setup
wifi.setmode(wifi.SOFTAP)
wifi.setphymode(wifi.PHYMODE_G)
wifi.sleeptype(wifi.NONE_SLEEP)
cfg={}
cfg.ssid="movipad_printer"
cfg.pwd="movicleanchile"
cfg.channel = 6
cfg.hidden = 1
cfg.max = 1
wifi.ap.config(cfg)
cfd ={}
cfd.ip="192.168.2.1"
cfd.netmask="255.255.255.0"
cfd.gateway="192.168.2.1"
wifi.ap.setip(cfd)

print("Red configurada exitosamente. Los parametros son:")
print("ssid=movipad_printer")
print("pswd=movicleanchile")
print("channel=6")
print("ip=192.168.2.1")
print("nm=255.255.255.0")
print("gw=192.168.2.1")
print("Se abrira un servidor TCP en el puerto 40 en 5 segundos.")
tmr.alarm(0, 5000, 0, function() dofile("printer.lc") end)
