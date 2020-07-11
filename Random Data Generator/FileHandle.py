import os

def mkdir( dirname ):
	if not ( os.path.exists( dirname ) ):
			os.mkdir( dirname )
			return True
	else: return False 	
	
def write( string, filename, format = None ) :
	if ( format != None ): filename = "%s.%s" % ( filename,fo rmat )
	Fp = open( filename, "w" )
	print( string, file = Fp )
	Fp.close()

def append( string, filename, format = None ):
	if ( format != None ): filename = "%s.%s" % ( filename,format )
	Fp = open( filename, "a" )
	print( string, file = Fp )
	Fp.close()

def read( filename ) :
	Fp = open( filename, "r" )
	string = Fp.readline()
	fRead.close()
	return string