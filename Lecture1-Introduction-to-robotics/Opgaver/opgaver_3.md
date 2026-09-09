# 🤖 Raspberry Pi 3 + L298N Motor Control

## Laboratory Assignments – Demo 1 to Demo 8

> **Course:** Autonomous Robot with Python and AI
> **Platform:** Raspberry Pi 3 Model B / B+
> **Programming Language:** Python
> **Motor Driver:** L298N Dual H-Bridge
> **Difficulty:** Beginner → Intermediate
> **Assignments:** 5

---

# 📚 Overview

In these assignments, you will develop a small two-wheel mobile robot step by step.

You will begin with basic motor movement and gradually develop:

* Forward movement
* Backward movement
* Stopping
* Left and right turns
* Square movement
* Zigzag movement
* Keyboard control
* Emergency stopping
* PWM motor-speed control
* Gradual acceleration

The overall development path is:

```text
Demo 1
Basic Motor Control
      ↓
Demo 2
Left / Right Turning
      ↓
Demo 3
Square Movement
      ↓
Demo 4
Zigzag Movement
      ↓
Demo 5
Keyboard Control
      ↓
Demo 6
Emergency Stop
      ↓
Demo 7
PWM Speed Control
      ↓
Demo 8
Gradual Speed Control
```

---

# 🔧 Hardware Requirements

Each group should have:

* Raspberry Pi 3 Model B / B+
* Raspberry Pi power supply
* MicroSD card with Raspberry Pi OS
* L298N motor driver
* 2 × DC motors
* 2 × wheels
* Robot chassis
* Battery pack for motors
* Jumper wires
* Breadboard if required
* Keyboard / SSH connection
* Computer with VS Code or terminal access

---

# 🔌 GPIO Configuration

The assignments use:

```python
GPIO.setmode(GPIO.BOARD)
```

Therefore, the numbers refer to **physical Raspberry Pi pin numbers**.

| Function              | Physical Pin | BCM GPIO | L298N |
| --------------------- | -----------: | -------: | ----- |
| Right Motor Control 1 |           29 |    GPIO5 | IN1   |
| Right Motor Control 2 |           31 |    GPIO6 | IN2   |
| Left Motor Control 1  |           32 |   GPIO12 | IN3   |
| Left Motor Control 2  |           33 |   GPIO13 | IN4   |
| Ground                | 30 / 34 / 39 |      GND | GND   |

---

# ⚠️ Safety Rules

Before starting:

1. Do not connect a DC motor directly to a Raspberry Pi GPIO pin.
2. Use the L298N motor driver between the Raspberry Pi and motors.
3. Raspberry Pi GND and L298N GND must be connected together.
4. Check motor battery polarity before applying power.
5. Do not connect 7–12 V motor power directly to Raspberry Pi GPIO.
6. Place the robot on a safe surface before testing.
7. During the first test, raise the wheels above the table.
8. Be ready to stop the program using:

```text
Ctrl + C
```

---

# 🟢 Assignment 1 – Basic Motor Movement

## 🎯 Objective

Create a Python program that controls both motors and makes the robot:

1. Move forward
2. Move backward
3. Stop

---

## 🧠 Concepts

You will work with:

* GPIO output
* `GPIO.HIGH`
* `GPIO.LOW`
* Python functions
* `time.sleep()`
* Motor direction
* H-bridge control
* Infinite loops
* Exception handling

---

## 📋 Requirements

Create the following functions:

```text
motor_a_forward()

motor_a_backward()

motor_b_forward()

motor_b_backward()

forward()

backward()

stop()
```

---

## 🚗 Required Robot Sequence

Your robot should perform:

```text
START
  │
  ▼
FORWARD
3 seconds
  │
  ▼
BACKWARD
3 seconds
  │
  ▼
STOP
2 seconds
  │
  ▼
REPEAT
```

---

## ✅ Expected Behaviour

