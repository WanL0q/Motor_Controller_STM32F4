# Motor_Controller_STM32F4
Controlling Motor Speed with STM32F407 Kit
## Configure pin_outs for STM32F407

![2](https://github.com/WanL0q/Motor_Controller_STM32F4/assets/134664967/6f5dd2d4-7768-4194-b607-57ba9f7a5470)

| Wheel | Pin       | Function        | Wheel | Pin       | Function        |
|-------|-----------|-----------------|-------|-----------|-----------------|
| **1**     | TIM1_CH1  | R_EN=L_EN= PWM | **2**     | TIM1_CH2  | R_EN=L_EN=PWM   |
|       | PE9       | L_EN            |       | PE11      | L_EN            |
|       |           | R_EN            |       |           | R_EN            |
|       | PC5       | RPWM            |       | PB1       | RPWM            |
|       | PB0       | LPWM            |       | PB2       | LPWM            |
|       | TIM2_CH1  | Channel A       |       | TIM3_CH1  | Channel A       |
|       | PA5       |                 |       | PA6       |                 |
|       | TIM2_CH2  | Channel B       |        | TIM3_CH2  | Channel B       |
|       | PB3       |                 |       | PB7       |                 |
|-------|-----------|-----------------|-------|-----------|-----------------|
| **3**     | TIM1_CH3  | R_EN=L_EN=PWM   | **4**    | TIM1_CH4  | R_EN=L_EN=PWM   |
|       | PE13      | L_EN            |       | PE14      | L_EN            |
|       |           | R_EN            |       |           | R_EN            |
|       | PB12      | RPWM            |       | PB14      | RPWM            |
|       | PB13      | LPWM            |       | PB15      | LPWM            |
|       | TIM4_CH1  | Channel A       |       | TIM5_CH1  | Channel A       |
|       | PD12      |                 |       | PA0       |                 |
|       | TIM4_CH2  | Channel B       |       | TIM5_CH2  | Channel B       |
|       | PB7       |                 |       | PA1       |                 |
|-------|-----------|-----------------|-------|-----------|-----------------|
| **UART**  | PA2       | USART2_TX       |       | PA3       | USART2_RX       |


![Untitled](https://github.com/WanL0q/Motor_Controller_STM32F4/assets/134664967/8cce08ca-791c-4710-b91d-051e33a09514)
