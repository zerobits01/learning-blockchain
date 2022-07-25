import smartpy as sp
class EventPlanner(sp.Contract):
    def __init__(self, initialOwner):
        self.init(owner = initialOwner,
                  nameToEvent = sp.map(tkey = sp.TString))
    @sp.entryPoint
    def setDate(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.checkEvent(params.name)
        self.data.nameToEvent[params.name].date = params.newDate
    @sp.entryPoint
    def setNumGuests(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.checkEvent(params.name)
        self.data.nameToEvent[params.name].numGuests = params.newNumGuests
    @sp.entryPoint
    def changeOwner(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.data.owner = params.newOwner
    def checkEvent(self, name):
        sp.if ~(self.data.nameToEvent.contains(name)):
            self.data.nameToEvent[name] = sp.record(date = "", numGuests = 0)




@addTest(name = "AdvancedTest")
def test():
    scenario = sp.testScenario()
    # Create HTML output for debugging
    scenario.h1("Event Planner")
    
    # Initialize test addresses
    firstOwner = sp.address("tz1-firstOwner-address-1234")
    secondOwner = sp.address("tz1-secondOwner-address-5678")
    
    # Instantiate EventPlanner contract
    c1 = EventPlanner(firstOwner)
    
    # Print contract instance to HTML
    scenario += c1
    
    # Invoke EventPlanner entry points and print results to HTML
    scenario.h2("Set date for Tezos Meetup to 11-28-2017")
    scenario += c1.setDate(name = "Tezos Meetup", newDate = "11-28-2017").run(sender = firstOwner)
    
    scenario.h2("Set number of guests for Tezos Meetup to 80")
    scenario += c1.setNumGuests(name = "Tezos Meetup", newNumGuests = 80).run(sender = firstOwner)
    
    scenario.h2("Change owner")
    scenario += c1.changeOwner(newOwner = secondOwner).run(sender = firstOwner)
    
    scenario.h2("New owner sets date for Tezos Meetup to 03-21-2019")
    scenario += c1.setDate(name = "Tezos Meetup", newDate = "03-21-2019").run(sender = secondOwner)
    
    scenario.h2("Old owner attempts to set date for Tezos Meetup")
    scenario += c1.setDate(name = "Tezos Meetup", newDate = "10-15-2018").run(sender = firstOwner, valid = False)
    
    # Verify expected results
    scenario.verify((c1.data.nameToEvent["Tezos Meetup"].date) == '03-21-2019')
    scenario.verify((c1.data.nameToEvent["Tezos Meetup"].numGuests) == 80)
    scenario.verify((c1.data.owner) == sp.address('tz1-secondOwner-address-5678'))