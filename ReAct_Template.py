# References:
# https://smith.langchain.com/hub/hwchase17/react-chat
# https://smith.langchain.com/hub/hwchase17/structured-chat-agent

STRING_PROMPT_TEMPLATE = """
{system_message}. You have access to the following tools:

{tool_details}

Respond to the the user with the right tool and input whenever is needed.
Use a json blob to specify a tool by providing a name key (tool name) and an arguments key (tool input).

Valid "action" values:  {tool_names}

Provide only ONE action per $JSON_BLOB, as shown:
```
{{
    "name": $TOOL_NAME,
    "arguments": $INPUT
}}
```

Follow this format:

Question: input question to answer
Thought: reasoning about previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond as final answer. Using tool to provide final answer
Final Answer: Final response to human

Remember to ALWAYS respond with a valid json blob of a single action when a tool MUST be used.
Use tools if necessary. Respond directly if appropriate.
Format is Action:```$JSON_BLOB```then Observation'

Previous conversation history:
{chat_history}

New conversation:
Question: {user_input}
Thought: {react_loop}
"""