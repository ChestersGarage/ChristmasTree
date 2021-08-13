class Star:
    def __init__:
        # 4700K, "White" and 9800K
        self.colors = [
            ( 255, 223, 194 ),
            ( 240, 240, 240 ),
            ( 206, 220, 255 )
            ]
        self.totalPixels = 65
        self.frameRate = 1 / 10
        self.ledString = [ [0,0,0] ] * totalPixels
        self.startMsg = 'Servicing ' + str(totalPixels) + ' LED pixels.'

    def __main__():
        numPixToChange = int(totalPixels / 5)
        if numPixToChange <= 1:
            numPixToChange = 1
        else:
            numPixToChange = random.randrange(numPixToChange * 2)

        p = 0
        while p < numPixToChange:
            brightness = random.randrange(60,80) / 100.0
            hue = colors[random.randrange(len(colors))]
            ledString[random.randrange(totalPixels)] = [ hue[0] * brightness, hue[1] * brightness, hue[2] * brightness ]
            p += 1

        #client.put_pixels(ledString,2)
        return ledString
