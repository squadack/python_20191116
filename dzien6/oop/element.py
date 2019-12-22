class Element:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class HeaderElement(Element):
    def render(self):
        text = super().render()
        return text + "\n" + "=" * len(text)

e = HeaderElement("Jakis napisadsfiuhdsjghfhdskjfhgkljhdsgjh")
print(e.render())