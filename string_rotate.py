def rotate(s,val):
    if s.islower():
        start = ord('a')
        end = ord('z')
    else :
        start = ord('A')
        end = ord('Z')
    
    return chr((ord(s)+val) % end + (int((ord(s)+val)/end) * start))

def encode(s,val):
    new_string_list = [rotate(s[i],val) if s[i].islower() else rotate(s[i],val) for i in range(len(s))]
    string = ""
    for i in new_string_list:
        string+=i
    return string