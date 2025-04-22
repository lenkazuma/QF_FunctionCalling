
# Python函数调用示例：Qianfan与Streamlit集成

本项目演示了如何将Qianfan ChatCompletion API与多个Python函数进行集成，执行例如查询员工信息、外卖订购和天气数据等任务。该应用使用Streamlit提供一个简单的Web界面，并通过Qianfan API处理和响应用户查询。

## 特性

- **函数调用**: 提供获取当前温度、外卖订购、员工信息提取等多个功能。
- **Streamlit界面**: 使用基本的Streamlit界面显示响应结果。
- **函数调用处理**: 根据Qianfan API的响应，调用相应的功能。

## 安装依赖

- Python 3.7+
- 安装所需的Python库：

```bash
pip install qianfan streamlit
```

## 如何运行

1. 克隆此仓库：

```bash
git clone https://github.com/your-username/qianfan-chat-function-demo.git
```

2. 进入项目目录：

```bash
cd qianfan-chat-function-demo
```

3. 运行Streamlit应用：

```bash
streamlit run app.py
```

4. 打开浏览器并访问 `http://localhost:8501` 与应用交互。

## 代码概览

### 主要功能

- **get_current_temperature**: 获取指定城市的当前气温。
  
  ```python
  def get_current_temperature(location: str, unit: str) -> dict:
      return {'temperature': 25, 'unit': '摄氏度'}
  ```

- **extract_employee_info**: 提取并记录员工信息。

  ```python
  def extract_employee_info(name: str, department: str, certificate: str, id: int) -> dict:
      return {'result': True}
  ```

- **delivery_inquiry**: 根据位置和预期价格查询外卖选项。

  ```python
  def delivery_inquiry(location: str, expect_price: int) -> dict:
      return {'id': 20, 'price': '50', 'food': '肯德基疯狂星期四'}
  ```

- **delivery_order**: 下单外卖。

  ```python
  def delivery_order(id: str, food: str) -> dict:
      return {'result': True}
  ```

### `eb_call` 函数

此函数处理调用Qianfan API，处理用户查询并根据API的响应调用相应的函数。

```python
def eb_call(prompt, round, messages):
    # API调用和响应处理代码
    return response
```

### 示例工作流程

1. **初始提示**: 应用接收用户的初始查询。
2. **函数调用**: 应用分析查询内容，决定调用哪个功能（例如天气、员工信息等）。
3. **执行函数**: 根据函数调用，应用执行相应的Python函数。
4. **返回响应**: 结果通过Streamlit显示。

### 示例提示

```python
prompt_list = [
    "114514+973580等于多少？",
    "南京路街道附近50元的午餐有哪些推荐？",
    "肯德基疯狂星期四不错，就买这个20号的肯德基疯狂星期四了",
    "新入职员工李红在HR部门工作，她有研究生文凭。她的工号是918604。",
    "张三的工号是114514，他本科毕业，在技术部工作。",
    "深圳市今天气温如何？"
]
```

### 期望的响应

- **调用函数**: 应用将显示调用的函数名称。
- **结果**: 调用结果（例如温度、外卖选项等）将通过Streamlit显示。

## 许可证

此项目遵循MIT许可证 - 详情请参阅[LICENSE](LICENSE)文件。
