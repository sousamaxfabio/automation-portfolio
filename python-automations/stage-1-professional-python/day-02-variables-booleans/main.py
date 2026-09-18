request_title = "Password reset"
resolved = False

print(request_title, resolved)

if resolved:
    print("This request is closed")
else:
    print("This request is still open")


minutes_open = 90

if minutes_open >= 60:
    print("The request needs attention")
else:
    print("The request is within the response window")


service_request = {
    "title": "Password reset",
    "resolved": False,
    "minutes_open": 90,
}

print(service_request["title"])
print(service_request["resolved"])
print(service_request["minutes_open"])
service_request["resolved"] = True
print(service_request["resolved"])
service_request["owner"] = "IT Support"
print(service_request["owner"])
tags = ["password", "access", "support"]

print(tags[1])

tags.append("urgent")

print(tags)
print(len(tags))
for tag in tags:
    print(f"Tag: {tag}")
for tag in tags:
    if tag == "urgent":
        print("Urgent tag found")