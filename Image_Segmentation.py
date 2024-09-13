#Image Segmentation
#Author : Shrenik Jobanputra
#Date Last Modified: 13/09/2024 

#All the imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

#===========  Start of Code =================================

# Original Diamond Image

imgDiaOrg = cv2.imread("diamond2.png") # Original Diamond Image
cv2.imshow("Diamond Original", imgDiaOrg ) # show the original Diamond Image
cv2.waitKey(0) # waits for a button press

#===================================================================
## Going to graph a histogram of the original Diamond Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDiaOrg = cv2.calcHist( [imgDiaOrg], [i], None, [256], [0,256] ) # histogram for the original Diamond Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDiaOrg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking

plt.title("ORIGNAL DIMAOND IMAGE")
plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes


#===================================================================

# 2 Times bigger Diamond Image

height, width = imgDiaOrg.shape[:2] # unpacks 2 things
imgDia2Size = cv2.resize( imgDiaOrg, (width * 2, height * 2), interpolation = cv2.INTER_CUBIC ) #INTER_CUBIC is for making it bigger
cv2.imshow("2 Times Bigger Diamond", imgDia2Size )  
cv2.waitKey(0)


#=================================================================
# Graphing the Histrogram for the 2 times bigger Diamond Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDia2Size = cv2.calcHist( [imgDia2Size], [i], None, [256], [0,256] ) # histogram for the original Diamond Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDia2Size, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking

plt.title("2 TIMES BIGGER DIMAOND IMAGE")
plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes


#================================================================

# 1/2 the size of Diamond Image

height, width = imgDiaOrg.shape[:2] # unpacks 2 things
imgDiaHalfSize = cv2.resize( imgDiaOrg, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA ) #INTER_AREA is for making it smaller
cv2.imshow("Half size of  Diamond", imgDiaHalfSize )  
cv2.waitKey(0)

#===============================================================

#Graphing the Histogram for the half Diamond Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDiaHalfSize = cv2.calcHist( [imgDiaHalfSize], [i], None, [256], [0,256] ) # histogram for the original Diamond Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDiaHalfSize, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("HALF SIZE DIMAOND IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================

# Rotation of the Diamond Original image ANTIclockwise by 90 degrees

height, width = imgDiaOrg.shape[:2]
imgDia90Deg = cv2.getRotationMatrix2D((width, height),90,1) #centre of rotation is width/2 and height/2, then angle, scale factor
transImgDia90Deg = np.float32([[1,0,int(width/2)],[0,1,int(height/2)]]) # translation matrix

transImgDia90DegAff = cv2.warpAffine(imgDiaOrg, transImgDia90Deg, (int(3*width/2), int(3*height/2))) # affine tranform for the translated image

imgDia90DegAff = cv2.warpAffine( transImgDia90DegAff, imgDia90Deg,(int(4*width/2),int(4* height/2))) # creates the size of the background from the centre of the image!!
cv2.imshow("90 degrees Rotated anticlockwise Diamond", imgDia90DegAff)
cv2.waitKey(0)

#===========================================================

#Graphing the Histogram for the Diamond Image rotated ACW 90 degrees

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDia90Deg = cv2.calcHist( [imgDia90DegAff], [i], None, [256], [0,256] ) # histogram for the original Diamond Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDia90Deg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("90 DEG ACW DIMAOND IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================


# Rotation of the Diamond Original image ANTIclockwise by 135 degrees

height, width = imgDiaOrg.shape[:2]
imgDia135Deg = cv2.getRotationMatrix2D((width, height),135,1) #centre of rotation is width/2 and height/2, then angle, scale factor
transImgDia135Deg = np.float32([[1,0,int(width/2)],[0,1,int(height/2)]]) # translation matrix

transImgDia135DegAff = cv2.warpAffine(imgDiaOrg, transImgDia135Deg, (int(3*width/2), int(3*height/2))) # affine tranform for the translated image

imgDia135DegAff = cv2.warpAffine( transImgDia135DegAff, imgDia135Deg,(int(4*width/2),int(4* height/2))) # creates the size of the background from the centre of the image!!
cv2.imshow("135 degrees Rotated anticlockwise Diamond", imgDia135DegAff)
cv2.waitKey(0)

#===========================================================

#Graphing the Histogram for the Diamond Image rotated ACW 135 degrees

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDia135Deg = cv2.calcHist( [imgDia135DegAff], [i], None, [256], [0,256] ) # histogram for the original Diamond Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDia135Deg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("135 DEG ACW DIMAOND IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================

