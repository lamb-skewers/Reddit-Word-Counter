## Analyze trending terms on Reddit!

#### This code allows you to select a subreddit on reddit.com and find the most common words used in titles from the first specified number of posts in a certain category (top, hot, and new). The code will automatically exclude common words such as articles and pronouns in order to filter out with words with little relevant data. I originally created this code to analyze /r/FireEmblemHeroes to gather data on which characters were most talked about during the game's "Choose Your Legends" voting campaign, but this code has other uses in determining trends and topics of interest in other online communities.

### User Notice

#### This code uses the Reddit API to collect information from the site so any users must comply with Reddit's OAuth to execute the code. This is easily done by creating an app at https://www.reddit.com/prefs/apps. Once you create the app, simply paste your client ID and secret in the spots allocated in the file. You may also need to install praw if it is not already in your library. To use the code, simply set the input variables to find your desired result. Note that inputs, particularly subreddit names, are case-sensitive. 
