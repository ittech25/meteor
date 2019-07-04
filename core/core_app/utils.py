from .database import *

def registerBot(uuid, interval, delta, hostname):
    print("registering bot")
    try:
        q = session.query(Host).filter(Host.hostname == hostname).one()
        hostid = q.id
    except:
        return [False, "Unknown hostname"]
    b = Bot(uuid, interval, delta, hostid)
    return [True, "None"]


def registerHost(hostname, interface, groupname):
    print("registering host")
    try:
        q = session.query(Group).filter(Group.name == groupname).one()
        groupid = q.id
    except:
        return [False, "Unknown group"]
    h = Host(hostname, interface, groupid)
    return [True, "None"]


def registerGroup(groupname):
    print("registering group")
    g = Group(groupname)
    return [True, "None"]


def hostlookup(hostname):
    try:
        q = session.query(Host).filter(Host.hostname == hostname).one()
        hostid = q.id
        return hostid
    except:
        return "ERROR"


def grouplookup(groupname):
    try:
        q = session.query(Group).filter(Group.name == groupname).one()
        gid = q.id
        return gid
    except:
        return "ERROR"


def singlecommandadd(mode, arguments, options, hostid):
    a = Action(mode, arguments, options, False, False, hostid)

def groupcommandadd(mode, arguments, options, groupid):
    q = session.query(Host).filter(Host.groupid == groupid)
    for result in q:
        hid = result.id
        singlecommandadd(mode, arguments, options, hid)
    return [True, "None"]


def addGroupAction(groupname, mode, arguments, options):
    gid = grouplookup(groupname)
    if gid == "Error":
        return [False, "Unknown host"]
    groupcommandadd(mode, arguments, options, gid)

def listHostsUtil():
    data = ""
    for instance in session.query(Host).order_by(Host.id):
        data += str(instance) + "\n"
    return data

def listBotsUtil():
    data = ""
    for instance in session.query(Bot).order_by(Bot.id):
        data += str(instance) + "\n"
    return data

def listGroupsUtil():
    data = ""
    for instance in session.query(Group).order_by(Group.id):
        data += str(instance) + "\n"
    return data

def listActionsUtil():
    data = ""
    for instance in session.query(Action).order_by(Action.id):
        data += str(instance) + "\n"
    return data

def dumpDatabase():
    data = "HOSTS:\n"
    for instance in session.query(Host).order_by(Host.id):
        data += str(instance) + "\n"
    data += "\nBOTS:\n"
    for instance in session.query(Bot).order_by(Bot.id):
        data += str(instance) + "\n"
    data += "\nGROUPS:\n"
    for instance in session.query(Group).order_by(Group.id):
        data += str(instance) + "\n"
    data += "\nACTIONS:\n"
    for instance in session.query(Action).order_by(Action.id):
        data += str(instance) + "\n"
    data += "\nRESPONSES:\n"
    for instance in session.query(Response).order_by(Response.id):
        data += str(instance) + "\n"
    return data