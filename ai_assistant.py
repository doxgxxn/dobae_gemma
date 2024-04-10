from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()
hugging_face_api = os.environ.get("HUGGING_FACE_API")
login(hugging_face_api)

class AIassistant():
    def __init__(self, model_name="google/gemma-2b-it", finetune_model="doxgxxn/dobae_gemma", temperature=0.2, top_k=50, top_p=0.95):
        """Initialize the AI assistant."""

        # Initialize attributes
        self.finetune_model = AutoModelForCausalLM.from_pretrained(finetune_model, device_map={"":0})
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, add_special_tokens=True)
        self.pipe_finetuned = pipeline("text-generation", model=self.finetune_model, tokenizer=self.tokenizer, max_new_tokens=512)
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
    
    def query(self, query):
        """Query the knowledge base of the AI assistant"""
        
        message = [
                     {
                        "role": "user",
                        "content": "다음 글을 답변해주세요:\n\n{}".format(query)
                    }
                  ]
        prompt = self.pipe_finetuned.tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True)
        outputs = self.pipe_finetuned(
                                        prompt,
                                        do_sample=True,
                                        temperature=self.temperature,
                                        top_k=self.top_k,
                                        top_p=self.top_p,
                                        add_special_tokens=True
            
                                        )
        return outputs[0]['generated_text'][len(prompt):]
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        
    def set_top_k(self, top_k):
        self.top_k = top_k
        
    def set_top_p(self, top_p):
        self.top_p = top_p