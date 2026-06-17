soil_moisture = int(input("Enter soil moisture (%): "))

if soil_moisture < 40:
    print("Soil is dry")
    print("Motor ON")
else:
    print("Soil moisture is sufficient")
    print("Motor OFF")
