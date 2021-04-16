# Simple PID controller

A PID controller with output saturation is implemented in python for a DC motor control application.

![Block Diagram](/images/block_diagram.svg)

The PID controller was implemented as a class named **SimplePIDController**.

```
class PIDControler(kp, ki, kd, lim_min, lim_max, T):
```

**Class Attributes:**

* **kp** – proportional gain
* **ki** – integral gain
* **kd** – derivative gain
* **lim_min** – min value for output saturation
* **lim_max** – max value for output saturation
* **T** – sample time
* Two additional parameters representing the integrator and error memory are also included. (**i** and **e_prev**)

**Class Methods**:

* **update_pid(reference, measurement)** – this function returns the PID controller
  output for a given pair of reference and measurement values
