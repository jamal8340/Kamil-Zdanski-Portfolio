using System.IO;
using System.Text.Json;
using System.Collections.Generic;
using System.Xml.Serialization;
using System.Linq;
using System.Globalization;


List<Tweet> Tweet_list = new List<Tweet>();

string filePath = "favorite-tweets.jsonl";

foreach (string line in File.ReadLines(filePath)){
    Tweet newtweet = JsonSerializer.Deserialize<Tweet>(line);
    Tweet_list.Add(newtweet);
}

List<Tweet> ListSortedTweetsByDate = new List<Tweet>();
ListSortedTweetsByDate = SortByDate(Tweet_list);
Tweet Oldest_tweet = ListSortedTweetsByDate[0];
Tweet Newest_tweet = ListSortedTweetsByDate[ListSortedTweetsByDate.Count -1]; 
Console.WriteLine('\n' +"najstarszy tweet: " + "\n    "+ Oldest_tweet.UserName + " \nnapisał: " +"\n    "+ 
Oldest_tweet.Text + '\n' + Oldest_tweet.Date );
Console.WriteLine('\n' +"najnowszy tweet: " +"\n    " + Newest_tweet.UserName + " \nnapisał: " +"\n    "+ Newest_tweet.Text + '\n'
+ Newest_tweet.Date );


Dictionary<string, List<Tweet>> users_dict = new Dictionary<string, List<Tweet>>();
foreach (Tweet tweet in Tweet_list)
{
    if (users_dict.ContainsKey(tweet.UserName))
    {
        users_dict[tweet.UserName].Add(tweet);
    }
    else{
        List<Tweet> new_list= new List<Tweet>();
        new_list.Add(tweet);
        users_dict[tweet.UserName]=new_list;
        }
}

char[] separators = new char[] { ' ', '.', ',', '!', '?', '"', '\'', '\n', '\r', ':', '/', '\\', '-', '@', '&', '<', '>', ';' ,')','('};
Dictionary<string, int>words= new Dictionary<string, int>();
foreach (Tweet tweet in Tweet_list)
{   
    string[] words_tweet = tweet.Text.ToLower().Split(separators,StringSplitOptions.RemoveEmptyEntries);
    foreach (string word in words_tweet)
    {
        if (words.ContainsKey(word))
        {
            words[word]++;
        }
        else
        {
            words[word]=1;
        }
    }
}




var sorted_10_words = words.Where(x => x.Key.Length>=5).OrderByDescending(x => x.Value).Take(10).ToDictionary(x => x.Key, x => x.Value);
foreach (string word in sorted_10_words.Keys)
{
    Console.WriteLine(word + " : " + sorted_10_words[word]);
}




int N=Tweet_list.Count;
Dictionary<string, double>IDF_dict= new Dictionary<string, double>();
foreach (string word in words.Keys)
{

    int Counttweets = 0;

    foreach (Tweet tweet in Tweet_list)
    {   
        
        string[] words_tweet = tweet.Text.ToLower().Split(separators,StringSplitOptions.RemoveEmptyEntries);
        if (words_tweet.Contains(word))
        {
            Counttweets++;
        }
    }

    double IDF=Math.Log10((double)N / Counttweets);
    IDF_dict[word] = IDF;
}
var top10_IDF = IDF_dict.OrderByDescending(x => x.Value).Take(10);

Console.WriteLine("\ntopka slow z najwyzszym IDF: ");
foreach (var item in top10_IDF)
{
    Console.WriteLine(item.Key + " : " + item.Value);
}





void SaveToXml(string filePath_xml, List<Tweet> data){
    XmlSerializer xml = new XmlSerializer(typeof(List<Tweet>));
    StreamWriter sw_xml = new StreamWriter(filePath_xml);
    xml.Serialize(sw_xml, data);
    sw_xml.Close();
}

List<Tweet> LoadFromXml(string filePath_xml){
    XmlSerializer xml = new XmlSerializer(typeof(List<Tweet>));
    StreamReader sr_xml = new StreamReader(filePath_xml);
    List<Tweet> tweet_list = (List<Tweet>)xml.Deserialize(sr_xml);
    sr_xml.Close();
    return tweet_list;
}

List<Tweet> SortByDate(List<Tweet> tweets)
{
    List<Tweet> sortedTweets = tweets.OrderBy(t => t.Date).ToList();
    return sortedTweets;
}

List<Tweet> SortByUser(List<Tweet> tweets)
{
    List<Tweet> sortedTweets = tweets.OrderBy(t => t.UserName).ToList();
    return sortedTweets;
}

public class Tweet
{
    public string Text{get;set;}
    public string UserName{get;set;}
    public DateTime Date{get=>DateTime.Parse(CreatedAt.Replace(" at ", " "), CultureInfo.InvariantCulture);}
    public string CreatedAt{get;set;}

    public Tweet(string text,string username, string time)
    {
        Text=text;
        UserName=username;
        CreatedAt=time;
    }
    public Tweet() {}


}


