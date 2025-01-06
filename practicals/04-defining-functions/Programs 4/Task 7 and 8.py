temperatures = []

while True:
    user_input = input(f"Enter a temperature: ")
    if user_input == "":
        break
    try:
        temp = float(user_input)
        temperatures.append(temp)
    except ValueError:
        print("Please enter a valid number.")

if len(temperatures) > 0:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print("Maximum temperature:", max_temp, "°C")
    print("Minimum temperature:", min_temp, "°C")
    print("Mean temperature:", mean_temp, "°C")

else:
    print("No temperatures entered.")
