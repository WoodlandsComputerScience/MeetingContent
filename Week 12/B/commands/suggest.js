const Command = require('./command')

class SuggestCommand extends Command{
    getAliases() {
        return ['suggest'];
    }

    async exec(msg, args) {
        return false; // return command status
    }

    getHelp() {
        return 'Suggest a topic to cover on!';
    }
}

module.exports = SuggestCommand