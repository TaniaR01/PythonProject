import pandas as pd
class uploader:
    def __init__(self):
        self.df = pd.DataFrame()
    def load_df(self,filename):
        self.df = pd.read_csv(filename)
    def preview_10_df(self):
        dshow = self.df.head(10)
        print(dshow)
