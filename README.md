# Autobahn

Author: Katerina Karagiannaki

E-mail: kat.karayan@gmail.com

## Table of Contents
1. [Description](#description)
2. [Deliverables](#deliverables)
5. [Installation and Usage](#installation)

## Description <a name="description"></a>
Autobahn is a Python application that retrieves cryptocurrency data using the AlphaVantage API.
It performs the following:
- Retrieves historical daily cryptocurrency data using a request to the API
- Stores data into a csv file
- Computes the average price of each week and stores it on a CSV file.
- Computes the week that had the greatest relative span on closing prices
and prints this on screen.


## Deliverables <a name="deliverables"></a>
The autobahn project directory contains the following files
- autobahn/
  *  README.md 
  *  Data.py - class that performs data transformations and I/O operations
  *  Calculations.py - class that performs calculations on data
  *  main.py - the main file of the project that executes the procedure
  *  files/ - directory where the files are stored and loaded



## Installation & Usage <a name="installation"></a>
### How to run source
Autobahn can be executed either as a script or though an IDE.
(In all cases you need to have a python 2.7 installation.)

1. To execute as a script:
- Open a terminal window
- Navigate into the project directory where the source files are located
    ```sh
    $ cd location-of-the-files-in-your-computer/autobahn
    ```
- Execute the following command
    ```sh
    $ python main.py
    ```

2. To execute through an IDE (Recommended: Pycharm)
Open Pycharm IDE, and import project by clicking on File -> Open -> Navigate to the stackstats source files.