# Document Perspective Correction
A computer vision implementation that transforms perspective-distorted document images into clean, flat scans using projective geometry and homography transformations.

This project implements the mathematical foundation for correcting perspective distortion in document images. It transforms photos of documents taken at an angle into flat, scan-like images using projective geometry and homography transformations.

## Technical Foundations

The system models:
- Pinhole camera model with optical center at origin
- Projection of 3D world space to 2D image space  
- Homogeneous coordinates for linear transformation operations
- Intrinsic and extrinsic camera parameters
- Calibration of a camera
- Homography matrices for perspective correction

## Usage

The main functionality requires specifying the four corners of the document in the image. Here's how to use it:
1. Launch the .ipynb code to use matplotlib to allow the user to click on the four corners and retrieve them.

Or,

2. Hardcode them like this :
```python
# Define the four corners of the document in the image
# Order: top-left, top-right, bottom-right, bottom-left
points_image = np.array([
    [x1, y1],  # top-left
    [x2, y2],  # top-right  
    [x3, y3],  # bottom-right
    [x4, y4]   # bottom-left
]
```

You can then save your new, distortion-free, flattened image !
