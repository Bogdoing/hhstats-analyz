from datetime import date, timedelta

from db import DB

import hh
import git
import langList


def getAnalyz():
    result_hh = []
    result_git = []
    
    for i in langList.region_HH:
        for j in langList.url_HH:
            res = hh.getAnalyz(j, i)
            result_hh.append({'region': i, 'lang': j, 'res' : res})

    for i in langList.lang_github:
        res = git.getAnalyz(i)
        result_git.append({'lang': i, 'res' : res})


    db = DB()
    for i in range(0, len(result_hh)):
        # lang, vac, vacRef, res, region, data
        db.insertHHData(
            result_hh[i]["lang"],
            result_hh[i]["res"][0],
            result_hh[i]["res"][1],
            result_hh[i]["res"][2],
            result_hh[i]["region"],
            date.today() + timedelta(days=30)
        )

    for i in range(0, len(result_git)):
        # count, lang, data
        db.insertGitData(
            result_git[i]["res"],
            result_git[i]["lang"],
            date.today() + timedelta(days=30)
        )
    db.closeDB()


    # return [
    #     result_git[0]["lang"],
    #     result_git[0]["res"]
    # ]

    return [result_hh, result_git]

print(getAnalyz())


# if __name__ == '__main__':
#     app.run()