```text
0–3 sec       Forward

3–6 sec       Backward

6–8 sec       Stop

8–11 sec      Forward

...
```

---

## 🧪 Student Tasks

### Task 1.1

Explain what the following instruction does:

```python
GPIO.setmode(GPIO.BOARD)
```

### Task 1.2

Explain the difference between:

```python
GPIO.HIGH
```

and

```python
GPIO.LOW
```

### Task 1.3

Explain why two GPIO pins are required to control the direction of one DC motor.

### Task 1.4

Change:

```python
time.sleep(3)
```

to:

```python
time.sleep(5)
```

Observe what happens.

### Task 1.5

Explain why `GPIO.cleanup()` should be used when the application finishes.

---

# 🔵 Assignment 2 – Left and Right Turning

## 🎯 Objective

Extend Assignment 1 so the robot can turn.

The robot must now support:

```text
Forward
Backward
Left
Right
Stop
```

---

# 🚗 Robot Movement Model

```text
                 FORWARD
                    ↑

                    │

        LEFT  ←  [ ROBOT ]  → RIGHT

                    │

                    ↓
                 BACKWARD
```

---

## 📋 Requirements

Create two additional functions:

```python
turn_left()
```

and

```python
turn_right()
```

---

## ↩️ Left Turn

For a pivot left turn:

```text
Right Motor → Forward

Left Motor → Backward
```

Result:

```text
          ↺

       [ ROBOT ]
```

---

## ↪️ Right Turn

For a pivot right turn:

```text
Right Motor → Backward

Left Motor → Forward
```

Result:

```text
       [ ROBOT ]

           ↻
```

---

## 🧪 Student Tasks

### Task 2.1

Implement:

```python
turn_left()
```

### Task 2.2

Implement:

```python
turn_right()
```

### Task 2.3

Create the following movement:

```text
Forward
   ↓
Left
   ↓
Forward
   ↓
Right
   ↓
Stop
```

### Task 2.4

Experiment with different turning times:

```text
0.3 sec
0.5 sec
0.7 sec
1.0 sec
```

Record your observations.

---

# 🟨 Assignment 3 – Drive in a Square

## 🎯 Objective

Program the robot to follow approximately a square path.

---

## 🗺️ Required Path

```text
START ───────────►

  ▲               │
  │               │
  │               ▼

  ◄───────────────
```

The robot should:

```text
Forward
   ↓
Turn Right
   ↓
Forward
   ↓
Turn Right
   ↓
Forward
   ↓
Turn Right
   ↓
Forward
   ↓
Turn Right
   ↓
Stop
```

---

## 💡 Programming Hint

Instead of writing the same code four times, consider:

```python
for side in range(4):
```

---

## 🧪 Student Tasks

### Task 3.1

Create a program where the robot drives approximately:

```text
1 meter forward
```

and then turns approximately:

```text
90°
```

### Task 3.2

Repeat the movement four times.

### Task 3.3

Determine experimentally how long your robot needs to turn approximately 90°.

Record the value:

```text
Turning time = __________ seconds
```

### Task 3.4

Explain why time-based turning is not always accurate.

Consider:

* Battery level
* Surface friction
* Motor differences
* Wheel size
* Robot weight

---

# 🟣 Assignment 4 – Zigzag Robot

## 🎯 Objective

Create a robot that moves through a zigzag pattern.

---

## 🗺️ Required Movement

```text
START

   ↗
     ↘
       ↗
         ↘
           ↗

        FINISH
```

---

## 📋 Suggested Sequence

```text
Forward
   ↓
Turn Left
   ↓
Forward
   ↓
Turn Right
   ↓
Forward
   ↓
Turn Left
   ↓
Forward
```

---

## 🧪 Student Tasks

### Task 4.1

Create a basic zigzag route.

### Task 4.2

Use a loop instead of repeating the same commands manually.

### Task 4.3

Modify your program to perform:

```text
10 zigzag movements
```

### Task 4.4

Experiment with:

