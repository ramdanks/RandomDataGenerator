from time import perf_counter_ns
from time import perf_counter

class Timer:

		#if not override, use start() to start the timer
	def __init__( self, title = "Undefined", override = False ):
		self.title = title
		self.override = override
		if not ( override ): self.start()

	def __del___( self ):
		if not ( override ): 
			self.stop()
			self.print()

	def start( self ):
		self.startTime = perf_counter_ns()
	
	def stop( self ):
		self.resTime = perf_counter_ns() - self.startTime

	def print( self ) :
		print( "%s %s : " % ( self.title,"Execution Time" ), end='' )
		if ( self.resTime < 1000 ):				print( "{:.3f}(ns)".format( self.resTime ) )
		elif ( self.resTime < 1000000 ):		print( "{:.3f}(us)".format( self.resTime/1000 ) )
		elif ( self.resTime < 1000000000 ):		print( "{:.3f}(ms)".format( self.resTime/1000000 ) )
		else :									print( "{:.3f}(sec)".format( self.resTime/1000000000 ) )