from dataclasses import dataclass


@dataclass
class SimplePIDController:
    # PID gains
    kp: float
    ki: float
    kd: float

    # output saturation
    lim_min: float
    lim_max: float

    # cycle time
    T: float

    # memory
    i: float = 0  # integrator
    e_prev: float = 0  # previous error

    def update_pid(self, reference: float, measurement: float):
        # error
        e = reference - measurement

        # proportional
        p = self.kp * e

        # integral
        self.i = self.i + self.ki * e * self.T

        # derivative
        d = self.kd * (e - self.e_prev) / self.T

        # update memory
        self.e_prev = e

        # output saturation
        output = p + self.i + d
        if output > self.lim_max:
            output = self.lim_max
        if output < self.lim_min:
            output = self.lim_min

        return output
