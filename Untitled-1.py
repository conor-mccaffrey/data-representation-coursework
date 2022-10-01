#DataRep W1

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
# if I want to store the xml in a file. You can comment this out later
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        # lets get everything
        dataList = []
        #for retrieveTag in retrieveTags:
            #datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
        dataList.append(traincode)
        train_writer.writerow(dataList)
 