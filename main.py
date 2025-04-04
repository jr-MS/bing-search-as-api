from fastapi import FastAPI, Query
import os  
  
from azure.ai.projects import AIProjectClient  
from azure.ai.projects.models import BingGroundingTool  
from azure.identity import DefaultAzureCredential  
from dotenv import load_dotenv

load_dotenv()
#Create the FastAPI application with optional metadata
app = FastAPI(
title="My Search API",
description="An example FastAPI application with a /search endpoint, complete with automatic Swagger docs at /docs.",
version="1.0.0"
)

@app.get("/search", summary="Search Endpoint", description="Accepts a query string and returns search results.")
async def search(query: str = Query(..., description="Search query")):

    """
    Search endpoint that accepts a query string and returns search results.
    
    Args:
        query (str): The search query provided by the user.
        
    Returns:
        dict: A dictionary containing the search results.
    """ 
    print("Starting the Bing Grounding AI agent setup process.")  
  
    # Step 0: Validate environment variables  
    print("Step 0: Validating environment variables...")  
    project_conn_str = os.environ.get("PROJECT_CONNECTION_STRING_ENV")
    bing_connection_name = os.environ.get("BING_CONNECTION_NAME_ENV")
    agent_name = os.environ.get("AGENT_NAME")
    agent_instructions = os.environ.get("AGENT_INSTRUCTIONS")
    agent_llm = os.environ.get("AGENT_LLM", 'gpt-4o')

    missing_vars = []
    if not project_conn_str:
        missing_vars.append("PROJECT_CONNECTION_STRING_ENV")
    if not bing_connection_name:
        missing_vars.append("BING_CONNECTION_NAME_ENV")
    if missing_vars:
        raise EnvironmentError(
            f"Missing environment variable(s): {', '.join(missing_vars)}"
        )
        raise EnvironmentError(  
            f"Missing environment variable(s): {', '.join(missing_vars)}"  
        )  
    print("Environment variables validated successfully.")  
  
    try:  
        # Step 1: Initialize the AI Project Client with default credentials  
        print("Step 1: Initializing Azure AI Project Client...")  
        credential = DefaultAzureCredential()  
        project_client = AIProjectClient.from_connection_string(  
            credential=credential,  
            conn_str=project_conn_str  
        )  
        print("Azure AI Project Client initialized.")  
  
        with project_client:  
            # Step 2: Enable the Grounding with Bing search tool  
            print("Step 2: Enabling Bing Grounding Tool...")  
            bing_connection = project_client.connections.get(  
                connection_name=bing_connection_name  
            )  
            bing_conn_id = bing_connection.id  
            print(f"Bing connection ID: {bing_conn_id}")  
  
            # Initialize the Bing Grounding tool with the connection ID  
            bing_tool = BingGroundingTool(connection_id=bing_conn_id)  

            agents = project_client.agents.list_agents()
            agent = next((a for a in agents.data if a.name == agent_name), None)

            if agent is None:
                # Step 3: Create an agent with the Bing Grounding tool  
                print("Step 3: Creating agent with Bing Grounding Tool...")  
                agent = project_client.agents.create_agent(  
                    model=agent_llm,  
                    name=agent_name,  
                    instructions=agent_instructions,  
                    tools=bing_tool.definitions,  
                    headers={"x-ms-enable-preview": "true"}  
                )  
            print(f"Created agent, ID: {agent.id}")  
  
            # Step 4: Create a conversation thread  
            print("Step 4: Creating conversation thread...")  
            thread = project_client.agents.create_thread()  
            print(f"Created thread, ID: {thread.id}")  
  
            # Step 5: Add a user message to the thread  
            print("Step 5: Adding user message to the thread...")  
            user_message = project_client.agents.create_message(  
                thread_id=thread.id,  
                role="user",  
                content=query  
            )  
            print(f"Created user message, message ID: {user_message.id}")  
  
            # Step 6: Run the agent  
            print("Step 6: Running the agent...")  
            run = project_client.agents.create_and_process_run(  
                thread_id=thread.id,  
                agent_id=agent.id  
            )  
            print(f"Run finished with status: {run.status}")  
  
            if run.status == "failed":  
                print(f"Run failed: {run.last_error}")  
            else:  
                # Step 8: Retrieve and print the agent's response  
                print("Step 8: Retrieving agent's response...")  
                messages = project_client.agents.list_messages(thread_id=thread.id)  
                last_msg = messages.get_last_text_message_by_role("assistant")  
  
                if last_msg:  
                    print(f"Agent Response: {last_msg.text.value}")  
                else:  
                    print("No response from the agent.")  
                return {"response": last_msg}
  
            # Step 9 (optional): Clean up resources  
            #print("Step 9: Cleaning up resources...")  
            #project_client.agents.delete_agent(agent.id)  
            #print(f"Deleted agent (ID: {agent.id})")  
  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
    print("Bing Grounding AI agent setup process completed.")  

