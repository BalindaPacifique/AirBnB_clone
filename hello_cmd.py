import cmd

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	prompt = "Fred% "
	
	def do_greet(self, line):
		print('Hello Frederick')
	
	def do_EOF(self, line):
		return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
