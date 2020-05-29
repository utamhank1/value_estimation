import joblib


def main():
    print("Hello, World, you are running make_predictions.py")

    # Import the previously trained model.
    model = joblib.load("trained_house_classifier_model.pkl")

    # House to valuate.
    # House features
    house_to_valuate = [
        1973,  # year_built
        1,  # stories
        4,  # num_bedrooms
        3,  # full_bathrooms
        0,  # half_bathrooms
        2200,  # livable_sqft
        2350,  # total_sqft
        400,  # garage_sqft
        0,  # carport_sqft
        True,  # has_fireplace
        False,  # has_pool
        True,  # has_central_heating
        True,  # has_central_cooling

        # Garage type: Choose only one
        1,  # attached
        0,  # detached
        0,  # none

        # City: Choose only one
        1,  # Amystad
        0,  # Brownport
        0,  # Chadstad
        0,  # Clarkberg
        0,  # Coletown
        0,  # Davidfort
        0,  # Davidtown
        0,  # East Amychester
        0,  # East Janiceville
        0,  # East Justin
        0,  # East Lucas
        0,  # Fosterberg
        0,  # Hallfort
        0,  # Jeffreyhaven
        0,  # Jenniferberg
        0,  # Joshuafurt
        0,  # Julieberg
        0,  # Justinport
        0,  # Lake Carolyn
        0,  # Lake Christinaport
        0,  # Lake Dariusborough
        0,  # Lake Jack
        0,  # Lake Jennifer
        0,  # Leahview
        0,  # Lewishaven
        0,  # Martinezfort
        0,  # Morrisport
        0,  # New Michele
        0,  # New Robinton
        0,  # North Erinville
        0,  # Port Adamtown
        0,  # Port Andrealand
        0,  # Port Daniel
        0,  # Port Jonathanborough
        0,  # Richardport
        0,  # Rickytown
        0,  # Scottberg
        0,  # South Anthony
        0,  # South Stevenfurt
        0,  # Toddshire
        0,  # Wendybury
        0,  # West Ann
        0,  # West Brittanyview
        0,  # West Gerald
        0,  # West Gregoryview
        0,  # West Lydia
        0,  # West Terrence

    ]


# Create an array to store the house_to_valuate variable.
    homes_to_value = [house_to_valuate]

    # Run the model and make a prediction as to the value of the house.
    predicted_home_values = model.predict(homes_to_value)

    # Examine the predicted value.
    predicted_value = predicted_home_values[0]

    print(f"This house has a predicted home value of ${predicted_value}")


if __name__ == "__main__":
    main()
