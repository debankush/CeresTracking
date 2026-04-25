import numpy as np
import numpy.linalg as linalg
import math
import cv2
import sys

fov = 9.85

ceresX = 155804126.275
ceresY = 178601623.169
ceresZ = -219473130.103

ceresR = 476.0
earthR = 6378.1

ceresDist = 323020000.0 #323019719.31274

obvloc = [2133.557,	-5150.694,	-3090.097]
zenith = np.array([0.334718, -0.808054, -0.484782])
north = np.array([-0.459117, -0.589109, 0.664953])
az = 44.687611
alt = 65.389639
dirc = np.array([-0.68124169,  0.56023172,  0.47122235])

targetVoxel1 = [0] * 3
targetVoxel2 = [0] * 3
targetVoxel3 = [0] * 3
targetVoxel4 = [0] * 3
targetVoxel5 = [0] * 3
targetVoxel6 = [0] * 3
targetVoxel7 = [0] * 3
targetVoxel8 = [0] * 3

targetVoxel1[0] = 155804126.275+500
targetVoxel1[1] = 178601623.169+500
targetVoxel1[2] = -219473130.103+500
targetVoxel2[0] = 155804126.275+500
targetVoxel2[1] = 178601623.169+500
targetVoxel2[2] = -219473130.103-500
targetVoxel3[0] = 155804126.275+500
targetVoxel3[1] = 178601623.169-500
targetVoxel3[2] = -219473130.103+500
targetVoxel4[0] = 155804126.275+500
targetVoxel4[1] = 178601623.169-500
targetVoxel4[2] = -219473130.103-500
targetVoxel5[0] = 155804126.275-500
targetVoxel5[1] = 178601623.169+500
targetVoxel5[2] = -219473130.103+500
targetVoxel6[0] = 155804126.275-500
targetVoxel6[1] = 178601623.169+500
targetVoxel6[2] = -219473130.103-500
targetVoxel7[0] = 155804126.275-500
targetVoxel7[1] = 178601623.169-500
targetVoxel7[2] = -219473130.103+500
targetVoxel8[0] = 155804126.275-500
targetVoxel8[1] = 178601623.169-500
targetVoxel8[2] = -219473130.103-500

#print(targetVoxel1)
#print(targetVoxel8)

targetMin = [155804626.275,178601123.169,-219472630.103]
targetMax = [155803626.275,178601123.169,-219472630.103]
distances = [0]*8

