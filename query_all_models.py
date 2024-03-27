import os
import ollama

from typing import List
from tqdm import tqdm


def list_language_models() -> List[str]:
    """
    Function to retrieve a list of available language models.
    Returns:
        List[str]: List of model names
    """

    language_models = ollama.list()
    # Extracting model names
    return [model["model"] for model in language_models.get("models", [])]


def query_all_models(question: str, output_file: str) -> None:
    """
    Queries all available language models with the given question
    and writes the answers to a text file.

    Args:
        question (str): The question to query the language models with.
        output_file (str): The name of the text file to write the answers to.
    """

    models = list_language_models()

    output_folder = "responses"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_file)

    with open(output_path, "w", encoding="utf-8") as file:
        for model in tqdm(models, desc="Writing output file", unit="model"):
            file.write(f"Model: {model}\n")
            file.write("=" * 20 + "\n")
            chat = ollama.chat(model=model,
                               messages=[{"role": "system", "content": question}], stream=True)
            responses = (response["message"]["content"] for response in chat)
            file.writelines(responses)
            file.write("\n\n")


def select_language_model() -> str:
    """
      Function to prompt the user to select a language model.
      Returns:
          str: Selected language model name
    """

    print("******* Select language model to use *******")
    models = list_language_models()
    for index, language_model in enumerate(models, start=1):
        print(f"{index} : {language_model}")

    while True:
        language_selected = input("Enter the index of the language module you prefer: ")
        try:
            language_index = int(language_selected) - 1
            if 0 <= language_index < len(models):
                selected_model = models[language_index]
                print(f"You have selected: {selected_model}")
                return selected_model
            else:
                print("Invalid index selected.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")


def create_superset_document(input_file: str, output_file: str, selected_model: str) -> None:
    """
        Combines responses from multiple language models to create an enhanced document.

        Args:
            input_file (str): Path to the file containing responses from different models.
            output_file (str): Path to save the enhanced document.
            selected_model (str): Name of the language model for enhancing the input document.

        Reads responses from the input file and constructs a user query. Uses the selected model
        to generate an enhanced document. Writes the enhanced document to the output file.

        Example:
        '''python
        create_superset_document("responses.txt", "enhanced_responses.txt", "enhancement_model")
        '''
    """

    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Clever prompt engineering
    messages = [{"role": "system",
                 "content": "As a seasoned professional in analyzing chatbot responses,"
                            "it's time to leverage your expertise. Analyze responses from various"
                            "language models, amalgamate them if necessary, to deliver an optimal"
                            "and refined solution."},
                {"role": "user", "content": content}]

    # Use the selected model to generate new document
    chat = ollama.chat(model=selected_model, messages=messages, stream=True)

    # Write the responses from the selected model to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for response in tqdm(chat, desc="Writing output file"):
            file.write(response["message"]["content"])
        print("Done!")


def main() -> None:
    """
    Main function to execute the chatbot interaction.
    """

    print(f"***** You have {len(list_language_models())} model(s) installed *****")
    models = list_language_models()

    for index, language_model in enumerate(models, start=1):
        print(f"{index} : {language_model}")

    question = input("\nEnter the prompt : ")

    while True:
        output_path_1 = input("\nEnter output_file name : ")

        # Check whether file name already exists
        if os.path.exists(os.path.join("responses", output_path_1)):
            print("File name already exists. Please provide a different file name!")
        else:
            query_all_models(question, output_path_1)
            break

    print("\nDo you want to create a superset document?")
    reply = input("Please respond with 'yes' to proceed, or any other input to terminate: ")

    if reply.lower() != "yes":
        exit()
    else:
        selected_model = select_language_model()

        while True:
            output_path_2 = input("\nEnter the name of output file : ")

            #  Check whether file name already exists
            if os.path.exists(os.path.join("responses", output_path_2)):
                print("File name already exists. Please provide a different file name!")
            else:
                output_path = os.path.join("responses", output_path_2)
                break

        input_path = os.path.join("responses", output_path_1)

        create_superset_document(input_file=input_path, output_file=output_path,
                                 selected_model=selected_model)


if __name__ == "__main__":
    main()
