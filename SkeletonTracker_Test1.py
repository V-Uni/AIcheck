import cv2
import mediapipe as mp

# Initialize the pose estimation model
mp_pose = mp.solutions.pose.Pose()

# Create a video capture object
cap = cv2.VideoCapture(0)

# Start the tracking
while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the human skeletons in the frame
    results = mp_pose.process(rgb_frame)

    # Extract the skeleton data for each person
    for person in results.pose_landmarks:
        # Iterate over the landmarks for the current person
        for landmark in person.landmark:
            # Get the landmark position
            landmark_position = landmark.x, landmark.y

            # Draw the landmark on the frame
            cv2.circle(frame, landmark_position, 2, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check if the user wants to quit
    key = cv2.waitKey(1)
    if key == ord('Q'):
        break

# Stop the tracking
cap.release()
cv2.destroyAllWindows()
