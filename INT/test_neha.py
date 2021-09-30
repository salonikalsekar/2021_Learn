def check(s):
    ssplit = s.split(":")

    def checkIdentifier(id):
        if id[0] == '0' or len(id) > 15:
            return False
        for ch in id[1:len(id)]:
            if not ch.isdigit():
                return False

        return True

    def checkIdentifierWeChat(id):
        if len(id) > 251 or len(id) < 1:
            return False
        for ch in id:
            if not (ch.isalnum() or ch != '+' or ch != '-' or ch != '_' or ch != '@' or ch != '.'):
                return False

        return True

    if len(ssplit) == 1:
        if checkIdentifier(ssplit[0]):
            return "SMS";
        else:
            return "INVALID_ADDRESS";
    elif len(ssplit) == 2:
        if ssplit[0] == "whatsapp":
            if checkIdentifier(ssplit[1]):
                return "WHATSAPP"
            else:
                return "INVALID_ADDRESS"
        elif ssplit[0] == "messenger":
            if checkIdentifier(ssplit[1]):
                return "MESSENGER"
            else:
                return "INVALID_ADDRESS"
        elif ssplit[0] == "wechat":
            if checkIdentifierWeChat(ssplit[1]):
                return "WECHAT"
            else:
                return "INVALID_ADDRESS"

    else:
        return "INVALID_ADDRESS";



print(check("whatsapp:155555555555"))
print(check("wechat:identifier:ghke83772"))
print(check("messenger:this_is_not_E164_number"))
print(check("wechat:ghke83772"))
print(check("messenger:+14155552671"))