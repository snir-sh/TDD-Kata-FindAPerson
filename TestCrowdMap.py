import unittest
from Crowdmap import Crowdmap

class TestCrowdmap(unittest.TestCase):
	def test_crowdmapForAPerson_returns_allPosts(self):
		crowdmap = Crowdmap()
		posts = crowdmap.get_all_posts_for("Or")
		self.assertEquals(posts, ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])
		
if __name__ == '__main__':
	unittest.main()