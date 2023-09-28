# Image-to-Pencil-Sketch
This Python code demonstrates how to transform a regular image into a pencil sketch using the OpenCV library. 
A pencil sketch effect can give your photos an artistic and hand-drawn appearance, making them visually appealing.

The Key Steps:
1. Importing the Libraries: Begin by importing the necessary libraries, including OpenCV (cv2).
2. Load the Image: Using OpenCV, load the image you want to convert into a pencil sketch.
3. Converting to Gray: Convert the loaded image to grayscale. This step simplifies the image by removing color information.
4. Invert the Image: Invert the grayscale image by subtracting it from 255. This step creates a negative image. (the max intensity value is
   255, thus each pixel is subtracted from 255 to produce the output image)
5. Blur the Image: Apply a Gaussian blur to the inverted image. This step will smoothen the image and reduce any noise.
6. Blend the Images: Blend the original grayscale image with the blurred, inverted image to create the pencil sketch effect. This can be done using the cv2.divide function.
7. Display the Result: Show the original image and the pencil sketch side by side for visual comparison.



The technique used in developing this code can be summarised as:
Original Image -> Gray Scale -> Invert -> Blur -> Invert -> Pencil Sketch
