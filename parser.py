import argparse

def main():
    #recupeation du fichier en entrer:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', type=str, help='the file to parse')
    args = parser.parse_args()

    print(args.file)
    res=[{},[]]
    #ouverture du fichier
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

if __name__ == "__main__":
    main()