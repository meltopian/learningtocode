print ('this program works out the size of a bitmap image')
width = input('input width: ')
height = input('input height: ')
bits = input('input bits: ')
width = int(width)
height = int(height)
bits = int(bits)
pixels = width * height
size = pixels * bits
print(size)
