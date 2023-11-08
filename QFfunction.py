import qianfan
import re
import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(123)
import json

   
def add_numbers(a: int, b: int):
    """
    This function adds two numbers.
    """
    return a + b

def say_hello(name: str):
    """
    This function greets the user.
    """
    return f"你好, {name}! 我是Ernie助手。"
    
def mutiply_numbers(a: int, b: int):
    """
    This function multiplies two numbers.
    """
    return a + b


def extract_employee_info(employee_list_df,name: str,department: str,certificate:str,id:int):
    """
    This function extracts the information of an employee and sort it into correct format, and updates the employee_list_df dataframe.
    """
    new_row = {'姓名': name, '工号': id, '部门': department, '学历': certificate} 
    employee_list_df.append(new_row, ignore_index=True)
    return employee_list_df

def eb_call(prompt, round):
    st.write(prompt)
    print('-' * 20,' Output ', '-'*20,"\n")

    response = chat_comp.do(
            model="ERNIE-Bot", 
            messages=[
                {"role": "user", "content": prompt},
                {"role": "assistant","content": "null", "function_call": {"name": "add_numbers", "arguments": "{ \"a\": \"114514\"}"}},
                {"role": "function", "name": "add_numbers", "content": "测试"}
                ],
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
                    "name": "mutiply_numbers",
                    "description": "This function multiplies two numbers.",
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
                },
                {
                    'name': 'extract_employee_info',
                    'description': 'Get the employee information from the body of the input text',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'name': {
                                'type': 'string',
                                'description': 'Name of the person'
                            },
                            'department': {
                                'type': 'string',
                                'description': 'Department the employee belongs to.'
                            },
                            'certificate': {
                                'type': 'string',
                                'description': 'The qualification or certificate that the employee holds.'
                            },
                            'id': {
                                'type': 'string',
                                'description': 'The id number of the employee. '
                            }
                            
                        }
                    }
                }
                ],
            stream="true"
            )


    st.write(response)
    return response

chat_comp = qianfan.ChatCompletion(ak="LrQvpiE6f4npsUwEvPL9vEWF", sk="CHTwBMVM0DlwyoGTLGEyRviBdctgOv4G")
prompt1 = "这两个数加起来是多少，42069420 和 6969420？"
prompt2 = "我叫Wenxin，你好"
prompt3 = "请问23乘109是多少"
prompt4 = "新入职员工李红在HR部门工作，她有研究生文凭。她的工号是918604"
prompt5 = "张三的工号是114514，他本科毕业，在技术部工作。请添加一下他的信息。"
prompt_list = [prompt1,prompt2,prompt3,prompt4,prompt5]


employee_list_df={}

for questions in prompt_list:
    response = eb_call(questions, round)
    st.write(response['result'])
    #response_message = response["choices"][0]["message"]

    if response.get('function_call'):
        # Which function call was invoked
        function_called = response_message['function_call']['name']
        
        # Extracting the arguments
        function_args  = json.loads(response_message['function_call']['arguments'])
        
        # Function names
        available_functions = {
            "say_hello": say_hello,
            "add_numbers": add_numbers,
            "mutiply_numbers": mutiply_numbers,
            "extract_employee_info": extract_employee_info
        }
        
        fuction_to_call = available_functions[function_called]
        response_message = fuction_to_call(*list(function_args .values()))
        
    else:
        #response_message = response_message['content']
        print("error")
    
    #print(f"\nSample#{i+1}\n")
    #print(response_message)

    st.write(employee_list_df)
