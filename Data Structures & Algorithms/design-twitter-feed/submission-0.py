import heapq

class Twitter:

    def __init__(self):
        # userId -> set of users they follow
        self.following = {}

        # userId -> list of (timestamp, tweetId)
        self.tweets = {}

        # Used to keep tweets ordered by time
        self.time = 0

    def postTweet(self, userId, tweetId):

        # Make sure user follows themself
        if userId not in self.following:
            self.following[userId] = set()

        self.following[userId].add(userId)

        # Store tweet with timestamp
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):

        # If user doesn't exist, create their self-follow
        if userId not in self.following:
            self.following[userId] = {userId}

        # Max heap:
        # (-timestamp, userId, index, tweetId)
        heap = []

        # Add the most recent tweet from every followed user
        for followee in self.following[userId]:

            if followee in self.tweets and self.tweets[followee]:

                index = len(self.tweets[followee]) - 1
                timestamp, tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-timestamp, followee, index, tweetId)
                )

        result = []

        # Get at most 10 most recent tweets
        while heap and len(result) < 10:

            neg_time, followee, index, tweetId = heapq.heappop(heap)

            result.append(tweetId)

            # Move to the previous tweet of this user
            index -= 1

            if index >= 0:

                timestamp, tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-timestamp, followee, index, tweetId)
                )

        return result

    def follow(self, followerId, followeeId):

        # Create follower's set if needed
        if followerId not in self.following:
            self.following[followerId] = set()

        # Follow the user
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):

        # A user cannot unfollow themselves
        if followerId == followeeId:
            return

        # Remove follow relationship if it exists
        if followerId in self.following:
            self.following[followerId].discard(followeeId)