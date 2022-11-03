from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Photographer',
    'location': 'Nawabi Road Haldwani, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Bar Tender',
    'location': 'Midway Bar, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Bike Mechanic',
    'location': 'Betalghat'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")
def hello_chutiyo():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Kumar-Ji-Careers')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)