import cv2 as cv


img = cv.imread('fry.jpg')
# img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img_copy = img.copy()

# Hair rectangle
cv.rectangle(img_copy, (100,250), (400,25), (0,255,0))
cv.rectangle(img_copy, (100, 25), (200, 0), (0, 255, 0), cv.FILLED)
cv.putText(img_copy, 'Fry\'s Hair', (100, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

# Coat rectangle
cv.rectangle(img_copy, (100, 415), (370, 305), (255, 0, 0))
cv.rectangle(img_copy, (100, 305), (200, 280), (255, 0, 0), cv.FILLED)
cv.putText(img_copy, 'Fry\'s Coat', (100, 295), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

# Face rectangle
cv.rectangle(img_copy, (230, 330), (390, 175), (255, 255, 0))
cv.rectangle(img_copy, (230, 175), (330, 150), (255, 255, 0), cv.FILLED)
cv.putText(img_copy, 'Fry\'s Face', (230, 165), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))


cv.imshow('image', img_copy)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)