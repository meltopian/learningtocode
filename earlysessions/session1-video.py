print ('this program works out the size in kilobytes of an uncompressed video')
width = input('input width: ')
height = input('input height: ')
bits = input('what is the bit depth?: ')
frames = input('what is the fps?: ')
duration = input('how long is it in seconds?: ')
width = int(width)
height = int(height)
bits = int(bits)
frames = int(frames)
duration = int(duration)

pixels = width * height

size = pixels * bits * frames * duration
finalresult = size / 1000
print(finalresult)