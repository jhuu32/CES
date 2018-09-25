
import csv

def saveEmbeddingVector(vectors, fileName):
    ''' save a dict of numerical array'''
    with open(fileName, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in vectors.items():
            writer.writerow([key, ",".join([str(i) for i in value])])
    csv_file.close()

def loadEmbeddingVector(fileName):
    ''' load a dict of numerical array'''
    with open(fileName, 'r') as csv_file:
        reader = csv.reader(csv_file);
        temp_dict = dict(reader)
        myDict={k:list(map(lambda x: float(x), v.split(','))) for k,v in temp_dict.items()}    
        csv_file.close()
        return myDict 
    return None