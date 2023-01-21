import random
import json
import re
import random_responses

# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("responses.json")

def get_response_small(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        #return 'Hey there!'

        random_list = [
            "Please try writing something more descriptive.",
            "Oh! It appears you wrote something I don't understand yet",
            "Do you mind trying to rephrase that?",
            "I'm terribly sorry, I didn't quite catch that.",
            "I can't answer that yet, please try asking something else."
        ]

        list_count = len(random_list)
        random_item = random.randrange(list_count)

        return random_list[random_item]

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'


def get_response(message: str) -> str:
    p_message = message.lower()

    p_message = re.split(r'\s+|[,;?!.-]\s*', p_message.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in p_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in p_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if p_message == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()