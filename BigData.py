﻿# -*- coding: utf-8 -*-
"""Exceções.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mM-2pkxpW_Qg_90qT6z3rA3Qp0whNFFA
"""

import requests
import json
from PIL import Image
from io import BytesIO

for i in range(20):
  # Get the image URL from the API
  response = requests.get('https://api.waifu.pics/nsfw/waifu')

  json_data = json.loads(response.content)
  image_url = json_data["url"]

  # Download the image
  response = requests.get(image_url)

  # Get the image dimensions
  image = Image.open(BytesIO(response.content))
  width, height = image.size

  # Resize the image to 1/3 of its original size
  new_width = width // 3
  new_height = height // 3
  resized_image = image.resize((new_width, new_width))


  # Display the image
  display(resized_image)
