import segno 
import segno.helpers

#QR para texto
holamundo = segno.make("Hola mundo")

holamundo.save("hola.png", scale=10)

#QR para wifi
wifi = segno.helpers.make_wifi(ssid='Megacable-6500', password='xxxx', security='WPA', hidden=False)
wifi.save("Wifi.png", scale=50)

#QR para coordenadas
coors = segno.helpers.make_geo(lat='xxxx', lng='xxxx')
coors.save("Coordenadas.png", scale=50)

