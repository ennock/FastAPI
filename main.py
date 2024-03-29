from fastapi import FastAPI


app = FastAPI()

@app.get('/')

def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')

def unpublished():
    return {'data':'unpublished blogs'}
        
    

@app.get('/about')
def about():
    return {'data':{'about page'}}