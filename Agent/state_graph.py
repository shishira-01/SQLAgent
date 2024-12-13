builder = StateGraph(State)

builder.add_node('assistant', assistant)
builder.add_node('tools', ToolNode(tools=tools))

builder.add_edge(START, 'assistant')
builder.add_conditional_edges('assistant', tools_condition)
builder.add_edge('tools', 'assistant')

graph = builder.compile()