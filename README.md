# Assistant-GPT: Your Virtual IoT Assistant

## Description

Assistant GPT, is a virtual assistant designed to interconnect various systems using IoT (Internet of Things), taking its own decisions powered by OpenAI's API. This project aims to automate tasks and manage IoT systems effectively, acting as a central hub for communication.

## Table of Contents

- [Technical Details](#technical-details)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technical Details

Unlike most systems, Assistant GPT does not interact directly with the final user, but communicates via the system instead. A list of initial commands that the bot can execute are provided to it, which are used whenever necessary.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required Python packages using pip:
    ```shell
    pip install -r requirements.txt
    ```
### Optional

4. For wakeword with pvporcupine create a account for free at https://picovoice.ai/ and get an api key
5. for text to speech with eleven labs create a account at https://beta.elevenlabs.io/

## Configuration

1. Please add your OpenAI API key and the tester's name in `config.json`:
    ```json
    {
    "openai_key":"sk-<your key here>",
    "model":"gpt-3.5-turbo",
    "name":"<your name here>",
    "max_allowed_tries": 3,
    "eleven_labs_api_key":"<your key here>",
    "eleven_labs_model":"<your model here>",
    "porcupine_api_key":"<your key here>"
    }
    ```
2. Adapt the `help.txt` file by adding the commands believed relevant for your application.
3. Modify the `assistant.txt` file to provide context to the Assistant GPT about its capabilities within the host machine.

## Usage

After configuring the application as described above, you can call the application with a prompt as follows:
    ```shell
    python app.py [prompt]
    ```

## Contributing

Contributions are welcome! Please message me at davida.sanchez@ciens.ucv.ve if you has any question.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](./LICENSE) file for details.
