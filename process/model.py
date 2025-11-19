from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def model():
    
    import numpy as np

    model = load_model("my_fruit_model.h5")

    img = image.load_img("image.jpg", target_size=(224, 224))
    img_array = np.expand_dims(image.img_to_array(img) / 255.0, axis=0)

    out = model.predict(img_array)

    out = out.flatten()

    lis = out.tolist()
    fruits = {
    "fresh_apple" : lis[0],
    "fresh_banana" : lis[1],
    "raw_apple" : lis[2],
    "raw_banana" : lis[3],
    "rotten_apple" : lis[4],
    "rotten_banana" : lis[5],
    }
    return fruits