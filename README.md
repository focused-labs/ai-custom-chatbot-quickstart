# ****** WORK IN PROGRESS ******

# Focused Labs Developer Kit · Getting Started · The Basics/Bare Minimum

# Prerequisites

1. A Pinecone Vector Database. You can create a free account [at Pinecone's website](https://www.pinecone.io/).
2. A Open AI API account (api key). You can sign up [at Open AI's website](https://platform.openai.com/signup).
3. Python (and your favorite IDE). We are using python v3.10.7.

# Set up your environment

To test and make sure you have your environment working,

- install dependencies: ` pip install -r  requirements.txt`
- start the app with the following command:  `python3 main.py`
- with your favorite request sender (we recommend Postman), send a `get` request to the root endpoint to confirm it's
  working
- If you receive the message `Hello World`, you're good to go!

# Importing Data

### Lives in `import_service.py`

- Create a Pinecone Account, Create an index
    - Give it a name
    - Dimensions = 1536. This is the number of output dimensions from Open AI's embedding
      model `text-embedding-ada-002`. [Source](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
    - Green light indicates that it's initialized and ready to go
- Update environment variables
    - In the `.env` file, you will need to update the `PINECONE_API_KEY` and `OPENAI_API_KEY` with your own keys.
    - In the `config.py` file, you will need to update `PINECONE_INDEX` and `PINECONE_ENVIRONMENT` values
- Use a Llama Index loader
- Start the app (`python3 main.py`)
    - You will hit the endpoint `/load-website-docs` with the website pages of your choice.
        - For example: the json body of your request will look something like this:
          ```
          {
            "page_urls": [
              "https://focusedlabs.io",
              "https://focusedlabs.io/about",
              "https://focusedlabs.io/contact",
              "https://focusedlabs.io/case-studies",
              "https://focusedlabs.io/case-studies/agile-workflow-enabled-btr-automation",
              "https://focusedlabs.io/case-studies/hertz-technology-new-markets",
              "https://focusedlabs.io/case-studies/aperture-agile-transformation",
              "https://focusedlabs.io/case-studies/automated-core-business-functionality"
            ]
          }```

- You'll see the vector number increase in your Pinecone dashboard.

Yay!!! Now you have data you can query.

# Query Data

### Lives in `query_service.py`

## Search Database

Alright, this is where things can get complicated. But, we'll start with the bare minimum.

First, we'll make sure we can query the database. This will execute semantic search on the data you've loaded.
For more details on what semantic search with Pinecone looks like, start
with [this article](https://www.pinecone.io/learn/search-with-pinecone/)

## (Optional) Add an agent

Ok, you can retrieve data from the database. But what happens when a user asks unrelated questions like "who are you?"
We need to add an agent. You can think of agents as the brain behind deciding what tool to use. Sometimes, you need to
query the database. Sometimes you don't. The agent decides.

#### FAQ

- If you run into a `PermissionError: [Errno 13] Permission denied:` then make sure you are running your app with
  Python3