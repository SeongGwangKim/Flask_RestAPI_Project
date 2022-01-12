import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import cv2


def preprocess_image(image, filename):
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  hr_image = image
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
  if hr_image.shape[-1] == 4:
    hr_image = hr_image[...,:-1]
  hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
  hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
  hr_image = tf.cast(hr_image, tf.float32)
  hr_image = tf.expand_dims(hr_image, 0)

  model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")
  fake_image = model(hr_image)
  fake_image = tf.squeeze(fake_image)
  fake_image = tf.clip_by_value(fake_image, 0, 255)
  fake_image = Image.fromarray(tf.cast(fake_image, tf.uint8).numpy())
  fake_image.save("rev_"+"%s" % filename)
  return fake_image

