import os
import Randomizer
import FileHandle
import Timer
import re
import math
from prettytable import PrettyTable

def clearscreen(): os.system("cls")
def pause(): os.system("pause")

def ShowData( filename, header, limit, delimiter='' ):

	def ShowInfo( limit, TotalData, PageIndex ):
		clearscreen()
		print( "Data Showed in Page: ", limit )
		print( "Data Loaded: ", TotalData )
		print( "Page %d out of %d" % ( PageIndex,TotalPage ) )
		
	TableData = PrettyTable( header )
	CatchData = FileHandle.read( filename )
	TotalData = len( CatchData )

	#Error Checking, If Header doesn't match the Data
	DataColumn = CatchData[0].split( delimiter )
	if not ( len(DataColumn) == len(header) ): return False
	
	if ( limit > TotalData ): limit = TotalData
	TotalPage = int( math.ceil(TotalData/limit) )
	PageIndex = 1
	DiscoverPage = True

	while( DiscoverPage ):
		ShowInfo( limit, TotalData, PageIndex )
		
		#Print Data Based on Limit and Starting Index (Page)
		StartingIndex = (PageIndex-1) * limit
		for i in range( StartingIndex, StartingIndex+limit ):
			DataColumn = CatchData[i].split( delimiter )
			TableData.add_row( DataColumn )
		print( TableData )
		TableData.clear_rows()
		
		if ( TotalPage > 1 ):
			while( True ):
				SelectPage = input("'0':Exit, Input Page to View:")
				if ( SelectPage == '' or SelectPage < '0' or SelectPage > '9' ): SelectPage = -1
				else: SelectPage = int(SelectPage)

				if ( SelectPage <= TotalPage and SelectPage > 0 ): 
					PageIndex = SelectPage
					break
				elif ( SelectPage == 0 ): 
					DiscoverPage = False
					break
				else: print( "Err:Invalid Range" )

	return True

def RandDataGenerator( filename, format, size, debug ) :
	
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
		FileHandle.append( string, filename, format )
	if ( debug ):
		perfcounter.stop()
		perfcounter.print()

#size = input( "Size to Generate:" )
#RandDataGenerator( "DataMahasiswa", "csv", int(size), debug=True )

header = [ "Nama", "NPM", "TTL", "Angkatan", "IPK" ]
ShowData( "DataMahasiswa.csv", header, 10, ',' )