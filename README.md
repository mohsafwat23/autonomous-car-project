# Autonomous Path Plan Robot Car Project
Video: https://youtu.be/mbgRzDDy74w

## Hardware 
<img src="https://github.com/mohsafwat23/autonomous-car-project/blob/f58edff6497e74ac6c898377fa7bc6cb5c12357d/Assets/assembley.jpg" width="500" height="500">

* Raspberry Pi
* L298N Motor Driver
* IMU Sensor (BNO055)
* DC Motors
* Wheels
* Chasis
* 9V Battery & Powerbank
* 3D Printer (Optional)

## Circuit 
The hardware is connected using the following circuit:
<img src="https://github.com/mohsafwat23/autonomous-car-project/blob/2aab08b30034cf3d4843e20c9825e95176afcf1a/Assets/circuit.jpeg" width="500" height="400">

Additionaly, the Raspberry Pi is powered using a powerbank.
## Code 
The main file is RobotGame.py.
* The car's orientation is obtained from the BNO055 sensor and the code is in AngleModule.py.
* The motors are controlled using the motor driver and the code is in MotorModule.py.
* I'm using Pygame to plan the path for the car as shown below:
* 
<img src="https://github.com/mohsafwat23/autonomous-car-project/blob/f58edff6497e74ac6c898377fa7bc6cb5c12357d/Assets/pygame.png" width="500" height="400">


