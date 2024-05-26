https://flask.palletsprojects.com/en/latest/quickstart/#

startup: flask --app mainWeb run
curr host: flask run --host=0.0.0.0
debug mod: flask --app mainWeb run --debug

db: python db.py
local: python main.py

dependencies:
pip install flask
pip install pandas
pip install statsmodels
pip install matplotlib
pip install joblib
pip install psycopg2

---

### Database

```sql
CREATE TABLE hhpredict (
    id SERIAL PRIMARY KEY,
    lang VARCHAR(255),
    vac INT,
    vacRef VARCHAR(255),
    res VARCHAR(255),
    region VARCHAR(255),
    data DATE
);
```

```sql
CREATE TABLE gitpredict (
    id SERIAL PRIMARY KEY,
    count INTEGER,
    lang VARCHAR(150),
    data DATE
);
```
