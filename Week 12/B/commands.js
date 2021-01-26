const config = require('./config.json')

const commandMap = new Map()
const helpMap = new Map()

function parseCommand(msg) {
    // Split commands into sections
    const args = msg.content.slice(config.prefix.length).split(/ +/);
    // The first "arg" is the command
    const cmd = args.shift().toLowerCase();

    // Lookup a command from the HashMap --> O(1)
    const qry = commandMap[cmd]

    if (qry) {
        qry.exec(msg, args)
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
    const aliases = o.getAliases()
    aliases.forEach(alias => {
        alias = alias.toLowerCase()
        commandMap[alias] = o
    });
    helpMap[aliases[0]] = o.getHelp()
}

// ES5 exports (since this isn't ES6)
module.exports = {
    helpMap: helpMap,
    init: init,
    parse: parseCommand,
}
