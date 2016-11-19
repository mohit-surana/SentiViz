# SentiViz
Sentiment Based Visualization of Tweets

Developers: Coldsp33d, cueo and doodhwala

At #code2k16 (19-11-2016 to 20-11-2016)

# The problem
For the last few years, Twitter has always been a channel for people to speak out on various topics. Anything that makes the news will inevitably become a trending topic on Twitter. These topical Tweets are often collected and analysed by news media to determine the sentiment of the public with respect to the issue. This is, a manual process - no one can go through every single tweet, and so the resultant analysis is not 100% representative of the entire populace.

# The idea
As a solution, we propose our idea, #ThePublicSpeaks - a tweet corpus summariser.

# The proposed implementation
Using readily available tools, collect all tweets pertaining to a trending topic from twitter. The thing about any trending topic is that different people voice different opinions. We want to ensure that this is not lost. Using K-means clustering, we segregate tweets into related clusters based on sentiment, and then perform text summarisation on each cluster using natural language processing with a deep learning approach. We then tabulate the results for each cluster, giving the weighted average sentiment score of the entire corpus. The weighted average takes into account the size of each cluster. Our system aims to operate on any given trending topic with a sufficiently large corpus (>5000) without any change in the model or model parameters.
