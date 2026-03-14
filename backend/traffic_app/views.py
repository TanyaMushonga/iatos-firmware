import os
import time
import numpy as np
import cv2
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Placeholder for Speed Enforcement Logic
def process_speed_enforcement(image_data):
    # image_data is raw JPEG bytes
    # 1. Convert to OpenCV format
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Invalid image"}

    # 2. RUN CV MODEL (YOLO, Tracking, etc.)
    # For now, just "detect" a vehicle at a random speed
    # In reality, you'd compare this frame with previous ones
    mock_speed = 50 + (time.time() % 20) 

    return {"speed": round(mock_speed, 2), "timestamp": time.time()}

@csrf_exempt
def upload_frame(request):
    if request.method == 'POST':
        # The ESP32 sends raw binary data in the body
        image_data = request.body
        
        if not image_data:
            return JsonResponse({"status": "error", "message": "No data received"}, status=400)

        # Optional: Save frame for debugging
        # filename = f"frames/frame_{int(time.time()*1000)}.jpg"
        # default_storage.save(filename, ContentFile(image_data))

        # Process the frame
        result = process_speed_enforcement(image_data)

        return JsonResponse({
            "status": "success", 
            "data": result
        })

    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=405)
