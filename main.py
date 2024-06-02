import telebot
import google.generativeai as genai

genai.configure(api_key="AIzaSyCbPY6JIOSJxrIZGS3ZlLoX4NlVlj6giAM")

bot = telebot.TeleBot("6394052562:AAE5aNrGaMGHf0XSSTnU8Y8ihm6rl3iP8Fs", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN   


 #Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)





@bot.message_handler(func=lambda m: True)
def echo_all(message):
	response = chat_session.send_message(message.text)
	bot.reply_to(message,response.text)
bot.infinity_polling()



