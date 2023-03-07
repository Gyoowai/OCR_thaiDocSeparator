# python pipeline.py pictures/example_02.jpg output/
import sys
import cv2
from preprocessor.preprocess import preprocess
from rowSeparator.rowSeparator import rowSeparator
from wordSeparator.wordSeparator import wordSeparator

if len(sys.argv) < 3:
    print("Please provide at least two arguments: image_path and output_path")
    exit()
else:
    IMG_PATH = sys.argv[1]
    OUT_DIR_PATH = sys.argv[2]
    print("Image path:", IMG_PATH)
    print("Output path:", OUT_DIR_PATH)

rgb_image, p_image = preprocess(IMG_PATH)
lines = rowSeparator(p_image)

count=0
for y_upper, y_lower in lines: 
  imgs = wordSeparator(rgb_image[y_upper:y_lower,:], p_image[y_upper:y_lower,:])
  for img in imgs: 
    filename = OUT_DIR_PATH + str(count) + ".jpg"
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename, img)
    count+=1