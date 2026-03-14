# IATOS: ESP32-CAM Traffic Enforcement System

This project contains the firmware for an ESP32-CAM to stream video to a Django backend for speed enforcement.

## Project Structure
- `firmware/`: C++ code for ESP32-CAM (compatible with Arduino/PlatformIO).
- `backend/`: Django project to receive and process video frames.

## Setup Instructions

### 1. ESP32-CAM Firmware
1.  Open `firmware/main.ino` in the Arduino IDE or your preferred C++ environment.
2.  Install the `ESP32` board manager and `ArduinoHttpClient` (if needed, though we use `HTTPClient.h` from core).
3.  Update the following variables in `main.ino`:
    - `ssid`: Your WiFi name.
    - `password`: Your WiFi password.
    - `serverUrl`: The IP address of your computer running the Django server (e.g., `http://192.168.1.50:8000/api/upload_frame/`).
4.  Select **AI-Thinker ESP32-CAM** as the board and upload.

### 2. Django Backend
1.  Navigate to the `backend/` directory.
2.  (Optional) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the server on your local network:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

### 3. Traffic Enforcement Logic
- The frame processing logic is located in `backend/traffic_app/views.py` under `process_speed_enforcement`.
- You can integrate your CV models (YOLO, OpenCV tracking) directly into that function.

## Notes
- Ensure your ESP32-CAM and computer are on the same WiFi network.
- For speed enforcement, you will need to calibrate the distance covered by the camera's field of view to calculate speed (Speed = Distance / Time).
