import dash
from dash import dcc
from dash import html
from pandas.io.formats import style
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv("data/OARMetricComp.csv")

#DVHX = 'V5Gy'
DVH_arr = ['V60Gy','V50Gy','V45Gy','V40Gy','V35Gy','V30Gy','V25Gy','V20Gy','V5Gy','D5cc','D0cc']
xUpper = 'Volume'
xLower = 'ALPO'

# Initialise the app
app = dash.Dash(__name__)

# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_leaf):
        dict_list = []
        for i in list_leaf:
                dict_list.append({'label':i, 'value':i})
        return dict_list

# Define the app
app.layout = html.Div(children=[
	html.Div(className='row', # define the row element
		children=[
			html.Div(className='four columns div-user-controls',
				children=[
					html.H2('Organs At Risk Dose Distribution Dashboard'),
					html.P('''Pick one or more leaf width to display'''),
					html.Div(className='div-for-dropdown',
						children=[
							dcc.Dropdown(id='leafselector',
								options=get_options(df['PlanID'].unique()),
                                                                placeholder="Select a leaf width",
								multi=True,
								value=[df['PlanID'].sort_values()[0]],
								style={'backgroundColor':'#1E1E1E'},
								className='leafselector'
							),
							dcc.Dropdown(id='oarselector',
								options=get_options(df['OAR'].unique()),
								placeholder="Select an Organ At Risk",
                                                                multi=True,
								value=[df['Site'].sort_values()[0]],
								style={'backgroundColor':'#1E1E1E'},
								className='oarselector'
							)
						],
					style={'color':'#1E1E1E'}
					),
                                        html.P('''Pick one dose metric to view'''),
                                        html.Div(className='div-for-dropdown',
						children=[
							dcc.Dropdown(id='dvhselector',
								options=get_options(DVH_arr),
                                                                placeholder="Select a dose metric",
								multi=False,
								value=DVH_arr[0],
								style={'backgroundColor':'#1E1E1E'},
								className='dvhselector'
							),
						],
					style={'color':'#1E1E1E'}
					),
                                        
				]
			), # Define the left element
			html.Div(className='eight columns div-for-charts bg-grey',
				children=[
					dcc.Graph(id='volume-v60',
						config={'displayModeBar':False},
						animate=True
					),
					dcc.Graph(id='conformity-v60',
						config={'displayModeBar':False},
						animate=True
					),
				]
			) # Define the right element
		]
	)
])

@app.callback(Output('volume-v60','figure'),
			[Input('leafselector','value'),
			Input('oarselector','value'),
                        Input('dvhselector','value')
			]
)
def update_volume_v60(leaf_dropdown_val, oar_dropdown_val,dose_met):
	trace = []
	df_sub = df
	DVHX = dose_met
	for leaf in leaf_dropdown_val:
                trace.append(go.Scatter(x=df_sub[df_sub['PlanID'] == leaf][xUpper],
								y=df_sub[df_sub['PlanID'] == leaf][DVHX],
								mode='markers',
								opacity=0.7,
								name=leaf,
								textposition='bottom center'
					)
		)
	for oar in oar_dropdown_val:
		trace.append(go.Scatter(x=df_sub[df_sub['OAR'] == oar][xUpper],
								y=df_sub[df_sub['OAR'] == oar][DVHX],
								mode='markers',
								opacity=0.7,
								name=oar,
								textposition='bottom center'
					)
		)
	traces = [trace]
	data = [val for sublist in traces for val in sublist]
	figure={'data':data,
			'layout':go.Layout(
				colorway=[],
				template='plotly_dark',
				paper_bgcolor='rgba(0,0,0,0)',
				plot_bgcolor='rgba(0,0,0,0)',
				margin={'b':15},
				hovermode='x',
				autosize=True,
				title={'text': xUpper+' v '+DVHX,'font':{'color':'white'},'x':0.5},
				xaxis={'title': xUpper,'range':[0,df_sub[xUpper].max()]},
                                yaxis={'title': DVHX,'range':[0,df_sub[DVHX].max()]},
	),
	}
	return figure


@app.callback(Output('conformity-v60','figure'),
			[Input('leafselector','value'),
			Input('oarselector','value'),
                        Input('dvhselector','value')
			]
)
def update_conformity_v60(leaf_dropdown_val, oar_dropdown_val,dose_met):
	trace = []
	df_sub = df
	DVHX = dose_met
	for leaf in leaf_dropdown_val:
		trace.append(go.Scatter(x=df_sub[df_sub['PlanID'] == leaf][xLower],
								y=df_sub[df_sub['PlanID'] == leaf][DVHX],
								mode='markers',
								opacity=0.7,
								name=leaf,
								textposition='bottom center'
					)
		)
	for oar in oar_dropdown_val:
		trace.append(go.Scatter(x=df_sub[df_sub['OAR'] == oar][xLower],
								y=df_sub[df_sub['OAR'] == oar][DVHX],
								mode='markers',
								opacity=0.7,
								name=oar,
								textposition='bottom center'
					)
		)
	traces = [trace]
	data = [val for sublist in traces for val in sublist]
	figure={'data':data,
			'layout':go.Layout(
				colorway=[],
				template='plotly_dark',
				paper_bgcolor='rgba(0,0,0,0)',
				plot_bgcolor='rgba(0,0,0,0)',
				margin={'b':15},
				hovermode='x',
				autosize=True,
				title={'text': xLower+' v '+DVHX,'font':{'color':'white'},'x':0.5},
				xaxis={'title': xLower,'range':[0,df_sub[xLower].max()]},
                                yaxis={'title': DVHX,'range':[0,df_sub[DVHX].max()]},
	),
	}
	return figure


"""
    [	
		html.H1(
			"Organs At Risk Dose Distribution Dashboard",
		),
		html.Div([
			html.Label("Organ"),
			dcc.Dropdown(
				id="organ-dropdown",
				options=[
					{"label": s, "value": s} for s in df.OAR.unique()
				],
				className="dropdown",
                        ),
                    ], className="row",
                ),
		html.Div(dcc.Graph(id='oar-plots', figure=fig, className="chart")),
	],
	className="container",

fig = px.scatter(
    df,
    x='V25Gy',
    y='PlanID',
    size='Volume',
    color='OAR',
    hover_name='OAR',
    #log_x=True,
    size_max=60,
)
"""

if __name__ == "__main__":
    app.run_server()
