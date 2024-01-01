import os
from dotenv import load_dotenv
from util.linkedin import get_linkedin_profile_data

dotenv_path = './.env'
load_dotenv(dotenv_path)

if __name__ == '__main__':

  linkedin_data = get_linkedin_profile_data(linkedin_profile_url='https://www.linkedin.com/in/igortrindadedev')

  print(linkedin_data)
