# Use VSCode app open project with "o" command.

![01.png](./img/01.png)

# Work in [Alfred5](https://www.alfredapp.com/alfred-5-whats-new/)

# Features

1. Supports specifying the search root directory through environment variables, with multiple root directories separated by colons.
2. Supports specifying the search depth through environment variables to avoid searching all directories.

# Installation

1. Click and download the [code.alfredworkflow](https://github.com/davidhong1/alfred-open-with-vscode-workflow/blob/main/code.alfredworkflow)
2. Double click the `.alfredworkflow` file to install

Note that the [Alfred Powerpack](https://www.alfredapp.com/powerpack/) is required to use workflows.

# Usage

1. [Install VSCode code command.](https://code.visualstudio.com/docs/setup/mac)

2. Define DIR_ARRAY and SEARCH_DEPTH env.
   ![02.png](./img/02.png)
   ![03.png](./img/03.png)

3. Trigger the Alfred App, type "o " (letter o and a space), followed by the complete or partial substring of the project you want to open. Choose the output directory for the search results and hit Enter to call the "code" command of Visual Studio Code to open the selected directory.

# More

[GitHub](https://github.com/davidhong1/alfred-open-with-vscode-workflow)