```text
Short turns

Medium turns

Sharp turns
```

### Task 4.5

Describe how changing the turning duration changes the robot's path.

---

# 🟠 Assignment 5 – Keyboard Controlled Robot

## 🎯 Objective

Create a simple manually controlled mobile robot.

Students should control the robot using keyboard commands.

---

# 🎮 Control Scheme

```text
              W
              ↑
           Forward

              │

     A ←── [ ROBOT ] ──→ D
    Left               Right

              │

              ↓
              S
           Backward
```

Additional commands:

```text
X = Stop

Q = Quit
```

---

## 📋 Required Commands

| Keyboard | Action     |
| -------- | ---------- |
| `W`      | Forward    |
| `S`      | Backward   |
| `A`      | Turn Left  |
| `D`      | Turn Right |
| `X`      | Stop       |
| `Q`      | Quit       |

---

## 💡 Programming Hint

You can read keyboard input using:

```python
command = input("Enter command: ").lower()
```

Then use:

```python
if

elif

else
```

to decide what the robot should do.

---

## 🧪 Student Tasks

### Task 5.1

Create a menu:

```text
========================
      ROBOT CONTROL
========================

W = Forward
S = Backward
A = Left
D = Right
X = Stop
Q = Quit

Enter command:
```

### Task 5.2

Implement all six commands.

### Task 5.3

Display the current action.

Example:

```text
Moving Forward...
```

or:

```text
Turning Left...
```

### Task 5.4

If the user enters an invalid command such as:

```text
Z
```

display:

```text
Invalid command!
```

### ⭐ Challenge

Add another command:

```text
H = Help
```

that redisplays the command menu.

---

# 🔴 Assignment 6 – Emergency Stop

## 🎯 Objective

Introduce safety concepts into robot programming.

Every mobile robot should have a mechanism that immediately stops its motors.

---

## 🚨 Emergency Stop Concept

```text
Robot Moving
     │
     │
     ▼
Emergency Condition
     │
     ▼
EMERGENCY STOP
     │
     ▼
Both Motors OFF
```

---

## 📋 Requirement

Create:

```python
def emergency_stop():
```

The function should:

1. Stop both motors.
2. Display an emergency message.

Example:

```text
!!!!!!!!!!!!!!!!!!!!!!!!
!!! EMERGENCY STOP !!!
!!!!!!!!!!!!!!!!!!!!!!!!
```

---

## 🧪 Student Tasks

### Task 6.1

Implement:

```python
emergency_stop()
```

### Task 6.2

Call the function while the robot is moving.

### Task 6.3

Explain why emergency-stop functionality is important for mobile robots.

### Task 6.4

Explain why this structure is useful:

```python
try:

    # robot program

finally:

    stop()
    GPIO.cleanup()
```

---

## ⭐ Advanced Challenge

Research how a physical push button could later be connected to a Raspberry Pi GPIO input and used as a stop button.

Do not implement it yet.

Create a simple block diagram showing your proposed design.

---

# 🏎️ Assignment 7 – PWM Speed Control

## 🎯 Objective

Control robot speed instead of running the motors only at full speed.

---

# 🧠 What is PWM?

PWM stands for:

> **Pulse Width Modulation**

PWM rapidly switches a signal ON and OFF.

Different duty cycles provide different average motor power.

```text
25%

███░░░░░░░░░


50%

██████░░░░░░


75%

█████████░░░


100%

████████████
```

---

# 🔌 L298N Speed Pins

The L298N provides:

```text
ENA → Motor A speed

ENB → Motor B speed
```

These pins can be controlled using PWM.

---

## ⚠️ Important

Many L298N modules include jumpers on:

```text
ENA

ENB
```

To control these pins from the Raspberry Pi, the appropriate jumpers normally need to be removed.

Check your particular L298N module before changing connections.

---

# 🧩 PWM Concept

