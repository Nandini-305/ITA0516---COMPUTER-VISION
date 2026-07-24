import cv2

video = cv2.VideoCapture("cv video.mp4")

if not video.isOpened():
    print("Video not found!")
else:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Resize frame
        frame = cv2.resize(frame, (640, 480))

        cv2.imshow("EX6 - CV Fast Motion Video", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video.release()
