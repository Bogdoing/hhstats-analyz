from analyz2 import Analyz
from db import DB




def analyzGit():
    
    lang_name = 'Php'
    training_steps = 1

    db = DB()
    data = db.getGitByLang(lang_name)
    db.closeDB()
    

    data_values =          []
    data_values_training = []

    for d in data:
        data_values.append(d[0])
        data_values_training.append(data_values[0])
        print(data_values)


    analyz = Analyz(training_steps, '01-01-2020')   
    # return [1,2,3]


    return analyz.analyze(lang_name, data_values, data_values_training, training_steps)


def getAnalyz(lang_name):

    training_steps = 1

    db = DB()
    data = db.getGitByLang(lang_name)
    db.closeDB()
    

    data_values =          []
    data_values_training = []

    for d in data:
        print(d)
        addData = int(d[0])

        data_values.append(addData)
        data_values_training.append(addData)


    analyz = Analyz(training_steps, '01-01-2020')   

    new_data = analyz.analyze(lang_name, data_values, data_values_training, training_steps)
    
    print(new_data)

    
    return new_data
