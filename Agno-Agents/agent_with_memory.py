from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import lance_db, SearchType

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

agent=Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You are an assistant please reply based on the user queries",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("summurize this video https://www.youtube.com/watch?v=f5Moynhe0XQ using its transcript", stream=True)