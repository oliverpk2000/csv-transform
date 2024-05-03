import pandas as pd

class CsvTransformer:

    def __init__(self, path: str) -> str:
        self.path = path
        self.file_ext = 'csv'

    def load(self):
        self.df = pd.read_csv(self.path)
        self.rep = self.df.to_csv

    def to_html(self):
        self.file_ext = 'html'
        self.rep = self.df.to_html()
        return self.rep
    
    def to_json(self):
        self.file_ext = 'json'
        self.rep = self.df.to_json
        return self.rep
    
    def to_markdown(self):
        self.file_ext = 'md'
        self.rep = self.df.to_markdown()
        return self.rep

    def get_output_file_name(self) -> str:
        return self.path.split('.')[0] + '.' + self.file_ext