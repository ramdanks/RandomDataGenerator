import os
import Randomizer
import FileHandle
import Timer
from prettytable import PrettyTable

def RandDataGenerator( size, debug ) :
	
	def RandomDOB():
		temp1 = Randomizer.RandName( "Random/province.txt" )
		temp2 = Randomizer.RandNum( 1, 30, 1 )
		temp3 = Randomizer.RandName( "Random/months.txt" )
		temp4 = Randomizer.RandNum( 1996, 2004, 1 )
		dob = "%s %d %s %d" % ( temp1,temp2,temp3,temp4 )
		return dob

	def RandomIPK():
		temp1 = Randomizer.RandNum( 1,3,1 )
		temp2 = Randomizer.RandNum( 0,9,2 )
		ipk = "%d.%d" % ( temp1,temp2 )
		return ipk

	def RandomName():
		prefix = Randomizer.RandName( "Random/prefix.txt" )
		suffix = Randomizer.RandName( "Random/suffix.txt" )
		name = "%s %s" % ( prefix, suffix )
		return name
	
	if ( debug ):
		perfcounter = Timer.Timer("Random Generator", override=True )
		perfcounter.start()
	#implementation
	if ( debug ): print( "Starting Generator!" )
	for i in range( size ):
		if ( debug ): print( "Generating: %d out of %d" % ( i+1,size ) )
		Name = RandomName()
		DOB = RandomDOB()
		Grade = RandomIPK()
		Year = Randomizer.RandNum( 2014, 2019, 1 )
		NPM = Randomizer.RandNum( 0,9,10 )
		string = "%s,%d,%s,%d,%s" % ( Name,NPM,DOB,Year,Grade )
		FileHandle.append( string, "DataMahasiswa", "csv" )
	if ( debug ):
		perfcounter.stop()
		perfcounter.print()

size = input( "Size to Generate:" )
RandDataGenerator( int(size), debug=True )