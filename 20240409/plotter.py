from matplotlib import pyplot as plt
import cmath
import numpy as np
import io

def plot_function(function_str):
    
    print(f"str recieved: {function_str}")
    x = np.linspace(-10 ,10, 400)
    y = eval(function_str)
    plt.figure(figsize=(10,10))
    
    plt.plot(x, y, label= "some function")
    plt.xlabel("x-Axis")
    plt.ylabel("y-Axis")
    print("all set up")
    
    result = io.BytesIO()
    print("binaries created")
    img = plt.savefig(result, format="png")
    result.seek(0)
    print("image created", result)
    
    
    plt.clf()
    plt.close()
    
    return result
    