# Unique_DataStructure ✍️

## Description
UniqueInt is a Python application that processes a user-specified text file, extracts integers within a specified range, ensures their uniqueness, sorts them, and writes the results to a new file. The application also moves the input file to a designated directory for easy management.

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
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Ensure you have Python 3 installed. You can check this by running:

    ```sh
    python --version
    ```

## Usage

1. Navigate to the directory containing the `UniqueInt.py` script.

    ```sh
    cd <repository_directory>
    ```

2. Run the script:

    ```sh
    python UniqueInt.py
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

    ```sh
    Type the ***path of your file*** or type ***quit*** to exit the program: /home/user/documents/sample_01.txt
    ```

3. The script processes the file, and the results are saved in `sample_results/sample_01.txt_results.txt`.

## Error Handling

- If the specified file does not exist, an error message will be displayed.
- If the file contains non-integer values or integers outside the specified range, they will be ignored.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

