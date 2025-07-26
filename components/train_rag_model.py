from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read text and split into chunks
with open("science_grade10.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Simple splitting (500 word chunks with overlap)
def split_text(text, max_words=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words - overlap):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
    return chunks

chunks = split_text(raw_text)

# Create vector DB using Chroma (fully local, new API)
chroma_client = chromadb.PersistentClient(path=".chroma")
collection = chroma_client.get_or_create_collection(name="science-book")

# Embed and store chunks
print(f"Loaded {len(chunks)} chunks.")
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(documents=[chunk], embeddings=[embedding], ids=[str(i)])
    print(f"Stored chunk {i+1}/{len(chunks)}")
print("All chunks stored successfully.")