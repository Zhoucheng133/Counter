import sqlite3
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

cookie="Input your cookie HERE"

class Counter:
    def __init__(self) -> None:
        conn = sqlite3.connect('data.db')
        c =conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS counter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            count INTEGER NOT NULL
        )
        ''')
        conn.commit()
        c.execute('SELECT COUNT(*) FROM counter')
        if c.fetchone()[0] == 0:
            c.execute('INSERT INTO counter (count) VALUES (0)')
            conn.commit()

    def add(self):
        conn = sqlite3.connect('data.db')
        c =conn.cursor()
        c.execute('''
            UPDATE counter
            SET count = count + 1
            WHERE rowid = 1;
        ''')
        conn.commit()
    
    def get(self):
        conn = sqlite3.connect('data.db')
        c =conn.cursor()
        c.execute('SELECT count FROM counter WHERE rowid = 1;')
        row = c.fetchone()
        if row:
            return row[0]
        return None
    
    def clear(self):
        conn = sqlite3.connect('data.db')
        c =conn.cursor()
        c.execute('''
            UPDATE counter
            SET count = 0
            WHERE rowid = 1;
        ''')
        conn.commit()

app = FastAPI()
counter=Counter()

@app.middleware("http")
async def check_cookie(request: Request, call_next):
    cookie_value = request.headers.get("Cookie")
    if cookie_value != cookie:
        return JSONResponse(
            status_code=403,
            content={"detail": "Invalid cookie"}
        )

    response = await call_next(request)
    return response

@app.post("/add")
def add():
    counter.add()
    return {"ok": True}

@app.get("/get")
def get():
    return counter.get()

@app.post("/clear")
def clear():
    counter.clear()
    return {"ok": True}