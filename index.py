from dash import html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
# from app import server
# from apps import page1, page2

app.layout = html.Div([
])

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
    if pathname == '/page2':
        return # page2.layout
    else:
        return '404 Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)