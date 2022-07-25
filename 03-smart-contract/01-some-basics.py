'''
Smart contracts are simply programs stored on a blockchain that run when predetermined conditions are met. 
They typically are used to automate the execution of an agreement so that all participants can be immediately 
certain of the outcome, without any intermediary’s involvement or time loss. They can also automate a workflow, 
triggering the next action when conditions are met.

Smart contracts work by following simple “if/when…then…” statements that are written into code on a blockchain. 
A network of computers executes the actions  when predetermined conditions have been met and verified. 
These actions could include releasing funds to the appropriate parties, registering a vehicle, 
sending notifications, or issuing a ticket. The blockchain is then updated when the transaction is completed. 
That means the transaction cannot be changed, and only parties who have been granted permission can see the results.

an application on blockchain platform
despite its name it is a program which gonna be run on all the systems

contract by usual is a set of rules or clauses we have to write the rules and the situation in programming languages

code on the blockchain, we have talked about data and transaction on blockchain why not having codes on it?

we have something namd bitcoin script which lets us to write different applications on bitcoin

SmartPy is an intuitive and powerful smart contract development platform for Tezos. 
Online EditorSmartPy CLIReleasesBlog postsExplorer Public Nodes Documentation.

'''
import smartpy as sp

class SimpleMath(sp.Contract):
    def __init__(self):
        self.init(sum = 0)
    @sp.entryPoint
    def computeSum(self, params):
        self.data.sum = params.augend + params.addend

@addTest(name = "MathTest")
def test():
    scenario = sp.testScenario()
    scenario.h1("Simple Math Tests")
    contract = SimpleMath()
    scenario += contract
    scenario.h2("Test Addition")
    scenario += contract.computeSum(augend = 1, addend = 2).run(sender = sp.address("tz1234"))
    
'''
we can create our own blockchain with python which saves code and triggers
this way we have created a platform for running codes on specific triggers when new blocks or transactions are added.
'''