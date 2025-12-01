to_print = ""
for x in range(1500,2701) :
    if x%5 == 0 and x%7 == 0 :
        to_print += f"{x},"
print(to_print[:-1])