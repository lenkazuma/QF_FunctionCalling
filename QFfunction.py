import qianfan
import re

def add_numbers(a: int, b: int):
    """
    This function adds two numbers.
    """
    return a + b

def say_hello(name: str):
    """
    This function greets the user.
    """
    return f"Hello, {name}!"


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
prompt = "你能计算一下42069420 + 6969420等于多少吗？###嗨你怎么样？###"
prompt_list = re.split(r"###", prompt)

for questions in prompt_list:
    response = eb_call(questions, round)
    st.write(response['result'])
