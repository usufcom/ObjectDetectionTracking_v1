import cv2
import os

def capture_faces(person_name="Teacher", camera_index=0):
    """
    Captures webcam frames and saves them to faces/person_name.
    Accepts a custom name and camera index.
    """
    if not person_name or type(person_name) != str:
        print("Error: Please provide a valid person's name as a string.")
        return

    # Set up the save directory inside the "faces" folder
    save_folder = os.path.join("faces", person_name)
    
    # Create the person's folder if it does not exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"Created new folder: {save_folder}")
    else:
        print(f"Folder ready: {save_folder}")

    # Count existing files so we don't overwrite older photos
    existing_files = [f for f in os.listdir(save_folder) if f.endswith('.png')]
    img_counter = len(existing_files) + 1

    # Open the webcam using the provided camera index variable
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Could not connect to camera at index {camera_index}.")
        return

    print(f"\n--- Face Capture Started for {person_name} (Camera {camera_index}) ---")
    print("Press 's' to save a photo.")
    print("Press 'q' or 'x' to quit.\n")

    while True:
        success, frame = cap.read()
        if not success or frame is None:
            print("Failed to read from camera.")
            break

        # Create a copy of the frame to draw text on (so the saved image stays clean)
        display_frame = frame.copy()
        
        # Display instructions and photo count on the live feed
        cv2.putText(display_frame, f"Subject: {person_name} | Photos saved: {img_counter - 1}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(display_frame, "Press 's' to save | 'q' to quit", 
                    (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Capture Training Images", display_frame)

        key = cv2.waitKey(1) & 0xFF
        
        # Save photo on 's'
        if key == ord('s'):
            img_name = os.path.join(save_folder, f"photo{img_counter}.png")
            cv2.imwrite(img_name, frame)
            print(f"Saved: {img_name}")
            img_counter += 1
            
        # Quit on 'q' or 'x'
        elif key == ord('q') or key == ord('x'):
            print("Exiting capture mode.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Test the function with defaults if run directly
    capture_faces()