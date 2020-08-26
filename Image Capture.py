#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
cam=cv2.VideoCapture(0)
while cam.isOpened():
    i, frame = cam.read()
    if i:
        gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        cv2.imshow('Title',gray)
        cv2.imwrite('Image.jpg',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release
cv2.destroyAllWindows()


# In[ ]:




