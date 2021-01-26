const config = require('./config.json')

const commandMap = {}
const helpMap = {}

function parseCommand(msg) {
    // Split commands into sections
    const args = msg.content.slice(config.prefix.length).split(/ +/);
    // The first "arg" is the command
    const cmd = args.shift().toLowerCase();

    // Lookup to
    const search = commandMap[cmd]

    if (search) {
        search.exec(msg, args)
    } else {
        // Do this if none of the above commands are correct...
        msg.reply('Command not found...')
        msg.react('❌')
    }
    console.log(`${msg.author.tag} executed ${msg.content}`);
};

function init() {
    registerCommand('help')
    console.log(commandMap)
    console.log(helpMap)
}

// hashes a map to do a look up whenever a command is ran
// basically, hash the command once and save time every time someone runs a command
function registerCommand(command) {
    const c = require(`./commands/${command}`)
    const o = new c()
    o.getAliases().forEach(alias => {
        alias = alias.toLowerCase()
        commandMap[alias] = o
        helpMap[alias] = o.getHelp()
    });
}

// ES5 exports (since this isn't ES6)
module.exports = {
    helpMap: helpMap,
    init: init,
    parse: parseCommand,
}
