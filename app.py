import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    df=web.DataReader("^DJI", 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    #df['Date'] = df.index.map(str)
    df['Date'] = df.index
    df['Date'] = df['Date'].dt.strftime("%d-%b-%y")
    #print(type(df['Date'][0]))
    #df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    #s = df[['Date', 'Open','High','Low','Close','Volume']].to_string(header=True
    s = '\\n'.join(','.join("%s" % x for x in y) for y in df[['Date', 'Open','High','Low','Close','Volume']].values)
    s = "Date,Open,High,Low,Close,Volume\\n" + s
    print(s)
    return render_template('index.html', symbol="Dow Jones Index", s=s)

@app.route('/<symbol>')
def draw(symbol):
    df=web.DataReader(symbol, 'yahoo', datetime(2016,1,1))
    df.sort_index(ascending=False)
    df['Date'] = df.index
    df['Date'] = df['Date'].dt.strftime("%d-%b-%y")
    # df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    s = '\\n'.join(','.join("%s" % x for x in y) for y in df[['Date', 'Open','High','Low','Close','Volume']].values)
    s = "Date,Open,High,Low,Close,Volume\\n" + s
    return render_template('index.html', symbol=symbol, s=s)
