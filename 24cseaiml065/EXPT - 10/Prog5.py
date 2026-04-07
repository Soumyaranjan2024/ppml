class parent:
    def __init__(self):
        print("Parent Constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
c = child()