# FinMatch: A Context-Aware Financial Product Recommendation System
--- 
**Documentation compléte du projet** 

**Auteurs : Mohamed Amine Rachid / Nour Zouari / Karim Dami / Eya Azouzi** 
______________________________________________________________________________________________________________________________________________________________________________________________________________
## Introduction 
______________________________________________________________________________________________________________________________________________________________________________________________________________

FinMatch is a multimodal embedding and vector search system that combines **text, image, and audio** data to enable semantic similarity search using a vector database.
The project converts different input modalities into embeddings, fuses them into a single vector representation, and stores them in **Qdrant** for efficient retrieval.
______________________________________________________________________________________________________________________________________________________________________________________________________________

## Features
______________________________________________________________________________________________________________________________________________________________________________________________________________

- Text chunking and preprocessing
- Embedding generation
- Multimodal fusion
- Vector storage and search
- CSV-based data ingestion
______________________________________________________________________________________________________________________________________________________________________________________________________________
 ## Tech Stack
- Python
- PyTorch
- CLIP
- Whisper
- Qdrant

--- 
## Pipeline

The FinMatch system follows the steps below:
-Load and preprocess data
  Raw data is loaded from text or CSV files and cleaned before processing.

-Split text into chunks
  Large documents are divided into smaller overlapping chunks to preserve semantic context.

-Generate embeddings
  Each chunk is converted into a dense vector using pretrained embedding models.

-Normalize vectors
  All embeddings are L2-normalized to ensure accurate cosine similarity comparison.

-Store vectors in Qdrant
  Normalized vectors are stored in a Qdrant collection along with metadata.

-Perform similarity search
  User queries are embedded and compared against stored vectors to retrieve the most relevant results.
______________________________________________________________________________________________________________________________________________________________________________________________________________
## Project Structure 
```text
.
├── README.md                    # Project documentation
├── basedd.txt                   # Sample / base text data
├── chunking.py                  # Text chunking logic
├── embed.py                     # Embedding generation
├── importingData.py             # Data loading and preprocessing
├── pythonfile.py                # Main execution / testing script
├── qdrant.py                    # Qdrant connection & vector insertion
├── app.html                     # Web application interface
└── hackaton_documentation.pdf   # Hackathon documentation
