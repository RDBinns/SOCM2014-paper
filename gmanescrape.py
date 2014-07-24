import scraperwiki
import lxml.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getGmane():
	for num in range(1-2171):
		html = scraperwiki.scrape("http://permalink.gmane.org/gmane.law.tos-dr/%d" % (num))
		# html = scraperwiki.scrape("http://permalink.gmane.org/gmane.law.tos-dr/2346")
		root = lxml.html.fromstring(html)
		author = root.cssselect("span.author a")[0]
		day = root.cssselect("span.day")[0]
		subject = root.cssselect("h2.title")[0]
		#body = root.cssselect("div.blogbody pre")
		entry = "%s,%s,%s,\n" % (author.text, day.text, subject.text)
		with open("archive.csv", "a") as archive:
				archive.write(entry)
		print "archived entry %s" % (num)
getGmane()
