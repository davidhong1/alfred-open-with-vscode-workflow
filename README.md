# Alfred Workflow: Open VSCode Projects

An Alfred workflow that helps you quickly open projects in Visual Studio Code using the "o" command.

![Workflow Demo](img/01.png)

## Features

- Quick project search and open with VSCode
- Configurable search root directories (supports multiple paths, use `:` to separate)
- Adjustable search depth to optimize performance
- Works with [Alfred 5](https://www.alfredapp.com/alfred-5-whats-new/)

## Prerequisites

- [Alfred Powerpack](https://www.alfredapp.com/powerpack/) (Required for workflows)
- [Visual Studio Code](https://code.visualstudio.com/)
- VSCode `code` command [installed in PATH](https://code.visualstudio.com/docs/setup/mac)

## Installation

- Download [code.alfredworkflow](https://github.com/davidhong1/alfred-open-with-vscode-workflow/blob/main/code.alfredworkflow)
- Double-click the downloaded file to install it in Alfred

## Configuration

- Configure search directories
  - Set `DIR_ARRAY` environment variable in Alfred
  - Multiple directories can be separated by colons (:)

- Set search depth
  - Configure `SEARCH_DEPTH` environment variable
  - Helps optimize search performance

- Demo
  ![Directory Configuration](img/02.png)
  ![Search Depth Configuration](img/03.png)

## Usage

- Trigger Alfred (default: ⌘ Space)
- Type `o` followed by a space
- Enter full or partial project name
- Select desired project from results
- Press Enter to open in VSCode

## Links

- [GitHub Repository](https://github.com/davidhong1/alfred-open-with-vscode-workflow)
