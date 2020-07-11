class Array :

	def __init__( self,size ) :
		self.arr = [ int ] * size
		self.size = int( size )
		self.index = 0
		self.set( None )

	def print( self ) :
		for i in range( self.size ) :
			if ( self.arr[i] != None ) :
				if ( i+1 < self.size ) and ( self.arr[i+1] != None ) :
					print( self.arr[i],end=',' )
				else :
					print( self.arr[i],end=' ' )
		print()

	def __eq__( self,value ) :
		for i in range( self.size ) :
			if ( value != self.arr[i] ) :
				return False
		return True

	def exist( self,value ) :
		for i in range( self.size ) :
			if ( value == self.arr[i] ) :
				return True
		return False

	def set( self,value ) :
		for i in range( self.size ) :
			self.arr[i] = value
		if ( value != None ) :
			self.index = self.size

	def push( self,value ) :
		if ( self.index < self.size ) :
			self.arr[self.index] = value
			self.index += 1

	def pop( self,value = 1 ) :
		for i in range( int( value ) ) :
			if ( self.index != 0 ) :
				self.arr[self.index - 1] = None
				self.index -= 1

	def sort( self ) :
		for i in range( self.size ) :
			check = self.arr[i]
			if ( self > self.arr[i] ) :
				temp = self.arr[i]
				self.arr[i] = self.arr[j]
				self.arr[j] = temp
	
	def refreshIndex( self ) :
		temp = 0
		for i in range( self.size ) :
			if ( self.arr[i] != None ) :
				temp += 1
		self.index = temp