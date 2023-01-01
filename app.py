from flask import Flask, render_template, url_for, request, flash
app = Flask(__name__)
app.secret_key = 'ezclap'

s = ""
n = ""
b = ""
nkk = ""

def binary_to_polynomial(binary):
    polynomial = ""
    for i, digit in enumerate(binary[::-1]):
        if digit == "1":
            if i == 0:
                polynomial += "1"
            elif i == 1:
                polynomial += "x"
            else:
                polynomial += "x^{}".format(i)
            if i != len(binary)-1:
                polynomial += "+"
    return polynomial

@app.route('/crc')
def index():
    return render_template('index.html')

@app.route('/result', methods =["GET", "POST"])
def result():
    
    if "1st" in request.form:
        #-------------------------------------------
        global s
        s=str(request.form['kod'])
        flash('Zadaná binární zpráva: {}'.format(s))
        global n
        n=list(str(request.form['nk']).split(","))
        k=[eval(i) for i in n]
        global nkk
        nkk=k[0]-k[1]
        global b
        b=str(request.form['gp'])
        flash('Zadaný generujicí polynom: {}'.format(b))
        a=s
        a=a+nkk*'0'
        print(a)

        while True:
            c=len(a)-len(b)
            if len(b) < len(a):
                b=b+c*'0'
            print(b)
            print(len(a)*'-')
            y=int(a,2) ^ int(b,2)
            if len(b) >= len(a):
                b=b.rstrip('0')
            a=format(y,'b')
            print(a)
            if len(a) <= nkk:
                break

        if len(a) < nkk:
            e=nkk-len(a)
            z=e*'0'+a
        else:
            z=a

        print("z je:",z)
        flash("Zabezpečující část: {}".format(z))
        v=s+z
        print("v je:",v)
        flash("Zabezpečená zpráva: {}".format(v))
        polynomial1 = binary_to_polynomial(v)
        flash('Zabezpečená zpráva ve formě polynomu: {}'.format(polynomial1))
        #-------------------------------------------
        # return render_template('index.html')
    
    elif "2nd" in request.form:
        #-------------------------------------------
        flash('Zadaná binární zpráva: {}'.format(s))
        flash('Zadaný generujicí polynom: {}'.format(b))
        a=s
        a=a+nkk*'0'
        print(a)

        while True:
            c=len(a)-len(b)
            if len(b) < len(a):
                b=b+c*'0'
            print(b)
            print(len(a)*'-')
            y=int(a,2) ^ int(b,2)
            if len(b) >= len(a):
                b=b.rstrip('0')
            a=format(y,'b')
            print(a)
            if len(a) <= nkk:
                break

        if len(a) < nkk:
            e=nkk-len(a)
            z=e*'0'+a
        else:
            z=a

        print("z je:",z)
        flash("Zabezpečující část je: {}".format(z))
        v=s+z
        print("v je:",v)
        flash("Zabezpečená zpráva je: {}".format(v))
        polynomial1 = binary_to_polynomial(v)
        flash('Zabezpečená zpráva ve formě polynomu: {}'.format(polynomial1))
        ch=str(request.form['err'])
        print("ch je:",ch)
        flash('Chybná zpráva: {}'.format(ch))
        polynomial2 = binary_to_polynomial(ch)
        flash('Chybná zpráva ve formě polynomu: {}'.format(polynomial2))

        while True:
            c=len(ch)-len(b)
            if len(b) < len(ch):
                b=b+c*'0'
            print(b)
            print(len(ch)*'-')
            y=int(ch,2) ^ int(b,2)
            if len(b) >= len(ch):
                b=b.rstrip('0')
            ch=format(y,'b')
            print(ch)
            if len(ch) <= nkk:
                break

        print('Tady zaciname:')
        i=len(b)-1
        h='1'+i*'0'

        while True:
            # if ch == '100':
            #     print('na pozici 3 byla chyba')
            #     break
            # elif ch == '10':
            #     print('na pozici 2 byla chyba')
            #     break
            # elif ch == '1':
            #     print('na pozici 1 byla chyba')
            #     break
            print(h)
            c=len(h)-len(b)
            if len(b) < len(h):
                b=b+c*'0'
            print(b)
            print(len(h)*'-')
            y=int(h,2) ^ int(b,2)
            if len(b) >= len(h):
                b=b.rstrip('0')
            h=format(y,'b')
            print(h)
            if h == ch:
                print('Chyba byla na pozici: {}'.format(i+1))
                flash('Chyba byla na pozici: {}'.format(i+1))
                break
            if i == len(v)-1:
                print('Přenos proběhl bez chyby')
                flash('Přenos proběhl bez chyby')
                break
            if len(h) <= nkk:
                i += 1
                h='1'+i*'0'
        #-------------------------------------------

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)