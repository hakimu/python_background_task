import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
from time import sleep




@newrelic.agent.background_task()
def adder():
	x = 100
	sleep(5)
	y = 200 
	return x + y

@newrelic.agent.background_task()
def greeter():
	print "hello"
	sleep(5)
	print "goodbye"


adder()

greeter()