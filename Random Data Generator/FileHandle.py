import os

def mkdir( dirname ):
	if not ( os.path.exists( dirname ) ):
			os.mkdir( dirname )
			return True
	else: return False 	
	
def write( string, filename, format=None ) :
	if ( format != None ): filename = "%s.%s" % ( filename,format )
	Fp = open( filename, "w" )
	print( string, file = Fp )
	Fp.close()

def append( string, filename, format=None ):
	if ( format != None ): filename = "%s.%s" % ( filename,format )
	Fp = open( filename, "a" )
	print( string, file = Fp )
	Fp.close()

def read( filename, line=None ):
	Fp = open( filename, "r" )
	string = []
	if ( line == None ): string = Fp.readlines()
	else:
		for i, line in enumerate(Fp):
			if i == line:
				string = str(line).rstrip()
				break
	Fp.close()
	return string