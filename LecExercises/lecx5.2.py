# function to frame string
def frame_string(string):
    a = len(string) + 6
    print('*'*a)
    print('*'*2,string,'*'*2)
    print('*'*a)
    
# execution
frame_string('Spanish Inquisition')
print()
frame_string('Ni')