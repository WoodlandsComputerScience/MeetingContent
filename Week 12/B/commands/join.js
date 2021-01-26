const Command = require('./command')

class JoinCommand extends Command{
    getAliases() {
        return ['join'];
    }

    async exec(msg, args) {
        return false; // return command status
    }

    getHelp() {
        return 'Suggest a topic to cover on!';
    }
}

module.exports = JoinCommand