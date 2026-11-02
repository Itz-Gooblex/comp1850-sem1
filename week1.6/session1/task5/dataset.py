# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        # Write code here to replace existing data with new earthquake data.
        raw_feed = self.feed.reader()
        # Use the value returned by the feed's reader() method as the
        # subject of a for loop.
        self.feed = []
        for current_quake_info in feed:
            Q = {}
            for attr in current_quake_info:
                match attr:
                    case "time":
                        Q["when"] = datetime.fromisoformat(current_quake_info["time"])
                    case "longitude":
                        Q["longitude"] = float(current_quake_info["longitude"])
                    case "latitude":
                        Q["latitude"] = float(current_quake_info["latitude"])
                    case "depth":
                        Q["depth"] = float(current_quake_info["depth"])
                    case "magnitude":
                        Q["magnitude"] = float(current_quake_info["mag"])
            self.feed.append(Quake(Q["when"], Q["longitude"], Q["latitude"], Q["depth"], Q["magnitude"]))

        # Keep in mind that the items obtained by this for loop will be
        # dictionaries. You will need to extract the required values from
        # each dictionary and convert them into the required types before
        # creating a Quake object and storing it in the list.

    def __len__(self):
        """
        Returns the size of this dataset.
        """
        # Write code here that returns the number of quakes downloaded
        return len(self.data)

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        return_string = ""
        return_string = return_string.join(f"Number of Quakes: {len(self)}")
        for quake in self.data:
            quake_string = f"Time: {quake.when.strftime("%c")}, "
            quake_string += f"Longitude : {quake.longitude}, "
            quake_string += f"Latitude : {quake.latitude}, "
            quake_string += f"Depth : {quake.depth} km, "
            quake_string += f"Magnitude : {quake.magnitude}"
            return_string += quake_string + "\n"
        # Write code here to create and return a string representation
        # (Include number of quakes and details of the feed that was used)

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """
        # Write code here that computes the mean magnitude of all the
        # quakes currently in the dataset
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.magnitude for quake in self.data)
        return total / len(self)

    def shallowest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest

    def strongest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        # Write code here that finds and returns the strongest quake
        # (i.e., the one with the largest magnitude)
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        strongest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth > shallowest.depth:
                strongest = quake
        return strongest
