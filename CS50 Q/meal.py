def main():
    time_input = input("Enter the time in 24-hour format: ")
    time = convert(time_input)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time_input):
    hours, minutes = map(int, time_input.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()
