import requests
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np


def db_get(url, params=None):
    api_key = "6d680224d118a0784d34efe88550115e"
    client_id = "d95e9f1c7c8f175d8b787361e851c33f"
    headers = {
        'DB-Client-Id': client_id,
        'DB-Api-Key': api_key,
        'accept': "application/json"
    }

    response = requests.get(url, headers=headers, params=params)
    return response


response = db_get(url="https://apis.deutschebahn.com/db-api-marketplace/apis/fasta/v2/facilities")
json_file = response.json()
df = pd.DataFrame(json_file)
df2=pd.read_excel('Station_data.xlsx')
selected = df2[['Bf-Nr','Bahnhof']]
numbertobahn = dict(selected.to_dict('split')['data'])
df['Bahnhof'] = df['stationnumber'].apply(lambda x: numbertobahn[x])



app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
perc = pd.DataFrame({
    'Number': [len(set(df['stationnumber'].values.tolist())),
            len(numbertobahn) - len(set(df['stationnumber'].values.tolist()))],
    'Label' : ["Total stations with facilities", "Total stations without facilities"]
})
fig1 = px.pie(perc, values = 'Number', names = 'Label')


facops = df['type'].unique()
nofacs = []
for i in facops:
    nofacs.append(len(df.loc[df['type'] == i]))
listofops= pd.DataFrame({
    'Facilities':facops,
    "Number of facilities" : nofacs
})
fig2 = px.pie(listofops,names= 'Facilities', values = 'Number of facilities')

state = df['state'].unique()
totalstate = []
for i in state:
    totalstate.append(len(df.loc[df['state'] == i]))
status = pd.DataFrame({
    'state' : state,
    'totalstate' : totalstate
})
fig3 = px.pie(status,names = "state", values = "totalstate")


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='Percentage of DB train stations with facilities',
        figure=fig1),

    dcc.Graph(
            id='Number of facilities operated by operators',
            figure=fig2),
dcc.Graph(
            id='Number of facilities in unique states',
            figure=fig3)


])

if __name__ == '__main__':
    app.run_server(debug=True)