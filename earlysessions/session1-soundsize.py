print ('this program works out the size in kilobytes of a CD quality sound sample')
duration = input('how long is your sound, in seconds?: ')
duration = int(duration)
bits = 16
channels = 2
frequency = 44100
size = frequency * bits * channels * duration
result = size / 1000
print(result)
