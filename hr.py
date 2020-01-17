'''Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.'''

if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        cmd, *args = input().split()
        if cmd == 'insert':
            l.insert(int(args[0]), int(args[1]))
        elif len(args) == 1:
            eval("l." + cmd + "(" + args[0] + ")")
        elif not args:
            if cmd == 'print':
                print(l)
            else:
                eval("l." + cmd + "(" + ")")
