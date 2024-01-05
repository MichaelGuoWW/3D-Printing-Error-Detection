import cv2
import os

directory = 'test_images'
count = 0

sr = cv2.dnn_superres.DnnSuperResImpl_create()
path = "EDSR_x4.pb"
sr.readModel(path)
sr.setModel("edsr", 4) # set the model by passing the value and the upsampling ratio

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith(".jpeg"):
        img = cv2.imread(f"test_images/{filename}")
        result = sr.upsample(img) # upscale the input image
        cv2.imwrite(f"test_sr_images/{filename}", result)
        count = count + 1
        print(f"{count}: {filename} is written successful")

