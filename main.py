import sys
import CsvTransformer as ct
import argparse


def write_data_to_file(data:str, output_path:str):
    f = open(output_path, 'w')
    f.write(data)
    f.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("format")
    parser.add_argument("input_file")
    args = parser.parse_args()
    
    transformer = ct.CsvTransformer(args.input_file)

    try:
        transformer.load()
    except:
        print("error loading file {}".format(transformer.path))

    if args.format == "html":
        transformer.to_html()
    elif args.format == "json":
        transformer.to_json()
    
    data = transformer.get_representation()
    output_file = transformer.get_output_file_name()

    write_data_to_file(data, output_file)

if __name__ == '__main__':
    main()
