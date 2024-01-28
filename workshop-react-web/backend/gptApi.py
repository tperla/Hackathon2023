 
import enum
import json
import requests

class role_options(enum.Enum):
    user = "user"
    assistant = "assistant"

    @classmethod
    def get_role_message(instance, role, message):
        if role == instance.user:
            return {"role": instance.user.value, "content": message}
        elif role == instance.assistant:
            return {"role": instance.assistant.value, "content": message}
        else:
            raise Exception("Invalid role")


class gpt_wrapper:
    class supported_models(enum.Enum):
        gpt_3_5_turbo = "gpt-3.5-turbo"

    @classmethod
    def get_tokens_per_dollar(instance, model : supported_models):
        if model == instance.supported_models.gpt_3_5_turbo:
            return 500000
        else:
            raise Exception("Invalid model name")
        
    @classmethod
    def tokens_to_dollars(instance, tokens, model : supported_models):
        return tokens / instance.get_tokens_per_dollar(model)

    @classmethod
    def get_response_with_history(instance, user_history : list, model : supported_models, api_key, loaded=False):
        refactored_user_history = [{"role": "system", "content": "You are an asistant for a person with cognitive difficulties."}]
        if loaded:
            for message in user_history:
                refactored_user_history.append(message)
        else:
            for message in user_history:
                if message[0] == role_options.user:
                    refactored_user_history.append({"role":"user", "content" : message[1]})
                elif message[0] == role_options.assistant:
                    refactored_user_history.append({"role":"assistant", "content" : message[1]})

        chatgpt_url = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key  # Replace with your actual API key
        }
        
        data = {
            "model" : model.value,
            #"model" : "gpt-4-0314",
            "messages": refactored_user_history
        }
        #print('getting image:\t' + prompt)
        response = requests.post(chatgpt_url, headers=headers, data=json.dumps(data))
        try:
            if response.status_code == 200:
                response_json = response.json()
                answer = response_json["choices"][0]["message"]["content"]
                token_amount = response_json['usage']['total_tokens']
                return answer, token_amount
        
        except:
            raise Exception("Sorry, we have encountered an error. Please try again")
        

    @classmethod
    def get_response(instance, message : str, model : supported_models, api_key):
        user_history = [(role_options.user, message)]
        return instance.get_response_with_history(user_history, model, api_key)
    
    @staticmethod
    def simplify_10_years_old(message : str):
        res = gpt_wrapper.get_response("Please simplify the following text for 10 years old children while retaining all the information and details.if the sentence is too small please give different sentence with the same meaning .if there are numbers high then 9999 please write it in words. Replace difficult words with easier synonyms and ensure the simplified version maintains the same original meaning. Please reply JUST with the text given. If anything goes wrong, reply with 'uh oh. 404: ' + a detailed reasoning of the error: "+message,
        #res = gpt_wrapper.get_response("You are a language model developed to assist young children in understanding complex sentences. Your goal is to rewrite the given sentence in a way that is clear and simple for a 10-year-old child. Make sure to preserve the original meaning of the sentence. Please simplify the following sentence:"+message,
        gpt_wrapper.supported_models.gpt_3_5_turbo, "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")
        return res[0]
    
    @staticmethod
    def simplify_5_years_old(message : str):
        res = gpt_wrapper.get_response("Please simplify the following text for 5 years old children while retaining all the information and details.if the sentence is too small please give different sentence with the same meaning .if there are numbers high then 9999 please write it in words. Replace difficult words with easier synonyms and ensure the simplified version maintains the same original meaning. Please reply JUST with the text given. If anything goes wrong, reply with 'uh oh. 404: ' + a detailed reasoning of the error: "+message,
        gpt_wrapper.supported_models.gpt_3_5_turbo, "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")
        return res[0]

    @staticmethod
    def cognitive_problems(message : str):
        res = gpt_wrapper.get_response("Please simplify the following text for people with a cognitive reading comprehension problem while preserving all the information and details.if the sentence is too small please give different sentence with the same meaning .if there are numbers high then 9999 please write it in words. Replace difficult words with easier synonyms and ensure the simplified version maintains the same original meaning. Please reply JUST with the text given. If anything goes wrong, reply with 'uh oh. 404: ' + a detailed reasoning of the error: "+message,
        #res = gpt_wrapper.get_response("You are a language model developed to assist individuals with cognitive disabilities. Your goal is to simplify the given text while preserving its meaning. Please rewrite the following sentence in a way that is easier to understand for someone with a cognitive disability:"+message,
        gpt_wrapper.supported_models.gpt_3_5_turbo, "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")
        return res[0]

    @classmethod
    def simplify_no_difficult_words(message : str):
        gpt_wrapper("Rephrase this text so a 5 year old kid will understand: "+message,
        gpt_wrapper.supported_models.gpt_3_5_turbo, "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")