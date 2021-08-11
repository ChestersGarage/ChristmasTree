import opc, time, math, random

client = opc.Client('christmastree.home:7890')

# 4700K, "White" and 9800K
colors = [
    ( 255, 223, 194 ),
    ( 226, 226, 226 ),
    ( 206, 220, 255 )
    ]

print('Starting LED Christmas tree scene: Tree Star.')

totalPixels = 265
frameRate = 1 / 60
ledString = [ [0,0,0] ] * totalPixels
client.put_pixels(ledString)
time.sleep(frameRate)

print('Servicing ' + str(totalPixels) + ' LED pixels.')

numPixToChange = int(totalPixels / 5)
if numPixToChange <= 1:
    numPixToChange = 1
else:
    numPixToChange = random.randrange(numPixToChange * 2)

while True:
    p = 0
    while p < numPixToChange:
        brightness = random.randrange(20, 30) / 100.0
        hue = colors[random.randrange(len(colors))]
        ledString[random.randrange(totalPixels)] = [ hue[0] * brightness, hue[1] * brightness, hue[2] * brightness ]
        p += 1

    client.put_pixels(ledString)
    time.sleep(frameRate)
