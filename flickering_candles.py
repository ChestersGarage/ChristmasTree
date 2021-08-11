import opc, time, math, os, random

client = opc.Client('christmastree.home:7890')

candleMap = [
    (  99, 14, 0 ),
    ( 100, 15, 0 ),
    ( 101, 16, 0 ),
    ( 102, 16, 0 ),
    ( 103, 17, 0 ),
    ( 104, 18, 0 ),
    ( 105, 19, 0 ),
    ( 106, 20, 0 ),
    ( 107, 21, 0 ),
    ( 108, 22, 0 ),
    ( 109, 23, 0 ),
    ( 110, 24, 0 ),
    ( 111, 24, 0 ),
    ( 112, 25, 0 ),
    ( 113, 26, 0 ),
    ( 114, 27, 0 ),
    ( 115, 28, 0 ),
    ( 116, 29, 0 ),
    ( 117, 29, 0 ),
    ( 118, 30, 0 ),
    ( 119, 31, 0 ),
    ( 120, 32, 0 ),
    ( 121, 33, 0 ),
    ( 122, 34, 0 ),
    ( 123, 34, 0 ),
    ( 124, 35, 0 ),
    ( 125, 36, 0 ),
    ( 126, 37, 0 ),
    ( 127, 38, 0 ),
    ( 128, 38, 0 ),
    ( 129, 39, 0 ),
    ( 130, 39, 0 ),
    ( 131, 40, 0 ),
    ( 132, 41, 0 ),
    ( 133, 42, 0 ),
    ( 134, 43, 0 ),
    ( 135, 44, 0 ),
    ( 136, 44, 0 ),
    ( 137, 45, 0 ),
    ( 138, 46, 0 ),
    ( 139, 47, 0 ),
    ( 140, 48, 0 ),
    ( 141, 49, 0 ),
    ( 142, 49, 0 ),
    ( 143, 50, 0 ),
    ( 144, 51, 0 ),
    ( 145, 52, 0 ),
    ( 146, 53, 0 ),
    ( 147, 53, 0 ),
    ( 148, 54, 0 ),
    ( 149, 55, 0 ),
    ( 150, 56, 0 ),
    ( 151, 57, 0 ),
    ( 152, 57, 0 ),
    ( 153, 58, 0 ),
    ( 154, 58, 0 ),
    ( 155, 59, 0 ),
    ( 156, 59, 0 ),
    ( 157, 60, 0 ),
    ( 158, 60, 0 ),
    ( 159, 61, 0 ),
    ( 160, 61, 0 ),
    ( 161, 62, 0 ),
    ( 162, 63, 0 ),
    ( 163, 63, 0 ),
    ( 164, 64, 0 ),
    ( 165, 64, 0 ),
    ( 166, 65, 0 ),
    ( 167, 66, 0 ),
    ( 168, 66, 0 ),
    ( 169, 67, 0 ),
    ( 170, 67, 0 ),
    ( 171, 68, 0 ),
    ( 172, 68, 0 ),
    ( 173, 69, 0 ),
    ( 174, 69, 0 ),
    ( 175, 70, 0 ),
    ( 176, 71, 0 ),
    ( 177, 72, 0 ),
    ( 178, 73, 0 ),
    ( 179, 74, 0 ),
    ( 180, 75, 0 ),
    ( 181, 76, 0 ),
    ( 182, 77, 0 ),
    ( 183, 78, 0 ),
    ( 184, 78, 0 ),
    ( 185, 79, 0 ),
    ( 186, 79, 0 ),
    ( 187, 80, 0 ),
    ( 188, 80, 0 ),
    ( 189, 81, 0 ),
    ( 190, 81, 0 ),
    ( 191, 82, 0 ),
    ( 192, 82, 0 ),
    ( 193, 83, 0 ),
    ( 194, 83, 0 ),
    ( 195, 84, 0 ),
    ( 196, 84, 0 ),
    ( 197, 85, 0 ),
    ( 198, 85, 0 ),
    ( 199, 86, 0 ),
    ( 200, 87, 0 ),
    ( 201, 88, 0 ),
    ( 202, 89, 0 ),
    ( 203, 90, 0 ),
    ( 204, 91, 0 ),
    ( 205, 92, 0 ),
    ( 206, 93, 0 ),
    ( 207, 93, 0 ),
    ( 208, 94, 0 ),
    ( 209, 94, 0 ),
    ( 210, 95, 0 ),
    ( 211, 95, 0 ),
    ( 212, 96, 0 ),
    ( 213, 97, 0 ),
    ( 214, 98, 0 ),
    ( 215, 99, 0 ),
    ( 216, 99, 0 ),
    ( 217, 100, 0 ),
    ( 218, 100, 0 ),
    ( 219, 101, 1 ),
    ( 220, 101, 1 ),
    ( 221, 102, 1 ),
    ( 222, 102, 1 ),
    ( 223, 103, 1 ),
    ( 224, 104, 1 ),
    ( 225, 105, 1 ),
    ( 226, 106, 1 ),
    ( 227, 107, 1 ),
    ( 228, 108, 1 ),
    ( 229, 109, 1 ),
    ( 230, 109, 1 ),
    ( 231, 110, 1 ),
    ( 232, 110, 1 ),
    ( 233, 111, 1 ),
    ( 234, 112, 1 ),
    ( 235, 112, 1 ),
    ( 236, 113, 1 ),
    ( 237, 114, 1 ),
    ( 238, 114, 1 ),
    ( 239, 115, 1 ),
    ( 240, 116, 1 ),
    ( 241, 116, 1 ),
    ( 242, 117, 1 ),
    ( 243, 118, 1 ),
    ( 244, 119, 1 ),
    ( 245, 119, 1 ),
    ( 246, 120, 1 ),
    ( 247, 121, 1 ),
    ( 248, 121, 1 ),
    ( 249, 122, 1 ),
    ( 250, 123, 1 ),
    ( 251, 123, 1 ),
    ( 252, 124, 1 ),
    ( 253, 125, 1 ),
    ( 254, 125, 1 ),
    ( 255, 126, 1 )
]
# 157 steps

