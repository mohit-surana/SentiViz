# -*- coding: utf-8 -*-
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from string import Template
import os

from preprocess import *

def setUp(self):
        self.test_output = os.path.join(os.getcwd(), 'out')
        self.hound = open(os.path.join(os.getcwd(), 'tweet.txt'), 'r')

        if not os.path.exists(self.test_output):
            os.mkdir(self.test_output )

def tearDown(self):
    self.hound.close()

def test_tag_counter(self):
    tag_list = get_tag_counts(self.hound.read())[:50]
    self.assertTrue(('sir', 350) in tag_list)

def test_layouts(self):
        start = time.time()
        tags = make_tags(get_tag_counts(self.hound.read())[:80], maxsize=120)
        for layout in LAYOUTS:
            create_tag_image(tags, os.path.join(self.test_output, 'cloud_%s.png' % layout),
                             size=(900, 600),
                             background=(255, 255, 255, 255),
                             layout=layout, fontname='Lobster')
        print "Duration: %d sec" % (time.time() - start)

def create_tags(tweet, out='out'):
	tweet = clean_tweet(tweet)
	output = os.path.join(os.getcwd(), out)
	# tag_list = get_tag_counts(self.hound.read())[:50]
	tags = make_tags(get_tag_counts(tweet)[:50], maxsize=50)
	for layout in LAYOUTS:
		create_tag_image(tags, './static/' + out + ('/cloud_%s.png' % layout),
		size=(500, 500),
		background=(255, 255, 255, 255),
		layout=layout, fontname='Lobster')
