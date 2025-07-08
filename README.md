# MongoDB Agent with Azure OpenAI

A powerful MongoDB database agent that uses Azure OpenAI and MongoDB MCP (Model Context Protocol) to perform intelligent database operations.

## Features

- 🍃 **Database Overview**: List all databases and collections
- 🔍 **Data Analysis**: Count documents and analyze data distribution
- 📈 **Schema Analysis**: Examine collection schemas and field types
- 🔎 **Sample Data Exploration**: View sample documents from collections
- 🏗️ **Database Operations**: Create collections and insert data
- 🔍 **Advanced Queries**: Perform aggregation queries and statistics
- 📊 **Index Analysis**: Review indexes and optimization opportunities
- 🧹 **Data Maintenance**: Find duplicates and data quality issues

## Prerequisites

- Node.js (for mongodb-mcp-server)
- Python 3.8+
- MongoDB instance running on localhost:27317
- Azure OpenAI API access

## Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   # Azure OpenAI Configuration
   AZURE_OAI_KEY=your_azure_openai_api_key_here
   AZURE_OAI_BASE_PATH=https://your-resource-name.openai.azure.com/
   AZURE_OAI_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OAI_API_VERSION=2024-02-15-preview
   
   # MongoDB Configuration (optional override)
   MONGODB_CONNECTION_STRING=mongodb://localhost:27317/?directConnection=true
   ```

3. **Start your MongoDB instance** (if not already running):
   ```bash
   # Example using Docker
   docker run -p 27317:27017 mongo:latest
   ```

## Usage

Run the MongoDB agent:

```bash
python mongodb_agent.py
```

### Example Queries

The agent can handle various MongoDB operations:

- **Database exploration**: "Show me all databases and their collections"
- **Data querying**: "Find all users with age greater than 25"
- **Schema analysis**: "What's the schema of the products collection?"
- **Data insertion**: "Insert a new user with name 'John', email 'john@example.com'"
- **Aggregation**: "Group sales by month and calculate totals"
- **Index management**: "Create an index on the email field"
- **Data maintenance**: "Find duplicate records in the users collection"

### Interactive Mode

The agent runs in interactive mode where you can:
1. Ask natural language questions about your MongoDB database
2. Request specific database operations
3. Get schema analysis and optimization suggestions
4. Perform data exploration and analysis

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│  Azure OpenAI    │───▶│  MongoDB MCP    │
│                 │    │     Agent        │    │    Server       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   LangGraph      │    │   MongoDB       │
                       │   ReAct Agent    │    │   Database      │
                       └──────────────────┘    └─────────────────┘
```

## Configuration

The agent uses the MongoDB MCP server with the following configuration:
- **Command**: `npx mongodb-mcp-server`
- **Connection**: `mongodb://localhost:27317/?directConnection=true`
- **Transport**: stdio

## Troubleshooting

1. **Connection Issues**: Ensure MongoDB is running on the specified port
2. **Azure OpenAI Errors**: Verify your API key and endpoint configuration
3. **MCP Server Issues**: Make sure `mongodb-mcp-server` is installed via npm

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License 