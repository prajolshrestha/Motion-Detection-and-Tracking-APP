## Motion Detector App
This is a simple motion detection application built with Python and OpenCV library to capture video frames and process them to acquire the duration of motion in real-time.

## Requirements
To use this application, you need to have Python 3.10 installed on your machine along with the following libraries:

OpenCV
Pandas
numpy
Folium
bokeh
time

You can install these libraries by running the following command:

pip install opencv-python pandas folium

## Usage
To use this motion detector app, follow these steps:

Clone the repository or download the ZIP file.
Navigate to the project directory.
Run the motion_detector.py file using the following command:

python motion_detector.py

The app will start detecting motion and display the video frame along with the duration of motion in real-time.
Once the app is closed, it will create a CSV file named Moton Time Stamp.csv which contains the exact date and time of the detected motion.
To visualize the motion data, run the motion_graph.py file using the following command:

python motion_graph.py

The app will create an HTML file named Time_data.html which contains the visualization of motion data using Folium library.

## Customization
You can customize the motion detector app by changing the value of the counter hyperparameter in the motion_detector.py file. This parameter determines the number of frames between each motion detection.

## Credits
This motion detector app was built by PRAJOL SHRESTHA as a personal project. If you have any feedback or suggestions, feel free to create a pull request or contact me via email.

## License
You are free to use, modify, and distribute this application as long as you give credit to the original author.
