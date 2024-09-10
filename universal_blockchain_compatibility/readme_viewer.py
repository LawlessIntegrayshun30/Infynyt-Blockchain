## readme_viewer.py

class ReadMeViewer:
    """
    ReadMeViewer class for displaying the content of the README file.
    """

    def __init__(self, file_path: str = 'README.md'):
        """
        Initializes the ReadMeViewer with the path to the README file.

        :param file_path: The path to the README file.
        """
        self._file_path = file_path

    def display_readme(self) -> str:
        """
        Reads the content of the README file and returns it as a string.

        :return: The content of the README file.
        """
        try:
            with open(self._file_path, 'r', encoding='utf-8') as readme_file:
                content = readme_file.read()
                return content
        except FileNotFoundError:
            return "README file not found."
        except Exception as e:
            return f"An error occurred while reading the README file: {e}"
