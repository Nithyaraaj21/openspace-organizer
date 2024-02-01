# OpenSpace Organizer

OpenSpace Organizer is a Python program that helps to organize seating arrangements in an open space environment. It allows you to define tables, assign seats randomly, and let you know if you need more tables to accommodate people.

## Features

- Create 6 tables with 4 seats each.
- Assign people to seats in a randomized manner.
- Display information about the seating arrangement and the sttistical info.
- Store the results in an Excel file for later reference.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Nithyaraaj21/openspace-organizer.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt ### Thanks to the Quiz session on python
    ```

## Usage

1. Prepare a list of colleagues in an Excel file named `colleagues.xlsx` via spreadsheet or via 'colleagues.py'
2. Run the main script: python main.py  
3. Booommmm "You have seating arrangement"
   
## Files and Directories

- `main.py`: The main script to run the OpenSpace Organizer.
- `src/`: Directory containing the source code.
  - `utils.py`: Utility functions for storing results.
  - `table.py`: Classes and functions related to tables and seats.
  - `openspace.py`: Functions for organizing the open space.

## Dependencies

- `pandas`: Data manipulation library.
- `openpyxl`: Library for reading and writing Excel files .
- 'zz': sss
## License

It's public "You are free to go"

## Acknowledgments

- Becode formation, tutorials, Tutors, and colleagues.
