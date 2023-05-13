from backend.posts import Tweet, Comment

# tweets = Tweet.objects.filter(id=1)
# print(tweets)
# print(tweets.query)
#
#
# comment = Comment.objects.get(id=1)
# print(comment.tweet)
#
# tweet = Tweet.objects.create(title='TWEET', body='BODY', user_id=1)
# comment = Comment(text='COMMENT', user_id=1, tweet_id=tweet.id)
# comment2 = Comment(text='COMMENT2', user=User.objects.get(id=1), tweet=tweet)
#
# comment.save()
# comment2.save()

# comments = Comment.objects.exclude(id=1)
# print(comments)
#
# for i in range(10):
#     Tweet.objects.create(title=f'Title {i}', body=f'Body{i}', user_id=1)

# tweets = Tweet.objects.filter(id__in=[1, 2, 3, 4, 5]).order_by('-id')[0:2]
# print(tweets)
# print(tweets.query)
#
# tweets_odds = tweets.filter(id__in=[1, 2, 3])
# print(tweets_odds)
# print(tweets.query)
#
# tweet_not_5 = tweets_odds.exclude(id=5)
# print(tweet_not_5)
# print(tweets.query)
#


tweets = Tweet.objects.filter(title__iexact='Title 0')
print(tweets)
print(tweets.query)


tweets_contain = Tweet.objects.filter(title_contains='Title')
print(tweets_contain)
print(tweets.query)


itweets_contain = Tweet.objects.filter(title_icontains='title')
print(itweets_contain)
print(itweets_contain.query)

tweets_greater_than_5 = Tweet.objects.filter(id_gt=5)
print(tweets_greater_than_5)
print(tweets_greater_than_5.query)


tweets_greater_than_or_equal_5 = Tweet.objects.filter(id_gte=5)
print(tweets_greater_than_or_equal_5)
print(tweets_greater_than_or_equal_5.query)

comments = Comment.objects.filter(tweet__title__iexact='tweet')
print(comments)
print(comments.query)

comments = Comment.objects.filter(tweet__user__id__lt=2)
print(comments)
print(comments.query)


