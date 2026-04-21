Sign = input("Enter sign (=+/=-/=*/=/):")

num_1 = float(input("ENTER FIRST NUMBER:"))
num_2 = float(input("ENTER SECOND NUMBER:"))

if Sign == '1':
    Result = num_1 + num_2
    print(f"Answer: {Result}")
elif Sign == '2':
    Result = num_1 - num_2
    print(f"Answer: {Result}")
elif Sign == '3':
    Result = num_1 * num_2
    print(f"Answer: {Result}")
elif Sign == '4':
    Result = num_1 / num_2
    print(f"Answer: {Result}")
else:
    print(f"error")