# Doing the Harris Corner Detector for the the Diamond Images

imgDiaGrayOrg = cv2.cvtColor(imgDiaOrg, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDiaGrayOrg = np.float32(imgDiaGrayOrg) #converting to numpy float32 type
dstDiaOrg = cv2.cornerHarris(imgDiaGrayOrg,2,3,0.04)
#result is dilated for making the corners, not important
dstDiaOrg = cv2.dilate(dstDiaOrg, None )
#Threshold for an optimal value
imgDiaOrg2 = imgDiaOrg # we won't be using the copy of the image
imgDiaOrg2[dstDiaOrg>0.01*dstDiaOrg.max()] = [255,0,0] #Blue color for the detecting corners

imgDiaGray2Size = cv2.cvtColor(imgDia2Size, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDiaGray2Size = np.float32(imgDiaGray2Size) #converting to numpy float32 type
dstDia2Size = cv2.cornerHarris(imgDiaGray2Size,2,3,0.04)
#result is dilated for making the corners, not important
dstDia2Size = cv2.dilate(dstDia2Size, None )
#Threshold for an optimal value
imgDia2Size2 = imgDia2Size # we won't be using the copy of the image
imgDia2Size2[dstDia2Size>0.01*dstDia2Size.max()] = [255,0,0] #Blue color for the detecting corners

imgDiaGrayHalfSize = cv2.cvtColor(imgDiaHalfSize, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDiaGrayHalfSize = np.float32(imgDiaGrayHalfSize) #converting to numpy float32 type
dstDiaHalfSize = cv2.cornerHarris(imgDiaGrayHalfSize,2,3,0.04)
#result is dilated for making the corners, not important
dstDiaHalfSize = cv2.dilate(dstDiaHalfSize, None )
#Threshold for an optimal value
imgDiaHalfSize2 = imgDiaHalfSize # we won't be using the copy of the image
imgDiaHalfSize2[dstDiaHalfSize>0.1*dstDiaHalfSize.max()] = [255,0,0] #Blue color for the detecting corners

imgDiaGray90DegAff = cv2.cvtColor(imgDia90DegAff, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDiaGray90DegAff = np.float32(imgDiaGray90DegAff) #converting to numpy float32 type
dstDia90DegAff = cv2.cornerHarris(imgDiaGray90DegAff,2,3,0.04)
#result is dilated for making the corners, not important
dstDia90DegAff = cv2.dilate(dstDia90DegAff, None )
#Threshold for an optimal value
imgDia90DegAff2 = imgDia90DegAff # we won't be using the copy of the image
imgDia90DegAff2[dstDia90DegAff>0.01*dstDia90DegAff.max()] = [255,0,0] #Blue color for the detecting corners

imgDiaGray135DegAff = cv2.cvtColor(imgDia135DegAff, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDiaGray135DegAff = np.float32(imgDiaGray135DegAff) #converting to numpy float32 type
dstDia135DegAff = cv2.cornerHarris(imgDiaGray135DegAff,2,3,0.04)
#result is dilated for making the corners, not important
dstDia135DegAff = cv2.dilate(dstDia135DegAff, None )
#Threshold for an optimal value
imgDia135DegAff2 = imgDia135DegAff # we won't be using the copy of the image
imgDia135DegAff2[dstDia135DegAff>0.01*dstDia135DegAff.max()] = [255,0,0] #Blue color for the detecting corners



cv2.imshow("Original Diamond Harris Corners", imgDiaOrg2)
cv2.imshow("2 Size Diamond Harris Corners", imgDia2Size2)
cv2.imshow("half Size Diamond Harris Corners", imgDiaHalfSize2)
cv2.imshow("90 Deg Diamond Harris Corners", imgDia90DegAff2)
cv2.imshow("135 Deg Dimamond Harris Corners", imgDia135DegAff2)
cv2.waitKey(0)

#============================================================

# SIFT Feature descriptor on the images

sift = cv2.xfeatures2d.SIFT_create()
KeyPointDiaOrg = sift.detect(imgDiaGrayOrg, None )
imgDiaOrg3 = imgDiaOrg
imgDiaOrg3 = cv2.drawKeypoints(imgDiaGrayOrg, KeyPointDiaOrg )
cv2.imshow("SIFT Diamond Original", imgDiaOrg3)

cv2.waitKey(0)


cv2.destroyAllWindows() # closes the windows before hand

#=============================================================

# Original Dugong Image
imgDuOrg = cv2.imread("dugong.jpg")  # Original Dugong Image
cv2.imshow("Dugong Original", imgDuOrg ) # show the original Dugong Image

cv2.waitKey(0) # waits for a button press

#===================================================================
## Going to graph a histogram of the original Dugong Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDuOrg = cv2.calcHist( [imgDuOrg], [i], None, [256], [0,256] ) # histogram for the original Dugong Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDuOrg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking

plt.title("ORIGNAL Dugong IMAGE")
plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes


#===================================================================

# 2 Times bigger Dugong Image

height, width = imgDuOrg.shape[:2] # unpacks 2 things
imgDu2Size = cv2.resize( imgDuOrg, (width * 2, height * 2), interpolation = cv2.INTER_CUBIC ) #INTER_CUBIC is for making it bigger
cv2.imshow("2 Times Bigger Dugong", imgDu2Size )  
cv2.waitKey(0)


#=================================================================
# Graphing the Histrogram for the 2 times bigger Dugong Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDu2Size = cv2.calcHist( [imgDu2Size], [i], None, [256], [0,256] ) # histogram for the original Dugong Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDu2Size, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking

plt.title("2 TIMES BIGGER Dugong IMAGE")
plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes


#================================================================

# 1/2 the size of Dugong Image

height, width = imgDuOrg.shape[:2] # unpacks 2 things
imgDuHalfSize = cv2.resize( imgDuOrg, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA ) #INTER_AREA is for making it smaller
cv2.imshow("Half size of  Dugong", imgDuHalfSize )  
cv2.waitKey(0)

#===============================================================

#Graphing the Histogram for the half Dugong Image

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDuHalfSize = cv2.calcHist( [imgDuHalfSize], [i], None, [256], [0,256] ) # histogram for the original Dugong Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDuHalfSize, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("HALF SIZE Dugong IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================

# Rotation of the Dugong Original image ANTIclockwise by 90 degrees

height, width = imgDuOrg.shape[:2]
imgDu90Deg = cv2.getRotationMatrix2D((width, height),90,1) #centre of rotation is width/2 and height/2, then angle, scale factor
transImgDu90Deg = np.float32([[1,0,int(width/2)],[0,1,int(height/2)]]) # translation matrix

transImgDu90DegAff = cv2.warpAffine(imgDuOrg, transImgDu90Deg, (int(3*width/2), int(3*height/2))) # affine tranform for the translated image

imgDu90DegAff = cv2.warpAffine( transImgDu90DegAff, imgDu90Deg,(int(4*width/2),int(4* height/2))) # creates the size of the background from the centre of the image!!
cv2.imshow("90 degrees Rotated anticlockwise Dugong", imgDu90DegAff)
cv2.waitKey(0)

#===========================================================

#Graphing the Histogram for the Dugong Image rotated ACW 90 degrees

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDu90Deg = cv2.calcHist( [imgDu90DegAff], [i], None, [256], [0,256] ) # histogram for the original Dugong Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDu90Deg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("90 DEG ACW Dugong IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================


# Rotation of the Dugong Original image ANTIclockwise by 135 degrees

height, width = imgDuOrg.shape[:2]
imgDu135Deg = cv2.getRotationMatrix2D((width, height),135,1) #centre of rotation is width/2 and height/2, then angle, scale factor
transImgDu135Deg = np.float32([[1,0,int(width/2)],[0,1,int(height/2)]]) # translation matrix

transImgDu135DegAff = cv2.warpAffine(imgDuOrg, transImgDu135Deg, (int(3*width/2), int(3*height/2))) # affine tranform for the translated image

imgDu135DegAff = cv2.warpAffine( transImgDu135DegAff, imgDu135Deg,(int(4*width/2),int(4* height/2))) # creates the size of the background from the centre of the image!!
cv2.imshow("135 degrees Rotated anticlockwise Dugong", imgDu135DegAff)
cv2.waitKey(0)

#===========================================================

#Graphing the Histogram for the Dugong Image rotated ACW 135 degrees

color = ('b', 'g', 'r' )
counter = 0

for i, col in enumerate(color):
    histDu135Deg = cv2.calcHist( [imgDu135DegAff], [i], None, [256], [0,256] ) # histogram for the original Dugong Image with 256 bins(buckets) with equl width and the x axis goes from 0 to 256
    plt.plot( histDu135Deg, color = col ) # plots all the colors
    plt.xlim([0,256])

plt.plot(block=False) # plt.show() is a blocking function, which means it does not go to the next line until the plot has been closed mannualy by clicking. So we turn off blocking
plt.title("135 DEG ACW Dugong IMAGE")

plt.pause(1) # the plot stays on for 2 seconds before going to next line 
plt.close() # the current plot closes

#================================================================

# Doing the Harris Corner Detector for the the Dugong Images

imgDuGrayOrg = cv2.cvtColor(imgDuOrg, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDuGrayOrg = np.float32(imgDuGrayOrg) #converting to numpy float32 type
dstDuOrg = cv2.cornerHarris(imgDuGrayOrg,2,3,0.04)
#result is dilated for making the corners, not important
dstDuOrg = cv2.dilate(dstDuOrg, None )
#Threshold for an optimal value
imgDuOrg2 = imgDuOrg # we won't be using the copy of the image
imgDuOrg2[dstDuOrg>0.01*dstDuOrg.max()] = [255,0,0] #Blue color for the detecting corners

imgDuGray2Size = cv2.cvtColor(imgDu2Size, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDuGray2Size = np.float32(imgDuGray2Size) #converting to numpy float32 type
dstDu2Size = cv2.cornerHarris(imgDuGray2Size,2,3,0.04)
#result is dilated for making the corners, not important
dstDu2Size = cv2.dilate(dstDu2Size, None )
#Threshold for an optimal value
imgDu2Size2 = imgDu2Size # we won't be using the copy of the image
imgDu2Size2[dstDu2Size>0.01*dstDu2Size.max()] = [255,0,0] #Blue color for the detecting corners

imgDuGrayHalfSize = cv2.cvtColor(imgDuHalfSize, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDuGrayHalfSize = np.float32(imgDuGrayHalfSize) #converting to numpy float32 type
dstDuHalfSize = cv2.cornerHarris(imgDuGrayHalfSize,2,3,0.04)
#result is dilated for making the corners, not important
dstDuHalfSize = cv2.dilate(dstDuHalfSize, None )
#Threshold for an optimal value
imgDuHalfSize2 = imgDuHalfSize # we won't be using the copy of the image
imgDuHalfSize2[dstDuHalfSize>0.1*dstDuHalfSize.max()] = [255,0,0] #Blue color for the detecting corners

imgDuGray90DegAff = cv2.cvtColor(imgDu90DegAff, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDuGray90DegAff = np.float32(imgDuGray90DegAff) #converting to numpy float32 type
dstDu90DegAff = cv2.cornerHarris(imgDuGray90DegAff,2,3,0.04)
#result is dilated for making the corners, not important
dstDu90DegAff = cv2.dilate(dstDu90DegAff, None )
#Threshold for an optimal value
imgDu90DegAff2 = imgDu90DegAff # we won't be using the copy of the image
imgDu90DegAff2[dstDu90DegAff>0.01*dstDu90DegAff.max()] = [255,0,0] #Blue color for the detecting corners

imgDuGray135DegAff = cv2.cvtColor(imgDu135DegAff, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
imgDuGray135DegAff = np.float32(imgDuGray135DegAff) #converting to numpy float32 type
dstDu135DegAff = cv2.cornerHarris(imgDuGray135DegAff,2,3,0.04)
#result is dilated for making the corners, not important
dstDu135DegAff = cv2.dilate(dstDu135DegAff, None )
#Threshold for an optimal value
imgDu135DegAff2 = imgDu135DegAff # we won't be using the copy of the image
imgDu135DegAff2[dstDu135DegAff>0.01*dstDu135DegAff.max()] = [255,0,0] #Blue color for the detecting corners



cv2.imshow("Original Dugong Harris Corners", imgDuOrg2)
cv2.imshow("2 Size Dugong Harris Corners", imgDu2Size2)
cv2.imshow("half Size Dugong Harris Corners", imgDuHalfSize2)
cv2.imshow("90 Deg Dugong Harris Corners", imgDu90DegAff2)
cv2.imshow("135 Deg Dugong Harris Corners", imgDu135DegAff2)
cv2.waitKey(0)

#============================================================


cv2.destroyAllWindows() # closes the windows before hand


