class file_util:
    """
    The util class for handling files.
    """

    def read_all_lines(self, file_name, encoding):
        """
        Read all texts by each lines in the specified file.

        Parameters
        ----------
        file_name : str
            The name of the file to be read.
        encoding : str
            The type of encoding in reading the file.

        Returns
        -------
        text_list : list of str
            The list of all texts in the file.
        """
        with open(file_name, encoding=encoding) as f:
            text_list = [line.strip() for line in f]
        return text_list
