import ollama
from typing import List


def list_language_models() -> List[str]:
    """
       Function to retrieve a list of available language models.
       Returns:
           List[str]: List of model names
    """

    language_models = ollama.list()
    # Extracting model names
    return [model["model"] for model in language_models.get("models", [])]


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


def main() -> None:
    """
    Main function to execute the chatbot interaction.
    """

    selected_model = select_language_model()

    messages = []

    while True:
        message = input("\nUser: ")
        if message.lower() == "/quit":
            print("Exiting ChatBot...")
            exit()
        elif message.lower() == "/list":
            selected_model = select_language_model()
        else:
            messages.append({"role": "user", "content": message})

            # # No streaming responses
            # print(f"ChatBot [{selected_model}]: ")
            # chat = ollama.chat(model=selected_model, messages=messages)
            # reply = chat.get("message", {}).get("content", "")
            # print(f" {reply}")
            # messages.append({"role": "assistant", "content": reply})

            # Enable streaming responses
            stream = ollama.chat(model=selected_model, messages=messages, stream=True)

            reply = ""
            print(f"ChatBot [{selected_model}]: ")

            for response in stream:
                reply += response["message"]["content"]
                print(response["message"]["content"], end="", flush=True)
            messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
