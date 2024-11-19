#from flask import Flask

#app = Flask (__name__)

#@app.route("/")
#def hello_world():
    #return "Hello, World!"

#if __name__ == "__main__":
    #app.run(debug=True)
   
   
#def write_email(name, greeting):
       #return f"""Hello{name}, {greeting}, I hope you are doing well...
   #Thanks for visiting my website!"""
   
#print(write_email)('Mathilde', 'Good morning')


#from flask import Flask, jsonify, request
#from openai import OpenAI

#api_key = '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'
#client = OpenAI(api_key=api_key)

#app =Flask(__name__)

#@app.route("/prompt")
#def prompt():
    #question = request.args.get('question')
    
    #completion = client.chat.completions.create(
       # model="gpt-4o"
       # messages= [
            #{"role": "system", "content": "You are a helpful assistant."}
            #["role": "user", "content": question]
    #]
    #)
    #data = {'name': 'David'}
    #return jsonify(data)

#if __name__ == "__main__":
    #app.run(debug=True)
    
from flask import Flask, jsonify, request
from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/prompt")
def prompt():
    question = request.args.get('question')
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user","content": question}
    ]
    )
    data = {'respone': completion.choices[0].message}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
