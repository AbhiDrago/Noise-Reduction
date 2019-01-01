import cv2
import numpy as np

Img=cv2.imread('noise.png');
cv2.imshow('Original Image',Img);
Red_Plane=Img[:,:,2];
blue_plane=Img[:,:,0];
green_plane=Img[:,:,1];
r,c=Red_Plane.shape;
img=Red_Plane;
members = [(0,0)] * 9
op=np.zeros((r,c),dtype=np.uint8);
for i in range(0,r-2):
    for j in range(0,c-2):
        members[0] = img[i-1,j-1]
        members[1] = img[i-1,j]
        members[2] = img[i-1,j+1]
        members[3] = img[i,j-1]
        members[4] = img[i,j]
        members[5] = img[i,j+1]
        members[6] = img[i+1,j-1]
        members[7] = img[i+1,j]
        members[8] = img[i+1,j+1]
        members.sort()
        op[i,j]=members[4]


img1=blue_plane;
op1=np.zeros((r,c),dtype=np.uint8);
for i in range(0,r-2):
    for j in range(0,c-2):
        members[0] = img1[i-1,j-1]
        members[1] = img1[i-1,j]
        members[2] = img1[i-1,j+1]
        members[3] = img1[i,j-1]
        members[4] = img1[i,j]
        members[5] = img1[i,j+1]
        members[6] = img1[i+1,j-1]
        members[7] = img1[i+1,j]
        members[8] = img1[i+1,j+1]
        members.sort()
        op1[i,j]=members[4]
img2=green_plane;
op2=np.zeros((r,c),dtype=np.uint8);
for i in range(0,r-2):
    for j in range(0,c-2):
        members[0] = img2[i-1,j-1]
        members[1] = img2[i-1,j]
        members[2] = img2[i-1,j+1]
        members[3] = img2[i,j-1]
        members[4] = img2[i,j]
        members[5] = img2[i,j+1]
        members[6] = img2[i+1,j-1]
        members[7] = img2[i+1,j]
        members[8] = img2[i+1,j+1]
        members.sort()
        op2[i,j]=members[4]

op3=np.zeros((r,c,3),dtype=np.uint8);
op3[:,:,0]=op1;
op3[:,:,1]=op2;
op3[:,:,2]=op;
cv2.imshow('output',op3)
cv2.waitKey(99999)
cv2.destroyAllWindows()
