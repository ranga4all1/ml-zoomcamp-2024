# Convert keras model to tensorflow SavedModel format


# Download model: wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5


import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('clothing-model.keras')

tf.saved_model.save(model, 'clothing-model')


# Verification:
# tree clothing-model
# ls -lhR clothing-model

# Look at signature
# saved_model_cli show --dir clothing-model --all | less
# OR
# saved_model_cli show --dir clothing-model --tag_set serve --signature_def serving_default