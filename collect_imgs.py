import os
import cv2

# Directory setup
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 5
dataset_size = 100

# Function to find the first available camera
def find_camera():
    for index in range(5):  # Trying indices from 0 to 4
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Using camera index: {index}")
            return cap
        cap.release()
    return None

# Initialize video capture
cap = find_camera()
if cap is None:
    print("Error: Could not find any available camera.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    # Prompt user to start collecting data for the class
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break
        if frame is None or frame.size == 0:
            print("Error: Captured frame is empty")
            break

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    # Capture dataset_size number of frames for the class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break
        if frame is None or frame.size == 0:
            print("Error: Captured frame is empty")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)

        counter += 1

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
