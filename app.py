#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load dataset
data = pd.read_csv('automobile_sales.csv')

# Initialize app
app = dash.Dash(__name__)

# Title
app.title = "Automobile Sales Statistics Dashboard"

# Year list
year_list = [i for i in range(1980, 2024, 1)]

# Layout
app.layout = html.Div([

    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 30}
    ),

    # Dropdown 1
    html.Div([
        html.Label("Select Statistics:", style={'text-size' : '30px'}),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            value=None,
            placeholder='Select a report type',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center', 'margin': '10px'}
        )
    ]),

    # Dropdown 2
    html.Div([
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=None,
            placeholder='Select year (for Yearly Report Only *)',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center', 'margin' : '10px'}
        )
    ]),

    # Output container
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flex-direction': 'column'})
])

# ---------------- CALLBACK 1 ----------------
# Enable/Disable year dropdown
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    return True

# ---------------- CALLBACK 2 ----------------
# Update graphs
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):

    if selected_statistics == 'Recession Period Statistics':

        recession_data = data[data['Recession'] == 1]

        # Plot 1
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        fig1 = px.line(yearly_rec, x='Year', y='Automobile_Sales',
                       title="Average Automobile Sales During Recession")

       

        # Plot 2
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        fig2 = px.bar(unemp_data,
                      x='unemployment_rate',
                      y='Automobile_Sales',
                      color='Vehicle_Type',
                      title='Unemployment vs Sales')
        
        # Plot 3
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        fig3 = px.pie(exp_rec, values='Advertising_Expenditure',
                      names='Vehicle_Type',
                      title="Ad Expenditure Share")
        
        # Plot 4
        avg_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        fig4 = px.bar(avg_sales, x='Vehicle_Type', y='Automobile_Sales',
                      title="Average Vehicles Sold by Type")

        return [
            html.Div([
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2)
            ], style={'display': 'flex'}),

            html.Div([
                dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4)
            ], style={'display': 'flex'})
        ]

    elif selected_statistics == 'Yearly Statistics' and input_year:

        yearly_data = data[data['Year'] == input_year]

        # Plot 1
        avg_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        fig1 = px.bar(avg_vdata, x='Vehicle_Type', y='Automobile_Sales',
                      title=f"Average Vehicles Sold in {input_year}")

        # Plot 2
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        fig2 = px.pie(exp_data,
                      values='Advertising_Expenditure',
                      names='Vehicle_Type',
                      title="Ad Expenditure Share")

        # Plot 3
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        fig3 = px.line(yas, x='Year', y='Automobile_Sales',
                       title="Yearly Automobile Sales")

        # Plot 4
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        fig4 = px.bar(mas, x='Month', y='Automobile_Sales',category_orders={"Month": month_order},
                       title="Monthly Sales")


        return [
            html.Div([
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2)
            ], style={'display': 'flex'}),

            html.Div([
                dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4)
            ], style={'display': 'flex'})
        ]

    else:
        return html.Div("Please select a report type above", style = {'font-weight': 'bold'} )

# Run app
server = app.server

if __name__ == '__main__':
    app.run(debug=True)