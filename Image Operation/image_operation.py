import cv2

def gray_scale():
    img = cv2.imread('image.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.jpg', gray)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize():
    img = cv2.imread('image.png')
    resized_img = cv2.resize(img, (300, 300))
    cv2.imwrite('resized_img.jpg', resized_img)
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_img():
    img = cv2.imread('image.png')
    crop = img[50:140, 50:200]
    cv2.imwrite('cropped_image.jpg', crop)
    cv2.imshow('Cropped Image', crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_on_img():
    img = cv2.imread('image.png')
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
    cv2.circle(img, (300, 150), 50, (255, 0, 0), -1)
    cv2.line(img, (0, 0), (400, 300), (0, 0, 255), 2)
    cv2.imwrite('draw_img.jpg', img)
    cv2.imshow('Draw on Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate_img():
    img = cv2.imread('image.png')
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rotated_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_img = cv2.warpAffine(img, rotated_matrix, (w, h))
    cv2.imwrite('rotated_img.jpg', rotated_img)
    cv2.imshow('Rotated Image', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def text_img():
    img = cv2.imread('image.png')
    cv2.putText(img, 'OpenCV Demo', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5, cv2.LINE_AA)
    cv2.imwrite('text_img.jpg', img)
    cv2.imshow('Text Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------ Switch Case Style Menu ------------------

options = {
    1: gray_scale,
    2: resize,
    3: crop_img,
    4: draw_on_img,
    5: rotate_img,
    6: text_img
}

while True:
    print("\nChoose an option:")
    print("1: Grayscale")
    print("2: Resize")
    print("3: Crop")
    print("4: Draw on Image")
    print("5: Rotate Image")
    print("6: Text on Image")
    print("0: Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid number.")
