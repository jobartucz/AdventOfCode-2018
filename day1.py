with open('day1.txt') as my_file:
    content = my_file.readlines()

# content = [+3, +3, +4, -2, -4]

val = 0
found = {}
done = False

while done == False:
    found['0'] = 1
    for i in content:
        val += int(i)
        # print(val)
        if (str(val) in found):
            print(val)
            done = True
            break
        else:
            found[str(val)] = 1

print("done")