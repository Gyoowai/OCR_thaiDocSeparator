import cv2

def preprocess(IMAGE_PATH):
  image = cv2.imread(IMAGE_PATH)
  rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # Remove paper edge area from scanning
  rgb_image = rgb_image[50:-50,50:-50]

  # Binarization: Otsu's Binarization
  p_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY) 
  p_image = cv2.threshold(p_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  return rgb_image, p_image