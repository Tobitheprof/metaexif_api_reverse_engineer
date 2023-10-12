import os
import requests

# API endpoint
upload_url = "https://exifmeta.com/api/upload"

# Get the directory of your Python script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the filename of the image in the same directory
image_filename = "test3.jpeg"  # Change to the actual image file name

# Construct the full path to the image file
image_file_path = os.path.join(script_directory, image_filename)

# Read the image file
with open(image_file_path, 'rb') as image_file:
    # Send the POST request with the image file
    response = requests.post(
        upload_url,
        files={"image": (image_filename, image_file)}  # Attach the image file
    )

# Check the response
if response.status_code == 200:
    print("Image uploaded successfully.")
    response_data = response.json()
    # Process response_data as needed
    print(response_data)
else:
    print(f"Error uploading image. Status code: {response.status_code}")
    print(response.text)
