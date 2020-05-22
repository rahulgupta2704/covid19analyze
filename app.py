from flask import Flask, render_template, send_file, make_response
from corona import total,table,first10cases,first10tests,second10tests,second10cases,third10tests,third10cases,tourists,gdp,urbanpop,touristslog
from flask import *
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route('/')
def show_tables():
    totals=total()
    tableDisplay = table()
    first10case = first10cases()
    first10test = first10tests()
    second10case = second10cases()
    second10test = second10tests()
    third10case = third10cases()
    third10test = third10tests()
    plot1 = tourists()
    plot2 = gdp()
    plot3 = urbanpop()
    plot4 = touristslog()
    return render_template('index.html', total_data=totals, returnList = tableDisplay, figure1 = first10case, figure2 = first10test, figure3 = second10case, figure4 = second10test, figure5 = third10case, figure6 = third10test, fig1 = plot1, fig2 = plot2, fig3 = plot3, fig4=plot4)
    

if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True)