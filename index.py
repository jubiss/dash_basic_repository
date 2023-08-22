from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server
# from apps import page1, page2
import dash_custom_components.my_components as c1 

link_list = [("01. Main Page", "/"),
             ("02. Data Profiling", "/profiling"),
             ]

navbar, CONTENT_STYLE = c1.navbar(link_list=link_list, color="#3957BD")

content = html.Div(id='page-content', style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), navbar, content])

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