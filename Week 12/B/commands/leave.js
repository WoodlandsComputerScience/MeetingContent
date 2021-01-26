const Command = require('./command')
const Roles = require('../utils/roles')
const config = require('../config.json')

class LeaveCommand extends Command {
    getAliases() {
        return ['leave'];
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
                if (!Roles.has(member, roleID))
                    msg.reply(`You **already** *left* __**Group ${group.toUpperCase()}**__`), msg.react('👎');
                else {
                    const res = Roles.remove(member, roleID)
                    if (res) {
                        msg.react('👍')
                        msg.reply(`You have been *removed* from **Group ${group.toUpperCase()}** role`)
                        console.log(`${msg.member.user.tag} was removed the Group ${group.toUpperCase()} role`)
                    } else { return false }
                }
                break
            default:
                msg.reply('Invalid Group')
                return false;
        }
        return true;
    }

    getHelp() {
        return 'Leave the notifications for a certain group';
    }
}

module.exports = LeaveCommand 