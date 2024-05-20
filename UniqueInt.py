import os
import shutil  # for copying the file to another specific path
"""Script of Uniquelnt.py which allows a user to input any file present on his system and the there will be returned the result file containing only integers which are unique in  a folder called sample_results """


class UniqueInt:
    """This is the base class for the whole application"""

    def __init__(self, file_path):
        """constructor function"""
        self.result_list = []
        self.full_path = file_path
        self.file_path = os.path.basename(file_path)
        self.file_name = os.path.join(
            "sample_inputs", os.path.basename(file_path))

    def read_file(self):
        """reads and process an input file and directly insert it in sample_inputs folder"""
        inprocess_list = []
        if os.path.exists(self.full_path):
            os.makedirs("sample_inputs", exist_ok=True)
            shutil.copy(self.full_path, self.file_name)
            try:
                with open(self.file_name, "r", errors='ignore') as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                        elif any(component == "" for component in line.split()):
                            continue
                        else:
                            try:
                                number = int(line)
                                if -1023 <= number <= 1023:
                                    inprocess_list.append(number)
                            except ValueError:
                                continue
            except Exception as e:
                print(f"There was an error in reading file {self.full_path}: {e}")

        else:
            print("\n --------------------\n***{}*** file path is not found.Please check well the file path you provided\n--------------------\n".format(self.full_path))

        return inprocess_list

    def unique_maker(self):
        """Making our results to have unique contents"""
        new_list = self.read_file()
        for value in new_list:
            if value not in self.result_list:
                self.result_list.append(value)
            else:
                continue

    def sort_list(self):
        """Using bubble algorthim to sort the contents in the result_file"""
        n = len(self.result_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.result_list[j] > self.result_list[j+1]:
                    self.result_list[j], self.result_list[j +
                                                          1] = self.result_list[j+1], self.result_list[j]

    def output_file(self):
        """Outputs the contents into a file having a name corresponding to an input file in sample_results directory"""

        if len(self.result_list) != 0:
            dir = 'sample_results'
            os.makedirs(dir, exist_ok=True)
            output_file_path = os.path.join(
                dir, f"{os.path.basename(self.file_name)}_results.txt")
            with open(output_file_path, "w") as output:
                for y in self.result_list:
                    output.write(f"{y}\n")
            print(
                f'\n--------------------\n***file operations are successful done check {self.file_name}_results.txt in sample_results folder for the results***\n--------------------\n')


def main():
    """Main function executes UniqueInt class methods"""
    print(" Welcome to Uniquelnt Application, Make a file of unique integers in few seconds.\n---------------------------------------------------------------------------------\n***TO QUIT THE APPLICATION TYPE QUIT. HAVE A FUN***\n--------------------------------------------------\n")
    while True:
        file_path = input(
            "Type the ***path of your file*** or type ***quit*** to exit the program: ")
        if file_path.lower() == 'quit':
            print('\n---------------------\nThanks for using our application.you are most welcome any time.\n--------------------')
            return
        else:
            My_File = UniqueInt(file_path)
            My_File.unique_maker()
            My_File.sort_list()
            My_File.output_file()


if __name__ == "__main__":
    main()
