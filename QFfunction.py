import qianfan
import re
import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(123)


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
            model="ERNIE-Bot-turbo", 
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
                 ]
            )


    #st.write(response)
    return response

chat_comp = qianfan.ChatCompletion(ak="LrQvpiE6f4npsUwEvPL9vEWF", sk="CHTwBMVM0DlwyoGTLGEyRviBdctgOv4G")
prompt1 = "这两个数加起来是多少，42069420 和 6969420？"
prompt2 = "我叫Wenxin，你好"
prompt3 = "请问23乘109是多少"
prompt4 = "新入职员工李红在HR部门工作，她有研究生文凭。她的工号是918604"
prompt5 = "张三的工号是114514，他本科毕业，在技术部工作。请添加一下他的信息。"
prompt_list = [prompt1,prompt2,prompt3,prompt4,prompt5]
st.input()

employee_list_df={}

for questions in prompt_list:
    response = eb_call(questions, round)
    st.write(response['result'])

st.write(employee_list_df)
