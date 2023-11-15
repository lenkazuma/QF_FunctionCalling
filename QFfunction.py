import qianfan
import streamlit as st
import json

def get_current_temperature(location: str, unit: str) -> dict:
    return {'temperature': 25, 'unit': '摄氏度'}

def extract_employee_info(name: str,department: str,certificate:str,id:int)-> dict:
    """
    This function extracts the information of an employee and sort it into correct format, and updates the employee_list_df dataframe.
    """
    #new_row = {name: str, department: str, certificate: str, id: str} 
    #employee_list_df.append(new_row, ignore_index=True)
    return {'result': True}

def delivery_inquiry(location: str, expect_price: int) -> dict:
    return {'id': 20, 'price': '50', 'food': '肯德基疯狂星期四'}

def delivery_order(id: str, food: str) -> dict:
    return {'result': True}


def eb_call(prompt,round,messages):
    st.write(prompt)
    st.write('-' * 20,' Output ', '-'*20,"\n")

    response = chat_comp.do(
        model="ERNIE-Bot", 
        messages=messages,
        temperature=0.000000001,
        functions=[
            {
                "name": "delivery_inquiry",
                "description": "查询商品",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "地址信息，包括街道、门牌号、城市、省份等信息"
                            },
                        "expect_price": {
                            "type": "int",
                            "description": "期望的价格"
                            }
                        },
                    "required": ["location"]
                    },
                "responses": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "商品id"
                            },
                        "price": {
                            "type": "int",
                            "description": "商品价格"
                            },
                        "food": {
                            "type": "string",
                            "description": "商品名称"
                            },
                        },
                    },
            },
            {
                "name": "delivery_order",
                "description": "外卖下单",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "商品id"
                            },
                        "food": {
                            "type": "string",
                            "description": "商品名称"
                            },
                        },
                    "required": ["id"]
                    },
                "responses": {
                    "type": "object",
                    "properties": {
                        "result": {
                            "type": "string",
                            "description": "是否下单成功"
                            },
                        }
                    },
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
                },
                "responses": {
                    "type": "object",
                    "properties": {
                        "result": {
                            "type": "string",
                            "description": "是否录入员工信息成功"
                            },
                        }
                    },
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
    )
    #st.write(response)
    return response

chat_comp = qianfan.ChatCompletion()

prompt2 = "南京路街道附近50元的午餐有哪些推荐？"
prompt3 = "肯德基疯狂星期四不错，就买这个20号的肯德基疯狂星期四了"
prompt4 = "新入职员工李红在HR部门工作，她有研究生文凭。她的工号是918604。"
prompt5 = "张三的工号是114514，他本科毕业，在技术部工作。"
prompt6 = "深圳市今天气温如何？"
prompt_list = [prompt2,prompt3,prompt4,prompt5,prompt6]

employee_list_df={}

round_no = 1

for questions in prompt_list:
    messages = [{"role": "user", "content": questions}]
    response = eb_call(questions,round,messages)
    st.write(response['result'])
    st.write(type(response))
    st.write(response.body)
    if hasattr(response.body,'function_call'):
        function_call = response['function_call']
        available_functions  = {'delivery_inquiry': delivery_inquiry,'delivery_order':delivery_order,'get_current_temperature':get_current_temperature,'extract_employee_info':extract_employee_info}
        fuction_to_call  = available_functions [function_call['name']]
        args = json.loads(function_call['arguments'])
        res = fuction_to_call (*list(args.values()))
        
        messages.append(
            {
                'role': 'assistant',
                'content': None,
                'function_call': function_call,
            }
        )
        messages.append(
            {
                'role': 'function',
                'name': function_call['name'],
                'content': json.dumps(res, ensure_ascii=False),
            }
        )
        st.write(messages)
        response = eb_call(questions,round,messages)
        st.write(response['result'])