import cv2
import numpy as np


def add_horizontal_line(image, y_position):
    color = (255, 0, 0)
    thickness = 1
    cv2.line(image, (0, y_position), (image.shape[1], y_position), color, thickness)
    return image

def check_fill_level(image, y_position, threshold=1000, min_contour_area=500):

    below_line = image[y_position:, :]
    below_gray = cv2.cvtColor(below_line, cv2.COLOR_BGR2GRAY)

    white_pixel_mask = below_gray > 200 
    white_pixel_count = np.sum(white_pixel_mask) 

    if white_pixel_count > threshold:
        contours, _ = cv2.findContours(white_pixel_mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        defective_count = 0 
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area: 
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y + y_position), (x + w, y + y_position + h), (0, 0, 255), 2)  # Kırmızı kutu
                defective_count += 1 
        return defective_count 
    else:
        return 0  

def main(image_path, y_position, threshold=1000, min_contour_area=500):
    image = cv2.imread(image_path)
    image_with_line = add_horizontal_line(image, y_position)
    defective_count = check_fill_level(image_with_line, y_position, threshold, min_contour_area)

    if defective_count > 0:
        print(f"{defective_count} hatali dolum tespit edildi!")
    else:
        print("Dolum normal.")

    cv2.imshow("Image", image_with_line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'C:/Users/fatma/PycharmProjects/week1/goruntu.PNG'
y_position = 55 
threshold = 1000
min_contour_area = 500 

main(image_path, y_position, threshold, min_contour_area)
