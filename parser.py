import argparse

def main():
    #recupeation du fichier en entrer:
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--file', '-f', type=str, help='the file to parse', required=False)
    args = parser.parse_args()
    
    # Si aucun fichier n'est spécifié, demander à l'utilisateur
    if not args.file:
        print("Enter path to the file to parse OR run the script with the path as an argument after --file.")
        args.file = input("File path: ")
        

    #print(args.file)
    res=[{},[]]
    #ouverture du fichier
    try:
        with open(args.file, 'r') as file:
            #recupere les 4 premier chiffres:
            datalines = file.read().split('\n')
            firstline = datalines[0].split()
            res[0]['numNodes'] = int(firstline[0])
            res[0]['numEdges'] = int(firstline[1])
            res[0]['Source'] = int(firstline[2])
            res[0]['Sink'] = int(firstline[3])
            for i in range(1, len(datalines)):
                #recuperation des arcs
                values = datalines[i].split()
                tab = [int(values[0]), int(values[1]), int(values[2]), int(values[3])]
                res[1].append(tab)
        return(res)
    
    except FileNotFoundError:
        print(f"File '{args.file}' not found. Please check the path and try again.")
        return None
    
    

if __name__ == "__main__":
    main()