from flask import Flask

from hh import HH

import git
import langList

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is from Flask Serverless Function'


@app.route('/analyz')
def getAnalyz():
    hh = HH()
    lang_name = 'React'
    region = '26'

    result_hh = []
    result_git = []
    
    for i in langList.region_HH:
        for j in langList.url_HH:
            res = hh.getAnalyz(j, i)
            result_hh.append({'region': i, 'lang': j, 'res' : res})

    for i in langList.lang_github:
        res = git.getAnalyz(i)
        result_git.append({'lang': i, 'res' : res})

    return [result_hh, result_git]




# if __name__ == '__main__':
#     app.run()