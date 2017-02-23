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
			    "kombtare/nderkombtare" : form_data['Nr_total_linja_qira_ofruara_rrjete_tjera_1'],
	            "njesiaofruara":form_data['njesia_ofruara'],
	            "sasiaofruara":form_data['sasia_ofruara'],
				"komenteofruara":form_data['komente_ofruara']
		      },
		      "te_marra":{
			    "kombtare/nderkombtare2" : form_data['Nr_total_linja_qira_ofruara_rrjete_tjera_2'],
	            "temarranjesia":form_data['temarra_njesia'],
	            "temarrasasia":form_data['temarra_sasia'],
				"temarrakomente":form_data['temarra_komente']
			  }
	      },
		  "Kapaciteti_total":{ #hapi3
	               "llojet_kapacitetev_linjav_meqera_nrrjet":form_data['Kapaciteti_total_furnizimit_linjave_me_qira_ne_rrjet'],
	               "segmente_terminuese_":form_data['segmente_terminuese'],
	               "trunk_segmente_":form_data['trunk_segmente'],
	               "segment_nderkombetare_":form_data['segment_nderkombetare'],
	               "te_tjera_":form_data['te_tjera'],
	               "perkufizime_te_tjera_":form_data['perkufizime_te_tjera'],
	               "te_tjera_2_":form_data['te_tjera_2'],
	               "Perkufizime_2_te_tjera_":form_data['Perkufizime_2_te_tjera'],
	               "komente_":form_data['komentet']
	     },
		 "Llojet_e_Linjave_me_qira_shperndara_perdoruesit_pakice":{ #************hapi 4
			       "Linja_Analoge_me_qira":{
			            "Njesia": form_data['njesia_analoge'],
			            "10KM":form_data['10km_analoge'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_analoge'],
			            "51_deri_100km":form_data['51KM_deri_100km_analoge'],
			            "100km":form_data['100km_analoge'],
			            "komente":form_data['komente_analoge']
			      },
			       "Linja_digjitale":{
					    "Njesia": form_data['njesia_digjitale'],
			            "10KM":form_data['10km_digjitale'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_digjitale'],
			            "51_deri_100km":form_data['51KM_deri_100km_digjitale'],
			            "100km":form_data['100km_digjitale'],
			            "komente":form_data['komente_digjitale']
			      },
			      "Deri_ne_64_kbps":{
				        "Njesia": form_data['njesia_64kbps'],
			            "10KM":form_data['10km_64kbps'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_64kbps'],
			            "51_deri_100km":form_data['51KM_deri_100km_64kbps'],
			            "100km":form_data['100km_64kbps'],
			            "komente":form_data['komente_64kbps']
			     },
			     "64_kbps_deri_ne_2mbps":{
			            "Njesia": form_data['njesia_2mbps'],
			            "10KM":form_data['10km_2mbps'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_2mbps'],
			            "51_deri_100km":form_data['51KM_deri_100km_2mbps'],
			            "100km":form_data['100km_2mbps'],
			            "komente":form_data['komente_2mbps']
			      },
			    "2Mbits_deri_ne_34Mbps":{
			  	        "Njesia": form_data['njesia_34mbps'],
			            "10KM":form_data['10km_34mbps'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_34mbps'],
			            "51_deri_100km":form_data['51KM_deri_100km_34mbps'],
			            "100km":form_data['100km_34mbps'],
			            "komente":form_data['komente_34mbps']
			      },
			    "34Mbps_deri_140_MBPS": {
			            "Njesia": form_data['njesia_140mbps'],
			            "10KM":form_data['10km_140mbps'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_140mbps'],
			            "51_deri_100km":form_data['51KM_deri_100km_140mbps'],
			            "100km":form_data['100km_140mbps'],
			            "komente":form_data['komente_140mbps']
			      }
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
