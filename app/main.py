from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from all origins (or specify specific origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data structure for command
class Command(BaseModel):
    command: str

# Data structure for Wi-Fi credentials
class WifiCredentials(BaseModel):
    ssid: str
    password: str

# Placeholder variables
current_command = "FAN_OFF"  # Default command
wifi_credentials = {"ssid": "Borderless Wifi", "password": "Borderless3.0"}

# Endpoint to get the current command for ESP32
@app.get("/get_command/")
async def get_command():
    return {"command": current_command}

# Endpoint to update the command
@app.post("/set_command/")
async def set_command(command: Command):
    global current_command
    current_command = command.command
    return {"message": f"Command set to {current_command}"}

# Endpoint to get the Wi-Fi credentials
@app.get("/get_wifi/")
async def get_wifi():
    return wifi_credentials

# Endpoint to update Wi-Fi credentials
@app.post("/set_wifi/")
async def set_wifi(credentials: WifiCredentials):
    global wifi_credentials
    wifi_credentials["ssid"] = credentials.ssid
    wifi_credentials["password"] = credentials.password
    return {"message": "Wi-Fi credentials updated successfully"}
