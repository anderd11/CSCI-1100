# function to calculate conversion
def convert2fahren(temp):
    fahr = (9/5)* temp + 32
    return fahr
    
# execution
print("0 ->",convert2fahren(0))
print("32 ->",convert2fahren(32))
print("100 ->",convert2fahren(100))