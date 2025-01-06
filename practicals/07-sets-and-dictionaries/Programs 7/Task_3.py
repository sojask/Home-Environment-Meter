import time

def countries_and_capitals():
    countries_capitals = {
        "england": "london",
        "wales": "cardiff",
        "japan":"tokyo",
        "russia": "moscow",
        "canada": "ottawa",
        "france": "paris",
        "germany": "berlin",
        "spain": "madrid",
        "italy": "rome"
    }

    while True:
        country = input("Enter a country (type 'done' to exit): ").lower()

        if country == 'done':
            break

        if country in countries_capitals:
            print(f"The capital city of {country} is {countries_capitals[country]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").lower()
            countries_capitals[country] = capital
            print(f"Thank you! The capital of {country} is now recorded as {capital}.")

countries_and_capitals()
