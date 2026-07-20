import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI
from src.labs.L1_1_sync_chat import sync_chat
from src.labs.L1_2_async_chat import async_chat
from src.labs.L2_1_web_search_tool import web_search_tool




# import namespaces



def run(): 
    #asyncio.run(async_chat())
    web_search_tool("example query")

if __name__ == '__main__': 
    run()