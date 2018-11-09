# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:09:15 2018

@author: Franck
"""

"""

---------------------------------------------------------------------------
PocketBeagle Arcade Machine
---------------------------------------------------------------------------

"""
import os
import random
import time

# ------------------------------------------------------------------------
# Global Constants
# ------------------------------------------------------------------------

# HT16K33 values
DISPLAY_I2C_BUS              = 1                 # I2C 1  
DISPLAY_I2C_ADDR             = 0x70
DISPLAY_CMD                  = "i2cset -y 1 0x70"         

# Peripheral path
GPIO_BASE_PATH               = "/sys/class/gpio"
ADC_BASE_PATH                = "/sys/bus/iio/devices/iio:device0"

# GPIO direction
IN                           = True
OUT                          = False

# GPIO output state
LOW                          = "0"
HIGH                         = "1"

# Button GPIO values
BUTTON0                      = (1, 27)           # gpio59 / P2_2
BUTTON1                      = (1, 25)           # gpio57 / P2_6
BUTTON2                      = (1, 15)           # gpio47 / P2_18
BUTTON3                      = (1, 14)           # gpio46 / P2_22
BUTTONS                      = [BUTTON0, BUTTON1, BUTTON2, BUTTON3]

# LED GPIO values
LED0                         = (1, 26)           # gpio58 / P2_4
LED1                         = (1, 28)           # gpio60 / P2_8 
LED2                         = (2, 0)            # gpio64 / P2_20
LED3                         = (1, 12)           # gpio44 / P2_24
LEDS                         = [LED0, LED1, LED2, LED3]
  
# Buzzer GPIO value
BUZZER                       = (1, 18)           # gpio50 / P2_1

# HT16K33 values
DISPLAY_I2C_BUS              = 1                 # I2C 1  
DISPLAY_I2C_ADDR             = 0x70
DISPLAY_CMD                  = "i2cset -y 1 0x70"         


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# GPIO/ADC access library
# ------------------------------------------------------------------------

def gpio_setup(gpio, direction, default_value=False):
    """Setup GPIO pin
    
      * Test if GPIO exists; if not create it
      * Set direction
      * Set default value
    """
    gpio_number = str((gpio[0] * 32) + gpio[1])
    path        = "{0}/gpio{1}".format(GPIO_BASE_PATH, gpio_number)
    
    if not os.path.exists(path):
        # "echo {gpio_number} > {GPIO_BASE_PATH}/export"
        print("Create GPIO: {0}".format(gpio_number))
        with open("{0}/export".format(GPIO_BASE_PATH), 'w') as f:
            f.write(gpio_number)
    
    if direction:
        # "echo in > {path}/direction"
        with open("{0}/direction".format(path), 'w') as f:
            f.write("in")
    else:
        # "echo out > {path}/direction"
        with open("{0}/direction".format(path), 'w') as f:
            f.write("out")
        
    if default_value:
        # "echo {default_value} > {path}/value"
        with open("{0}/value".format(path), 'w') as f:
            f.write(default_value)
    
# End def


def gpio_set(gpio, value):
    """Set GPIO ouptut value."""
    gpio_number = str((gpio[0] * 32) + gpio[1])
    path        = "{0}/gpio{1}".format(GPIO_BASE_PATH, gpio_number)
    
    # "echo {value} > {path}/value"
    with open("{0}/value".format(path), 'w') as f:
        f.write(value)

# End def


def gpio_get(gpio):
    """Get GPIO input value."""
    gpio_number = str((gpio[0] * 32) + gpio[1])
    path        = "{0}/gpio{1}".format(GPIO_BASE_PATH, gpio_number)
    
    # "cat {path}/value"
    with open("{0}/value".format(path), 'r') as f:
        out = f.read()
    
    return float(out)

# End def


def adc_get(channel):
    """Get ADC input value.
    
    Returns:
        value (float):  Value will be between 0 (0V) and 1.0 (1.8V)."""
    with open("{0}/{1}".format(ADC_BASE_PATH, channel), 'r') as f:
        out = f.read()
    
    return float(float(out) / float(4096))

# End def

# ------------------------------------------------------------------------
# Display Class
# ------------------------------------------------------------------------
HEX_DIGITS                  = [0x3f, 0x06, 0x5b, 0x4f,    # 0, 1, 2, 3
                               0x66, 0x6d, 0x7d, 0x07,    # 4, 5, 6, 7
                               0x7f, 0x6f, 0x77, 0x7c,    # 8, 9, A, b
                               0x39, 0x5e, 0x79, 0x71]    # C, d, E, F

CLEAR_DIGIT                 = 0x7F
POINT_VALUE                 = 0x80

DIGIT_ADDR                  = [0x00, 0x02, 0x06, 0x08]
COLON_ADDR                  = 0x04
                      
HT16K33_BLINK_CMD           = 0x80
HT16K33_BLINK_DISPLAYON     = 0x01
HT16K33_BLINK_OFF           = 0x00
HT16K33_BLINK_2HZ           = 0x02
HT16K33_BLINK_1HZ           = 0x04
HT16K33_BLINK_HALFHZ        = 0x06

HT16K33_SYSTEM_SETUP        = 0x20
HT16K33_OSCILLATOR          = 0x01

HT16K33_BRIGHTNESS_CMD      = 0xE0
HT16K33_BRIGHTNESS_HIGHEST  = 0x0F
HT16K33_BRIGHTNESS_DARKEST  = 0x00

def display_setup():
    """Setup display"""
    # i2cset -y 0 0x70 0x21
    os.system("{0} {1}".format(DISPLAY_CMD, (HT16K33_SYSTEM_SETUP | HT16K33_OSCILLATOR)))
    # i2cset -y 0 0x70 0x81
    os.system("{0} {1}".format(DISPLAY_CMD, (HT16K33_BLINK_CMD | HT16K33_BLINK_OFF | HT16K33_BLINK_DISPLAYON)))
    # i2cset -y 0 0x70 0xEF
    os.system("{0} {1}".format(DISPLAY_CMD, (HT16K33_BRIGHTNESS_CMD | HT16K33_BRIGHTNESS_HIGHEST)))

# End def


def display_clear():
    """Clear the display to read '0000'"""
    # i2cset -y 0 0x70 0x00 0x3F
    os.system("{0} {1} {2}".format(DISPLAY_CMD, DIGIT_ADDR[0], HEX_DIGITS[0]))
    # i2cset -y 0 0x70 0x02 0x3F
    os.system("{0} {1} {2}".format(DISPLAY_CMD, DIGIT_ADDR[1], HEX_DIGITS[0]))
    # i2cset -y 0 0x70 0x06 0x3F
    os.system("{0} {1} {2}".format(DISPLAY_CMD, DIGIT_ADDR[2], HEX_DIGITS[0]))
    # i2cset -y 0 0x70 0x08 0x3F
    os.system("{0} {1} {2}".format(DISPLAY_CMD, DIGIT_ADDR[3], HEX_DIGITS[0]))
    
    os.system("{0} {1} {2}".format(DISPLAY_CMD, COLON_ADDR, 0x0))
    
# End def


def display_encode(data, double_point=False):
    """Encode data to TM1637 format.
    
    This function will convert the data from decimal to the TM1637 data fromt
    
    :param value: Value must be between 0 and 15
    
    Will throw a ValueError if number is not between 0 and 15.
    """
    ret_val = 0
    
    try:
        if (data != CLEAR_DIGIT):
            if double_point:
                ret_val = HEX_DIGITS[data] + POINT_VALUE
            else:
                ret_val = HEX_DIGITS[data]
    except:
        raise ValueError("Digit value must be between 0 and 15.")

    return ret_val

# End def


def display_set(data):
    """Display the data.
    
    data is a list containing 4 values
    """
    for i in range(0,3):
        display_set_digit(i, data[i])
    
# End def


def display_set_digit(digit_number, data, double_point=False):
    """Update the given digit of the display."""
    os.system("{0} {1} {2}".format(DISPLAY_CMD, DIGIT_ADDR[digit_number], display_encode(data, double_point)))    

# End def


def update_display(value):
    """Update the value on the display.  
    
    This function will clear the display and then set the appropriate digits
    
    :param value: Value must be between 0 and 9999.
    
    Will throw a ValueError if number is not between 0 and 9999.
    """  
    """
    if (value < 0) or (value > 9999):
       raise ValueError("Value is not within 0 and 9999.") 
    
    if (value < 10):
        display_set_digit(3, value)
        display_set_digit(2, 0)
        display_set_digit(1, 0)
        display_set_digit(0, 0)
    else:
        if (value < 100):
            display_set_digit(3, value % 10)
            display_set_digit(2, value / 10)
            display_set_digit(1, 0)
            display_set_digit(0, 0)
    
    """
    for i in range(0,4):
        display_set_digit((3 - i), (value % 10))
        value = (value / 10)
    #"""
    #pass
    

