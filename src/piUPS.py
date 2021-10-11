import smbus2 as sm

class PiUPS:

    # IC reference https://www.ti.com/lit/ds/symlink/bq25601.pdf




    # Select target charging current (only one)

    # CHG_LIM = 0b00000000 # 100mA
    # CHG_LIM = 0b00000001 # 200mA
    # CHG_LIM = 0b00000010 # 300mA
    # CHG_LIM = 0b00000011 # 400mA
    CHG_LIM = 0b00000100 # 500mA
    # CHG_LIM = 0b00000101 # 600mA
    # CHG_LIM = 0b00001001 # 1A
    # CHG_LIM = 0b00001110 # 1.5A
    # CHG_LIM = 0b00010100 # 2A
    # CHG_LIM = 0b00010111 # 2.4A
    # CHG_LIM = 0b00011111 # 3.2A MAX




    # Select target battery voltage for charging (select one)

    # VBAT_MAX = 0b00000000 # 3.856V
    # VBAT_MAX = 0b00000100 # 3.984V
    # VBAT_MAX = 0b00000110 # 4.048V
    # VBAT_MAX = 0b00001000 # 4.112V
    VBAT_MAX = 0b00001011 # 4.208V


    # Select shutdown voltage (one)
    # VSYS_MIN = 0b00000010 # 3 V
    # VSYS_MIN = 0b00000011 # 3.2 V
    # VSYS_MIN = 0b00000100 # 3.4 V
    VSYS_MIN = 0b00000101 # 3.5 V (default)
    # VSYS_MIN = 0b00000110 # 3.6 V
    # VSYS_MIN = 0b00000111 # 3.7 V
    
    # Internal vars:

    I2C_ADDR = 0x6B

    CHG_ADDR = 0x00
    VBMAX_ADDR = 0x04
    VSMIN_ADDR = 0x01
    VSYS_STAT_ADDR = 0x08
    BATEFET_ADDR = 0x07

    BATFET_TIMER = 0b00010000
    BATFET_TURN_OFF = 0b00000100 

    