```text
Raspberry Pi
      │
      │ PWM
      ▼
    ENA
      │
      ▼
Right Motor Speed


Raspberry Pi
      │
      │ PWM
      ▼
    ENB
      │
      ▼
Left Motor Speed
```

---

## 📋 Requirements

Create two PWM objects.

Example concept:

```python
right_pwm = GPIO.PWM(...)
left_pwm = GPIO.PWM(...)
```

Start them using:

```python
start()
```

and change motor speed using:

```python
ChangeDutyCycle()
```

---

## 🧪 Student Tasks

### Task 7.1

Run both motors at:

```text
25%
```

### Task 7.2

Run both motors at:

```text
50%
```

### Task 7.3

Run both motors at:

```text
75%
```

### Task 7.4

Run both motors at:

```text
100%
```

### Task 7.5

Create a table containing your observations.

|  PWM | Robot Speed | Observation |
| ---: | ----------- | ----------- |
|  25% |             |             |
|  50% |             |             |
|  75% |             |             |
| 100% |             |             |

---

## ⭐ Challenge – Curved Movement

Try:

```text
Left motor  = 30%

Right motor = 80%
```

Observe the robot.

Then reverse them:

```text
Left motor  = 80%

Right motor = 30%
```

Answer:

> Why does the robot curve when the motors have different speeds?

---

# 🚀 Assignment 8 – Gradual Acceleration

## 🎯 Objective

Create a robot that gradually increases its speed.

Instead of immediately starting at maximum power:

```text
STOP

  ↓

100%
```

the robot should accelerate:

```text
20%
 ↓
40%
 ↓
60%
 ↓
80%
 ↓
100%
```

---

# 📈 Acceleration Diagram

```text
Speed

100% |                         █████
 80% |                    █████
 60% |               █████
 40% |          █████
 20% |     █████
  0% |________________________________

       1     2     3     4     5

                 Time
```

---

## 💡 Programming Hint

You can use:

```python
for speed in range(20, 101, 20):
```

This generates:

```text
20
40
60
80
100
```

---

## 🧪 Student Tasks

### Task 8.1

Start the robot at:

```text
20%
```

### Task 8.2

Increase speed every:

```text
2 seconds
```

until reaching:

```text
100%
```

### Task 8.3

Display the current speed.

Example:

```text
Robot Speed: 20%

Robot Speed: 40%

Robot Speed: 60%

Robot Speed: 80%

Robot Speed: 100%
```

---

# ⭐ Challenge 8A – Gradual Deceleration

After reaching 100%, gradually decrease speed:

```text
100%
 ↓
80%
 ↓
60%
 ↓
40%
 ↓
20%
 ↓
STOP
```

---

# ⭐ Challenge 8B – Complete Acceleration Cycle

Create:

```text
START
  │
  ▼
20%
  │
  ▼
40%
  │
  ▼
60%
  │
  ▼
80%
  │
  ▼
100%
  │
  ▼
80%
  │
  ▼
60%
  │
  ▼
40%
  │
  ▼
20%
  │
  ▼
STOP
```

---

# 🏆 Final Challenge – Combine Demo 1–8

After completing all eight assignments, create one final robot-control program.

The application should contain:

```text
                    ROBOT SYSTEM

                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼

       MOVEMENT         SPEED          SAFETY

          │              │              │
    ┌─────┼─────┐      PWM        Emergency Stop
    │     │     │
 Forward Left Right
    │
 Backward
```

---

## Required Features

Your final program should support:

* Forward
* Backward
* Left
* Right
* Stop
* Keyboard commands
* Emergency stop
* PWM speed control
* Gradual acceleration
* Gradual deceleration

---

# 💻 Suggested Program Structure

Students may organize the program like this:

```text
Import libraries

      ↓

GPIO configuration

      ↓

Pin configuration

      ↓

PWM configuration

      ↓

Motor functions

      ↓

Movement functions

      ↓

Speed functions

      ↓

Emergency stop

      ↓

Keyboard interface

      ↓

Main program

      ↓

GPIO cleanup
```

