def main():

   layer = input(print("Descent atmosphere layer:"))

        #voy a ponerlo doble por si ponen la primera letra en mayuscula para que el programa no se confunda
   if layer == "exosphere":
        print("your altitude level will be between 700–10,000 km")
   elif layer == "Exosphere":
        print("your altitude level will be between 700–10,000 km")

   elif layer == "Thermosphere":
        print("your altitude level will be between 85–700 km")
   elif layer == "thermosphere":
        print("your altitude level will be between 85–700 km")

   elif layer == "Mesosphere":
        print("your altitude level will be between 50–85 km")
   elif layer == "mesosphere":
        print("your altitude level will be between 50–85 km")

   elif layer == "Stratosphere":
        print("your altitude level will be between 12–50 km")
   elif layer == "stratosphere":
        print("your altitude level will be between 12–50 km")

   elif layer == "Troposphere":
        print("your altitude level will be between 0–12 km")
   elif layer == "troposphere":
        print("your altitude level will be between 0–12 km")

   else:
       print("")

   altitude = float(input(print("Enter exact altitude in km:")))

   exo = 4650
   thermo = 1230
   meso = 175
   strato = 506.7
   tropo = 600

   if altitude < exo:
        result1 = (altitude * 1000 / 2000) + thermo + meso + strato + tropo
        print("result in seconds", result1)

   elif altitude < thermo:
        result2 = (altitude * 1000 / 500) + meso + strato + tropo
        print("result in seconds", result2)

   elif altitude < meso:
        result3 = (altitude * 1000 / 200) + strato + tropo
        print("result in seconds", result3)

   elif altitude < strato:
           result4 = (altitude * 1000 / 75) + tropo
           print("result in seconds", result4)

   elif altitude < tropo:
              result5 = (altitude * 1000 / 20)
              print("result in seconds", result5)












if __name__ == "__main__":
    main()
