import math

# currentType must be one of the following strings: DC / Single phase AC / Three phase AC
def wattsToAmps(currentType):
    currentType = currentType.lower()
    power = float(input('Enter power in watts: '))   
    if currentType == 'single phase ac' or currentType == 'three phase ac':
        powerFactor = float(input('Enter power factor: '))   
    if currentType == 'three phase ac':
        voltageType = input('Enter voltage type (line-to-line or line-to-neutral: ').lower()        
    voltage = float(input('Enter voltage in volts: '))
    
    if currentType == 'dc':
        amps = power / voltage
    if currentType == 'single phase ac':
        amps = power / (powerFactor * voltage)      
    if currentType == 'three phase ac' and voltageType == 'line-to-line':
        amps = power / (math.sqrt(3) * powerFactor * voltage)      
    if currentType == 'three phase ac' and voltageType == 'line-to-neutral':
        amps = power / (3 * powerFactor * voltage)
        
    try:
        print('This is', amps, 'A')
    except:
        print('Could not calculate amperes based on the information you have provided, please check the documentation for help.')


