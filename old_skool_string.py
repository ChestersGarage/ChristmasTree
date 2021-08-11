import opc, time, math, random

client = opc.Client('christmastree.home:7890')

# Red, blu, yel, cyn, mag, wht, grn
colors = [
    ( 255,   0,   0 ),
    (   0,   0, 255 ),
    ( 255, 255,   0 ),
    (   0, 255, 255 ),
    ( 255,   0, 255 ),
    ( 255, 255, 255 ),
    (   0, 255,   0 )
]

print('Starting LED Christmas tree scene: Old Skool String.')

timeIncrement = 1
holdTime = 10
stringLength = 265
ledString = [ [0,0,0] ] * stringLength

while True:
    i = 0
    while i < stringLength:
        ledString[i] = colors[random.randrange(len(colors))]
        while ledString[i] == ledString[i-1]:
            ledString[i] = colors[random.randrange(len(colors))]
        i += 1
    d = 0
    while d <= holdTime:
        client.put_pixels(ledString)
        time.sleep(timeIncrement)
        d += timeIncrement
