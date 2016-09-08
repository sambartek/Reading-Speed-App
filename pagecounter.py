# this is the page reader started on
beginning_page = int(raw_input("Starting Page: "))
# this is the page the reader ended on
ending_page = int(raw_input("Ending Page: "))

# total pages read equals the end page minus the beginning page
total_page = ending_page - beginning_page

print "You read %r pages." % total_page

# 275 comes from a total average of 250-300 from online average
total_words_read = total_page * 275 

# amount of time in minutes the reader read
time_read = int(raw_input("Duration in minutes: "))

# words per minute equals total words read divided by time spent reading
words_per_minute = total_words_read / time_read  

print "Your reading speed is %r words per minute." % words_per_minute

if words_per_minute >= 0 and words_per_minute < 50:
	print "Your reading level: Kindergarten"
if words_per_minute >= 50 and words_per_minute < 100:
	print "Your reading level: 3rd Grader"
if words_per_minute >= 100 and words_per_minute < 150:
	print "Your reading level: 5th Grader"
if words_per_minute >= 150 and words_per_minute < 250:
	print "Your reading level: Freshman High School"
if words_per_minute >= 250 and words_per_minute < 400:
	print "Your reading level: College Student"
if words_per_minute >= 400 and words_per_minute < 575:
	print "Your reading level: High Level Executive"
if words_per_minute >= 575 and words_per_minute < 675:	
	print "Your reading level: College Proffesor"
if words_per_minute >= 675 and words_per_minute < 1250:
	print "Your reading level: Speed Reader"
if words_per_minute >= 1250 and words_per_minute < 10000:
	print "Your reading level: Proffesional Speed Reader"
if words_per_minute >= 10000:
	print "Your reading level: Computer" 

print "Good job!"
