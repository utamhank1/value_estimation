import pandas as pd
import webbrowser
import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Enter the path of the .csv file that you wish to read in and upload"
                                                 "to a web page")

    parser.add_argument("-f", "--file", type=str, help="Path to the directory containing the .csv file that you wish"
                                                       "to read in and upload to a webpage.")

    arguments = parser.parse_args()
    file = arguments.file

    return file


def main(file):
    print("Hello, World: You are running file view_data.py")

    # Read the ml_house_data_set into a pandas data table.
    ml_house_data_set = pd.read_csv(file)

    # Create the data into a web page for easy viewing.
    html = ml_house_data_set[0:100].to_html()

    # Save the web html to a temporary file.
    with open("data.html", "w") as f:
        f.write(html)

    # Open the web page in our browser.
    full_filename = os.path.abspath("data.html")
    webbrowser.open(f"file://{full_filename}")


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
