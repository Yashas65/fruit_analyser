from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def model():
    
    import numpy as np

    model = load_model("my_fruit_model.h5")

    img = image.load_img("banana_test.jpg", target_size=(224, 224))
    img_array = np.expand_dims(image.img_to_array(img) / 255.0, axis=0)

    out = model.predict(img_array)

    out = out.flatten()

    lis = out.tolist()

    print(f"fresh apple : {lis[0]} \n  fresh_banana : {lis[1]} \n raw_apple {lis[2]} \n raw_banana : {lis[3]}, \n rotten_apple : {lis[4]}, \n rotten_banana : {lis[5]}")
