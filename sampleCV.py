#%%
import cv2
src = cv2.imread('sampleimage_2.jpg')
dst = cv2.flip(src, 0)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
