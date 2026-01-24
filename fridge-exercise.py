# The Fridge

"""
Get the user to enter a temperature in celsius

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"

"""

temperature = float(input("Enter a temperature in celsius: "))

STATUS_BROKEN = "Fridge is broken"
STATUS_OK = "Fridge OK"
STATUS_COLD = "Fridge too cold"
STATUS_WARM = "Fridge too warm"

status = STATUS_BROKEN

if temperature < 0:
    status = STATUS_COLD
elif temperature < 4:
    status = STATUS_OK
elif temperature <=6:
    status = STATUS_WARM
# else:
#     status = STATUS_BROKEN

print(status)
print("Program finished")
