# Bing Grounding API

## Description

This FastAPI application provides a search endpoint that leverages Azure AI Project Client and Bing Grounding to process user queries. It initializes an AI agent with Bing Grounding capabilities, creates conversation threads, and retrieves relevant search results to provide accurate responses.

## Features

-   **Search Endpoint:** Accepts a query string and returns search results using Bing Grounding.
-   **Azure AI Integration:** Utilizes Azure AI Project Client for agent creation, thread management, and message processing.
-   **Bing Grounding:** Enhances search accuracy by grounding the agent with Bing search results.
-   **Environment Variable Validation:** Ensures all required environment variables are set before running the application.
-   **Error Handling:** Implements comprehensive error handling to catch and log exceptions.
-   **Resource Cleanup:** Deletes the created agent after the search process is complete.

## Prerequisites

-   Python 3.12
-   Azure subscription
-   Azure AI Project configured with Bing Grounding enabled
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