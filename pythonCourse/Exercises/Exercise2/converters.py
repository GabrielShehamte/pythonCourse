def convert(feet, inches):
    ft = feet*12*2.54
    inc = inches*2.54
    conversion = ft/100 + inc/100
    return conversion 