# Bing Grounding API

## Description

This FastAPI application provides a search endpoint that leverages Azure AI Project Client and Bing Grounding to process user queries. It initializes an AI agent with Bing Grounding capabilities, creates conversation threads, and retrieves relevant search results to provide accurate responses.

Example usage:
![Screenshot 2025-04-03 125616](https://github.com/user-attachments/assets/748fad33-8282-49c5-99c7-62e54ec299ca)

Example request:
`http://127.0.0.1:8000/search?query=wisconsin%20election`

Example response:

```
{
  "response": {
    "type": "text",
    "text": {
      "value": "In the Wisconsin elections held on April 1, 2025, one of the key races was for a seat on the state Supreme Court. This race between Liberal Susan Crawford and Conservative Brad Schimel became notable for being the most expensive state court race in U.S. history. Additionally, voters were deciding on a constitutional amendment regarding the state's Voter ID law【3:0†source】.",
      "annotations": [
        {
          "type": "url_citation",
          "text": "【3:0†source】",
          "start_index": 362,
          "end_index": 374,
          "url_citation": {
            "url": "https://www.wisn.com/article/wisconsin-live-election-results-april-2025/64326481",
            "title": "Live results: Wisconsin election April 2025 - WISN Channel 12"
          }
        }
      ]
    }
  }
}
```

## Features

-   **Search Endpoint:** Accepts a query string and returns search results using Bing Grounding.
-   **Azure AI Integration:** Utilizes Azure AI Project Client for agent creation, thread management, and message processing.
-   **Bing Grounding:** Enhances search accuracy by grounding the agent with Bing search results.

## Prerequisites

-   Python 3.12
-   Azure subscription
-   Azure AI Agent configured with Bing Grounding enabled
    -    [ai agent quickstart](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry-portal)
    -    [bing-grounding documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/bing-grounding)
-   Required environment variables:
    -   `PROJECT_CONNECTION_STRING_ENV`: Connection string for the Azure AI Project.
    -   `BING_CONNECTION_NAME_ENV`: Name of the Bing connection in the Azure AI Project.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install dependencies using Pip:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set the required environment variables:

    ```bash
    export PROJECT_CONNECTION_STRING_ENV="<your_project_connection_string>"
    export BING_CONNECTION_NAME_ENV="<your_bing_connection_name>"
    ```

## Usage

1.  Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2.  Access the search endpoint:

    ```
    http://localhost:8000/search?query=<your_search_query>
    ```

3.  View the Swagger documentation:

    ```
    http://localhost:8000/docs
    ```
    ** This is a POC and performance is not optimized.

## API Endpoint

### `/search`

-   **Summary:** Search Endpoint
-   **Description:** Accepts a query string and returns search results.
-   **Method:** GET
-   **Query Parameters:**
    -   `query` (string, required): The search query.
-   **Returns:**
    -   `dict`: A dictionary containing the search results.

## Error Handling

The application includes error handling to manage exceptions that may occur during the search process. Errors are logged to the console.

## Cleanup

After each search, the application deletes the created agent to clean up resources.

## Contributing

Contributions are welcome! Please submit a pull request with your proposed changes.

## License

[MIT](LICENSE)
