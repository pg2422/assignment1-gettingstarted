### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    qa = {
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "mtls", 
        "Are encoding and encryption the same? - Yes/No": "No",
        "Is it possible to decrypt a message without a key? - Yes/No": "No",
        "Is it possible to decode a message without a key? - Yes/No": "Yes",
        "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
        "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code": "42b76fe51778764973077a5a94056724",
        "Is MD5 a secured hashing algorithm? - Yes/No": "No",
        "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number": 3,
        "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number": 4
    }

    if (question in qa):
      return qa[question]

    return(None)

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
