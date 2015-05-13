import unittest
from Crowdmap import Crowdmap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])
		
    def test_getAllPostsForName(self):
        posts = self.crowdmap.get_all_posts_for("Or")
        self.assertIn(posts, ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])
						
if __name__ == '__main__':
	unittest.main()