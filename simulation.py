import matplotlib.pyplot as plt
import numpy as np
import control


def simulate_controller(G, dt, pid, ref):
    t = np.arange(0, 1, dt)  # response was obtained for 1s
    x_prev = np.zeros(len(G.pole()))  # variable to store previous state of system

    # vectors to store outputs
    y_vect = np.zeros(len(t))  # output speed (measured speed)
    pwm_vect = np.zeros(len(t))  # PWM duty cycle (control signal)

    # simulate the control loop for each sample
    for i, t_i in enumerate(t):
        pwm = pid.update_pid(ref, y_vect[i - 1])  # call update function of PID
        pwm_vect[i] = pwm
        t_temp, y_temp, x_temp = control.forced_response(G, [t_i - dt, t_i], [pwm, pwm], X0=x_prev, return_x=True,
                                                         squeeze=True)
        y_vect[i] = y_temp[-1]
        x_prev = x_temp[:, -1]

    # Plotting the results

    # motor speed (plant output)
    ax = plt.figure(dpi=100).gca()
    ax.plot(t, y_vect)
    ax.grid()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speed (rad/s)")

    # duty ratio (control signal)
    ax = plt.figure(dpi=100).gca()
    ax.plot(t, pwm_vect, 'g')
    ax.set_ylim([0, 1])
    ax.grid()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Duty ratio")

    return y_vect, pwm_vect, t
