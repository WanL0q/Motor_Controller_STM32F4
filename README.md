# Motor_Controller_STM32F4
Controlling Motor Speed with STM32F407 Kit
Configure pin_outs for STM32F407

![2](https://github.com/WanL0q/Motor_Controller_STM32F4/assets/134664967/6f5dd2d4-7768-4194-b607-57ba9f7a5470)

*) Wheel 1:
- TIM1_CH1 (PE9) : R_EN=L_EN= PWM 
- GPIO_Output (PC5) : RPWM
- GPIO_Output (PB0) : LPWM
- TIM2_CH1 (PA5) : Channel A
- TIM2_CH2 (PB3) : Channel B

*) Wheel 2:
- TIM1_CH2 (PE11) : R_EN=L_EN=PWM
- GPIO_Output (PB1) : RPWM
- GPIO_Output (PB2) : LPWM
- TIM3_CH1 (PA6) : Channel A
- TIM3_CH2 (PB7) : Channel B

*) Wheel 3:
- TIM1_CH3 (PE13) : R_EN=L_EN=PWM
GPIO_Output (PB12) : RPWM
GPIO_Output (PB13) : LPWM
TIM4_CH1 (PD12) : Channel A
TIM4_CH2 (PB7) : Channel B

*) Wheel 4
TIM1_CH4 (PE14) : R_EN=L_EN=PWM	
GPIO_Output (PB14) : RPWM
GPIO_Output (PB15) : LPWM
TIM5_CH1 (PA0) : Channel A
TIM5_CH2 (PA1) : Channel B

PA2: USART2_TX
PA3: USART2_RX
