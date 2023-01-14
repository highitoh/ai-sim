#@title Imports and function definitions

# For running inference on the TF-Hub module.
import base64
import pickle
import requests
import sys
import tempfile
import time
import uvicorn

import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt

from fastapi import FastAPI
from pydantic import BaseModel
from six.moves.urllib.request import urlopen
from six import BytesIO
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

print("Import Completed")
#----- End Import Library -----

url = " https://XXXXX.execute-api.ap-northeast-1.amazonaws.com/api"
port = 8000
type = "client"

exec_id      = []
pre_exec_id  = []
post_exec_id = []

send_data = None
recv_data = None
src_img = None
app = FastAPI()

output_data = np.empty([360, 30])
start_time_all = None
end_time_all = None
start_time = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
end_time   = [-1,-1,-1,-1,-1,-1,-1,-1,-1]

#----- Begin Load MobileNet Model -----
#detector = hub.load("https://tfhub.dev/tensorflow/faster_rcnn/resnet152_v1_1024x1024/1")
detector = tf.saved_model.load("/home/ubuntu/work/ai-sim/evaluation/model/resnet50")
print("Import Completed")
#----- End Load MobileNet Model -----

class ClientData(BaseModel):
  data: str

def display_image(image):
  fig = plt.figure(figsize=(20, 15))
  plt.grid(False)
  # plt.imshow(image)
  plt.imsave("result.jpg", image)

def download_and_resize_image(url, new_width=256, new_height=256,
                              display=False):
  global exec_id, send_data, start_time, end_time
  filename = None
  
  if 1 in exec_id:
    # Preprocess for Task1
    if exec_id[0] == 1:
      image_data = None
    start_time[0] = time.time()

    # Main Process of Task1
    _, filename = tempfile.mkstemp(suffix=".jpg")
    response = urlopen(url)
    image_data = response.read()
    image_data = BytesIO(image_data)

    # Postprocess for Task1
    end_time[0] = time.time()
    send_data = image_data

  if 2 in exec_id:
    # Preprocess for Task2
    if exec_id[0] == 2:
      image_data = recv_data
    start_time[1] = time.time()

    # Main Process of Task2
    pil_image = Image.open(image_data)
    pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)
    pil_image_rgb = pil_image.convert("RGB")

    # Postprocess for Task2
    end_time[1] = time.time()
    send_data = pil_image_rgb

  if 3 in exec_id:
    # Preprocess for Task3
    if exec_id[0] == 3:
      pil_image_rgb = recv_data
    start_time[2] = time.time()

    # Main Process of Task3
    pil_image_rgb.save(filename, format="JPEG", quality=90)
    # print("Image downloaded to %s." % filename)  # Not Needed
    # if display:
    #  display_image(pil_image)

    # Postprocess for Task3
    end_time[2] = time.time()
    send_data = None

  return filename

def draw_bounding_box_on_image(image,
                               ymin,
                               xmin,
                               ymax,
                               xmax,
                               color,
                               font,
                               thickness=4,
                               display_str_list=()):
  """Adds a bounding box to an image."""
  draw = ImageDraw.Draw(image)
  im_width, im_height = image.size
  (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                ymin * im_height, ymax * im_height)
  draw.line([(left, top), (left, bottom), (right, bottom), (right, top),
             (left, top)],
            width=thickness,
            fill=color)

  # If the total height of the display strings added to the top of the bounding
  # box exceeds the top of the image, stack the strings below the bounding box
  # instead of above.
  display_str_heights = [font.getsize(ds)[1] for ds in display_str_list]
  # Each display_str has a top and bottom margin of 0.05x.
  total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

  if top > total_display_str_height:
    text_bottom = top
  else:
    text_bottom = top + total_display_str_height
  # Reverse list and print from bottom to top.
  for display_str in display_str_list[::-1]:
    text_width, text_height = font.getsize(display_str)
    margin = np.ceil(0.05 * text_height)
    draw.rectangle([(left, text_bottom - text_height - 2 * margin),
                    (left + text_width, text_bottom)],
                   fill=color)
    draw.text((left + margin, text_bottom - text_height - margin),
              display_str,
              fill="black",
              font=font)
    text_bottom -= text_height - 2 * margin


