// NOTE: there are times when you don't need to add 
const config = require('./config.json')
const prefix = config.prefix
const version = require('./package.json').version

// keep in mind that you don't need to put the .js file ending to import
const commands = require('./commands')

const TOKEN = config.token;

const Discord = require('discord.js');
const api = new Discord.Client(); // some people call this `client` as well

console.log('Registering methods...\n\n')

// Runs when the bot is authenticated with Discord and only ONCE
api.once('ready', () => {
    console.log('========================================')
    console.log('WCSBot2 is ready!!!'); // notice that this actually appears after the command BELOW!
    console.log(`Connected as ${api.user.tag}`)
    console.log(`The current version is "${version}"`)
    console.log(`Prefix is "${prefix}"`)
    console.log('========================================')

    api.user.setActivity(`${config.prefix}help | v${version}`,
        { type: 'WATCHING' });
});

// Runs this when ever the bot sees a new message
api.on('message', async (msg) => {
    if (msg.author.bot) return; // filter bots
    /** 
     * ! I just wanted to point out that there is a
     * ! difference between SUBSTRING and SUBSTR; and
     * ! === and ==
     */
    if (msg.content.substring(0,prefix.length) === prefix) { // if matches command prefix
        commands.parse(msg)
    }
});

// Some other possible events
api.on('guildMemberAdd', (member) => {
    console.log(`${member.user.tag} has joined the server`)
})
api.on('guildMemberRemove', (member) => {
    console.log(`${member.user.tag} has left the server`);
});
api.on('disconnect', () => {
    console.log("WCSBot2 is disconnecting...")
});


console.log('WCSBot2 is authenticating with Discord...\n')

api.login(TOKEN);
