import face_recognition
import os
import pickle
import PIL.Image
import numpy as np

known_face_encodings = []
known_face_names = []
root = "known_faces"
for dirpath, dirnames, filenames in os.walk(root):
    for file in filenames:
        print("file:", file)
        im = PIL.Image.open(os.path.join(dirpath, file))
        im = im.resize((250,250))
        im = im.convert("RGB")
        image = np.array(im)
        print(im.size)
        image_encoding = face_recognition.face_encodings(image)[0] 
        known_face_encodings.append(image_encoding)
        filename, extension = os.path.splitext(file)
        known_face_names.append(filename)
new_dict = {}
new_dict["known_face_encodings"] = known_face_encodings
new_dict["known_face_names"] = known_face_names

with open("face_encodings.pickle","wb") as f:
    pickle.dump(new_dict,f, pickle.HIGHEST_PROTOCOL)
    print("加载入文件完成...")