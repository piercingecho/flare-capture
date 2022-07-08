import csv

def findConcentrations(substance):

    lowConc = -1.0
    highConc = -1.0

    with open('conc.csv', mode='r') as f:
        try:
            csvFile = csv.reader(f)
            
            for line in csvFile:
                if(line[0] == substance):
                    lowConc = float(line[1])
                    highConc = float(line[2])
                    break #don't need to go through the rest of the file; we already have what we need!
    
            if(lowConc == -1.0 or highConc == -1.0):
                raise Exception("Substance not found in conc.csv.")

        except Exception as e:
            print("Error in reading conc.csv. Either: file not in directory, or substance not in file.")
            print(e)
        finally:
            f.close()

    return lowConc, highConc


def main():
    low, high = findConcentrations("Trypsin")
    print("Low:", low, "High:", high)

if __name__ == '__main__':
    main()
