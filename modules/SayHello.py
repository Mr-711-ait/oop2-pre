class SayHello:
def　init　(self, target="World"):
self.target = target

def say(self):
print(f"Hello, {self.target}!!")

if__name__== 'main':
app = SayHello()
app.say()
app = SayHello("Someone")
app.say()