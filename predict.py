#additing the comments to each line
import sys
import os 


#setting environment variables and importing libraries
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "sa-neophilex-automl-admin.json"
from google.cloud import automl


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = automl.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  project_id = sys.argv[2]
  model_id = sys.argv[3]

  with open(file_path, 'rb') as ff:
    content = ff.read()

  print(get_prediction(content, project_id, model_id))
