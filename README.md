# Simple Object Detection and Tracking Labs

By YOUSSOUFA Mohamadou 

[Get Code from Github Repo](https://github.com/usufcom/ObjectDetectionTracking_v1) 

A tutorial for reading images and videos, object detection, face detection, and face recognition. You will run four Jupyter notebooks in **VS Code** on a **CPU** (no GPU required).


| Lab    | Notebook                                               | What you will do                                                                    |
| ------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Lab 01 | `Lab01_Reading, writing and displaying images.ipynb`   | Read, write, and display images and videos with OpenCV                              |
| Lab 02 | `Lab02_ObjectDetection in Images.ipynb`                | Detect objects and faces in still images with YOLO                                  |
| Lab 03 | `Lab03_Object and Face Detection in Live Videos.ipynb` | Run the same detection on a live camera feed                                        |
| Lab 04 | `Lab04_Face_Recognition.ipynb`                         | Train an OpenCV LBPH recognizer on your own photos and recognize faces in real time |


Labs 03 and 04 need a webcam (built-in or USB). Lab 01 also has an optional webcam section.

## What you need

1. [Python 3.12](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/)
3. These VS Code extensions (install from the Extensions view):
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)



## CPU setup with uv

Open a terminal in the project folder (in VS Code: **Terminal → New Terminal**).

Create and activate a virtual environment:

```
python -m venv .venv
```

- Linux / macOS: `source .venv/bin/activate`
- Windows: `.venv\Scripts\activate`

Install **uv**, then the CPU PyTorch wheels, YOLO, and OpenCV. Ultralytics installs `opencv-python`; uninstall it and replace it with `opencv-contrib-python` so Lab 04 can use the LBPH face recognizer.

```
pip install uv
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
uv pip install ultralytics
uv pip uninstall opencv-python
uv pip install opencv-contrib-python
```

Install the remaining packages:

Install the packages you need if you do not have them already : 

```
uv pip install numpy
uv pip install Pillow
uv pip install ipython
uv pip install ipykernel
uv pip install jupyter
```



## Run the labs in VS Code

1. Open this folder in VS Code (**File → Open Folder**).
2. Open one of the four `.ipynb` lab files.
3. Click **Select Kernel** in the top right of the notebook.
4. Choose the `.venv` interpreter you just created.
5. Run the cells from top to bottom.

N.B:

- Some of the YOLO models are found inside the `yolo_models/` folder.  
- For other  YOLO models,  when you run athe YOLO cell, the model file is downloaded automatically into `yolo_models/`.



## Face detection model source

This workflow uses official YOLO models downloaded from Python code, plus a community face model, `yolov8m-face.pt`, from [akanametov/yolo-face](https://github.com/akanametov/yolo-face).

Please give Akanametov a star if you use this workflow: [https://github.com/akanametov](https://github.com/akanametov)

## Demo images

Clone this repository. The resized demo images are already included and ready to use.

If you prefer the original high-resolution files, download them from Magnific and resize them yourself.

- demo.jpg (Girl + Cat): [Download](https://www.magnific.com/free-photo/beautiful-stylish-woman-purple-suit-hat-walking-city-street-spring-summer-autumn-season-fashion-trend-black-cat_11576374.htm)
- demo1.jpg (Cyclist + Cars): [Download](https://www.magnific.com/free-photo/cyclist-riding-bridge-city-dynamic-motion-with-blur-effect_427602721.htm)
- demo2.jpg (Kitchen): [Download](https://www.magnific.com/free-photo/portrait-beautiful-brunette-girl-chopping-vegetables-meal-making-salad-kitchen-eating_78042227.htm)
- demo3.jpg (Dog + Sheep): [Download](https://www.magnific.com/free-photo/mother-sheep-with-its-two-baby-sheep-grassy-field-daytime_11063035.htm)
- demo4.jpg (Laptop, Cup & Mouse): [Download](https://www.magnific.com/free-photo/laptop-mouse-top-view_7342965.htm)

Resize each downloaded image to about 15% of its original size:

```python
import cv2

img = cv2.imread("original_image_name.jpg")

resized_img = cv2.resize(
    img,
    None,
    fx=0.15,
    fy=0.15
)

cv2.imwrite("resized_image_name.jpg", resized_img)
```



## Acknowledgements

These tutorials were made thanks to resources shared by:

1. MariyaSha [here](https://github.com/MariyaSha/FaceRecognition)
2. Akanametov [here](https://github.com/akanametov/yolo-face)

