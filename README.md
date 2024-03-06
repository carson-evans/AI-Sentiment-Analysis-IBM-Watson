
# Emotion Detector API

## Introduction
The Emotion Detector API is a Python-Flask application that uses natural language processing to analyze text and identify the dominant emotion from the given input. It's part of an educational project for an IBM certification in developing AI applications. This app only works through IBM's cloud IDE.

## Getting Started
This section provides instructions to get the project running on your local machine for development and testing purposes.

### Prerequisites
You need Python 3.6+ and Flask installed on your system.

### Installation
Clone the repository and install the required dependencies within a virtual environment:

```bash
git clone https://github.com/carson-evans/Emotion-Detector-API.git
cd Emotion-Detector-API
python -m venv venv
source venv/bin/activate  # Use `venv\ScriptsActivate` on Windows
pip install -r requirements.txt
```

### Usage
Launch the server with:

```bash
python server.py
```

Send a POST request to `http://localhost:5000/emotionDetector` with a JSON body like:

```json
{
    "textToAnalyze": "I feel fantastic!"
}
```

The API will return a JSON response with the detected emotions.

### Running Tests
To run the automated tests:

```bash
python test_emotion_detection.py
```

Additionally, you can lint the server file to ensure code quality:

```bash
pylint server.py
```

## Built With
* Flask - The web framework used.

## Author
* **Carson Evans** - [Profile](https://www.github.com/carson-evans)

## License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgments
* IBM for the educational opportunity provided.
* Coursera for hosting the IBM certification program.
* All open-source contributors whose tools made this project possible.
