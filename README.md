# GitHub Stats Analyser

## Table of Contents

- [GitHub Stats Analyser](#github-stats-analyser)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)
    - [GitHub Action Pre-built Image](#github-action-pre-built-image)
    - [GitHub Action Inputs](#github-action-inputs)
  - [License](#license)

## Introduction

This project is a tool to analyse the statistics of a user's GitHub repositories.

It is designed to be used as a GitHub Action.

The tool is written in Python and uses the GitHub API to some of the statistics. As well it clones the repositories to be analysed and analyses the files in the repositories.

## Usage

### GitHub Action Example

The GitHub Action is designed to be used in a workflow.

```yaml
- name: Analyse GitHub repositories
  uses: jackplowman/github-stats-analyser@latest
  with:
    REPOSITORY_OWNER: jackplowman # Put your GitHub username here or use ${{ github.REPOSITORY_OWNER }}
```

> [!TIP]
> It's recommended to use the pre-built Docker image as it will be faster to install.

### GitHub Action Pre-built Image

You can use the pre-built Docker image by adding the following to your workflow:

```yaml
- name: GitHub Stats Analyser
      uses: docker://ghcr.io/jackplowman/github-stats-analyser:v1.1.0
      with:
        GITHUB_TOKEN: ${{ inputs.token }}
```

### GitHub Action Inputs

| Name               | Required | Description                                         | Type   | Default               |
| ------------------ | -------- | --------------------------------------------------- | ------ | --------------------- |
| `REPOSITORY_OWNER` | yes      | The GitHub username of the repositories to analyse. | string | N/A                   |
| `GITHUB_TOKEN`     | no       | A GitHub token to authenticate API requests.        | string | `${{ github.token }}` |

## License

[MIT](https://github.com/jackplowman/github-stats-analyser/blob/master/LICENSE)
