import pandas as pd

class HealthData():
    """Uses pandas library to build Dataframes"""
    
    def __init__(self, data: dict) -> None:
        self.data = pd.DataFrame(data, index=range(1))
        
    
    def getAvg(self, colName : str)->float:
        """This method calculates the average from the column selected

        Args:
            colName (str): name of the column that user wants to get the average from 

        Returns:
            float: the average of the column selected 
        """
        return self.data[colName].sum() / self.data[colName].size
    
    def add(self, points) -> None:
        """This method adds a row to the table in the user's dataframe

        Args:
            points: row to be added.
        """
        new_row = pd.Series(points, index=['Sleep', 'Diet', 'Exercise'])
        self.data = self.data.append(new_row, ignore_index=True)
    
    def newCol(self, name: str, val : list)->None:
        """It adds a new column to the user's dataframe

        Args:
            name (str): name of the new column
            val (list): value of the new column
        """
        self.data[name] = pd.Series(val)
        
    def toCSV(self)->None:
        """It puts the data into a csv file
        """
        self.data.to_csv(r".\Data\User.csv",index=False)
        
    def printDf(self)->None:
        print(self.data)