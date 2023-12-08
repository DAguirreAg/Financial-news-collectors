from fastapi import FastAPI
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from starlette.responses import RedirectResponse

def execute_notebook(filename):

    with open(filename) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
        
    ep = ExecutePreprocessor(timeout=None, kernel_name='python')
    nb_out = ep.preprocess(nb_in)

app = FastAPI()

@app.get("/")
def main():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/download_webpages")
def download_webpages():
    filename = 'webpage_downloader.ipynb'
    execute_notebook(filename)
    return None

@app.get("/etl_bbc")
def etl_bbc():
    filename = 'etl_bbc.ipynb'
    execute_notebook(filename)
    return None