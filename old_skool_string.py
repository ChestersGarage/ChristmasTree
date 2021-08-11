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

stringLength = 5
string = [ [0,0,0] ] * stringLength
client.put_pixels(string)
time.sleep(5)

while True:
    i = 0
    while i < stringLength:
        string[i] = colors[random.randrange(7)]
        while string[i] == string[i-1]:
            string[i] = colors[random.randrange(7)]
        i += 1

    client.put_pixels(string)
    time.sleep(3)
    client.put_pixels(string)
    time.sleep(3)
