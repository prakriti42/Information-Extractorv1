import cv2 as cv 
import pytesseract as pt 
import numpy as np 
import logging as logger 
import json 

def extract(image):
        image= cv.imread(image)
        h,w,c = image.shape
        output = {}
        roi = [[(31, 23),(818 ,49) , "text", "Master B/L#"],
                [(30, 54),(815 ,81) , "text", "House B/L#"]   , 
                [(27, 83),(817 ,112) , "text", "Port of Loading"],
                [(28, 113),(816 ,139) , "text", "Port of UnLading"],
                [(820, 21),(1919 ,45) , "text", "Something"],
                [(819, 53),(1903 ,79) , "text", "ABC"],
                [(820, 85),(1919 ,104) , "text", "TEST"],
                [(820, 113),(1919 ,139) , "text", "AALU"]]
      
        scopy = image.copy()
        imgMask = np.zeros_like(scopy) 
        for x,r in enumerate(roi):
            imgshow = cv.addWeighted(scopy, 1, imgMask, 0.1, 0)
            imgCrop = imgshow[r[0][1]:r[1][1], r[0][0]:r[1][0]]
            output[r[3]] = str(pt.image_to_string(imgCrop)).replace("\n","").replace("\/x0c","").replace(r[3],"").replace("\f","")
        return output

def export_to_json(output):
        j = json.dumps(output)
        with open('output.json', 'w') as f:
            f.write(j)
            f.close()
        return logger.info("Done")

if __name__ == "__main__":
    output = extract("Image.png")
    export_to_json(output)

    