def draw_boxes(image, boxes, class_names, scores, max_boxes=10, min_score=0.1):
  """Overlay labeled boxes on an image with formatted scores and label names."""
  colors = list(ImageColor.colormap.values())

  try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf",
                              25)
  except IOError:
    print("Font not found, using default font.")
    font = ImageFont.load_default()

  for i in range(min(boxes.shape[0], max_boxes)):
    if scores[i] >= min_score:
      ymin, xmin, ymax, xmax = tuple(boxes[i])
      display_str = "{}: {}%".format(class_names[i],
                                     int(100 * scores[i]))
      color = colors[hash(class_names[i]) % len(colors)]
      image_pil = Image.fromarray(np.uint8(image)).convert("RGB")
      draw_bounding_box_on_image(
          image_pil,
          ymin,
          xmin,
          ymax,
          xmax,
          color,
          font,
          display_str_list=[display_str])
      np.copyto(image, np.array(image_pil))
  return image

def load_img(path):
  global exec_id, send_data, start_time, end_time, src_img
  img = None

  if 4 in exec_id:
    # Preprocess for Task4
    if exec_id[0] == 4:
      pass
    start_time[3] = time.time()

    # Main Process of Task4
    img = tf.io.read_file(path)

    # Postprocess for Task4
    end_time[3] = time.time()
    send_data = img

  if 5 in exec_id:
    # Preprocess for Task5
    if exec_id[0] == 5:
      img = recv_data
    start_time[4] = time.time()

    # Main Process of Task5
    img = tf.image.decode_jpeg(img, channels=3)

    # Postprocess for Task5
    end_time[4] = time.time()
    send_data = img
    src_img = img
  return img

def run_detector(detector, path):
  global exec_id, send_data, src_img, start_time, end_time

  img = load_img(path)

  print(exec_id)  
  if 6 in exec_id:
    # Preprocess for Task6
    if exec_id[0] == 6:
      img = recv_data
    start_time[5] = time.time()

    # Main Process of Task6
    converted_img  = tf.image.convert_image_dtype(img, tf.uint8)[tf.newaxis, ...]

    # Postprocess for Task6
    end_time[5] = time.time()
    send_data = converted_img

  if 7 in exec_id:
    # Preprocess for Task7
    if exec_id[0] == 7:
      converted_img = recv_data
    start_time[6] = time.time()

    # Main Process of Task7
    result = detector(converted_img)
    result = {key:value.numpy() for key,value in result.items()}

    # Postprocess for Task7
    end_time[6] = time.time()
    send_data = result

    print("Found %d objects." % len(result["detection_scores"][0]))
    # print("Inference time: ", end_time-start_time)

  if 8 in exec_id:
    # Preprocess for Task8
    if exec_id[0] == 8:
      result = recv_data
    if img is None:
      img = src_img
    start_time[7] = time.time()

    # Main Process of Task8
    image_with_boxes = draw_boxes(
        img.numpy(), result["detection_boxes"][0],
        result["detection_classes"][0], result["detection_scores"][0])

    # Postprocess for Task8
    end_time[7] = time.time()
    send_data = image_with_boxes

  if 9 in exec_id:
    # Preprocess for Task9
    if exec_id[0] == 9:
      image_with_boxes = recv_data
    start_time[8] = time.time()

    # Main Process of Task9
    display_image(image_with_boxes)

    # Postprocess for Task9
    end_time[8] = time.time()
    send_data = None

