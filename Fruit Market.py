name = input("Welcome to GC Fruit Market! What is your name?")
apple, orange, grape = 0, 0, 0

fruit_start = input("Welcome" + name + ". Which fruit would you like to buy? "
                                       "\n1. Apples $2 "
                                       "\n2. Grape $1 "
                                       "\n3. Orange $3")
if fruit_start == '1':
    apple += 1
elif fruit_start == '2':
    grape += 1
elif fruit_start == '3':
    orange += 1
while input("Would you like to buy another fruit? y/n") != 'n':
    fruit_start = input("Welcome" + name + ". Which fruit would you like to buy? "
                                           "\n1. Apples $2 "
                                           "\n2. Grape $1 "
                                           "\n3. Orange $3")
    if fruit_start == '1':
        apple += 1
    elif fruit_start == '2':
        grape += 1
    elif fruit_start == '3':
        orange += 1

subtotal = (apple * 2) + grape + (orange * 3)
print(f"Order for Grand Chirpus\n"
      f"{str(apple)} apple(s) at $2 a piece\n"
      f"{str(grape)} grape(s) at $1 a piece\n"
      f"{str(orange)} orange(s) at $3 a piece\n"
      f"Sub Total: ${str(subtotal)}"
      f"5% Tax: {str(round(subtotal * 0.05,3))}\n"
      f"Total: {str(round(subtotal * 1.05,3))}")


