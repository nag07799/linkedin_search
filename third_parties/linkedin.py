import requests
import os 
from dotenv import load_dotenv


def scrape_linkedln_profile(linkedin_profile_url:str,mock:bool = False):
    
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/nag07799/967f2eb6528fe593c44d428d9ed693e6/raw/99fe4ac8a5eeb474a605084c21d4798778dc8db2/eden-marco-scrapin.json"
        response = requests.get(linkedin_profile_url,timeout=10)
    
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params={
            "apikey":os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }

        response = requests.get(
            api_endpoint,  
            params =params,
            timeout=10
        )
    data =response.json().get("person")
    data ={
            k:v 
            for k,v in data.items()
            if v not in ([],"","",None)
            and k not in ["certifications"]
        }
    
    return data 




if __name__ =="__main__":
    print(
        scrape_linkedln_profile("https://www.linkedin.com/in/pendekanti/",True)
    )