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

delayTime = 10
stringLength = 265
string = [ [0,0,0] ] * stringLength
client.put_pixels(string)
time.sleep(delayTime)

while True:
    i = 0
    while i < stringLength:
        string[i] = colors[random.randrange(len(colors))]
        while string[i] == string[i-1]:
            string[i] = colors[random.randrange(len(colors))]
        i += 1

    client.put_pixels(string)
    time.sleep(delayTime)
    client.put_pixels(string)
    time.sleep(delayTime)
