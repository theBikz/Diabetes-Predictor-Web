from flask import Flask,render_template,url_for,request,redirect
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/git1')
def github():
    return redirect("https://github.com/theBikz/Sketch-to-Image-using-GANs-Keras")
@app.route('/git2')
def github2():
    return redirect("https://github.com/theBikz/Sketch-to-Image-Flask-Web-App")

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/mainpage',methods=['GET','POST'])
def mainpage():
    return render_template('mainpage.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    pregnancies = request.form.get('pregnancies')
    pregnancies = float(pregnancies)
    glucose = request.form.get('glucose')
    glucose = float(glucose)
    bp = request.form.get('bp')
    bp = float(bp)
    st = request.form.get('st')
    st = float(st)
    insulin = request.form.get('insulin')
    insulin = float(insulin)
    bmi = request.form.get('bmi')
    bmi = float(bmi)
    pedigree = request.form.get('pedigree')
    pedigree = float(pedigree)
    age = request.form.get('age')
    age = float(age)
    model = load_model('C:/Users/BIPIN/Desktop/diabetes/data/model.h5')
    Scalar = StandardScaler()
    data = [[pregnancies,glucose,bp,st,insulin,bmi,pedigree,age]]
    Scalar.fit(data)
    pred = model.predict(data)
    if(pred >0.5):
        diabetes = "It seems like you have Diabetes. Consult a Doctor soon."
    else:
        diabetes = "You have no Diabetes"
    return (render_template("view.html", diabetes = diabetes))


if __name__ == '__main__':
    app.run(debug=True)