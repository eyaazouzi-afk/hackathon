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

  
---
## File Descriptions
# Core Python Scripts
*chunking.py

Purpose: Text chunking logic

Functionality: Splits large text documents into manageable chunks

Key Features:
     Configurable chunk size
     Overlap handling for context preservation
     Smart splitting (respects sentences/paragraphs)

*embed.py

Purpose: Embedding generation

Functionality: Converts text chunks into vector embeddings

Key Features:
   Uses pre-trained embedding models
   Batch processing support
   Vector dimension management
   
*importingData.py

Purpose: Data loading and preprocessing

Functionality: Handles data import and initial processing

Key Features:
   Multiple data format support
   Data validation
   Preprocessing pipeline

*qdrant.py

Purpose: Qdrant connection & vector insertion

Functionality: Manages vector database operations

Key Features:
   Database connection setup
   Vector insertion/retrieval
   Collection management

*pythonfile.py

Purpose: Main execution / testing script
Functionality: Orchestrates the entire workflow
Key Features:
   Pipeline execution
   Testing utilities
   Command-line interface

# Data Files
*basedd.txt

Purpose: Sample / base text data

Content: Reference text for testing and demonstration

Usage: Input data for processing pipeline

*Frontend
app.html

Purpose: Web application interface

Functionality: User interface for interacting with the system

Features:
   Query input
   Results display
   Interactive components



# Documentation
*README.md

Purpose: Project documentation

Content:
    Project overview
    Setup instructions
    Usage guide
    API documentation

*hackaton_documentation.pdf

Purpose: Hackathon documentation

Content: Detailed project specifications and requirements
__________________________________________________________
## Quick Start 
## Install dependencies
pip install -r requirements.txt

## Import and process data
python importingData.py

## Run the main application
python pythonfile.py

## Open the web interface
open app.html

____________________________________________________________________________________________________________________________________________________
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
