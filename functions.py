num = int(input("Input the temperature: "))
conversion = input("Choose your conversion type. C for Celsius and F for Fahrenheit: ")
c_to_f = (num*9/5)+32
f_to_c = num-32*(5/9)
if conversion == 'c':
    print(num , "°Celcius = ", c_to_f,"F")
else:
    print(num , "°Fahrenheit = ", c_to_f,"C")



#write a function that converts C to F
