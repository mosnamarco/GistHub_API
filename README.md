# GistHub API - Summarization Backend

Welcome to the **GistHub API**! This is the backend part of the GistHub webapp that powers the summarization feature using Facebook's BART model from Hugging Face. 🎉

## Requirements

- **Python version**: 3.13.0 (for the closest match to the development environment, use this version).
- **Virtual Environment (venv)**: Highly recommended to keep your dependencies isolated and your life less chaotic.
  
### 1. **Set Up Your Python Environment**

To ensure you're using the correct Python version and dependencies, we recommend setting up a **virtual environment**. This will help you avoid version conflicts with other Python projects.

#### Install Python 3.13.0
If you don't already have Python 3.13.0 installed, you can download it from the official [Python website](https://www.python.org/downloads/release/python-1310/).

#### Create a Virtual Environment

Run the following commands to create and activate your virtual environment.

```bash
# Navigate to the project directory
cd GistHub_API

# Create a virtual environment
python3.13 -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

Once you're in your virtual environment, you'll see `(venv)` at the beginning of your command line, indicating you're in the right environment.

### 2. **Install Dependencies**

With your virtual environment activated, install the required Python dependencies by running:

```bash
# Install dependencies
pip install -r requirements.txt
```

This will install all the necessary packages for running the API, including Flask and Hugging Face's `transformers` library.

### 3. **Run the API**

Once everything is set up, you can run the Flask backend API. 

```bash
# Run the Flask API
python app.py
```

By default, the API will run on `http://localhost:5000`. You can test it using a tool like **Postman** or **curl**, or by making requests from the frontend of the app.

### 4. **Testing the API**

To test the summarization feature, you can send a POST request to the `/api/summarize` endpoint with the following JSON payload:

```json
{
  "payload": "Your text to be summarized goes here."
}
```

You'll get a summary response with the text you provided.

### 5. **Deactivating the Virtual Environment**

Once you're done, don't forget to deactivate your virtual environment:

```bash
# Deactivate the virtual environment
deactivate
```

This will return you to the global environment.

## Notes:

- **Python Version**: For best results, use Python 3.13.0, the version used in development.
- **Virtual Environment**: It's strongly recommended to use a virtual environment to avoid conflicts with other projects. If you're new to virtual environments, check out the [official Python documentation](https://docs.python.org/3/tutorial/venv.html).
  
## Contributing

Feel free to contribute to the API by forking the repo, making changes, and submitting pull requests. If you find any bugs or want to suggest improvements, open an issue and we'll take a look!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
