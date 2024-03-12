#                      ~:~ CODECHEF-sweshikreddy ~:~
# --> Copying code? Ctrl+C might work, but karma will undo it. <--
# --> So Better understand my approach and write it on your own! <--

def min_operations(S):
    count = {}
    max_segment = 1
    operations = 0
    
    for char in S:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        
        if char == S[max_segment - 1]:
            max_segment += 1
        else:
            max_segment = 1
    
    for char, count in count.items():
        if count > 1:
            operations += (count - 1) * (max_segment - 1) + 1
    
    return operations

for _ in range(int(input())):
    # Fine here's my logic
    s = input()
    print(min_operations(s))