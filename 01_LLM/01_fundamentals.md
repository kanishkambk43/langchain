# LLM Fundamentals

## What is an LLM?

LLM stands for **Large Language Model**.

An LLM is a type of NLP model that is trained on a very large amount of data and can perform different language-related tasks.

For example, an LLM can be used to:

- Generate text
- Categorize text
- Evaluate text
- Answer questions
- Summarize information

The material explains that LLMs are built on top of **Transformer models**.

---

## LLM as an NLP Model

LLMs can perform tasks that traditionally required separate NLP or machine learning models.

For example, consider customer reviews.

```text
Customer Review
       ↓
      LLM
       ↓
Positive / Negative
```

Instead of building a separate NLP model specifically for categorizing the reviews, an LLM can be given the review and instructed to categorize it.

---

## LLMs Need Instructions

An LLM can perform a task, but we need to clearly tell it what we want.

For example, if we want to classify a review:

```text
Review
  ↓
LLM
  ↓
"Positive" or "Negative"
```

We need to instruct the LLM to return only the required output.

The material emphasizes that the LLM needs to be **guided** through the prompt.

For example:

```text
You are a review evaluator.

Classify the following review as:
- Positive
- Negative

Return only the classification.
```

---

## LLM and Structured Output

An LLM normally generates text.

When an application requires a specific format, we need to guide the model to produce that format.

The material connects this idea with **structured output** and Pydantic.

For example:

```text
LLM
 ↓
Structured Output
 ↓
Expected format
```

This makes the LLM's output easier for an application to work with.

---

## LLM vs AI Agent

An important distinction is made between an LLM and an AI agent.

An LLM by itself can generate text:

```text
User
 ↓
LLM
 ↓
Response
```

When developers add capabilities such as **tools** to an LLM, it can perform specific tasks using those tools.

```text
              ┌── Tool 1
              │
LLM ──────────┼── Tool 2
              │
              └── Tool 3
                   ↓
                 Task
```

The material describes this combination of an LLM with tools as an **AI agent**.

---

## LLM and External Data

An LLM's knowledge does not automatically contain information from every external data source.

For example, if we ask for current information, the LLM may need access to an external tool or data source.

This is where tools and RAG can be used.

### With a Tool

```text
User
 ↓
LLM
 ↓
Tool
 ↓
External Information
 ↓
LLM
 ↓
Response
```

### With RAG

The material gives a high-level view of RAG where external data is stored as vectors and a user's question is also converted into a vector.

```text
External Data
     ↓
  Vectors
     ↓
Vector Store

User Question
     ↓
Query Vector
     ↓
Relevant Vector
     ↓
Relevant Information
     ↓
LLM
     ↓
Answer
```

---

## LLMs and Transformers

The material explains that LLMs are NLP models built on top of the **Transformer architecture**.

Transformers provide the underlying architecture that allows modern LLMs to process and generate language.

```text
Transformer Architecture
          ↓
         LLM
          ↓
Language-related Tasks
```

---

## Simple Understanding

The basic idea can be summarized as:

```text
                LLM
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    Generate   Evaluate  Categorize
      Text       Text       Text
       │
       ↓
   With proper
   instructions
       │
       ↓
 Structured Output
```

And when additional capabilities are connected:

```text
LLM
 │
 ├── Tools → AI Agent
 │
 └── External Data → RAG
```

### Key Point

**An LLM is a Transformer-based NLP model trained on a large amount of data that can perform various language-related tasks. It can be guided through prompts and extended with tools or external data to build more capable applications.**