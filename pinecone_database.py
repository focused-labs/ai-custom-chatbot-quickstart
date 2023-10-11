from llama_index.vector_stores import PineconeVectorStore
from llama_index import StorageContext, VectorStoreIndex
from config import PINECONE_INDEX, PINECONE_ENVIRONMENT


def get_pinecone_index():
    storage_context = get_pinecone_storage_context()
    index = VectorStoreIndex([], storage_context=storage_context)
    return index


def get_pinecone_storage_context():
    vector_store = get_vector_store()
    return StorageContext.from_defaults(vector_store=vector_store)


def get_vector_store():
    return PineconeVectorStore(
        index_name=PINECONE_INDEX,
        environment=PINECONE_ENVIRONMENT
    )
