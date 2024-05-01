import pandas as pd

class CsvTransformer:

    def __init__(self, path: str) -> str:
        self.path = path

    def load(self):
        self.df = pd.read_csv(self.path)

    def to_html(self):
        return self.df.to_html()
    
    def to_json(self):
        return self.df.to_json()
    
    def to_markdown(self):
        self.df.to_markdown()