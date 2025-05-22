import os 
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

client = AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free", openai_client=client),
    name="my_agent",
    instructions="you are a helpful assistant",
)

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("agent", agent)

@cl.on_message
async def main(message: cl.Message):
    # Get the agent from user session
    agent = cl.user_session.get("agent")
    
    # Create a Chainlit message to stream the response
    msg = cl.Message(content="")
    await msg.send()
    
    # Run the agent with user input
    jawab = Runner.run_streamed(starting_agent=agent, input=message.content)
    
    full_response = ""
    async for event in jawab.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            delta = event.data.delta
            full_response += delta
            await msg.stream_token(delta)
    
    # Update the message with final content
    await msg.update()
    # await msg.update(content=full_response)
