# RAG Fundamentals

**RAG** stands for **Retrieval-Augmented Generation**.

RAG allows an LLM to use external data that was not directly available to the model.

---

## 1. The Problem With a Plain LLM

A normal LLM does not automatically have access to our private or external data.

For example:

```text
User Question
      |
      v
     LLM
      |
      v
   Answer
```

If the information exists in our own data but the LLM does not have access to that data, it cannot directly use it.

---

## 2. What Is RAG?

RAG connects an LLM with external data.

The high-level idea is:

```text
             Our Data
                |
                v
         Vector Storage
                |
                |
User --> Query --> Query Vector
                      |
                      v
               Similarity Search
                      |
                      v
                Relevant Data
                      |
                      v
                     LLM
                      |
                      v
                   Answer
```

RAG is a multi-step process that retrieves relevant information and provides it to the LLM as context.

---

## 3. Data Is Stored as Vectors

In RAG, data is stored in the form of vectors.

For example:

```text
Vector 1
Vector 2
Vector 3
```

The number of vectors depends on how the data is divided and the context size being used.

---

## 4. User Question → Query Vector

When a user asks a question, the question is also converted into a vector.

This is called a **query vector**.

For example:

```text
User Question
      |
      v
Query Vector
```

The query vector is then compared with the vectors stored in the vector storage.

---

## 5. Similarity Search

The query vector is compared with the stored vectors to find the relevant vector/data.

Conceptually:

```text
Query Vector
     |
     v
+------------+
|  Vector 1  |
|  Vector 2  |  ← Relevant
|  Vector 3  |
+------------+
```

Similarity can be calculated using methods such as:

- Cosine similarity
- Euclidean distance

At this stage, we do not need to know the mathematical formulas behind these methods.

LangChain provides functionality for similarity search, while vector databases have their own ways of comparing and retrieving data.

---

## 6. Retrieval

The first part of RAG is **Retrieval**.

The system retrieves information that is relevant to the user's question.

```text
User Question
      |
      v
Query Vector
      |
      v
Similarity Search
      |
      v
Relevant Vector/Data
```

This is the **Retrieval** part of RAG.

---

## 7. Augmentation

The retrieved text was not previously available to the LLM.

We provide this retrieved information to the LLM as additional context.

This is called **Augmentation**.

```text
Retrieved Data
      +
LLM
      |
      v
Additional Context
```

In simple terms, we are augmenting the model with information that it did not previously have access to.

---

## 8. Generation

After retrieving the relevant information and providing it to the LLM as context, the LLM generates the final answer.

```text
User Question
      |
      v
Query Vector
      |
      v
Similarity Search
      |
      v
Relevant Information
      |
      v
LLM + Context
      |
      v
Final Answer
```

This is the **Generation** part.

---

## 9. Why Is It Called RAG?

The name describes the three main steps:

### R — Retrieval

Retrieve relevant information.

### A — Augmented

Provide the retrieved information to the LLM as additional context.

### G — Generation

Generate the final answer using that context.

Therefore:

```text
Retrieval
    +
Augmentation
    +
Generation
    =
RAG
```

---

## 10. Complete High-Level RAG Flow

The complete process can be understood as:

```text
1. Store data as vectors
          |
          v
2. User asks a question
          |
          v
3. Convert question into a query vector
          |
          v
4. Perform similarity search
          |
          v
5. Retrieve relevant data
          |
          v
6. Provide retrieved data to the LLM as context
          |
          v
7. LLM generates the answer
```

Or, in one diagram:

```text
                 External Data
                      |
                      v
                Vector Storage
                      |
                      |
User Question --> Query Vector
                      |
                      v
               Similarity Search
                      |
                      v
                Relevant Data
                      |
                      v
                 LLM + Context
                      |
                      v
                 Final Answer
```

---

## Key Idea

A plain LLM works with the information available to it.

RAG allows the LLM to retrieve relevant external information and use that information as context when generating an answer.

```text
External Data
      |
      v
Similarity Search
      |
      v
Relevant Data
      |
      v
     LLM
      |
      v
   Answer
```

**RAG = Retrieve relevant information → Augment the LLM with that information → Generate an answer.**