library(ggplot2)
yelp_data = read.table("star_sentimentscore.txt", sep = "\t", col.names = c("avg_star_rating", "avg_review_sentiment"))

ggplot(yelp_data, aes(x=avg_star_rating, y=avg_review_sentiment)) + geom_point() + geom_smooth(method=lm, se=FALSE) + ggtitle("Average Star Rating and Review Sentiment\n in the Yelp Academic Dataset")

ggplot(yelp_data, aes(x=avg_star_rating, y=avg_review_sentiment)) + stat_binhex() + ggtitle("Average Star Rating and Review Sentiment\nin the Yelp Academic Dataset")
cor(yelp_data, method ="pearson")