# ♻️ AI-Based Smart Waste Segregation System

An AI-powered smart waste segregation system designed to automatically identify and sort different types of waste using computer vision, Raspberry Pi, sensors, and motor-based mechanisms.

The project combines **Artificial Intelligence, Computer Vision, Raspberry Pi, Python, and automation** to improve the process of waste classification and segregation.

---

## 📌 Project Overview

Waste segregation is an important step in effective waste management. Traditional waste segregation methods often require manual sorting, which can be time-consuming and inefficient.

This project aims to automate the process by using a camera and an AI-based detection system to identify waste and control the sorting mechanism accordingly.

The Raspberry Pi acts as the main controller, processing the captured images and controlling the connected hardware components.

---

## ✨ Features

- ♻️ AI-based waste identification
- 📷 Camera-based image capture
- 🤖 Automated waste segregation
- 🍃 Classification of different waste categories
- 🔧 Raspberry Pi-based hardware control
- ⚙️ Servo and stepper motor control
- 📊 Detection and training results
- 🖥️ Python-based implementation
- 🔊 Audio output support

---

## 🛠️ Technologies Used

### Software

- Python
- Computer Vision
- Artificial Intelligence / Machine Learning
- YOLO-based object detection
- OpenCV
- Raspberry Pi OS
- Git & GitHub

### Hardware

- Raspberry Pi
- Raspberry Pi Camera
- Servo Motor
- Stepper Motor
- Motor Driver
- Sensors
- Waste collection mechanism

---

## 📂 Project Structure

```text
WASTE_SORTER/
│
├── runs/
│   └── detect/
│       └── train/
│           ├── args.yaml
│           ├── results.csv
│           └── ...
│
├── final_code.py
├── servo_code.py
├── stepper_test.py
│
├── annotated_image.jpg
├── captured_image.jpg
├── count.mp3
│
└── README.md
```

---

## 📄 Main Files

**final_code.py**
Main Python program responsible for running the waste sorting system and coordinating the different components.

**servo_code.py**
Python program used for testing and controlling the servo motor.

**stepper_test.py**
Python program used for testing the stepper motor mechanism.

**captured_image.jpg**
Sample image captured during the project.

**annotated_image.jpg**
Sample image containing detection/annotation results.

**count.mp3**
Audio file used as part of the project.

**runs/**
Contains generated training and detection results from the AI model.

---

## ⚙️ How the System Works

The basic workflow of the system is:

```
        Waste Item
            │
            ▼
     📷 Camera Capture
            │
            ▼
      🧠 AI Detection
            │
            ▼
    Waste Classification
            │
            ▼
    Raspberry Pi Processing
            │
            ▼
     Motor Controller
            │
            ▼
     ⚙️ Sorting Mechanism
            │
            ▼
     ♻️ Segregated Waste
```

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/shalahthaikkadan/-AI-Based-Smart-Waste-Segregation-System.git
```

### 2. Enter the project directory
```bash
cd -AI-Based-Smart-Waste-Segregation-System
```

### 3. Enter the project folder
```bash
cd WASTE_SORTER
```

### 4. Install required Python packages

If a `requirements.txt` file is available:
```bash
pip install -r requirements.txt
```

Otherwise, install the required Python libraries according to the modules used in `final_code.py`.

---

## ▶️ Running the Project

Run the main program:
```bash
python final_code.py
```

For servo testing:
```bash
python servo_code.py
```

For stepper motor testing:
```bash
python stepper_test.py
```

Hardware-related programs should be executed on a compatible Raspberry Pi setup with the required components connected.

---

## 🧪 Model Training

The `runs` directory contains generated results from the model training and detection process.

Example files include:

```text
runs/
└── detect/
    └── train/
        ├── args.yaml
        ├── results.csv
        └── ...
```

These files can be used to review training configuration and results.

---

## 🔌 Hardware Workflow

The Raspberry Pi works as the central controller.

The general hardware workflow is:

```
Camera
   │
   ▼
Raspberry Pi
   │
   ├── AI Detection
   │
   ├── Waste Classification
   │
   └── Motor Control
          │
          ├── Servo Motor
          └── Stepper Motor
```

The motors operate the physical sorting mechanism based on the detected waste category.

---

## 🎯 Project Objectives

- Automate waste segregation
- Reduce manual waste sorting
- Demonstrate practical applications of AI and computer vision
- Integrate machine learning with embedded systems
- Control physical hardware using Raspberry Pi
- Improve the efficiency of waste classification

---

## 🔮 Future Improvements

Possible future improvements include:

- Improve AI detection accuracy
- Add more waste categories
- Improve real-time detection performance
- Add a conveyor belt system
- Add additional environmental sensors
- Add a web-based monitoring dashboard
- Store classification statistics in a database
- Add IoT-based monitoring
- Improve the mechanical sorting mechanism
- Add remote system monitoring

---

## 📸 Project Images

Sample images from the project are included in this repository:

- captured_image.jpg
- annotated_image.jpg

---

## 👨‍💻 Developers

This project was developed as a team effort by:

- **Shalah Thaikkadan**
- **Muhammed Afsal V**
- **Muhammed Samil A.C**
- **Sahal A.C**

B.Tech Computer Science & Engineering

GitHub: https://github.com/shalahthaikkadan
LinkedIn: https://www.linkedin.com/in/shalah-thaikkadan-40142b32b/
Email: shalahthaikkadan@gmail.com

---

## 📜 License

This project is available for educational and project demonstration purposes.

---

## ⭐ Acknowledgement

This project was developed as an academic/project implementation combining:

- Artificial Intelligence
- Computer Vision
- Python
- Raspberry Pi
- Embedded Systems
- Automation

---

⭐ If you find this project useful, consider giving the repository a star!
