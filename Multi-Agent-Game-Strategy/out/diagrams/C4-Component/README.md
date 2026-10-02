# Multi-Agent Game Strategy

## Project Overview

This project presents the architecture of a Multi-Agent Game Strategy system using the C4 Model.

The system uses multiple AI agents to analyze the current game state, coordinate decisions, develop strategies, and select appropriate game actions.

## C4 Architecture

The architecture is represented using four C4 levels:

### Level 1 – System Context

Shows the Player interacting with the Multi-Agent Game Strategy System.

### Level 2 – Container

Shows the main containers of the system:

- Game Input Module
- Coordinator Agent
- Strategy Agent
- Action Agents
- Game Engine

### Level 3 – Component

Shows the internal components of the Coordinator Agent:

- Game State Manager
- Strategy Decision Manager
- Agent Communication Manager
- Action Selection Manager

### Level 4 – Code

The code-level overview identifies the main classes and functions used by the system.

## Diagrams

The PlantUML source files are stored in the `diagrams` folder.

Generated PNG diagrams are stored in the `out/diagrams` folder.

## Tools Used

- PlantUML
- Graphviz
- Visual Studio Code
- C4 Model

## Conclusion

The C4 Model provides a clear way to visualize the Multi-Agent Game Strategy system from a high-level system context down to the code-level elements.