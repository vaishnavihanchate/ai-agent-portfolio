# ADR 001: Selection of Tech Stack for Basic AI Agent

## Status

**Accepted**

## Context

We are building a basic AI Agent as part of the **AI-Augmented Workflow** course.

The purpose of the project is to understand how an AI Agent can receive a user request, process it using a Large Language Model (LLM), and generate an appropriate response.

As this is a beginner-level college project, the technology stack should be easy to learn, suitable for AI development, compatible with AI-assisted coding tools, and easy to test and maintain.

## Decision

We will use the following technology stack:

| Component | Selected Technology | Purpose |
|---|---|---|
| Programming Language | Python | Main programming language |
| AI/LLM API | OpenAI API | Provides access to an LLM |
| Alternative | Ollama | Local/open-source alternative |
| Version Control | Git | Tracks project changes |
| Code Hosting | GitHub | Stores and shares the project |
| Documentation | Markdown | Used for documentation and ADRs |

### Why Python?

Python is beginner-friendly, has simple syntax, and is widely used in Artificial Intelligence and Machine Learning.

### Why OpenAI API?

The OpenAI API provides a straightforward way for a Python application to communicate with an AI model without building a model from scratch.

### Why Ollama as an Alternative?

Ollama can be considered for experimenting with supported open-source models locally.

### Why Git and GitHub?

Git tracks changes to the project, while GitHub provides online storage and makes the project easy to share as an e-Portfolio.

## Consequences

### Advantages

- Python is beginner-friendly.
- Python has strong AI and ML support.
- The OpenAI API makes LLM integration easier.
- Git provides version control.
- GitHub makes the project easy to share.
- The stack works well with AI-assisted coding tools.
- AI tools can help generate, explain, debug, and improve Python code.
- Ollama provides an option for experimenting with local models.

### Disadvantages

- Using the OpenAI API may involve usage costs.
- A cloud-based API requires an internet connection.
- API keys must be kept secure and must not be uploaded to GitHub.
- AI-generated code may contain errors and must be reviewed and tested.
- Local models using Ollama may require more computer resources.

## AI-Assisted Coding Compatibility

The selected technology stack is suitable for AI-assisted software development.

AI coding tools can help with:

1. Generating Python code.
2. Explaining programming concepts.
3. Creating API integration examples.
4. Finding and explaining errors.
5. Suggesting code improvements.
6. Creating documentation.
7. Generating test cases.

However, AI assistance will be used as a development aid and not as a replacement for understanding the code.

All AI-generated code should be reviewed, understood, tested, and modified when necessary before being included in the project.

## Decision Summary

For the basic AI Agent project, we choose **Python with the OpenAI API**, supported by **Git and GitHub** for development and version control.

**Ollama** will be considered as an alternative for experimenting with locally running supported open-source models.
