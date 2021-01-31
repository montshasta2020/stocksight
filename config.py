elasticsearch_host = "localhost"
elasticsearch_port = 9200
elasticsearch_user = " elastic"
elasticsearch_password = "xxI9rfGHlqnnQDTHJEEJ2iRS"
consumer_key = "P8frEjZKxEOpPUWF28pM9ezRL"
consumer_secret = "SlmjP5LysL0dmjJxEff4MNe5suyNhypuekN3eICNlaQPgjitDu"
access_token = "1353117267345567744-tW4KqbGJJxCnyF8DeHVLYGOePLorGp"
access_token_secret = "QYXtrFxfCL5scxjRAifJCH83YDQudcHnx7U90QXu5R8MD"
nltk_tokens_required = ("neuralink", "solar", "tesla", "@tesla", "#tesla", "tesla", "tsla", "#tsla", "elonmusk", "elon", "musk", "spacex", "starlink")
nltk_min_tokens = 1
nltk_tokens_ignored = ("win", "giveaway")
twitter_feeds = ["@elonmusk", "@cnbc", "@benzinga", "@stockwits",
                 "@Newsweek", "@WashingtonPost", "@breakoutstocks", "@bespokeinvest",
                 "@WSJMarkets", "@stephanie_link", "@nytimesbusiness", "@IBDinvestors",
                 "@WSJDealJournal", "@jimcramer", "@TheStalwart", "@TruthGundlach",
                 "@Carl_C_Icahn", "@ReformedBroker", "@bespokeinvest", "@stlouisfed",
                 "@muddywatersre", "@mcuban", "@AswathDamodaran", "@elerianm",
                 "@MorganStanley", "@ianbremmer", "@GoldmanSachs", "@Wu_Tang_Finance",
                 "@Schuldensuehner", "@NorthmanTrader", "@Frances_Coppola", "@bySamRo",
                 "@BuzzFeed","@nytimes"]


sudo su -c "echo "network.host: 0.0.0.0" >> /etc/elasticsearch/elasticsearch.yml"


curl -XDELETE http://3.19.255.120:9200/.kibana*
https://3.19.255.120/


echo '
elasticsearch.url: "https://ec2-18-191-209-224.us-east-2.compute.amazonaws.com:9200/" 
server.host: "0.0.0.0"
' | sudo tee /etc/kibana/kibana.yml


