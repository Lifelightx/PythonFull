from flask import Flask, request, render_template, redirect, url_for
import pywhatkit as wpkit
import threading

app = Flask(__name__)
  # Required for flash messages

def send_message(phone, msg):
    try:
        wpkit.sendwhatmsg_instantly(
            phone_no=phone,
            message=msg,
            wait_time=20,
            tab_close=True,
            close_time=1
        )
        
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wpmsg', methods=['POST'])
def wpmsg():
    if request.method == 'POST':
        phone = request.form['phone']
        msg = request.form['msg']

        
        if not phone or not msg: 
            return redirect(url_for('home'))


        if not phone.startswith("+") or len(phone) < 10:
            return redirect(url_for('home'))
        thread = threading.Thread(target=send_message, args=(phone, msg))
        thread.start()

        
        return redirect(url_for('home'))

    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
