from analyz2 import Analyz
from db import DB


def getAnalyz(lang_name, region):
    training_steps = 1
    analyz = Analyz(training_steps, '01-01-2020')

    db = DB()
    data = db.getHHLengRegionData(lang_name, region)
    db.closeDB()
    
    new_data = []

    '''
        0 var 
        1 varRef
        2 res
    '''
    for i in range(0, 3):
        data_values =          []
        data_values_training = []
        for d in data:
            print(d)
            addData = int(d[i])

            data_values.append(addData)
            data_values_training.append(addData)
        
        new_data.append(analyz.analyze(lang_name, data_values, data_values_training, training_steps))
    
    # data_values =          []
    # data_values_training = []
    # for d in data:
    #         print(d)
    #         addData = int(d[2])

    #         data_values.append(addData)
    #         data_values_training.append(addData)
    # new_data.append(analyz.analyze(lang_name, data_values, data_values_training, training_steps))

    return new_data
    # return {'new_data':new_data, 'region': region}
