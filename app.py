from flask import Flask,jsonify,request,render_template
app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        carat=request.form.get('carat')
        table=request.form.get('table')
        xxx=request.form.get('x')
        yyy=request.form.get('y')
        zzz=request.form.get('z')
        color_encoded=request.form.get('color_encoded')
        print(carat,table,xxx,yyy,zzz,color_encoded)
        return render_template('success.html',data={'Diamond Price':87897})
    else:
        return render_template('predict.html')





if __name__=='__main__':
    app.run()

