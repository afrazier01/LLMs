from transformers import pipeline, Conversation
import gradio

chatbot=pipeline("conversational", model="facebook/blenderbot-400M-distill")

message_list=[]
response_list=[]

def simply_chatbot(message, history):
    conversation=Conversation(text=message, # User inputs
                              past_user_inputs=message_list, # Context so the chatbot understands the conversation before responding
                              generated_responses=response_list)
    conversation=chatbot(conversation)
    
    return conversation.generated_responses[-1] #return the last generated response

demo_chatbot=gradio.ChatInterface(simply_chatbot, # pass chatbot object
                                  title="Simply-Chatbot",
                                  description="Enter text to begin chatting!")

demo_chatbot.launch()
