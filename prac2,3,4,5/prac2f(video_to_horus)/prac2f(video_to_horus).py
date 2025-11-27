#video to horus :-
import cv2
import pandas as pd

# Input and Output Files
video_file = "C:/Atiya/FY-MSC-IT/Data Science/DS Practs/eagle.mp4"   # Path to the video file
output_csv = "C:/Atiya/FY-MSC-IT/Data Science/DS Practs/HORUS-Video.csv"   # Path to save the CSV file

# Open the video file
cap = cv2.VideoCapture(video_file)

# Initialize a list to store data
horus_data = []

# Process each frame
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()  # Read a frame
    if not ret:
        break  # Stop if no more frames are available

    frame_count += 1  # Keep track of the frame number
    print("Processing Frame {}...".format(frame_count))

    # Convert frame to rows of data
    for y in range(frame.shape[0]):  # Loop through rows (height)
        for x in range(frame.shape[1]):  # Loop through columns (width)
            red, green, blue = frame[y, x]  # Get RGB values for each pixel
            horus_data.append([frame_count, y, x, red, green, blue])  # Add data to the list

# Close the video file
cap.release()

# Create a DataFrame and save to CSV
columns = ["Frame", "Y", "X", "Red", "Green", "Blue"]
df = pd.DataFrame(horus_data, columns=columns)
df.to_csv(output_csv, index=False)

print("Video converted to HORUS format and saved as:", output_csv)
