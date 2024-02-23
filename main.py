import numpy as np

index = 0 # Index of Token

def match(char):
    global token
    global index

    if token[index] == char:
        index += 1
        return "Match! Advance Input"
    else:
        return f"Mismatch: {char} is not{token[index]} ! backtrack..."

buffer = [] # Buffer of input gramma
couter = 0  # Couter of gramma
while True:
    gramma = input("Input Gramma: ")
    if (gramma == 'exit'):
        break
    buffer.append(gramma)
    couter += 1
    # a,b = gramma.split('=',1)

main_gramma = [couter]
token = input("Input Token: ")

for i in range(couter):
    a,b = buffer[i].split('=',1)
    main_gramma.append(a)

    test = b.split("|")
    main_gramma.append(test)
del main_gramma[0]

print(f"\nGramma is:\n------------------\n")
for i in range(0,len(main_gramma),2):
    print(f"{main_gramma[i]} -> ",end="")
    for j in main_gramma[i+1]:
        print(f"{j} | ",end="")
    print('\n')

print("------------------")
#   ======================
# Main

print(f"\nToken Stream is: {token}\n")
for round in range(len(token)):
    print(f"------------------------------------")
    for index_gramma in range(1,len(main_gramma),2):
        for j in main_gramma[index_gramma]:
            for k in j:
                if index >= len(token):
                    print("End of input, accept")
                    exit()
                print(f"Gramma[{k}] Token is: {token[index-1]} Index is: [{index}]")
                print(f"Status: {match(k)}")
                print('\n')

print("End of input, reject")