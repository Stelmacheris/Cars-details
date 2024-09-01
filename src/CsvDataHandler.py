import pandas as pd

class CsvDataHandler:
    """A class for handling CSV file operations with pandas.

    This class provides methods to read and process CSV files, including adjusting data formats
    and modifying column headers.

    Attributes:
        file_path (str): The file path of the CSV file to be handled.
    """

    def __init__(self, file_path):
        """Initialize the CsvDataHandler with a specific file path.

        Args:
            file_path (str): The file path of the CSV file to be handled.
        """
        self.file_path = file_path

    def read_and_process_csv(self):
        """Read the CSV file using pandas and process the data.

        This method reads a CSV file into a DataFrame, trims whitespace and replaces commas
        in string values with dots, and modifies column names to ensure they are free of parentheses.

        Returns:
            pd.DataFrame: The processed pandas DataFrame.
        """
        df = pd.read_csv(self.file_path)
        df = df.applymap(lambda x: x.strip().replace(',', '.') if isinstance(x, str) else x)
        df.columns = [self._replace_parentheses(col) for col in df.columns]
        return df

    def _replace_parentheses(self, column_name):
        """Helper method to replace parentheses in column names with underscores or remove them.

        This method replaces the first occurrence of '(' with '_', removes the immediate
        following ')' and ensures that any remaining parentheses are removed from the column name.

        Args:
            column_name (str): The original column name.

        Returns:
            str: The modified column name free of parentheses.
        """
        column_name = column_name.replace('(', '_', 1)
        column_name = column_name.replace(')', '', 1)
        column_name = column_name.replace('(', '').replace(')', '')
        return column_name
