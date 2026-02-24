# LLMs, RAG, and Foundations of NLP & ML

## GenAI Course Notes

------------------------------------------------------------------------

# 1️⃣ Foundations: Machine Learning (ML)

## What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence (AI) where
systems **learn patterns from data instead of being explicitly
programmed**.

Instead of writing rules like:

    if word == "love" → positive

We give the model many examples and it learns patterns automatically.

------------------------------------------------------------------------

## Core Types of ML

  ------------------------------------------------------------------------
  Type            Description                     Example
  --------------- ------------------------------- ------------------------
  Supervised      Learn from labeled data         Spam detection
  Learning                                        

  Unsupervised    Find structure in unlabeled     Customer clustering
  Learning        data                            

  Reinforcement   Learn via rewards and penalties Game playing
  Learning                                        
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## Supervised Learning Example

Goal: Predict whether a review is positive or negative.

Input: "I love this product"

Label: Positive

The model learns associations between words and sentiment.

------------------------------------------------------------------------

## Key ML Concepts

### Features

Numerical representation of data.

### Training vs Inference

-   Training → Model learns patterns\
-   Inference → Model makes predictions

### Overfitting

When a model memorizes training data and performs poorly on new data.

------------------------------------------------------------------------

# 2️⃣ Fundamentals of NLP

NLP enables machines to process human language.

## Traditional NLP Pipeline

1.  Tokenization\
2.  Stopword removal\
3.  Stemming/Lemmatization\
4.  Feature extraction (TF-IDF)\
5.  ML model

------------------------------------------------------------------------

## Tokenization

"I love AI" → \["I", "love", "AI"\]

Modern systems use subword tokenization like BPE or WordPiece.

------------------------------------------------------------------------

## Text Representation

### Bag of Words

Counts word frequency.

### TF-IDF

Weights important words more heavily.

### Word Embeddings

Dense vectors capturing semantic meaning.

Example: king - man + woman ≈ queen

------------------------------------------------------------------------

# 3️⃣ Transformers

Transformers introduced attention mechanisms allowing models to consider
all words in parallel and understand context relationships.

Key idea: **Attention**

------------------------------------------------------------------------

# 4️⃣ Large Language Models (LLMs)

LLMs are:

-   Deep neural networks\
-   Based on Transformers\
-   Trained on massive datasets\
-   Optimized for next-token prediction

Example:

Input: "The capital of France is"

Output: Paris

------------------------------------------------------------------------

## Pretraining vs Fine-Tuning

Pretraining: - Large dataset\
- Self-supervised

Fine-Tuning: - Task-specific\
- Smaller dataset

------------------------------------------------------------------------

# 5️⃣ Limitations of LLMs

1.  Hallucinations\
2.  Knowledge cutoff\
3.  Cannot access private/live data without integration\
4.  Expensive to retrain

------------------------------------------------------------------------

# 6️⃣ Retrieval-Augmented Generation (RAG)

RAG = Retrieval + Generation

Instead of relying only on model memory:

1.  Retrieve relevant documents\
2.  Provide them as context\
3.  Generate grounded response

------------------------------------------------------------------------

## RAG Architecture

Step 1: Chunk documents\
Step 2: Create embeddings\
Step 3: Store in vector database\
Step 4: Embed user query\
Step 5: Perform similarity search\
Step 6: Send retrieved context to LLM

------------------------------------------------------------------------

# 7️⃣ RAG vs Fine-Tuning

  Feature                    Fine-Tuning   RAG
  -------------------------- ------------- -------
  Knowledge updates          ❌            ✅
  Requires retraining        ✅            ❌
  Private data integration   Hard          Easy
  Cost                       High          Lower

------------------------------------------------------------------------

# 8️⃣ Conceptual RAG Code Example

``` python
# Embed documents
doc_embeddings = embed(documents)

# Store in vector DB
vector_db.store(doc_embeddings)

# Embed query
query_embedding = embed(user_query)

# Retrieve matches
matches = vector_db.search(query_embedding)

# Generate answer
response = llm.generate(context=matches, question=user_query)
```

------------------------------------------------------------------------

# Big Picture Summary

Traditional NLP: Text → Feature Engineering → ML Model → Output

Modern GenAI: Text → Transformer LLM → Generated Output

Enterprise GenAI: Query → Embedding → Vector Search → Context → LLM →
Answer
