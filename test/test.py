import CsvTransformer

transformer = CsvTransformer("test\data\Pokemon.csv")

transformer.load()

print(transformer.to_html())