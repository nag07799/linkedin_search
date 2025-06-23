import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedln_profile

# information = """

# """



if __name__ =='__main__':
    print("Hello Langchain!")
    # print(os.environ["OPENAI_API_KEY"])
    
    summary_template = """
given the Linkedln information {information} about a person from I want you to create :
    1. a short summary
    2. two interesting facts about them 

"""
    summary_prompt_template = PromptTemplate(input_variables="information",template= summary_template)
    llm = ChatOpenAI(temperature=0,model_name = "gpt-3.5-turbo")
    # llm = ChatOllama(model = "mistral")
    linkedin_data = scrape_linkedln_profile(linkedin_profile_url="https://www.linkedin.com/in/pendekanti/")
    chain = summary_prompt_template|llm #langchain operator
  
    res = chain.invoke(input={"information":linkedin_data})


    print(res.content)




