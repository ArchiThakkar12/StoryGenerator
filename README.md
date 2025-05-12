# **AI Story Generator**

## **Overview**

AI Story Generator is a web application that uses a pre-trained **GPT-2** model to generate creative stories based on user-provided prompts. The system takes a prompt as input and uses **Generative AI** to predict and generate a continuation of the story, mimicking human-like writing patterns.

This project is built using **Streamlit** for the front-end interface and **HuggingFace Transformers** for loading the GPT-2 model.

---

## **Features**

- Simple web interface to input prompts.
- Uses a pre-trained GPT-2 model for story generation.
- Customizable story length based on user input.
- Instant story generation with minimal delay.

---

## **Technologies Used**

- Python
- Streamlit (for web interface)
- HuggingFace Transformers (for the GPT-2 model)
- PyTorch (for running the GPT-2 model)
- Git (for version control)

---

## **Setup and Installation**

### **1. Clone the Repository**

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/ArchiThakkar12/StoryGenerator.git
```
### 2. Install Python
Ensure that you have Python 3.6+ installed on your machine. You can download the latest version of Python from the official [Python website](https://www.python.org/).

### 3. Create a Virtual Environment (Optional but Recommended)
It's highly recommended to create a virtual environment to avoid conflicts with other projects.

## 1. Navigate to your project folder:
   ```bash
   cd AI-Story-Generator
   ```
   ### Create a Virtual Environment

## 2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   ### Activate the Virtual Environment

  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    
### 4. Install Dependencies
Install all the required packages and libraries using pip:

```bash
pip install -r requirements.txt
```

### 5. Manually Install Dependencies (if `requirements.txt` is missing)
If you don't have a `requirements.txt` file, you can install the required libraries manually:

```bash
pip install transformers streamlit torch
```

- **transformers**: To load and use the pre-trained GPT-2 model.
- **streamlit**: To build the web interface for user interaction.
- **torch**: To support GPT-2 model execution (PyTorch backend).

## Usage

### 1. Running the Streamlit App
To run the web application, simply execute the following command in your terminal:
```bash
streamlit run app.py
```

This will start the Streamlit server and open a web page in your default browser where you can interact with the AI Story Generator.

### 2. Interact with the Application
Once the application is running, you can enter a story prompt into the provided text box. Press the "Generate Story" button, and the application will display a story continuation based on your prompt.

- **Default Prompt**: "Once upon a time,"
- You can change the prompt to whatever you like!

### 3. Customizing Story Generation
You can modify the code in `app.py` to adjust settings such as:

- **Max Length of Story**: Modify the `max_length` argument in the `generate_story` function to change how long the story will be.
- **Temperature Settings**: You can experiment with `top_p`, `top_k`, and `no_repeat_ngram_size` parameters in the `generate_story` function for different creative outputs.

## Directory Structure
```bash
AI-Story-Generator/
├── app.py               # Main Streamlit app to run the web interface
├── requirements.txt     # Required Python packages for the project
├── README.md            # Documentation for setup and usage
└── .gitignore           # Git ignore file
```

## Testing

### 1. Unit Testing
The project doesn’t include formal unit tests, but you can test individual components such as:

- The model loading function
- The story generation function
- Streamlit input/output interface

### 2. Performance Testing
The application has been tested with various input sizes to ensure it performs well and generates output promptly. You may want to add more tests based on your specific needs, such as longer inputs or edge cases.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your improvements. Please ensure your contributions follow the coding style used in the project.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **HuggingFace's Transformers library** for providing the GPT-2 pre-trained model.
- **Streamlit** for providing an easy-to-use framework for creating web applications.
- **PyTorch** for supporting the backend to run the GPT-2 model.
