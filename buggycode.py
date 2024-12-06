"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def tract_and_rearrange(string): #FUNCTION WAS NOT DEFINED and spellimg mistakes
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize() 
    str_2 = "".join(string[6:13].split('ro')) #spelling mistake on split
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17])) 
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " +str_4 #the plus sign was missing

def ultra_extrct_and_rearrange(string): #missing colon after defining the function 
    first_transform = tract_and_rearrange(string)
    return first_transform
print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv")) #unneeded quotation and spelling

