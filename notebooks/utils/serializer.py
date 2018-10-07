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
    
def loadFixMap(fileName):
    '''load the map word>fixed word '''
    reader = csv.reader(open(fileName, 'r'))
    fixMap = {}
    for row in reader:
       k, v = row
       fixMap[k] = v
    return fixMap    
    
def loadWords(fileName):
    '''load set of words '''
    reader = csv.reader(open(fileName, 'r'))
    words = set()
    for row in reader:
       if len(row) > 0:
           words.add(row[0])
    return words        