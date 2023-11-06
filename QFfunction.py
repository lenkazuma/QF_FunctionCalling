import qianfan
import re
import streamlit as st

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
                   }
                 ]
            )


    st.write(response)
    return response

chat_comp = qianfan.ChatCompletion(ak="LrQvpiE6f4npsUwEvPL9vEWF", sk="CHTwBMVM0DlwyoGTLGEyRviBdctgOv4G")
prompt = "百度大厦-北京海淀区上地十街10号的附近，午餐有哪些推荐？###能不能帮我点一个20元以内的？###"
prompt_list = re.split(r"###", prompt)

for questions in prompt_list:
    response = eb_call(questions, round)
    st.write(response['result'])
