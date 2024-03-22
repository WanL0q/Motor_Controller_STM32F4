# Motor_Controller_STM32F4
Controlling Motor Speed with STM32F407 Kit
![Untitled](https://github.com/WanL0q/Motor_Controller_STM32F4/assets/134664967/8cce08ca-791c-4710-b91d-051e33a09514)
# Configure pin_outs for STM32F407

![3](https://github.com/WanL0q/Motor_Controller_STM32F4/assets/134664967/fe212cb8-827a-4e58-b334-2dcba47d07bd)

| Wheel    | Pin       | Function        | Wheel | Pin       | Function        |
|----------|-----------|-----------------|-------|-----------|-----------------|
| **1**    | PE9       | R_EN=L_EN= PWM  | **2** | PE11      | R_EN=L_EN=PWM   |
|          | PC5       | RPWM            |       | PB1       | RPWM            |
|          | PB0       | LPWM            |       | PB2       | LPWM            |
|          | PA5       | Encoder CH_A    |       | PA6       | Encoder CH_A    |
|          | PB3       | Encoder CH_B    |       | PA7       | Encoder CH_B    |
|----------|-----------|-----------------|-------|-----------|-----------------|
| **3**    | PE13      | R_EN=L_EN=PWM   | **4** | PE14      | R_EN=L_EN=PWM   |
|          | PB12      | RPWM            |       | PB14      | RPWM            |
|          | PB13      | LPWM            |       | PB15      | LPWM            |
|          | PD12      | Encoder CH_A    |       | PA0       | Encoder CH_A    |
|          | PB7       | Encoder CH_B    |       | PA1       | Encoder CH_B    |
|----------|-----------|-----------------|-------|-----------|-----------------|
| **UART** | PA2       | USART2_TX       |       | PA3       | USART2_RX       |

# Communication between ROS and STM32
- Topic "cmd_vel": Longitudinal velocity and angular velocity set for the robot.
- Topic "vel_set": Velocity is set for 4 motors.
- Topic "vel_enc": Velocity of the 4 motors calculated from encoders.
