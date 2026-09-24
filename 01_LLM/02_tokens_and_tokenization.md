# Tokens and Tokenization

## 1. What Is a Token?

An LLM does not directly process text exactly as humans read it.

Before text is given to the model, it is broken into smaller pieces called **tokens**.

For example:

```text
"I love programming"
        ↓
   Tokenizer
        ↓
[Token 1, Token 2, Token 3, ...]
```

A token is **not always equal to one word**.

A token can represent:

* A complete word
* Part of a word
* Punctuation
* Spaces or characters
* Special tokens

So:

> **Token ≠ necessarily a word**

---

## 2. What Is Tokenization?

**Tokenization** is the process of breaking text into tokens.

```text
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs
 ↓
LLM
```

For example:

```text
"Artificial intelligence is powerful"
```

is passed through a tokenizer, which breaks the text into smaller pieces that the model can process.

---

## 3. Tokens Are Not Always Words

A common misconception is:

```text
1 word = 1 token
```

This is **not always true**.

A tokenizer can split a single word into multiple tokens.

For example, conceptually:

```text
"unbelievable"
       ↓
"un" + "believ" + "able"
```

The exact splitting depends on the tokenizer used by the model.

Different models can tokenize the same sentence differently.

---

## 4. Token IDs

After text is divided into tokens, each token is represented by a numerical **token ID**.

Conceptually:

```text
"Hello world"
      ↓
  Tokenization
      ↓
["Hello", " world"]
      ↓
[Token ID, Token ID]
```

The model works with these numerical representations.

So the simplified flow is:

```text
Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Model
```

---

## 5. Seeing Tokens in Python

We can use a tokenizer library such as `tiktoken` to see how text is divided into tokens.

Install it with:

```bash
pip install tiktoken
```

### Example

```python
import tiktoken

# Create a tokenizer
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

text = "Hello, I am learning LangChain."

# Convert text into token IDs
token_ids = encoding.encode(text)

print("Token IDs:")
print(token_ids)

print("\nNumber of tokens:")
print(len(token_ids))

# Show each token
print("\nIndividual tokens:")

for token_id in token_ids:
    token = encoding.decode([token_id])
    print(token_id, "->", repr(token))
```

The output will show something conceptually like:

```text
token_id -> 'Hello'
token_id -> ','
token_id -> ' I'
token_id -> ' am'
token_id -> ' learning'
...
```

This makes it clear that tokens are not necessarily complete words.

---

## 6. Converting Tokens Back to Text

Token IDs can also be converted back into text.

```python
decoded_text = encoding.decode(token_ids)

print(decoded_text)
```

Output:

```text
Hello, I am learning LangChain.
```

So we can think of the process as:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
LLM
```

And token IDs can also be decoded back:

```text
Token IDs
 ↓
Decoding
 ↓
Text
```

---

## 7. Why Tokens Matter

Tokens are important because LLMs process text in terms of tokens rather than normal human-readable words.

The number of tokens in an input affects:

* How much text can be processed
* The model's context limit
* Input/output usage

For example, a long document contains many tokens, while a short sentence contains fewer tokens.

---

## Key Takeaways

* **Token** = a small piece of text processed by an LLM.
* **Tokenization** = the process of breaking text into tokens.
* A token is **not necessarily a complete word**.
* Tokens are represented using **token IDs**.
* LLMs process these token representations.
* Different models/tokenizers can divide the same text differently.

### Simple Flow

```text
"I am learning AI"
        ↓
    Tokenizer
        ↓
      Tokens
        ↓
    Token IDs
        ↓
       LLM
```
