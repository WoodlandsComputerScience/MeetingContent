const Command = require('./command')

module.exports = class HelpCommand extends Command {
    getAliases() {
        return ["help", "h", "heelp", "hlep", ""];
    }

    async exec(msg, args) {
        console.log('hi')
        return true;
    }

    getHelp() {
        return '...';
    }
}
