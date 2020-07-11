import os
import random

def LineCount( filename ):
	f = open( filename, 'rb' )
	lines = 0
	buf_size = 1024 * 1024
	read_f = f.raw.read

	buf = read_f(buf_size)
	while buf:
	    lines += buf.count(b'\n')
	    buf = read_f(buf_size)

	return lines

def RandNum( lowBound, upBound, Length, Step = 1 ) :
	temp = [int] * Length
	for i in range(Length):
		temp[i] = random.randrange( lowBound,upBound+1,Step )
	string = map( str,temp )
	string = ''.join( string )
	return int( string )

def RandName( filename ):
	string = None
	rand_value = RandNum( 0, LineCount( filename ), 1 )
	with open( filename ) as fp:
		for i, line in enumerate(fp):
			if i == rand_value:
				string = str(line).rstrip()
				break
	return string