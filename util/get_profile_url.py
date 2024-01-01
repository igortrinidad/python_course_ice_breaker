
import os
from util.CustomSerpAPIWrapper import CustomSerpAPIWrapper

def get_profile_url(text: str) -> str :

  """Searches for a Linkedin profile URL in a given text."""

  print(os.getenv('SERPAPI_API_KEY'))
    

  search = CustomSerpAPIWrapper(serpapi_api_key=os.getenv('SERPAPI_API_KEY'))
  
  res = search.run(f'"{text}"')
  
  return res