'''
My project reads 100 posts and filters the posts flared as "discussion" in the r/Naruto subreddit. Identifies posts discussing the
user inputed character and how many upvotes and comments the post has + a link to the post.
'''
import requests
from unidecode import unidecode 

# Extract
def extract_reddit():
    '''requests data from r/Naruto to be used'''
    url = f"https://www.reddit.com/r/Naruto.json?limit=100" #takes data from 100 posts rather than the default 26

    head = {'user-agent': 'Safiyya A App v0.0.1'} 

    r = requests.get(url, headers = head)
    raw_data = r.json()
    return raw_data

# Transform
def reddit_transform(raw_data):
    '''iterates over 100 posts and identifies posts with character name in the title along with the upvotes, comments, and link'''
    character = input("Name a Naruto character:") #user input
    post = 0
    processed_data = [] #stores each iteration

    while post <= 99:
        flare = (raw_data ['data']['children'][post]['data']['link_flair_text'])
        title = (raw_data ['data']['children'][post]['data']['title'])
        flare_str = str(flare)
        if flare_str == "Discussion" and character in title:
            title = unidecode(title)

            upvotes = (raw_data['data']['children'][post]['data']['ups'])
            comments = (raw_data['data']['children'][post]['data']['num_comments'])
            link = (raw_data['data']['children'][post]['data']['url'])

            data = {'Title': title, 'Upvotes': upvotes, 'Comments': comments, "URL": link}
            processed_data.append(data.copy())

        post = post + 1   #counter for iteration
          
    return processed_data

        

# Load
def reddit_load(processed_data):
    '''
    Given the processed data dictionary from reddit_transform,
    save the data in a csv with given filename
    '''
    f = open('project-2.csv', 'w')
    f.write('Title,Upvotes,Comments,URL\n')
    for data in processed_data: #iterates and stores each discussion post
        f.write(f"{data['Title']}#{data['Upvotes']}#{data['Comments']}#{data['URL']}\n")

    f.close()     

raw_data = extract_reddit()
processed_data = reddit_transform(raw_data)
reddit_load(processed_data)

