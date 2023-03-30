class Message:
    """

    """
    cnt = 0

    def __init__(self, sender: str, receiver: str, data: dict):
        Message.cnt += 1
        self.id = Message.cnt
        self.sender = sender
        self.receiver = receiver
        self.data = data

    def to_string(self):
        return "Msg-%02d: %s->%s" % (self.id, self.sender, self.receiver)
