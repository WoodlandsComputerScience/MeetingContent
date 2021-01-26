const Command = require('./command')
const Roles = require('../utils/roles')
const config = require('../config.json') // the ID of the roles are located in `config.roles.<a,b>`

class JoinCommand extends Command {
    getAliases() {
        return ['join'];
    }

    async exec(msg, args) {
        const group = args[0]
        switch (group) {
            case 'a':
            case 'b':
            case 'A':
            case 'B':
                const member = msg.member
                const roleID = config.roles[group.toLowerCase()]
                if (Roles.has(member, roleID))
                    msg.reply(`You **already** *are* in __**Group ${group.toUpperCase()}**__`), msg.react('👎'); // <-- seems super illegal but totally works
                else { // yes you could mix these
                    const res = Roles.add(member, roleID) // status of weather adding the role was successful
                    if (res) {
                        msg.react('👍')
                        msg.reply(`You have been *given* the **Group ${group.toUpperCase()}** role`)
                        console.log(`${msg.member.user.tag} was given the Group ${group.toUpperCase()} role`)
                    } else { return false; }
                }
                break
            default:
                msg.reply('Invalid Group')
                return false;
        }
        return true;
    }

    getHelp() {
        return 'Join the notifications for a certain group';
    }
}

module.exports = JoinCommand