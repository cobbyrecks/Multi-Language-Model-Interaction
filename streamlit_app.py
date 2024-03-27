import os
import streamlit as st
import ollama
from typing import List


# Function to retrieve a list of available language models
def list_language_models() -> List[str]:
    language_models = ollama.list()
    # Extracting model names
    return [model["model"] for model in language_models.get("models", [])]


# Function to query all available language models with the given question and write the answers to a text file
def query_all_models(question: str, output_file: str) -> None:
    models = list_language_models()

    output_folder = "responses"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, output_file)

    with open(output_path, "w", encoding="utf-8") as file:
        for model in models:
            file.write(f"Model: {model}\n")
            file.write("=" * 20 + "\n")
            chat = ollama.chat(model=model, messages=[{"role": "system", "content": question}], stream=True)
            responses = (response["message"]["content"] for response in chat)
            file.writelines(responses)
            file.write("\n\n")


# Function to create a superset document by combining responses from multiple language models
def create_superset_document(content: str, selected_model: str, output_file: str) -> None:
    messages = [{"role": "system",
                 "content": "As a seasoned professional in analyzing chatbot responses,"
                            "it's time to leverage your expertise. Analyze responses from various"
                            "language models, amalgamate them if necessary, to deliver an optimal"
                            "and refined solution."},
                {"role": "user", "content": content}]

    chat = ollama.chat(model=selected_model, messages=messages, stream=True)

    output_path = os.path.join("responses", output_file)

    with open(output_path, "w", encoding="utf-8") as file:
        for response in chat:
            file.write(response["message"]["content"])


def main():
    st.title(":blue[_Language Model Interaction_]")
    st.sidebar.header("Options")
    options = st.sidebar.selectbox("Select an option", ["List Models", "Query Models", "Create Superset Document"])

    if options == "List Models":
        st.header("Installed Language Models")
        models = list_language_models()
        for index, model in enumerate(models, start=1):
            st.write(index, model)

    elif options == "Query Models":
        st.header("Query Language Models")
        question = st.text_input("Enter your question")
        output_file = st.text_input("Enter output file name")
        if st.button("Query"):
            query_all_models(question, output_file)
            st.success("Query completed successfully. Check the output file in the 'responses' folder.")

    elif options == "Create Superset Document":
        st.header("Create Superset Document")
        input_file = st.file_uploader("Upload responses file")
        if input_file is not None:
            content = input_file.read().decode("utf-8")
            selected_model = st.selectbox("Select a model", list_language_models())
            output_file = st.text_input("Enter output file name")
            if st.button("Create"):
                create_superset_document(content, selected_model, output_file)
                st.success("Superset document created successfully.")


if __name__ == "__main__":
    main()
