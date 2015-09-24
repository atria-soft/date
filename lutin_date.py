#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import datetime

def get_desc():
	return "Date buid date of the program"


def create(target):
	# module name is 'edn' and type binary.
	my_module = module.Module(__file__, 'date', 'LIBRARY')
	# add the file to compile:
	
	
	my_module.add_src_file([
		'date/date.cpp'
		])
	
	my_module.add_header_file([
		'date/date.h'
		])
	
	now = datetime.datetime.now()
	
	my_module.compile_flags('c++', [
		'-Wno-write-strings',
		'-Wall',
		"-DBUILD_DAY=\""+str(now.day)+"\"",
		"-DBUILD_MONTH=\""+str(now.month)+"\"",
		"-DBUILD_YEAR=\""+str(now.year)+"\"",
		"-DBUILD_HOUR=\""+str(now.hour)+"\"",
		"-DBUILD_MINUTE=\""+str(now.minute)+"\"",
		"-DBUILD_SECOND=\""+str(now.second)+"\""])
	
	my_module.add_path(tools.get_current_path(__file__))
	
	# add the currrent module at the 
	return my_module


