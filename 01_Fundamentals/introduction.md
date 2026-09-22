# LangChain Introduction

## What is LangChain?

LangChain is a framework for building applications powered by Large Language Models (LLMs).

It provides reusable components and tools that make it easier to build applications that interact with LLMs.

Instead of writing everything from scratch, LangChain provides building blocks that can be connected together to create more complex LLM applications.

## Why LangChain?

An LLM by itself mainly works with the information provided to it through prompts.

When building real applications, we often need additional functionality such as:

- Connecting an LLM with different components
- Creating reusable prompts
- Connecting multiple operations together
- Using tools
- Building agents
- Working with external data

LangChain provides components that help organize and connect these parts.

## LangChain Under the Hood

At its core, LangChain provides reusable Python components for building LLM-powered and agentic applications.

These components can be combined to create workflows where different steps work together.

For example:


Input
  ↓
Prompt
  ↓
LLM
  ↓
Output


More complex applications can connect additional components:


Input
  ↓
Prompt
  ↓
LLM
  ↓
Tool
  ↓
LLM
  ↓
Final Output


The main idea is that LangChain provides the building blocks needed to construct these workflows.

## LangChain and Agents

LangChain can also be used to build AI agents.

An agent can interact with tools and decide which actions to take while solving a task.

This allows applications to go beyond simply sending a prompt to an LLM.

## In Simple Words

**LangChain = a framework that provides building blocks for creating applications around LLMs.**

It helps connect things like:


LLM
 ↓
Prompts
 ↓
Chains
 ↓
Tools
 ↓
Agents
 ↓
External Data