for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel1[0]-obvloc[0])**2 + (targetVoxel1[1]-obvloc[1])**2 + (targetVoxel1[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel2[0]-obvloc[0])**2 + (targetVoxel2[1]-obvloc[1])**2 + (targetVoxel2[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel3[0]-obvloc[0])**2 + (targetVoxel3[1]-obvloc[1])**2 + (targetVoxel3[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel4[0]-obvloc[0])**2 + (targetVoxel4[1]-obvloc[1])**2 + (targetVoxel4[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel5[0]-obvloc[0])**2 + (targetVoxel5[1]-obvloc[1])**2 + (targetVoxel5[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel6[0]-obvloc[0])**2 + (targetVoxel6[1]-obvloc[1])**2 + (targetVoxel6[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel7[0]-obvloc[0])**2 + (targetVoxel7[1]-obvloc[1])**2 + (targetVoxel7[2]-obvloc[2])**2)
for i in range(0,3):
    distances[i] = math.sqrt((targetVoxel8[0]-obvloc[0])**2 + (targetVoxel8[1]-obvloc[1])**2 + (targetVoxel8[2]-obvloc[2])**2)

distMax = 0
distMin = 0

for i in range(0,8):
    if(distances[distMax] < distances[i]):
        distMax = i
    if(distances[distMin] > distances[i]):
        distMin = i

if(distMin == 0):
    targetMin[0] = targetVoxel1[0]
    targetMin[1] = targetVoxel1[1]
    targetMin[2] = targetVoxel1[2]
elif(distMin == 1):
    targetMin[0] = targetVoxel2[0]
    targetMin[1] = targetVoxel2[1]
    targetMin[2] = targetVoxel2[2]
elif(distMin == 2):
    targetMin[0] = targetVoxel3[0]
    targetMin[1] = targetVoxel3[1]
    targetMin[2] = targetVoxel3[2]
elif(distMin == 3):
    targetMin[0] = targetVoxel4[0]
    targetMin[1] = targetVoxel4[1]
    targetMin[2] = targetVoxel4[2]
elif(distMin == 4):
    targetMin[0] = targetVoxel5[0]
    targetMin[1] = targetVoxel5[1]
    targetMin[2] = targetVoxel5[2]
elif(distMin == 5):
    targetMin[0] = targetVoxel6[0]
    targetMin[1] = targetVoxel6[1]
    targetMin[2] = targetVoxel6[2]
elif(distMin == 6):
    targetMin[0] = targetVoxel7[0]
    targetMin[1] = targetVoxel7[1]
    targetMin[2] = targetVoxel7[2]
elif(distMin == 7):
    targetMin[0] = targetVoxel8[0]
    targetMin[1] = targetVoxel8[1]
    targetMin[2] = targetVoxel8[2]

if(distMax == 0):
    targetMax[0] = targetVoxel1[0]
    targetMax[1] = targetVoxel1[1]
    targetMax[2] = targetVoxel1[2]
elif(distMax == 1):
    targetMax[0] = targetVoxel2[0]
    targetMax[1] = targetVoxel2[1]
    targetMax[2] = targetVoxel2[2]
elif(distMax == 2):
    targetMax[0] = targetVoxel3[0]
    targetMax[1] = targetVoxel3[1]
    targetMax[2] = targetVoxel3[2]
elif(distMax == 3):
    targetMax[0] = targetVoxel4[0]
    targetMax[1] = targetVoxel4[1]
    targetMax[2] = targetVoxel4[2]
elif(distMax == 4):
    targetMax[0] = targetVoxel5[0]
    targetMax[1] = targetVoxel5[1]
    targetMax[2] = targetVoxel5[2]
elif(distMax == 5):
    targetMax[0] = targetVoxel6[0]
    targetMax[1] = targetVoxel6[1]
    targetMax[2] = targetVoxel6[2]
elif(distMax == 6):
    targetMax[0] = targetVoxel7[0]
    targetMax[1] = targetVoxel7[1]
    targetMax[2] = targetVoxel7[2]
elif(distMax == 7):
    targetMax[0] = targetVoxel8[0]
    targetMax[1] = targetVoxel8[1]
    targetMax[2] = targetVoxel8[2]

#targetMin[0] = targetVoxel[distMin][0]
#targetMin[1] = targetVoxel[distMin][1]
#targetMin[2] = targetVoxel[distMin][2]

#targetMax[0] = targetVoxel[distMax][0]
#targetMax[1] = targetVoxel[distMax][1]
#targetMax[2] = targetVoxel[distMax][2] 

print(targetMax)
print(targetMin)

def makeUnit(x):
    return x / linalg.norm(x)

def xParV(x, v):
    # (x' * v / norm(v)) * v / norm(v)
    # = (x' * v) * v / norm(v)^2
    # = (x' * v) * v / (v' * v)
    return np.dot(x, v) / np.dot(v, v) * v


def xPerpV(x, v):
    return x - xParV(x, v)


def xProjectV(x, v):
    par = xParV(x, v)
    perp = x - par
    return {'par': par, 'perp': perp}


def rotateAbout(a, b, theta):
    proj = xProjectV(a, b)
    w = np.cross(b, proj['perp'])
    return (proj['par'] +
            proj['perp'] * np.cos(theta) +
            linalg.norm(proj['perp']) * makeUnit(w) * np.sin(theta))

img = cv2.imread('frame_1799.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows = img.shape[0]
columns = img.shape[1]

ceresVec = [ceresX-obvloc[0],ceresY-obvloc[1],ceresZ-obvloc[2]]
ceresVec = ceresVec/np.linalg.norm(ceresVec)

d = [np.array]*4

for i in range(0, 4):
    if(i < 2):
        targetVector = north
        axis = zenith
        amount = az
        targetVector = rotateAbout(targetVector, axis, amount)
        axis = np.cross(targetVector, zenith)
        if(i % 2 == 0):
            amount = alt
            targetVector = rotateAbout(targetVector, axis, amount)
            d[i] = targetVector
        else:
            amount = 360 - alt
            targetVector = rotateAbout(targetVector, axis, amount)
            d[i] = targetVector
    else:
        
        targetVector = north
        axis = zenith
        amount = 360 - az
        targetVector = rotateAbout(targetVector, axis, amount)
        axis = np.cross(targetVector, zenith)
        if(i % 2 == 0):
            amount = alt
            targetVector = rotateAbout(targetVector, axis, amount)
            d[i] = targetVector
        else:
            amount = 360 - alt
            targetVector = rotateAbout(targetVector, axis, amount)
            d[i] = targetVector

for z in range(0,4):
    for i in range(0, rows):
        for j in range(0, columns):
            if(img[i][j] == 255):
                targetVector = d[z]
                screenspaceX = np.cross(zenith, d[z])
                screenspaceY = np.cross(screenspaceX, d[z])
                axis = screenspaceY
                amount = (abs((rows/2)-i)*((fov/2)/(rows/2)))*(np.pi/180)
                txc = rotateAbout(targetVector, axis, amount)
                amount = 360 - amount
                txcc = rotateAbout(targetVector, axis, amount)
                axis = screenspaceX
                amount = (abs((columns/2)-j)*((fov/2)/(columns/2)))*(np.pi/180)
                tyc = rotateAbout(targetVector, axis, amount)
                amount = 360 - amount
                tycc = rotateAbout(targetVector, axis, amount)
                t1 = txc + tyc
                t1 = t1/np.sqrt(np.sum(t1**2))
                t2 = txcc + tyc
                t2 = t2/np.sqrt(np.sum(t2**2))
                t3 = txc + tycc
                t3 = t3/np.sqrt(np.sum(t3**2))
                t4 = txcc + tycc
                t4 = t4/np.sqrt(np.sum(t4**2))
                print(np.arccos(np.clip(np.dot(ceresVec, t1), -1.0, 1.0))*(180/np.pi))
                print(np.arccos(np.clip(np.dot(ceresVec, t2), -1.0, 1.0))*(180/np.pi))
                print(np.arccos(np.clip(np.dot(ceresVec, t3), -1.0, 1.0))*(180/np.pi))
                print(np.arccos(np.clip(np.dot(ceresVec, t4), -1.0, 1.0))*(180/np.pi))
                if(np.arccos(np.clip(np.dot(ceresVec, t1), -1.0, 1.0))*(180/np.pi) > 150):
                    print("match found")
                    print(ceresX)
                    print(ceresY)
                    print(ceresZ)
                    sys.exit()
                if(np.arccos(np.clip(np.dot(ceresVec, t2), -1.0, 1.0))*(180/np.pi) > 150):
                    print("match found")
                    print(ceresX)
                    print(ceresY)
                    print(ceresZ)
                    sys.exit()
                if(np.arccos(np.clip(np.dot(ceresVec, t3), -1.0, 1.0))*(180/np.pi) > 150):
                    print("match found")
                    print(ceresX)
                    print(ceresY)
                    print(ceresZ)
                    sys.exit()
                if(np.arccos(np.clip(np.dot(ceresVec, t4), -1.0, 1.0))*(180/np.pi) > 150):
                    print("match found")
                    print(ceresX)
                    print(ceresY)
                    print(ceresZ)
                    sys.exit()
                t1 = [i * 323019719.31274 for i in t1]
                t2 = [i * 323019719.31274 for i in t2]
                t3 = [i * 323019719.31274 for i in t3]
                t4 = [i * 323019719.31274 for i in t4]
                t1[0] += obvloc[0]
                t1[1] += obvloc[1]
                t1[2] += obvloc[2]
                t2[0] += obvloc[0]
                t2[1] += obvloc[1]
                t2[2] += obvloc[2]
                t3[0] += obvloc[0]
                t3[1] += obvloc[1]
                t3[2] += obvloc[2]
                t4[0] += obvloc[0]
                t4[1] += obvloc[1]
                t4[2] += obvloc[2]
                #print(t1)
                #print(t2)
                #print(t3)
                #print(t4)
                #break
                if(t1[0]>targetMin[0] and t1[1]>targetMin[1] and t1[2]>targetMin[2]):
                    if(t1[0]<targetMax[0] and t1[1]<targetMax[1] and t1[2]<targetMax[2]):
                        print("match found")
                        sys.exit()
                if(t2[0]>targetMin[0] and t2[1]>targetMin[1] and t2[2]>targetMin[2]):
                    if(t2[0]<targetMax[0] and t2[1]<targetMax[1] and t2[2]<targetMax[2]):
                        print("match found")
                        sys.exit()
                if(t3[0]>targetMin[0] and t3[1]>targetMin[1] and t3[2]>targetMin[2]):
                    if(t3[0]<targetMax[0] and t3[1]<targetMax[1] and t3[2]<targetMax[2]):
                        print("match found")
                        sys.exit()
                if(t4[0]>targetMin[0] and t4[1]>targetMin[1] and t4[2]>targetMin[2]):
                    if(t4[0]<targetMax[0] and t4[1]<targetMax[1] and t4[2]<targetMax[2]):
                        print("match found")
                        sys.exit()
                if(t1[0] == ceresX or t2[0] == ceresX or t3[0] == ceresX or t4[0] == ceresX):
                    print("match found")
                d1 = math.sqrt((t1[0]-ceresX)**2+(t1[1]-ceresY)**2+(t1[2]-ceresZ)**2)
                d2 = math.sqrt((t2[0]-ceresX)**2+(t2[1]-ceresY)**2+(t2[2]-ceresZ)**2)
                d3 = math.sqrt((t3[0]-ceresX)**2+(t3[1]-ceresY)**2+(t3[2]-ceresZ)**2)
                d4 = math.sqrt((t4[0]-ceresX)**2+(t4[1]-ceresY)**2+(t4[2]-ceresZ)**2)
                if(d1 < 1200):
                    print("match found")
                if(d2 < 1200):
                    print("match found")
                if(d3 < 1200):
                    print("match found")
                if(d4 < 1200):
                    print("match found")

print("no matches found")
