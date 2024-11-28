import re

# Step 1: Load threat words from a text file
def load_threat_words(file_path):
    with open(file_path, 'r') as file:
        threat_words = file.read().splitlines()
    return set(threat_words)

# Step 2: Function to preprocess text (tokenize and clean the posts)
def preprocess_text(text):
    # Convert text to lowercase and remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    return text.split()

# Step 3: Function to check for threat words in a post
def detect_threat(post, threat_words):
    tokens = preprocess_text(post)
    return any(word in threat_words for word in tokens)

# Step 4: Filter posts containing threat words
def filter_threat_posts(posts, threat_words):
    return [post for post in posts if detect_threat(post, threat_words)]

# Example usage:
if __name__ == "__main__":
    # Sample social media posts
    posts = [
    "There is a bomb threat in the city center.",
    "The weather is beautiful today, perfect for a walk in the park.",
    "I'm afraid something terrible is about to happen soon.",
    "The government building is being targeted by extremists.",
    "Stay away from the subway today, it’s not safe.",
    "Had a relaxing day at the spa, feeling so refreshed.",
    "The concert venue is at risk of a terrorist attack.",
    "Someone mentioned planning an explosion at the shopping mall.",
    "The bridge has been sabotaged, people are trapped.",
    "I overheard someone talking about a robbery planned for tomorrow night.",
    "Can't wait to watch the new movie that just came out!",
    "We’re tracking a hacker group targeting our systems.",
    "I'm seeing violent protests getting out of control in the city.",
    "Someone is talking about setting fire to a government office.",
    "Avoid the city tonight, there might be riots.",
    "I think they are planning to detonate a bomb in the main square.",
    "Just got word that a kidnapping is going down at the school."
]

    
    # Load threat words (e.g., 'threat_words.txt' contains words like 'bomb', 'attack', etc.)
    threat_words = load_threat_words('C:/Users/Wajiz.pk/Desktop/face/threats_words.txt')



    # Filter posts that contain threat words
    flagged_posts = filter_threat_posts(posts, threat_words)

    # Print flagged posts
    print("Posts containing threats:")
    for post in flagged_posts:
        print(post)