# Simple PID controller



A PID controller with output saturation is implemented in python for a DC motor control application.

![Block Diagram](/images/block_diagram.svg)



### Implementation

The PID controller was implemented as a class named [**SimplePIDController**](controller.py)

```python
class PIDControler(kp, ki, kd, lim_min, lim_max, t):
```

**Class attributes and methods:**

```python
kp: float  # proportional gain
ki: float  # integral gain
kd: float  # derivative gain
lim_min: float  # min value for output saturation
lim_max: float  # max value for output saturation    
t: float  # sample time
    
i: float = 0  # controller memory - integral term
e_prev: float = 0  # controller memory - previous error
    
def update_pid(reference, measurement):
    return output # returns the PID controller output for a given pair of reference and measurement values
```



### Testing and simulation

To test the PID controller, an **armature controlled permanent magnet dc motor** was selected. with the following motor parameters

* Kt (torque constant) = 0.06 Nm/A
* Ke (voltage constant) = 0.06 Vs/rad
* L (armature inductance) = 0.02 H
* R (armature resistance) = 1.2 Ohm
* J (inertia) = 6.2e−4 Nm^2/rad
* B (friction coefficient)= 0.0001 Nms/rad



***Transfer function for motor*** *(between the armature voltage and the motor speed)*



![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B%5COmega%28s%29%7D%7BE%28s%29%7D%20%3D%5Cfrac%7BK_t%7D%7BRJs%5E2%2B%28RJ%2BBL%29s%2B%28K_tK_e%2BRB%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)



![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B%5COmega%28s%29%7D%7BE%28s%29%7D%20%3D%5Cfrac%7B0.06%7D%7B1.24%5Ctimes%2010%5E%7B-4%7D%20s%5E2%20%2B%200.000746%20s%2B0.00372%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)



**Transfer function for _plant_**

To implement this, we can use a microcontroller to generate a PWM which will in turn control the input voltage to the motor (via a motor drive)

<img src="images/plant.svg" />

If we assume the motor drive   is linear, then we can consider the effect of both the PWM generator and motor drive as scaling the duty cycle by a constant. This implies a constant transfer function. Therefore, we can express the transfer function for the complete plant as follows. Here Ω is the angular speed and D is the duty ratio.



![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B%5COmega%28s%29%7D%7BD%28s%29%7D%20%3D%5Cfrac%7B24%5Ctimes0.06%7D%7B1.24%5Ctimes%2010%5E%7B-4%7D%20s%5E2%20%2B%200.000746%20s%2B0.00372%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)



**Control algorithm**

<img src="images/system.svg" />

To implement the transfer function and obtain the response at a given point, the [Python Control Systems library](https://pypi.org/project/control) has been used . The [NumPy](https://numpy.org/) library was used for matrix manipulation.



**Results**

The following curves were obtained for kp=0.1, ki=0.5 and kd=0.004

![results](images/output_plant.png)![results](images/output_controller.png)

**Code for simulation**

* The code for simulating and plotting can be found [here](simulation.py) 

* Example usage can be found [here](simulation.ipynb)
