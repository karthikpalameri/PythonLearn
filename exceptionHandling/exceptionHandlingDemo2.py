def exceptionHandlingDemo2():
    car = {"make": "someMake", "model": "someModel", "year": "someYear"}
    print(car.get("maked", "returnSomeDefaultValueIfTheKeyIsNotPresent"))

    try:
        print(car["color"])
    except:
        print("key not found check key , so executing except block")

    else:
        print("If no Exception then I will run -else")


    finally:
        print("I will run no matter what -finally")

exceptionHandlingDemo2()