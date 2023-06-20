from machine import ADC
import utime

temp_sensor = ADC(4) # Defauclt connection of on board temperature sensor

while True:
    #get raw sensor data
    raw_sensor_data = temp_sensor.read_u16()
    
    # convert raw value to equivalent voltage
    sensor_voltage = (raw_sensor_data / 65535)*3.3
    
    # convert voltage to temperature (celcius)
    temperature = 27 - (sensor_voltage - 0.706)/0.001721
    
    print(f"Temperature : {round(temperature,2)}, dgreee cecius")
    utime.sleep(1)
    