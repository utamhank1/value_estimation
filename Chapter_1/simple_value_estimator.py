import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Enter the size in sqft and the number of bedrooms of the house in "
                                                 "in question.")

    parser.add_argument("-s", "--size_in_sqft", type=int, help="Size of the house in square feet.")

    parser.add_argument("-b", "--number_of_bedrooms", type=int, help="number of bedrooms in the house.")

    arguments = parser.parse_args()

    size_in_sqft = arguments.size_in_sqft
    number_of_bedrooms = arguments.number_of_bedrooms

    return size_in_sqft, number_of_bedrooms


def estimate_home_value(size_in_sqft, number_of_bedrooms):
    # Baseline home price = 50,000.
    value = 50000

    # Adjust value of house based on the size of the house.
    value = value + (size_in_sqft * 92)

    # Adjust value of the house based on the number of bedrooms.
    value = value + (number_of_bedrooms * 10000)

    return value


def main(size_in_sqft, number_of_bedrooms):
    print(f"size_in_sqft: {size_in_sqft}, number_of_bedrooms: {number_of_bedrooms}, "
          f"home value: {estimate_home_value(size_in_sqft, number_of_bedrooms)}")


if __name__ == "__main__":
    args = parse_arguments()
    main(*args)
