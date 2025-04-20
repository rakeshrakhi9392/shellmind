import os

def set_environment_variable():
    # Take user input for OpenAI API key
    openai_api_key = input("Enter your OpenAI API key: ")

    # Set the value for the OPENAI_API_KEY environment variable
    os.environ['OPEN_API_KEY'] = openai_api_key

    # Set the value for the SAGE_PATH environment variable
    os.environ['SAGE_PATH'] = os.getcwd()

    # Get the user's shell configuration file based on the default shell
    shell = os.getenv('SHELL')
    if shell.endswith('zsh'):
        shell_config_file = os.path.expanduser("~/.zshrc")
    elif shell.endswith('bash'):
        shell_config_file = os.path.expanduser("~/.bashrc")
    else:
        print(f"Unsupported shell: {shell}")
        return

    # Append the export statements to the shell configuration file
    with open(shell_config_file, 'a') as file:
        file.write(f'\nexport OPEN_API_KEY={openai_api_key}\n')
        file.write(f'export SAGE_PATH={os.getcwd()}\n')
        file.write(f'export PATH=$PATH:{os.path.join(os.getcwd(), "scripts")}\n')

    print(f'Environment variables set in {shell_config_file}')

    # Restart the shell to apply the changes
    print("Restart your shell to apply the changes.")

if __name__ == "__main__":
    set_environment_variable()

