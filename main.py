'''
จัดทำโดย
    นาย กิตติกานต์ มากผล 6410450087
    นาย นิสิต นะมิตร 6410451148
    นาย พีรสิษฐ์ พลอยอร่าม 6410451237
    นาย ศิวกร ภาสว่าง 6410451423
    ข้อ 1
'''

index = 0 # Index of Token

def match(char):
    global token
    global index

    if token[index] == char:
        index += 1                      # Move Pointer
        return "Match! Advance Input"
    else:
        return f"Mismatch: {char} is not{token[index]} ! backtrack..."


buffer = [] # Buffer of input gramma
couter = 0  # Couter of gramma

while True:
    gramma = input("Input Gramma: ")
    if (gramma == 'exit'):
        break
    buffer.append(gramma)       # Add to Buffer
    couter += 1                 # Count

main_gramma = [couter]          # Init Main Buffer Gramma
token = input("Input Token: ")

for i in range(couter):
    a,b = buffer[i].split('=',1)        # Split Header and Gramma e -> t | t+e
    main_gramma.append(a)

    gramma_split = b.split("|")
    main_gramma.append(gramma_split)    # t | t+e
del main_gramma[0]                      # Delete Counter

print(f"\nGramma is:\n------------------\n")    # Print Gramma
for i in range(0,len(main_gramma),2):
    print(f"{main_gramma[i]} -> ",end="")
    for j in main_gramma[i+1]:
        print(f"{j} | ",end="")
    print('\n')

print("------------------")

#   ======================
#   Main
print(f"\nToken Stream is: {token}\n")
for round in range(len(token)):
    print(f"------------------------------------")
    for index_gramma in range(1,len(main_gramma),2):    # Index Loc Gramma
        for j in main_gramma[index_gramma]:             # Gramma
            for k in j:                                 # Each Gramma
                if index >= len(token):                 # If Accept
                    print("End of input, accept")
                    exit()

                print(f"Gramma[{k}] Token is: {token[index-1]} Index is: [{index}]")
                print(f"Status: {match(k)}\n")
                                                        # Reject
print("End of input, reject")