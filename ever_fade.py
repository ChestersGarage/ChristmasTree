import opc, time, math, random

client = opc.Client('192.168.1.125:7890')

"""
colors = [
    ( 255, 0, 0 ),
    ( 255, 64, 0 ),
    ( 255, 255, 0 ),
    ( 127, 255, 0 ),
    ( 0, 255, 0 ),
    ( 0, 255, 127 ),
    ( 0, 255, 255 ),
    ( 0, 127, 255 ),
    ( 0, 0, 255 ),
    ( 127, 0, 255 ),
    ( 255, 0, 255 ),
    ( 255, 0, 64 )
]
# 12 colors
"""
colors = [
    ( 255, 0, 0 ),
    ( 0, 0, 255 ),
    ( 255, 192, 0 ),
    ( 127, 0, 127 ),
    ( 255, 92, 0 ),
    ( 0, 255, 0 )
]
# 6 colors

print('Starting LED Christmas tree scene: Ever-Fade.')

stringLength = 5
string = [ [0,0,0] ] * stringLength
client.put_pixels(string)
time.sleep(5)

while True:
    i = 0
    while i < stringLength:
        string[i] = colors[random.randrange(6)]
        while string[i] == string[i-1]:
            string[i] = colors[random.randrange(6)]
        i += 1

    client.put_pixels(string)
    time.sleep(5)
    client.put_pixels(string)
    time.sleep(5)
