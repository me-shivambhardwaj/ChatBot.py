
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from fastapi import FastAPI
from langserve import add_routes

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()

llm = ChatGroq(model= "openai/gpt-oss-20b")

tools = [search.run]
prompt = "you are a assistant and can search on google for user queries."

agent = create_agent(
    model = llm,
    tools = tools,
    system_prompt = prompt
)


# app = FastAPI(
#     title = "My AI Agent",
# )

# add_routes(
#     app,
#     agent,
#     path ="/agent"
# )
# query = "Address of ONETHE416 Technology?"

# response = agent.invoke(
#     {"messages":[ {"role": "user", "content": query}]}
# )

# print(response["messages"][-1].content)