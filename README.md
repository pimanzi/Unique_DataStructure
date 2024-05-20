# Unique_DataStructure ✍️

## Description  
UniqueInt is a Python application that simplifies text file processing by extracting integers within a specified range, ensuring uniqueness, sorting them, and saving the results to a new file in the folder called sample_results. Integrated with an array data structure, it offers efficiency and accuracy. Users input the file path interactively, and UniqueInt seamlessly handles the data, organizing it into sample_results for output and sample_input for input files, ensuring effortless data management. Furthermore, Unique_DataStructure, in the first place, has some already files in sample_input and in sample_results; these are files that were used to test the application. Feel free to go through them and observe how the function filters to get unique integers in a result file.

## Features

- Reads integers from a specified file.
- Filters integers within the range of -1023 to 1023.
- Ensures all integers are unique.
- Sorts the integers in ascending order using the bubble sort algorithm.
- Saves the results to a new file in a designated output directory.
- Copies the input file to a designated directory for organized storage.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/pimanzi/Unique_DataStructure.git
    cd Unique_DataStructure
    ```

2. Ensure you have Python 3 installed. You can check this by running:

    ```
    python --version
    ```

## Usage

1. Navigate to the directory containing the `UniqueInt.py` script.

    ```
    cd Unique_DataStructure
    ```

2. Run the script:

    ```
    python3 UniqueInt.py
    ```

3. Follow the prompts in the command line:

    - **File Path**: Enter the full path to the file you wish to process. The file should contain integers, one per line.
    - **Quit**: Type `quit` to exit the application.

4. The application will:

    - Copy the input file to a directory named `sample_inputs`.
    - Create a unique, sorted list of integers within the range of -1023 to 1023 from the input file.
    - Write the results to a new file in a directory named `sample_results`. The result file will have the same name as the input file with `_results` appended.

## Example

1. You have a file `sample_01.txt` located at `/home/user/documents/sample_01.txt`.

2. Run the script and enter the file path:

    ```
    Type the ***path of your file*** or type ***quit*** to exit the program: /home/user/documents/sample_01.txt
    ```

3. The script processes the file, and the results are saved in `sample_results/sample_01.txt_results.txt`.

## Error Handling

- If the specified file does not exist, an error message will be displayed.
- If the file contains non-integer values or integers outside the specified range, they will be ignored.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

we are always happy to gain contributors to our projects. Feel free to suggest changes to  adopt or any feedback .

*Happy coding😇*

## Author
Imanzi Kabisa Placide 
