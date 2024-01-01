import os
import requests
import json
from dotenv import load_dotenv
from util.save_json import save_json
from util.hash_string import hash_string

def scrape_linkeding_profile(linkedin_profile_url: str):

  api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
  header_dic = { "Authorization": f'Bearer {os.environ.get("PROXY_CURL_API_KEY")}' }

  response = requests.get(
    api_endpoint,
    headers=header_dic,
    params={ "url": linkedin_profile_url }
  )

  data = response.json()

  new_data = {
      k: v
      for k, v in data.items()
      if v not in ([], "", "", None)
      and k not in ["people_also_viewed", "certifications"]
  }
  if data.get("groups"):
      for group_dict in data.get("groups"):
          group_dict.pop("profile_pic_url")

  return new_data

def get_linkedin_profile_data(linkedin_profile_url: str):

  hashed_linkedin_profile_url = hash_string(linkedin_profile_url)
  directory = './data'
  file_name = f'{hashed_linkedin_profile_url}.json'

  file_path = os.path.join(directory, file_name)

  if os.path.exists(file_path):
    print('Loading linkedin data from file')
    with open(file_path, 'r') as f:
      linkedin_data = json.load(f)
  else:
    print('Loading linkedin data from ProxyCurl API')
    linkedin_data = scrape_linkeding_profile(linkedin_profile_url=linkedin_profile_url)
    save_json(data=linkedin_data, directory=directory, file_name=file_name)

  return linkedin_data
