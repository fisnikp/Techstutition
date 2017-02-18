from flask import Blueprint, render_template, request, redirect, url_for, Response
from app import mongo
from bson import ObjectId

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
		     "infraskrtuktura_rrjetit":{
	            "deri_ne_dhe_perfshire_64Kb/s":{
	               "segmente_terminuese":form_data['segmente_terminuese'],
	               "trunk_segmente":form_data['trunk_segmente'],
	               "segment_nderkombetare":form_data['segment_nderkombetare'],
	               "te_tjera":form_data['te_tjera'],
	               "perkufizime_te_tjera":form_data['perkufizime_te_tjera'],
	               "te_tjera_2":form_data['te_tjera_2'],
	               "Perkufizime_2_te_tjera":form_data['"Perkufizime_2_te_tjera'],
	               "Komente":form_data['"Perkufizime_2_te_tjera']
	            },
	            "deri_dhe_perfshire_2Mb/s":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "Deri_ne_dhe_përfshire_34Mb/s":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "140_Mbps":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "STM_1":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "STM_16":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "STM_64":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            },
	            "STM_tjera":{
	               "segmente_terminuese":"",
	               "trunk_segmente":"",
	               "segment_nderkombetare":"",
	               "te_tjera":"",
	               "perkufizime_te_tjera":"",
	               "te_tjera_2":"",
	               "Përkufizime_2_te_tjera":"",
	               "Komente":""
	            }
			 }

		}
		db.insert(form_data)
		return render_template("formulari.html", mesazhi="Falemderit, forma u plotesua" )

	else:
		return "Go Home, you are Drunk"

@mod_main.route('/list', methods=["GET"])
def list():
	db = mongo.db.arkep
	rekordet = db.find()
	return 	render_template('list.html', rekordet=rekordet)


@mod_main.route('/remove/<string:remove_id>', methods=["POST"])
def remove(remove_id):
	db = mongo.db.arkep
	remove = db.remove({"_id": ObjectId(remove_id)})
	return Response(200)

@mod_main.route('/raporti/<string:report_id>')
def raporti(report_id):
	db = mongo.db.arkep
	report=db.find_one({"_id": ObjectId(report_id)})
	return render_template('raporti.html', report=report)