print('Starting LED Christmas tree scene: Flickering Candles.')

# Total addressable LEDs
stringLength = 265
# Set all LEDs to off
ledString = [ [0,0,0] ] * stringLength
sequenceCounter = [0] * stringLength

def burn_sine(steps, flicker, brightness):
    """
    Create one full sine wave within the number of steps provided, and return a pattern of brightness values.

    Flicker - how bright and dim the flicker gets (Range: 0 thru int(157/2), from candleMap)
    Brightness - average brightness, (Range: bandWidth thru (157-bandWidth).n, from candleMap)
    """

    i = 0
    burnSequence = []
    while i < steps:
        # Pre-calculate the sine wave values
        burnSequence.append(int((flicker*math.sin(i*(math.pi*2)/steps))+brightness))
        i += 1

    return burnSequence

def makePixelSequence(type=''):
    if type == "bounce":
        pixelSequence = []
        steps = random.randrange(5,10)
        flicker = 10
        brightness = 106 # Centered on 50 flicker
        # Ramp up the flicker intensity
        while flicker < 50:
            pixelSequence.extend(burn_sine(steps, flicker, brightness))
            flicker = flicker * 1.1
            if flicker > 50:
                flicker = 50

        # Sustain the intense flick for a moment
        iters = 0
        maxIters = random.randrange(30)
        while iters < maxIters:
            pixelSequence.extend(burn_sine(steps, flicker, brightness))
            iters += 1

        # ramp down the flicker intensity
        while flicker > 8:
            pixelSequence.extend(burn_sine(steps, flicker, brightness))
            flicker = flicker * .95

    else:
        steps = random.randrange(50,400)
        flicker = random.randrange(30,50)
        brightness = 106 # Centered on 50 flicker
        sequenceIterations = random.randrange(1,4)
        pixelSequence = burn_sine(steps, flicker, brightness) * sequenceIterations

    return pixelSequence

def doNextSequence():
    jump = random.randrange(10)
    if jump == 3:
        nextSequence = makePixelSequence('bounce')
    else:
        nextSequence = makePixelSequence()
    return nextSequence

def makeStringSequence():
    stringSequence = []
    for pixel in ledString:
        pixelSequence = makePixelSequence()
        stringSequence.append(pixelSequence)
    return stringSequence

def run_sequence(stringSequence):
    """
    Runs through a sequence once.
    """
    for index,pixel in enumerate(ledString):
        ledString[index] = [
                                  candleMap[ stringSequence[index][ sequenceCounter[index] ] ][0],
                                  candleMap[ stringSequence[index][ sequenceCounter[index] ] ][1],
                                  candleMap[ stringSequence[index][ sequenceCounter[index] ] ][2]
                                ]
        sequenceCounter[index] += 1
        if sequenceCounter[index] == len(stringSequence[index]):
            stringSequence[index] = doNextSequence()
            sequenceCounter[index] = 0

    client.put_pixels(ledString,0)
    # Sleep value = 1/FPS, i.e. 1/50 = .02
    time.sleep(1/30)

# Do it
stringSequence = makeStringSequence()
while True:
    run_sequence(stringSequence)
