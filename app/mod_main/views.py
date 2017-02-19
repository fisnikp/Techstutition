from flask import Blueprint, render_template, request, redirect, url_for, Response
from app import mongo
from bson import ObjectId
from bson.json_util import dumps

mod_main = Blueprint('main', __name__)


@mod_main.route('/')
def index():
	db = mongo.db.arkep
	return render_template("index.html")

@mod_main.route('/formulari', methods=['GET', 'POST'])
def form():

	if request.method == 'GET':
		return render_template("formulari.html")
	elif request.method == 'POST':
		db = mongo.db.arkep
		form_data = request.form.to_dict()
		print form_data
		data = {
          "nderrmarja":{
            "emri":form_data['emri_ndermarrjes'],
            "numri_regjistrimi":form_data['nr_regjistrimit'],
            "adresa":form_data['adresa'],
            "personi_kontaktues":form_data['personi_kontaktues'],
            "telefoni":form_data['telefoni'],
            "email":form_data['email'],
          },
		   "linjat_me_qera":{ #hapi-2
		      "ofruara":{
		         "kombtare":{
		            "njesia":form_data['njesia_kombetare'],
		            "sasia":form_data['sasia_kombetare'],
					"komente":form_data['komente_kombetare']
		         }

		      },
		      "te_marra":{
		         "kombtare":{
		            "njesia":form_data['temarra_njesia_kombetare'],
		            "sasia":form_data['temarra_sasia_kombetare'],
					"komente":form_data['temarra_komente_kombetare']
		         }
			  }
	      },
			 "data_plotesimit_formularit":{
		  		"tremujori":form_data['tremujori'],
				"i_vitit":form_data['ivitit'],
				"peridudhaprej":form_data['periudhaprejj'],
				"peiudhaderi":form_data['peridudhaderime']
		     }
	 }
		db.insert(data)
		return render_template("formulari.html", mesazhi="Falemderit, forma u plotesua" )

	else:
		return "Go Home, you are Drunk"

@mod_main.route('/list', methods=["GET"])
def list():
	db = mongo.db.arkep
	rekordet = db.find()
	return 	render_template('list.html', rekordet=rekordet)


@mod_main.route('/remove/<string:remove_id>', methods=['POST'])
def remove(remove_id):
    db = mongo.db.arkep
    remove = db.remove({"_id" : ObjectId(remove_id)})
    if remove['n'] == 1:
        return Response(response=dumps({"removed": True}),
        status=200,
        mimetype='application/json')
    else:
        return Response(response=dumps({"removed": False}),
        status=500,
        mimetype='application/json')

@mod_main.route('/raporti/<string:report_id>')
def raporti(report_id):
	db = mongo.db.arkep
	report=db.find_one({"_id": ObjectId(report_id)})
	return render_template('raporti.html', report=report)
