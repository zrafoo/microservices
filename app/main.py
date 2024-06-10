from flask import Flask, Response, request
import requests,random
import redis
import html

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
default_requests_number='0'
limit=10000000


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    if request.method=='POST':
        requests_number = request.form.get('How_much_requests')
    if requests_number is not None:
        if 0<int(requests_number)<limit:
            for rid in range(0,int(requests_number)):        
                cache.set(rid,random.randint(0,100))
        
    return '''
             <form method="POST">
                 <div><label>Request number: <input type="text" name="How_much_requests"></label></div>
                 <input type="submit" value="Enter">
             </form>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
