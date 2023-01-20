import speech_recognition as sr
import pyttsx3

import my_text2speech as t2s
import my_speech2text as s2t

def main():
    text = s2t.s2t()
    t2s.t2s(text)


if  __name__ == "__main__":
     main()



# 1. Learn how to push code to git
# 2. Split code into two files a) text to speech b) speech to text
# 3. Run the current code with machine learning as is
# 4. Integrate this code with speech code as described below
# 5. Update Machine Learning Code to Add other currency notes and update step 4

# algorithm 

# * say start 
# * camera on
# * "place currency note"
# * use AI/ML to detect currency note
# * say value of note 