# End def
    
def setup_game():
    "Setup the buttons for the game"
    
    gpio_setup(BUTTON0, IN)
    gpio_setup(BUTTON1, IN)
    gpio_setup(BUTTON2, IN)
    gpio_setup(BUTTON3, IN)    

    gpio_setup(LED0, OUT, LOW)
    gpio_setup(LED1, OUT, LOW)
    gpio_setup(LED2, OUT, LOW)
    gpio_setup(LED3, OUT, LOW)
    
    gpio_setup(BUZZER, OUT, LOW)
        
    display_setup

# ------------------------------------------------------------------------
# Reflex Tester Code
# ------------------------------------------------------------------------
        
def play_reflex(rand):
    #playing_game = True
        
    #while (playing_game):
        #self.random_path = random.randint(1, 4)
            
    time.sleep(random.random() * 6 + 3)      # Wait between 3 and 10 seconds before activating LED
        
    print(LEDS[rand])
        
    gpio_set(LEDS[rand], HIGH)              # Activate random LED
            
    initial_time = time.time()    
    
    while (gpio_get(BUTTONS[rand]) == 1):   # Wait until correct button is pressed
        pass
    
    button_press_time = time.time() 
    gpio_set(LEDS[rand], LOW)
        
    if ((button_press_time - initial_time) < 10):
        # Diplay the first three/four digits of the time spent before clicking button
        update_display((int)((button_press_time - initial_time) * 1000)) 
    else:
        display_set_digit(0, 13)            # "D"
        display_set_digit(1, 14)            # "E"
        display_set_digit(2, 10)            # "A"
        display_set_digit(3, 13)            # "D"

# End def

# ------------------------------------------------------------------------
# Simon Says Class
# ------------------------------------------------------------------------

def play_simon_says():
    pattern = []
    user_input = []
    playing_game = True
    
    while (playing_game):
        rand = random.randint(0, 3)
        pattern.append(rand)
        
        for i in pattern:
            gpio_set(LEDS[pattern[i]], HIGH)
            time.sleep(0.5)

# End class
    
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------
        
if __name__ == '__main__':
    setup_game()
    play_reflex(0)
    