---

# 📝 Student Documentation

For every assignment, students should document:

## 1. Objective

What should the robot accomplish?

## 2. Hardware

Which components were used?

## 3. GPIO Pins

Which Raspberry Pi pins were connected?

## 4. Algorithm

Describe the program logic.

## 5. Python Program

Include your completed source code.

## 6. Test

Describe how you tested the robot.

## 7. Result

Did the robot behave as expected?

## 8. Problems

What problems occurred?

## 9. Solution

How did you solve them?

## 10. Reflection

What did you learn?

---

# 📦 Submission Structure

Create a GitHub repository similar to:

```text
raspberry-pi-motor-control/
│
├── README.md
│
├── demo01_basic_motor.py
├── demo02_turning.py
├── demo03_square.py
├── demo04_zigzag.py
├── demo05_keyboard.py
├── demo06_emergency_stop.py
├── demo07_pwm.py
├── demo08_acceleration.py
│
├── images/
│   ├── wiring.jpg
│   ├── robot.jpg
│   └── test.jpg
│
└── report/
    └── observations.md
```

---

# 📊 Assessment Criteria

| Area                          |  Points |
| ----------------------------- | ------: |
| Correct GPIO configuration    |      10 |
| Forward / backward / stop     |      10 |
| Left / right movement         |      10 |
| Square and zigzag movement    |      10 |
| Keyboard control              |      15 |
| Emergency-stop implementation |      10 |
| PWM speed control             |      15 |
| Gradual acceleration          |      10 |
| Code quality                  |       5 |
| Documentation                 |       5 |
| **Total**                     | **100** |

---

# 🎓 Reflection Questions

Answer the following after completing Demo 1–8.

### Question 1

Why should DC motors not be connected directly to Raspberry Pi GPIO pins?

### Question 2

What is the purpose of the L298N?

### Question 3

What is an H-bridge?

### Question 4

What happens when:

```text
IN1 = HIGH
IN2 = LOW
```

### Question 5

What happens when:

```text
IN1 = LOW
IN2 = HIGH
```

### Question 6

What is the difference between:

```text
GPIO.BOARD
```

and:

```text
GPIO.BCM
```

### Question 7

Why must the Raspberry Pi and L298N share a common ground?

### Question 8

How can a two-wheel robot turn without using a steering wheel?

### Question 9

What is PWM?

### Question 10

How does PWM control motor speed?

### Question 11

Why might two apparently identical DC motors rotate at slightly different speeds?

### Question 12

Why is time-based navigation not sufficiently accurate for advanced autonomous robots?

---

# 🌟 What Comes Next?

After Demo 1–8 you are ready to add **sensors**.

```text
Motor Control
     │
     ▼
PWM Speed Control
     │
     ▼
Ultrasonic Sensor
     │
     ▼
Obstacle Detection
     │
     ▼
IR Sensors
     │
     ▼
Line Following
     │
     ▼
Camera
     │
     ▼
OpenCV
     │
     ▼
AI Decision Making
     │
     ▼
🤖 Autonomous Robot
```

The next recommended project is:

# 📡 Demo 9 – HC-SR04 Autonomous Obstacle Avoidance

The robot will move from:

```text
Programmed movement
```

to:

```text
Sense
  ↓
Think
  ↓
Decide
  ↓
Act
  ↓
Sense Again
```

which is the foundation of an **autonomous robotic system**.

---

## 🚀 Final Goal

By completing Demo 1–8, you should understand how Python software can control physical robot hardware:

```text
🐍 Python Program
       │
       ▼
🧠 Raspberry Pi
       │
       ▼
🔌 GPIO
       │
       ▼
⚡ L298N Motor Driver
       │
       ▼
⚙️ DC Motors
       │
       ▼
🚗 Robot Movement
```

> **From Python code to physical movement — this is where programming becomes robotics. 🤖**
