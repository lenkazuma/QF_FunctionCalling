import qianfan
import streamlit as st
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

def get_current_temperature(location: str, unit: str) -> dict:
    return {'temperature': 25, 'unit': '摄氏度'}

def extract_employee_info(employee_list_df,name: str,department: str,certificate:str,id:int):
    """
    This function extracts the information of an employee and sort it into correct format, and updates the employee_list_df dataframe.
    """
    new_row = {'姓名': name, '工号': id, '部门': department, '学历': certificate} 
    employee_list_df.append(new_row, ignore_index=True)
    return employee_list_df




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
        "description": "打招呼并自我介绍。",
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
        'description': '将员工信息录入。',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': '姓名'
                },
                'department': {
                    'type': 'string',
                    'description': '部门'
                },
                'certificate': {
                    'type': 'string',
                    'description': '学历文聘'
                },
                'id': {
                    'type': 'string',
                    'description': '工号 '
                }
                
            }
        }
    },
    {
        'name': 'get_current_temperature',
        'description': "获取指定城市的气温",
        'parameters': {
            'type': 'object',
            'properties': {
                'location': {
                    'type': 'string',
                    'description': "城市名称",
                },
                'unit': {
                    'type': 'string',
                    'enum': [
                        '摄氏度',
                        '华氏度',
                    ],
                },
            },
            'required': [
                'location',
                'unit',
            ],
        },
        'responses': {
            'type': 'object',
            'properties': {
                'temperature': {
                    'type': 'integer',
                    'description': "城市气温",
                },
                'unit': {
                    'type': 'string',
                    'enum': [
                        '摄氏度',
                        '华氏度',
                    ],
                },
            },
        },
    }
]

def eb_call(prompt,round_no,functions,messages):
    st.write(prompt)
    st.write('-' * 20,' Output ', '-'*20,"\n")

    response = chat_comp.create(
            model="ERNIE-Bot", 
            messages = [{"role": "user", "content": prompt}],
            temperature=0.000000001,
            functions=functions
    )
    st.write(response)
    round_no+=1
    return response

chat_comp = qianfan.ChatCompletion()

prompt1 = "这两个数加起来是多少，42069420 和 6969420？"
prompt2 = "我叫Wenxin，你好"
prompt3 = "请问23乘109是多少"
prompt4 = "新入职员工李红在HR部门工作，她有研究生文凭。她的工号是918604。"
prompt5 = "张三的工号是114514，他本科毕业，在技术部工作。"
prompt6 = "深圳市今天气温如何？"
prompt_list = [prompt1,prompt2,prompt3,prompt4,prompt5,prompt6]


employee_list_df={}

round_no = 1

for questions in prompt_list:
    response = eb_call(questions,round_no,functions,messages)
    st.write(response['result'])

    import json

    if hasattr(response, 'function_call'):
        function_call = response.function_call
        name2function = {'get_current_temperature': get_current_temperature}
        func = name2function[function_call['name']]
        args = json.loads(function_call['arguments'])
        res = func(location=args['location'], unit=args['unit'])

        st.write(employee_list_df)
        
