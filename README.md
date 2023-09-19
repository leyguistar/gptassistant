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

## Configuration

1. Please add your OpenAI API key and the tester's name in `config.json`:
    ```json
    {
      "openai_key": "your-openai-api-key",
      "name": "tester-name"
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

Contributions are welcome! Please read the [Contributing Guide](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](./LICENSE) file for details.
