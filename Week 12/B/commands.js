const config = require('./config.json')

function parseCommand(msg) {
    // Split commands into sections
    const args = msg.content.slice(config.prefix.length).split(/ +/);
    // The first "arg" is the command
    const cmd = args.shift().toLowerCase();

    // Check which command it is
    switch (cmd) {
        case 'help':
            break;
        case 'rules':
            break;
        case 'suggest':
            break;
        case 'join':
            break;
        default: // Do this if none of the above commands are correct...
            msg.reply('Command not found...')
            msg.react('❌')
    }
    console.log(`${msg.author.tag} executed ${msg.content}`);
};

// ES5 exports (since this isn't ES6)
module.exports = {
    parse: parseCommand,
}