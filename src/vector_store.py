import faiss
from src.models import get_embedding_model_data

def build_faiss_index():
    # Create a FAISS index for vector similarity search ( it is creating a faiss container)
    dimension, model, embed_model = get_embedding_model_data()
    index = faiss.IndexFlatIP(dimension)

    return index, embed_model



def build_index(docs):
    