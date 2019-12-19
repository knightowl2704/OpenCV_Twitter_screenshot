<h2> Twitter Screenshot 'Following' Button segmentation using OpenCV </h2>


* OpenCV 
* Python 

**Task**
<br>
The task was to create bounding boxes around the 'following' buttons given in the screenshots from twitter.

**Approach**

One way to deal with this was using pre trained models and training them on the custom dataset. But even though this is a robust method, I feel that this task can be easily implemented by using **OpenCV** and the contour functions in OpenCV. And I believe in simplicity :)
<br>

My approach is basically creating a **colour filter**, since all the buttons are of same colour, with an upper threshold and a lower threshold of the button colour. Getting the correct values is little difficult, but after some hit and trial these can be tweaked easily.

This can be masked with the original image, resulting into an image just with the required colours.

This however includes whatever is in the blue color range. Basically the text which is blue colour or some profile pictures that have blue colour in them are also included. 

Now the challenge is to remove the unwanted texts and images. This can be done using the *contours* functions in OpenCV.

Run findcontours on the image obtained after masking, this will create an array `contours` that includes all the contours. Now we can see that the area of contours of the buttons should be same and in the case was close to 11000. All the rest of the contour areas were very small in range of 0-100. 

Thus I applied a thershold of 10000 on contour area and created a new array `contours1`. Appended all the contours with area > 10000.

Basically they all are the 'Following' buttons. 

Now we draw a bounding rectangle around the obtained contours and obtain their coordinates. 

**After Mask is applied:**
  
![Image](https://github.com/knightowl2704/OpenCV_Twitter_screenshot/blob/master/assets/Screenshot%20(48).png)

**Final Image:**

![FinalImage](https://github.com/knightowl2704/OpenCV_Twitter_screenshot/blob/master/assets/Screenshot%20(47).png)

