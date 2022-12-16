# Knee_bend_counter

This repository contains the code for knee bend counter and some characteristics include:
* There is a timer that shows the time for which the knee is kept bent and the bend counter goes up if the knee is kept bent for atleast 8 seconds.
* The state of bendness that is if the knee is straight or partially bent or fully bent is shown.
* The leg which is bent more is considered for the count.
* There are no restrictions for back angle.
* A feedback message to keep your knee bent is shown if the knee is taken to straight position in less than eight seconds.

***
## How to run
First of all make sure you have opencv-python==4 or above and numpy==1.19.2 or above installed.
* To use webcam run the knee_bend_counter_cam.py file
* To use on any video run the knee_bend_counter_vid.py file and change the path in line 29 with the path of your video.
* set the camera position and distance such that it can see the legs clearly.




