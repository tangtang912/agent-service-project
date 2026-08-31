"""
总结服务类：用户提问，搜索参考资料，将提问和参考资料提交给模型，让模型总结回复
"""

from rag.vector_store import VectorStoreService
from langchain_core.document import Document
from langchain_core.output.parser import StrOutputParser
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model_factory import chat_model

class RagSummarizeService(object):
  self.vector_store = VectorStoreService()
  self.retriever = self.vector_store.get_retriever()
  self.prompt_text = load_rag_prompts()
  self.template_prompt= PromptTemplate.from_template(self.prompt_text)
  self.model = chat_model
  self.chain = self.__init__chain

def __init__chain(self):
  chain = self.prompt_template | chat_model | StrOutputParser()
  return chain

def retriever_docs(self,query:str) ->list[Document]:
  return self.retriver.invoke(query)

def rag_summarize(self,query:str) ->str:

  context_docs = self.retriever_docs(query)
  context = ""
  counter = 0
  for doc in context_docs:
    counter += 1
    context = f"[参考资料{counter}:参考资料:{doc.page_content} | 参考元数据：{doc.metadata}\n"
    return self.chain.invoke(
      {
        "input":query,
        "context":context,
      }
    )

if __name__ == '__main__':
  rag = RagSummarizeService()
  print(rag.rag_summarize("小户型适合什么扫地机器人")
        

  
  




