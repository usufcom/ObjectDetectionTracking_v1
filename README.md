# Simple Object Detection and Tracking Labs

By YOUSSOUFA Mohamadou 

[Get Code from Github Repo](https://github.com/usufcom/ObjectDetectionTracking_v1) 

A tutorial for object detection, face detection, and face recognition. You will run three Jupyter notebooks in **VS Code** on a **CPU** (no GPU required).


| Lab    | Notebook                                    | What you will do                                                                    |
| ------ | ------------------------------------------- | ----------------------------------------------------------------------------------- |
| Lab 01 | `Lab01_Face Detection in Images.ipynb`      | Detect objects and faces in still images with YOLO                                  |
| Lab 02 | `Lab02_Face Detection in Live Videos.ipynb` | Run the same detection on a live camera feed                                        |
| Lab 03 | `Lab03_Face_Recognition.ipynb`              | Train an OpenCV LBPH recognizer on your own photos and recognize faces in real time |


Labs 02 and 03 need a webcam (built-in or USB).

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

Install **uv**, then the CPU PyTorch wheels, YOLO, and OpenCV. Ultralytics installs `opencv-python`; uninstall it and replace it with `opencv-contrib-python` so Lab 03 can use the LBPH face recognizer.

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
2. Open one of the three `.ipynb` lab files.
3. Click **Select Kernel** in the top right of the notebook.
4. Choose the `.venv` interpreter you just created.
5. Run the cells from top to bottom.

The first time you run a YOLO cell, the model file is downloaded automatically into `yolo_models/`.

## Lab presentations

Each lab notebook can be presented as slides in VS Code.

1. Open the lab notebook.
2. Select the `.venv` kernel.
3. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **View as Slide Show**.


| Lab    | Notebook                                    | What the slides cover                                                                    |
| ------ | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Lab 01 | `Lab01_Face Detection in Images.ipynb`      | Object detection with the official YOLO model, then face detection on still images       |
| Lab 02 | `Lab02_Face Detection in Live Videos.ipynb` | The same detection pipeline on a live camera feed                                        |
| Lab 03 | `Lab03_Face_Recognition.ipynb`              | Training an OpenCV LBPH recognizer on your own photos and recognizing faces in real time |


To export a standalone HTML slideshow (optional):

```
jupyter nbconvert "Lab01_Face Detection in Images.ipynb" --to slides
jupyter nbconvert "Lab02_Face Detection in Live Videos.ipynb" --to slides
jupyter nbconvert "Lab03_Face_Recognition.ipynb" --to slides
```

Each command writes a `.slides.html` file next to the notebook. Open that file in a browser.

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

