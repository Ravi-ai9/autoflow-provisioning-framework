from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

status_store = {}

@app.get("/")
def home():
    return {"message": "Autoflow Dashboard Running"}


@app.get("/status/{guid}", response_class=HTMLResponse)
def get_status(guid: str):

    data = status_store.get(guid, {})

    html = f"""
    <html>
    <head>
        <title>Autoflow Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            table {{
                border-collapse: collapse;
                width: 50%;
                background: white;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #333;
                color: white;
            }}
        </style>
    </head>
    <body>

        <h2>🚀 Autoflow Dashboard</h2>
        <h3>GUID: {guid}</h3>

        <table>
            <tr>
                <th>STATE</th>
                <th>STATUS</th>
            </tr>
    """

    for state, status in data.items():
        html += f"""
            <tr>
                <td>{state}</td>
                <td>{status}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html