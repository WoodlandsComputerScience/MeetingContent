module.exports = {
    has: (member, id) => { // you could also use `.has(id)`
        if (!member || !id)
            return false
        else
            return member.roles.cache.some((role) => role.id === id);
    },
    add: (member, id) => {
        if (!member.user.bot && member && id) { // not a bot
            const role = getRole(member, id)
            if (role) {
                member.roles.add(role);
                return true;
            } else {
                console.log(`Role ${id} was not found in ADD`)
            }
        }
        return false;
    },
    remove: (member, id) => {
        if (!member.user.bot && member && id && member.roles.cache.has(id)) {
            const role = getRole(member, id)
            if (role) {
                member.roles.remove(role);
                return true;
            } else {
                console.log(`Role ${id} was not found in REMOVE`)
            }
        }
        return false;
    }
}

getRole = (member, id) => {
    return member.guild.roles.cache.get(id)
}