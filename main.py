import sys, getopt
import CsvTransformer as ct

def match_sub_command(sub_command:str, input_path:str):
    transformer = ct.CsvTransformer(input_path)
    transformer.load()

    match sub_command:
        case 'to_html':
            print(transformer.to_html())

def write_data_to_file(data:str, output_path:str):
    f = open(output_path, 'w')
    f.write(data)
    f.close()

def main(argv:list):
    if (len(argv) < 3):
        print('invalid program arguments')
    
    sub_command = argv[1]
    input_path = argv[2]

    match_sub_command(sub_command, input_path)

if __name__ == '__main__':
    main(sys.argv)
