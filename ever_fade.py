import opc, time, math, random

client = opc.Client('christmastree.home:7890')

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

stringLength = 265
ledString = [ [0,0,0] ] * stringLength
client.put_pixels(ledString)
time.sleep(5)

while True:
    for pixel in ledString:
        ledString[pixel] = colors[random.randrange(len(colors))]
        while ledString[pixel] == ledString[pixel-1]:
            ledString[pixel] = colors[random.randrange(len(colors))]

    client.put_pixels(ledString)
    time.sleep(5)
    client.put_pixels(ledString)
    time.sleep(5)
