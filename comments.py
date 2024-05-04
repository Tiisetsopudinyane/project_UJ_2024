# Define a dictionary to store comments
comments = {}

# Function to add a comment
def add_comment(comment_id, text):
    if comment_id not in comments:
        comments[comment_id] = {
            'text': text,
            'replies': []
        }
        print("Comment added successfully!")
    else:
        print("Comment with this ID already exists. Please choose another ID.")

# Function to add a reply to a comment
def add_reply(comment_id, reply_text):
    if comment_id in comments:
        comments[comment_id]['replies'].append(reply_text)
        print("Reply added successfully!")
    else:
        print("Comment with this ID does not exist. Please check the comment ID.")

# Example usage:
#add_comment(1, "This is the first comment.")
#add_reply(1, "Replying to the first comment.")
#add_comment(2, "Another comment.")
#add_reply(2, "Reply to another comment.")
#add_reply(1, "Another reply to the first comment.")
