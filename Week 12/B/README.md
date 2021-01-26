# WCSBot2
<!-- Add badges to show the status of the bot -->
## What is this?

This is a bot made to replace `WCSBot` which is currently deprecated. The bot utilizes powerful web technologies such as **Node.js** to write a Discord bot such as `WCSBot2`. Made by [Nathan](https://github.com/Nathan13888) and [Max](https://github.com/jcoptre).

## Running the bot

1. `npm install` - installs all the Node.js dependencies
2. Configure `config.json` using `config.json.example`
3. `npm start` or `npm run dev`

## Deployment

*There are many options for deploying this bot. We are currently deploying this bot on a private Digital Ocean droplet :)*

- Some VPS that runs Node
- Package as a Docker image then put it somewhere that runs Docker (Docker Engine, Kubernetes, etc.)
- Heroku --> configure a `worker` dyno (`Procfile` not included currently)

## Features

- Self-assigned Roles
- Suggest a topic!
- Misc. features (help, rules, etc...)

## TODO

**SUBMIT your suggestions here! Select the `pen` icon then suggest the changes, press `commit` and make a "pull request".**

- move to separate repo and add it back here as a submodule
- **Dockerize** bot!
- route logs to the logging channel as well
- use PM2 instead
- converting to using Typescript instead
- other useful development tools (eg. eslint, coverage, CIs, etc.)
- status badge