def detect():
  global src_img

  image_url = "https://upload.wikimedia.org/wikipedia/commons/6/60/Naxos_Taverna.jpg"  #@param
  downloaded_image_path = None

  # Begin Prepare Image (Temporary)
  #_, filename = tempfile.mkstemp(suffix=".jpg")
  #response = urlopen(image_url)
  #image_data = response.read()
  #image_data = BytesIO(image_data)
  #pil_image = Image.open(image_data)
  #pil_image = ImageOps.fit(pil_image, (1280, 856), Image.ANTIALIAS)
  #pil_image_rgb = pil_image.convert("RGB")
  #pil_image_rgb.save(filename, format="JPEG", quality=90)
  #src_img = tf.io.read_file(filename)
  #src_img = tf.image.decode_jpeg(src_img, channels=3)
  # End Prepare Image (Temporary)

  if(any(x in exec_id for x in [1,2,3])):
    downloaded_image_path = download_and_resize_image(image_url, 1280, 856, True)
  if(any(x in exec_id for x in [4,5,6,7,8,9])):
    run_detector(detector, downloaded_image_path)

def send(send_data, port):
    # Make Data for Json Request
    byte_data = pickle.dumps(send_data)
    json_data = base64.b64encode(byte_data).decode('utf-8')
    json_message = {"data": json_data}

    try:
        print("Send Data to {}".format(url))
        with open("message.json", mode="w") as f:
          import json
          f.write(json.dumps(json_message))
        response = requests.post(url, json=json_message, timeout=300)
        if response.ok:
          response_data = response.json()
        else:
          print("HTTP %d => %s" % (response.status_code,
                                   response.content.decode("utf-8")), flush=True)
          response_data = None           
    except Exception as e:
        print(e, flush=True)
        response_data = None
    return response_data

def client_run(port):
  global type, exec_id, send_data, recv_data, start_time_all, end_time_all

  start_time_all = time.time()
  response_data = None
  if type == "client":
    exec_id = pre_exec_id
    detect()
    if send_data is not None:
      response_data = send(send_data, port)
    if response_data is not None:
      exec_id = post_exec_id
      decoded_b = base64.b64decode(response_data["data"].encode())
      recv_data = pickle.loads(decoded_b)
      detect()
  end_time_all = time.time()
  
@app.post("/invoke")
def server_run(client_data: ClientData):
  global recv_data, type, port
  decoded_b = base64.b64decode(client_data.data.encode())
  recv_data = pickle.loads(decoded_b)
  print("server_run")
  if type == "server":
    detect()
    if send_data != None:
      send(send_data, port+1)
  df = pd.DataFrame(np.array([start_time, end_time, np.array(end_time)-np.array(start_time)]).T, columns=["start", "end", "elapsed"])
  df.to_excel("{}_{}.xlsx".format(type, port))

def collect_data():
  elapsed_time_all = end_time_all - start_time_all
  elapsed_time = np.array(end_time) - np.array(start_time)
  output_data[i] = np.hstack([start_time_all, end_time_all, elapsed_time_all, start_time, end_time, elapsed_time]).reshape(1,30)

def output_excel():
  column_name = ['start_time','end_time','elapsed_time','st1','st2','st3','st4','st5','st6','st7','st8','st9',
               'et1','et2','et3','et4','et5','et6','et7','et8','et9',
               'el1','el2','el3','el4','el5','el6','el7','el8','el9']
  df = pd.DataFrame(output_data, columns=column_name)
  df.to_excel("{}_{}.xlsx".format(type, port))

# USAGE
# python edgeapp.py [type] [exed_id] [port]
# type: "client" / "server"
# pre_exec_id : 1,2,3,4,5,6 (comma-separated)
# post_exec_id: 8,9 (comma-separated)
# port: 8000 (default=8000)
# ex.) python edgeapp.py server 1,2,3,4,5,6 8,9 8001

if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 3:
      type = sys.argv[1]
      pre_exec_id = [int(x) for x in sys.argv[2].split(',')]
      print("pre_exec_id :" + str(pre_exec_id))
      post_exec_id = [int(x) for x in sys.argv[3].split(',')]
      print("post_exec_id:" + str(post_exec_id))
      if type == "client":
        for i in range(0, 360):
          print("CLIENT RUN " + str(i))
          client_run(port)
          collect_data()
          print("ELAPSED TIME:" + str(end_time_all - start_time_all))
          time.sleep(10)
        output_excel()
      elif type == "server":
        port = 8000   # default
        if len(args) >= 4:
          port = int(sys.argv[4])
        uvicorn.run(app, host="0.0.0.0", port=port)
