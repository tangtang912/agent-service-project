import os ,hashlib
from utils.logger_handler import logger
from langchain.core.documents import Document
from langchain.community.document_loaders import PyPDFLoader,TextLoader


def get_file_md5_hex(filepath:str):

  if not os.path exists(filepath):
    logger.error(f"[md5计算]文件{filepath}不存在")
    return 

  if not os.path isfile(filepath):
    logger.error(f"[md5计算]路径{filepath}不是文件")
    return

  md5_obj = hashlib.md5()

  chunk_size = 4096
  try:
    with open (filepath,"rb")as f:
      while chunk := f.read(chunk_size):
        md5_obj.update(chunk)
        md5_hex = hexdigest()
  except Exception as e:
    logger.error(f"计算文件{filepath}md5失败，{str(e)})
    return None

def listdir_with_allowed_type(path:str,pathtype:tuple[str]):
  files = []

   if not os.path.isdir(path):
    logger.error(f"[listdir_with_allowed_type]{path}不是文件夹)
    return []

  for f in os.listdir(path):
    if f endwith (allowed_type):
      files append(os.path.join(path,f))

def pdf_loader(filepath:str,password:None)->list[Document]:
  return PyPDFLoader(filepath,password).load

def text_load(filepath:str)->list[Document]:
  return TextLoader(filepath).loader
