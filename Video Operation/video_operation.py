import cv2
import os

def show_video(video_path):
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

def read_and_save_frames(video_path, output_video_path):
    video = cv2.VideoCapture(video_path)
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while True:
        ret, frame = video.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow("Frames", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    out.release()
    video.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_video_path}")

def extract_audio(video_path, audio_output):
    if not VideoFileClip:
        print("moviepy is not installed. Cannot extract audio.")
        return
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_output)
    print(f"Audio extracted and saved as {audio_output}")

def extract_images_from_video(video_path, output_folder):
    video = cv2.VideoCapture(video_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_num = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        filename = os.path.join(output_folder, f"frame_{frame_num:04d}.jpg")
        cv2.imwrite(filename, frame)
        frame_num += 1
        cv2.imshow("Extracting Frames", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    print(f"Saved {frame_num} images to '{output_folder}' folder.")

# ------------------------------
# MENU
# ------------------------------
def video_menu():
    video_path = "video.mp4"  
    while True:
        print("\n--- Video Operations Menu ---")
        print("1. Show Video")
        print("2. Read & Save Video as Output")
        print("3. Extract Audio from Video")
        print("4. Extract Images from Video Frames")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_video(video_path)
        elif choice == "2":
            output_path = "output.mp4"
            read_and_save_frames(video_path, output_path)
        elif choice == "3":
            extract_audio(video_path, "audio.mp3")
        elif choice == "4":
            extract_images_from_video(video_path, "extracted_frames")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
video_menu()
