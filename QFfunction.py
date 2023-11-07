import qianfan
import re
import streamlit as st

def list_synonyms(synonyms: list[str]):
    """
    Show a list of synonyms to the user.
    """
    return synonyms
    
def add_numbers(a: int, b: int):
    """
    This function adds two numbers.
    """
    return a + b

def say_hello(name: str):
    """
    This function greets the user.
    """
    return f"你好, {name}!"


def eb_call(prompt, round):
    print(prompt)
    print('-' * 20,' Output ', '-'*20,"\n")

    response = chat_comp.do(
            model="ERNIE-Bot", 
            messages=[{
                "role": "user",
                "content": prompt
                }],
            temperature=0.000000001,
            functions=[
                {
                    "name": "add_numbers",
                    "description": "This function adds two numbers.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "a": {
                                "type": "integer",
                                "description": ""
                            },
                            "b": {
                                "type": "integer",
                                "description": ""
                            }
                        },
                        "required": [
                            "a",
                            "b"
                        ]
                    }
                },
                {
                    "name": "say_hello",
                    "description": "This function greets the user.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": ""
                            }
                        },
                        "required": [
                            "name"
                        ]
                    }
                }
                 ]
            )


    st.write(response)
    return response

chat_comp = qianfan.ChatCompletion(ak="LrQvpiE6f4npsUwEvPL9vEWF", sk="CHTwBMVM0DlwyoGTLGEyRviBdctgOv4G")
prompt = "这两个数加起来是多少，42069420 和 6969420？### 我叫ZZ，你好###"
prompt_list = re.split(r"###", prompt)

for questions in prompt_list:
    response = eb_call(questions, round)
    st.write(response['result'])
