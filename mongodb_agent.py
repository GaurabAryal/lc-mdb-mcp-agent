from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def create_mongodb_agent():
    """Create a MongoDB-focused agent with database operation capabilities"""
    
    client = MultiServerMCPClient(
        {
            "mongodb": {
                "command": "npx",
                "args": [
                    "-y",
                    "mongodb-mcp-server",
                    "--connectionString",
                    "mongodb://localhost:27317/?directConnection=true"
                ],
                "transport": "stdio"
            }
        }
    )
    
    tools = await client.get_tools()
    
    # Configure Azure OpenAI
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OAI_BASE_PATH"),
        api_key=os.getenv("AZURE_OAI_KEY"),
        api_version=os.getenv("AZURE_OAI_API_VERSION"),
        deployment_name=os.getenv("AZURE_OAI_DEPLOYMENT_NAME"),
        temperature=0.1
    )
    
    agent = create_react_agent(llm, tools)
    
    return agent

async def main():
    """Main function to demonstrate MongoDB agent capabilities"""
    
    print("🍃 Initializing MongoDB Agent...")
    agent = await create_mongodb_agent()
    
    # Example queries showcasing MongoDB capabilities
    queries = [
        {
            "description": "📊 Database Overview",
            "query": "List all databases and their collections. Show me what's available in this MongoDB instance."
        },
        {
            "description": "🔍 Data Analysis",
            "query": "Find the total count of documents in each collection across all databases. Show me the data distribution."
        },
        {
            "description": "📈 Schema Analysis",
            "query": "Analyze the schema of the largest collection. What fields are available and what are their types?"
        },
        {
            "description": "🔎 Sample Data Exploration",
            "query": "Show me sample documents from the most interesting collection. What kind of data is stored?"
        },
        {
            "description": "🏗️ Database Operations",
            "query": "Create a new collection called 'analytics_logs' and insert some sample log entries with timestamps, user_id, action, and metadata fields."
        },
        {
            "description": "🔍 Advanced Query",
            "query": "Perform an aggregation query to group data by a meaningful field and calculate statistics like count, average, or sum."
        },
        {
            "description": "📊 Index Analysis",
            "query": "Show me all indexes on the collections. Are there any performance optimization opportunities?"
        },
        {
            "description": "🧹 Data Maintenance",
            "query": "Find any duplicate records or data quality issues. Suggest cleanup operations if needed."
        }
    ]
    
    print("\n🚀 MongoDB Agent is ready! Here are some example operations:\n")
    
    for i, query_info in enumerate(queries, 1):
        print(f"{i}. {query_info['description']}")
        print(f"   Query: {query_info['query']}")
        print()
    
    # Interactive mode
    print("💬 Interactive Mode - Ask me anything about your MongoDB database!")
    print("Examples:")
    print("- 'Show me all users from the users collection'")
    print("- 'Create an index on the email field'")
    print("- 'Find documents created in the last 7 days'")
    print("- 'Aggregate sales data by month'")
    print("- 'What's the schema of the products collection?'")
    print("\nType 'quit' to exit.\n")
    
    while True:
        user_input = input("🔍 Your MongoDB query: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if not user_input:
            continue
            
        try:
            print(f"\n🔄 Processing: {user_input}")
            response = await agent.ainvoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            
            print(f"\n📋 Response:")
            # Handle different response formats
            if hasattr(response, 'content'):
                print(response.content)
            elif isinstance(response, dict):
                if 'messages' in response:
                    last_message = response['messages'][-1]
                    if hasattr(last_message, 'content'):
                        print(last_message.content)
                    elif isinstance(last_message, dict):
                        print(last_message.get('content', str(last_message)))
                    else:
                        print(str(last_message))
                else:
                    print(str(response))
            else:
                print(str(response))
            print("\n" + "="*50 + "\n")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("Please try a different query.\n")

if __name__ == "__main__":
    asyncio.run(main()) 