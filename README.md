# Image Segmentation from Images
Program to find Image histogrms, Harris Corner detection and SIFT Key Points. 
Further in the problem statement, it also highlight tasks such as finding Image Features, conducting object extraction and doing image segmentation using K-means.

**I have made it very easy to follow here with simple words and easy steps!**

# 1) Description of Project
This project aims to use the library called OpenCV (open Computer Vision) in Python to perform various operation on images such as segmentation and object extraction.

The problem statement has been provided, along with the two images that are taken as input.
The code in python is provided wich performs the image segmentation.

There is also a report added in which I have written the results.

**Example from current program:**

**Test Image:**

![diamond2](https://github.com/user-attachments/assets/c5ba6118-e39f-4a5a-877c-712e3ee6b625)

![dugong](https://github.com/user-attachments/assets/074d0f79-afa2-425a-b118-0a1c235f9668)


# 2) Getting Started
To run the code in Python, first we need to get the environment. 

## NOTE:

- If you are using Linux, just open a terminal and run the following commands. 
- If you using Windows, get the Linux Terminal from Microsoft Store (search up on Google if you don't know how to get around this).

## Follow the steps to get started:

#### i) Git clone the repository:

#### ii) Install Virtual Environment:
```shell
$ pip3 install virtualenv
```

#### iii) Activate the Virtual Environment:

Linux/Mac
```shell
$ python3 -m venv env
$ source env/bin/activate
```
Windows
```shell
$ python3 -m venv env
$ source env/Script/activate
```

#### iv) Install the required packages:
```shell
$ pip3 install -r requirement.txt
```

#### v) This step is for *Windows* users only (For Linux users, skip this step):
> When the Python file is run, it will display images. To view them, a software called Xming needs to be downloaded. 

> a) To download Xming, follow this link and click download: 
   - https://sourceforge.net/projects/xming/
> b) After Xming is downloaded, run the following command to see if it works:
```shell
$ xeyes
```
- If you see a small pop-up window with eyes, it works!
- if you don't see it, maybe try another version of Xming.

#### vi) Now to run the code:
```shell
$ python3 Image_Segmentation.py
```
> The code will take some time to run...
> Just press enter to run through the images, and you can see what number is detected in the "Output folder"!


# We are done! 









