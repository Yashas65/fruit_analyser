# processing the image and returning the output list

#rember the order in the list is as follows fresh_apple fresh_banana raw_apple raw_banana rotten_apple rotten_banana

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from process.sensor import read_data

def model():
        
    import numpy as np

    model = load_model("process/image_model.h5")
    
    #image
    img = image.load_img("process/image.jpg", target_size=(224, 224))
    img_array = np.expand_dims(image.img_to_array(img) / 255.0, axis=0)
    
    #sensors
    sensor_readings = read_data()
    final_arr = []
    final_arr.append(img_array)
    final_arr.append(sensor_readings)

    out = model.predict(final_arr)

    out = out.flatten()

    lis = out.tolist()
    return lis
