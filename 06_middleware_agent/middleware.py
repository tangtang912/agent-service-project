from typing import Callable
from langchain.agents import AgentState
from langchain.agents.middleware import wrap_tool_call, before_model, dynamic_prompt, ModelRequest
from langchain_core.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolCallRequest
from langgraph.runtime import Runtime
from langgraph.types import Command
from utils.logger_handle import logger
from utils.prompt_loader import load_report_prompts, load_system_prompts


@wrap_tool_call
def monitor_tool(
        request:ToolCallRequest,
        handler:Callable[[ToolCallRequest],ToolMessage | Command],
)->ToolMessage | Command:
    logger.info(f"[monitor tool]执行工具：{request.tool_call['name']}")
    logger.info(f"[monitor tool]执行工具：{request.tool_call['args']}")

    try:
        result = handler(request)
        logger.info(f"[monitor tool]工具：{request.tool_call['name']}调用成功")
        if request.tool_call['name'] == "fill_context_for_report":
            request.runtime.context["report"] = True

        return result
    except Exception as e:
        logger.info(f"[monitor tool]工具：{request.tool_call['name']}调用失败，原因：{str(e)}")
        raise e

@before_model
def log_before_model(
        state:AgentState,
        runtime:Runtime,
):
    logger.info(f"[log_before_model]即将调用模型，带有{len(state['messages'])}条消息")
    logger.debug(f"[log_before_model]{type(state['messages'][-1].__name__)} {state['messages'][-1].content.strip()}")

    return None

@dynamic_prompt
def report_prompt_switch(request:ModelRequest):
    is_report = request.runtime.context.get("report",False)
    if is_report:
        return load_report_prompts()
    return load_system_prompts()
