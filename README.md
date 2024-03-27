# Multi Language Model Interaction

This repository contains Python scripts for interacting with various language models using the Ollama library. The scripts provide functionalities such as listing available language models, querying models with user input, and creating a superset document by combining responses from multiple models. Additionally, there is a Streamlit web application for a user-friendly interface to interact with the language models.

## Contents

1. [Scripts](#scripts)
    - [Script 1: `language_model_chatbot.py`](#script-1)
    - [Script 2: `query_all_models.py`](#script-2)
    - [Script 3: `streamlit_app.py`](#script-3)
2. [Usage](#usage)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [License](#license)

---

## Scripts

### Script 1: `language_model_chatbot.py`

This script allows users to interact with language models via a command-line interface. It provides functionalities to list available models, select a model, and engage in a conversation with the chosen model.

### Script 2: `query_all_models.py`

This script queries all available language models with a given question and writes the answers to a text file. It also provides an option to create a superset document by combining responses from multiple models.

### Script 3: `streamlit_app.py`

This script implements a Streamlit web application for interacting with language models. It offers options to list models, query models with user input, and create a superset document using a user-friendly interface.

---

## Usage

### Command-Line Interface:

Run `python language_model_chatbot.py` in your terminal to interact with language models.

### Querying Models:

Run `python query_all_models.py` to query all available models with a specific question.

### Streamlit Web Application:

Run `streamlit run streamlit_app.py` to start the Streamlit app for a user-friendly interface.

---

## Requirements

- Python 3.x
- [Ollama library](https://github.com/ollama/ollama)
- Streamlit (for the web application)

---

## Setup

1. Clone this repository:

```bash
git clone https://github.com/cobbyrecks/multi-language-model-interaction.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Run the desired script as per your interaction preference.

---

## License

This project is licensed under the MIT License.

Feel free to contribute or provide feedback for improving the functionalities of these scripts.

