import opc, time, math, random

client = opc.Client('christmastree.home:7890')

colors = [
    ( 255,   0,   0 ),
    (   0, 255,   0 ),
    (   0,   0, 255 ),
    ( 192, 128,   0 ),
    ( 192,   0, 192 ),
    ( 192,   0, 192 )
]
# 6 colors

print('Starting LED Christmas tree scene: Ever-Fade.')

stringLength = 200
fadeTime = 5
ledString = [ [0,0,0] ] * stringLength

while True:
    while p < stringLength:
        ledString[p] = colors[random.randrange(len(colors))]
        while ledString[p] == ledString[p-1]:
            ledString[p] = colors[random.randrange(len(colors))]

    client.put_pixels(ledString,0)
    time.sleep(fadeTime)
