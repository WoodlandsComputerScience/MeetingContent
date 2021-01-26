class Command {
    getAliases() {
        return [];
    }

    async exec(msg, args) {
        return false; // return command status
    }

    getHelp() {
        return '...';
    }
}

module.exports = Command