import argparse

def main():
    #recupeation du fichier en entrer:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', type=str, help='the file to parse')
    args = parser.parse_args()

    print(args.file)
    #ouverture du fichier
    with open(args.file, 'r') as file:
        data = file.read().replace('\n', '')
        print(data)
    
    print("ouee")

if __name__ == "__main__":
    main()