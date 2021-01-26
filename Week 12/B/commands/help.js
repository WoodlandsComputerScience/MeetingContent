const Command = require('./command')
const commands = require('../commands')
const Discord = require('discord.js')
const bot = require('../bot')

module.exports = class HelpCommand extends Command {
    getAliases() {
        return ["help", "h", "heelp", "hlep", ""];
    }

    // TODO: make an `aliases` command
    // TODO: make an `usage` command
    async exec(msg, args) {
        const embed = this.getEmbed() // get the default help embed template
        var x = args // by default, show the help message of all the commands listed in args

        const hm = commands.helpMap
        if (args.length == 0) {
            x = commands.helpCommands
        }

        for (const command of x) { // just can't think of a better name...
            if (!command && !hm.has(command)) continue; // skip the command if it isn't found
            embed.addField(
                `**${command}**`,
                `*${hm[command]}*`,
            )
        }
        msg.reply(embed)
    }

    getEmbed() {
        const embed = new Discord.MessageEmbed()
            .setColor('#069406')
            .setTitle('WCSBot2 Help')
            .setTimestamp()
            .setFooter(
                bot.user.username,
                bot.user.displayAvatarURL,
            )
            .setURL('https://github.com/WoodlandsComputerScience')

        return embed
    }

    qryCommand(command) {
        // Query a command's help message
        const qry = commands.helpMap[args[0]]
        return true;
    }

    getHelp() { // notice the how the ' was "escaped"
        return 'Search up a command\'s help message'
    }
}
