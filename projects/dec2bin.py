#    Function Dec2Bin(ByVal denary as Integer) As String
#        Dim output As String = ""
#        While denary > 0
#            Const remainder As Integer = denary Mod 2
#            output = remainder & output
#            denary = (denary - remainder) / 2
#        End While
#        Dec2Bin = output
#    End Function

#Part 1.0 - denary to binary
#Part 1.5 - add doctests (write doctests that capture errors)
#Part 2.0 - binary to denary
#Part 3.0 - try crazy nubers, decimal numbers, etc.
def Dec2Bin(denary):
  output = ""
  while denary > 0:
    remainder = denary % 2
    output = str(remainder) + output
    denary = int((denary - remainder) / 2)
  return output
  
thenumber = int(input('enter a number to convert: '))
print(f"Binary value = {Dec2Bin(thenumber)}")