import numpy as np
import pandas as pd # type: ignore

class TimeSeriesProcessor:
    def __init__(self, csv_file):
        """
        Initialize the TimeSeriesProcessor class.

        Parameters:
        csv_file (str): Path to the CSV file containing time series data.
        """
        self.time_vector = None
        self.values = None
        self.channel_names = None

        self._read_csv(csv_file)

    def _read_csv(self, csv_file):
        """
        Read time series data from a CSV file.

        Parameters:
        csv_file (str): Path to the CSV file.
        """
        try:
            data = pd.read_csv(csv_file)

            # Extract channel names (column headers excluding the first column)
            self.channel_names = data.columns[1:].tolist()

            # Extract time vector (first column)
            self.time_vector = data.iloc[:, 0].to_numpy()

            # Extract values (all columns except the first one)
            self.values = data.iloc[:, 1:].to_numpy()

        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def get_channel_names(self):
        """
        Get the names of the channels.

        Returns:
        list: List of channel names.
        """
        return self.channel_names

    def get_time_vector(self):
        """
        Get the time vector.

        Returns:
        numpy.ndarray: Array containing the time vector.
        """
        return self.time_vector

    def get_values(self):
        """
        Get the values of the time series.

        Returns:
        numpy.ndarray: 2D array containing the values of the time series.
        """
        return self.values

