import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash()

df = pd.read_csv("OARMetricComp.csv")  # csv file

fig = px.scatter(
    df,
    x='V5Gy',            # x-axis metric
    y='Volume',          # y-axis metric
    size='CI_RTOG100',   # size of data point (don't use )
    color='PlanID',      # colour of data point
    hover_name='OAR',
    #log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id='oar-dash', figure=fig)])

if __name__ == "__main__":
    app.run_server()
