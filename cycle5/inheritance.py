class parent:
    parentattr = 100
    def __init__(self):
        print ("calling parent costructor")

    def parentmethod(self):
        print ("calling parent method")

class child(parent):
    def __init__(self):
        print ("calling child constructor")

    def childmethod(self):
        print ("calling child mathod")

c = child()
c.childmethod()
c.parentmethod()

