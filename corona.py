import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import plotly
import plotly.figure_factory as ff 
import plotly.express as px
import plotly.graph_objects as go

def total():
    df=scrape()
    Total_Cases=df["Total_Cases"].sum()
    Total_Deaths=df["Total_Deaths"].sum()
    Active_Cases=df["Active_Cases"].sum()
    Total_Recovered=df["Total_Recovered"].sum()
    return [Total_Cases,Total_Deaths,Active_Cases,Total_Recovered]

def scrape ():
    url1 = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url1)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    coronatable = tables[0]
    country = []
    totalcases = []
    totaldeaths = []
    totalrecovered = []
    activecases = []
    totaltests = []
    rows = coronatable.find_all("tr")[9:-8]
    colname = [country,totalcases,totaldeaths,totalrecovered,activecases,totaltests]
    colnum = [1,2,4,6,7,11]
    for row in rows:
        col = row.find_all("td")
        for i,j in zip(colname,colnum):
            s = col[j].text.strip()
            s1 = s.replace(",","")
            i.append(s1)
    df = pd.DataFrame(list(zip(country,totalcases,totaldeaths,totalrecovered,activecases,totaltests)), columns=["Country","Total_Cases","Total_Deaths","Total_Recovered","Active_Cases","Total_Tests"])
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df.replace(np.nan,0, inplace=True)
    df.replace("N/A",0,inplace = True)
    df.Total_Cases = pd.to_numeric(df.Total_Cases)
    df.Total_Deaths = pd.to_numeric(df.Total_Deaths)
    df.Total_Recovered = pd.to_numeric(df.Total_Recovered)
    df.Active_Cases = pd.to_numeric(df.Active_Cases)
    df.Total_Tests = pd.to_numeric(df.Total_Tests)
    df.sort_values("Country",ignore_index=True,inplace=True)
    population = pd.read_csv("2_Population_data.csv")
    gdp = pd.read_csv("3_GDP_data.csv")
    travel = pd.read_csv("4_Travel_data.csv")
    result1 = pd.merge(df,gdp, on='Country')
    result2 = pd.merge(result1,travel, on='Country')
    final = pd.merge(result2,population, on='Country')
    final = final.sort_values('Total_Cases',ascending=False,ignore_index=False)
    final.reset_index(drop=True,inplace=True)
    return final

def table():
    df2 = scrape()
    df3 = ff.create_table(df2)
    # return df3
    return plotly.offline.plot(df3,output_type='div')

def first10cases():
    df4 = pd.read_csv("owid-covid-data.csv")
    df4 = df4[df4.date > '2020-02-29']
    df4 = df4[['location', 'date', 'total_cases']]
    df4 = df4[df4.location.isin(['Russia', 'United Kingdom','Spain', 'Italy', 'Germany', 'Turkey', 'France', 'Iran', 'India','China'])]
    df4['date'] = pd.to_datetime(df4['date'])
    df4.set_index(['date', 'location'], inplace=True)
    df4.sort_index(inplace=True)
    df4 = df4.unstack(level=[1])
    df4.columns = df4.columns.droplevel()
    df4col = df4.columns.values.tolist()
    graph4 = []
    for i in df4col:
        graph4.append(
            go.Line(name = i, x=df4.index, y=df4[i])
        )
    fig4 = go.Figure(data=graph4)
    fig4.update_layout(
        title="Total Cases v/s Timeline",
        xaxis_title="Timeline",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig4,output_type='div')

def first10tests():
    df5 = pd.read_csv('owid-covid-data.csv')
    df5 = df5[df5.date > '2020-02-29']
    df5 = df5[['location', 'date', 'total_tests_per_thousand']]
    df5 = df5[df5.location.isin(['Russia', 'United Kingdom','Spain', 'Italy', 'Germany', 'Turkey', 'France', 'Iran', 'India','China'])]
    df5['date'] = pd.to_datetime(df5['date'])
    df5.set_index(['date', 'location'], inplace=True)
    df5.sort_index(inplace=True)
    df5 = df5.unstack(level=[1])
    df5.columns = df5.columns.droplevel()
    df5col = df5.columns.values.tolist()
    graph5 = []
    for i in df5col:
        graph5.append(
            go.Line(name = i, x=df5.index, y=df5[i])
        )
    fig5 = go.Figure(data=graph5)
    fig5.update_layout(
        title="Total Tests per Thousand",
        xaxis_title="Timeline",
        yaxis_title="Total tests per thousand",
    )
    return plotly.offline.plot(fig5,output_type='div')

def second10cases():
    df6 = pd.read_csv("owid-covid-data.csv")
    df6 = df6[df6.date > '2020-02-29']
    df6 = df6[['location', 'date', 'total_cases']]
    df6 = df6[df6.location.isin(['Canada', 'Belgium', 'Mexico', 'Chile', 'Ecuador', 'Qatar','Switzerland', 'Portugal'])]
    df6['date'] = pd.to_datetime(df6['date'])
    df6.set_index(['date', 'location'], inplace=True)
    df6.sort_index(inplace=True)
    df6 = df6.unstack(level=[1])
    df6.columns = df6.columns.droplevel()
    df6col = df6.columns.values.tolist()
    graph6 = []
    for i in df6col:
        graph6.append(
            go.Line(name = i, x=df6.index, y=df6[i])
        )
    fig6 = go.Figure(data=graph6)
    fig6.update_layout(
        title="Total Cases",
        xaxis_title="Timeline",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig6,output_type='div')

