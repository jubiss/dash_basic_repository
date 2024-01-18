import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

link_list = [("01. Main Page", "/"),
             ("02. Data Profiling", "/profiling"),
             ]

# navbar, CONTENT_STYLE = c1.navbar(link_list=link_list, color="#3957BD")

# content = html.Div(id='page-content', style=CONTENT_STYLE)
# app.layout = html.Div([dcc.Location(id="url"), navbar, content])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """
    Determines the content to display based on the current URL pathname.

    Args:
        pathname (str): Current URL pathname.

    Returns:
        str or dash.Dash: Layout of the selected page or "404 Page not found" message.
    """
    if pathname == '/':
        return # page1.layout
    if pathname == '/profiling':
        return #c1.pandas_profiling_layout(rf'assets/profilling/{profile_file_name}.html')
    else:
        return '404 Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)