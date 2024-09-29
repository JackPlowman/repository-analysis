# GitHub Stats Analyser

## Table of Contents

- [GitHub Stats Analyser](#github-stats-analyser)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)
    - [GitHub Action Inputs](#github-action-inputs)

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
    repository_owner: jackplowman # Put your GitHub username here or use ${{ github.repository_owner }}
```

### GitHub Action Inputs

| Name               | Required | Description                                         | Type   | Default               |
| ------------------ | -------- | --------------------------------------------------- | ------ | --------------------- |
| `repository_owner` | yes      | The GitHub username of the repositories to analyse. | string | N/A                   |
| `github-token`     | no       | A GitHub token to authenticate API requests.        | string | `${{ github.token }}` |