def second10tests():
    df7 = pd.read_csv('owid-covid-data.csv')
    df7 = df7[df7.date > '2020-02-29']
    df7 = df7[['location', 'date', 'total_tests_per_thousand']]
    df7 = df7[df7.location.isin(['Canada', 'Belgium', 'Mexico', 'Chile', 'Ecuador', 'Qatar','Switzerland', 'Portugal'])]
    df7['date'] = pd.to_datetime(df7['date'])
    df7.set_index(['date', 'location'], inplace=True)
    df7.sort_index(inplace=True)
    df7 = df7.unstack(level=[1])
    df7.columns = df7.columns.droplevel()
    df7col = df7.columns.values.tolist()
    graph7 = []
    for i in df7col:
        graph7.append(
            go.Line(name = i, x=df7.index, y=df7[i])
        )
    fig7 = go.Figure(data=graph7)
    fig7.update_layout(
        title="Total Tests per Thousand",
        xaxis_title="Timeline",
        yaxis_title="Total tests per thousand",
    )
    return plotly.offline.plot(fig7,output_type='div')

def third10cases():
    df8 = pd.read_csv("owid-covid-data.csv")
    df8 = df8[df8.date > '2020-02-29']
    df8 = df8[['location', 'date', 'total_cases']]
    df8 = df8[df8.location.isin(['Bangladesh', 'Poland', 'Indonesia', 'Romania', 'Israel', 'Japan', 'Austria', 'South Korea'])]
    df8['date'] = pd.to_datetime(df8['date'])
    df8.set_index(['date', 'location'], inplace=True)
    df8.sort_index(inplace=True)
    df8 = df8.unstack(level=[1])
    df8.columns = df8.columns.droplevel()
    df8col = df8.columns.values.tolist()
    graph8 = []
    for i in df8col:
        graph8.append(
            go.Line(name = i, x=df8.index, y=df8[i])
        )
    fig8 = go.Figure(data=graph8)
    fig8.update_layout(
        title="Total Cases",
        xaxis_title="Timeline",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig8,output_type='div')

def third10tests():
    df9 = pd.read_csv('owid-covid-data.csv')
    df9 = df9[df9.date > '2020-02-29']
    df9 = df9[['location', 'date', 'total_tests_per_thousand']]
    df9 = df9[df9.location.isin(['Bangladesh', 'Poland', 'Indonesia', 'Romania', 'Israel', 'Japan', 'Austria', 'South Korea'])]
    df9['date'] = pd.to_datetime(df9['date'])
    df9.set_index(['date', 'location'], inplace=True)
    df9.sort_index(inplace=True)
    df9 = df9.unstack(level=[1])
    df9.columns = df9.columns.droplevel()
    df9col = df9.columns.values.tolist()
    graph9 = []
    for i in df9col:
        graph9.append(
            go.Line(name = i, x=df9.index, y=df9[i])
        )
    fig9 = go.Figure(data=graph9)
    fig9.update_layout(
        title="Total Tests per Thousand",
        xaxis_title="Timeline",
        yaxis_title="Total tests per thousand",
    )
    return plotly.offline.plot(fig9,output_type='div')

def tourists():
    df10 = scrape()
    df10 = df10[df10.Total_Cases < 300000]
    df10 = df10[df10.Total_Cases > 5000]
    df10 = df10[df10.GDP_in_Mn < 5000000]
    df10 = df10[df10['Urban_Pop_%'] > 0]
    fig10 = px.scatter(df10, x="Tourists_in_1000s", y="Total_Cases", hover_data=['Country'],trendline="ols")
    fig10.update_layout(
        title="No. of tourists arrival in 1000s v/s Total Cases",
        xaxis_title="Tourists arrival in 1000s",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig10,output_type='div')

def gdp():
    df11 = scrape()
    df11 = df11[df11.Total_Cases < 300000]
    df11 = df11[df11.Total_Cases > 5000]
    df11 = df11[df11.GDP_in_Mn < 5000000]
    df11 = df11[df11['Urban_Pop_%'] > 0]
    fig11 = px.scatter(df11, x="GDP_in_Mn", y="Total_Cases", hover_data=['Country'],trendline="ols")
    fig11.update_layout(
        title="GDP in million dollars v/s Total Cases",
        xaxis_title="GDP in Mn",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig11,output_type='div')

def urbanpop():
    df12 = scrape()
    df12 = df12[df12.Total_Cases < 300000]
    df12 = df12[df12.Total_Cases > 5000]
    df12 = df12[df12.GDP_in_Mn < 5000000]
    df12 = df12[df12['Urban_Pop_%'] > 0]
    fig12 = px.scatter(df12, x="Urban_Pop_%", y="Total_Cases", hover_data=['Country'],trendline="ols")
    fig12.update_layout(
        title="Urban population percentage v/s Total Cases",
        xaxis_title="Urban population percentage",
        yaxis_title="Total Cases",
    )
    return plotly.offline.plot(fig12,output_type='div')

def touristslog():
    df13 = scrape()
    fig13 = px.scatter(df13, x="Total_Cases", y="Tourists_in_1000s", hover_data=['Country'])
    fig13.update_layout(xaxis_type="log")
    fig13.update_layout(
        title="Total Cases v/s Tourists arrival in 1000s for all the countries",
        xaxis_title="Total Cases",
        yaxis_title="Tourists arrival in 1000s",
    )
    return plotly.offline.plot(fig13,output_type='div')
