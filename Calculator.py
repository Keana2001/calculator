def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter a number: "))
                num2 = float(input("Enter a number: "))

                if choice == '1':
                    print(f"Answer: {num1 + num2}")
                elif choice == '2':
                    print(f"Answer: {num1 - num2}")
                elif choice == '3':
                    print(f"Answer: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Cannot divide by zero.")
                    else:
                        print(f"Answer: {num1 / num2}")
            except ValueError:
                print("That number does not exist. Choose a valid number")
        else:
            print("That is not an option. Please select from 1 to 5.")


def trip_cost_estimator():
    print("\nTrip Cost Estimator")
    try:
        cost_of_airfare = float(input("What is the cost of the airfare: "))
        cost_of_hotel_nights = int(input("Number of nights in hotel: "))
        nightly_hotel_cost = float(input("Cost of nightly stays in hotel: "))
        rental_car_days = int(input("Number of car rental days: "))
        daily_car_rental_cost = float(input("Cost of rental car per day: "))

        tax_rate = 0.1
        hotel_tax_rate = 0.05

        total_airfare_cost = cost_of_airfare + (cost_of_airfare * tax_rate)
        total_hotel_cost = (cost_of_hotel_nights * nightly_hotel_cost) + ((cost_of_hotel_nights * nightly_hotel_cost) * hotel_tax_rate)
        total_car_rental_cost = rental_car_days * daily_car_rental_cost
        total_trip_cost = total_airfare_cost + total_hotel_cost + total_car_rental_cost

        print("The total cost of your trip is: R", format(total_trip_cost, '.2f'))

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


def main():
    while True:
        print("\nMain Menu")
        print("1. Calculator")
        print("2. Trip Cost Estimator")
        print("3. Exit")

        main_choice = input("Select an option (1-3): ")

        if main_choice == '1':
            calculator()
        elif main_choice == '2':
            trip_cost_estimator()
        elif main_choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
