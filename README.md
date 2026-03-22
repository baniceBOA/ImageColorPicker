
------------------------------
## 📸 ImageColorPicker
A cross-platform mobile and desktop application built with Kivy and KivyMD that allows users to extract dominant colors and specific pixel values from any image.
✨ Features

* Color Extraction: Tap/click anywhere on an uploaded image to get real-time RGB, HSV, HLS, and HEX values 
* Palette Generation: Automatically identifies the top 5 dominant colors in any selected image 
* Cross-Platform: Optimized layouts for both Mobile and Desktop interfaces 
* Clipboard Integration: Easily copy color codes with a single click 

## 🛠 Tech Stack

* Framework: Kivy & KivyMD (Material Design widgets) 
* Image Processing: Pillow (PIL) 
* System Integration: Plyer (for native file choosing) 

## 🚀 Installation & Setup1. Prerequisites
Ensure you have Python 3.11+ installed.
### 2. Install Dependencies
''' bash
pip install kivy kivymd pillow plyer
'''
### 3. Running the App
''' bash
python main.py
'''
### 🤖 CI/CD & Deployment
The project includes GitHub Actions for automated Android builds using Buildozer 

* Build Workflow: .github/workflows/build.yaml (Debug APK/AAB) 
* Release Workflow: .github/workflows/release.yaml (Production AAB) 

