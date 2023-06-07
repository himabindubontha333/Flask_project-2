from flask import Flask
FAI=Flask(__name__)
@FAI.route('/wish/<Kanna>/')
def wish(Kanna):
    return f'Hello,How are you {Kanna}'
if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.43.92')

