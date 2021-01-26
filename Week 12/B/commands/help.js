const Command = require('./command')
const commands = require('../commands')
const Discord = require('discord.js')
const bot = require('../bot')

module.exports = class HelpCommand extends Command {
    getAliases() {
        return ['help', 'h', 'heelp', 'hlep', 'hlpe', ''];
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
            const qry = hm[command]
            if (qry == undefined || qry == '') continue; // skip the command if it isn't found
            embed.addField(
                `**${command}**`,
                `*${qry}*`,
            )
        }
        if (embed.fields.length == 0) // you don't need brackets if the statement only needs to affect one line
            embed.addField('\u200b', '*No commands found...*')

        msg.reply(embed)

        return true
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

    getHelp() { // notice the how the ' was "escaped"
        return 'Search up a command\'s help message'
    }
}
