# betting_website_client.py

"""  
A simple FastAPI application for a betting website.

This file serves as a client for the betting platform where users can place bets, view betting statistics, and more.

The application uses FastAPI for creating the web server and rendering HTML templates dynamically. 
"""

from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Additional route example
@app.get("/bet")
async def place_bet(request: Request, bet: int = 0):
    # Logic for placing a bet here
    return templates.TemplateResponse("bet.html", {"request": request, "bet": bet})

if __name__ == "__main__":
    # For local development you can use Uvicorn to run the server as follows:
    # uvicorn betting_website_client:app --reload
    # For production use, set up Cloudflared tunnel configuration to allow access to the FastAPI app
    # cloudflared tunnel --url http://localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)