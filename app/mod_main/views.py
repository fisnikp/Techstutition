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
		  "data_plotesimit_formularit":{
		      "tremujori":form_data['tremujori'],
			  "i_vitit":form_data['ivitit'],
		   	  "peridudhaprej":form_data['periudhaprejj'],
			  "peiudhaderi":form_data['peridudhaderime']
 		  },
          "nderrmarja":{
            "emri":form_data['emri_ndermarrjes'],
            "numri_regjistrimi":form_data['nr_regjistrimit'],
            "adresa":form_data['adresa'],
            "personi_kontaktues":form_data['personi_kontaktues'],
            "telefoni":form_data['telefoni'],
            "email":form_data['email'],
          },#******hapi-2*************
		   "linjat_me_qera":{
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
	      }, #*********hapi3***********
		  "Kapaciteti_total":{
	               "llojet_kapacitetev_linjav_meqera_nrrjet":form_data['Kapaciteti_total_furnizimit_linjave_me_qira_ne_rrjet'],
	               "segmente_terminuese_":form_data['segmente_terminuese'],
	               "trunk_segmente_":form_data['trunk_segmente'],
	               "segment_nderkombetare_":form_data['segment_nderkombetare'],
	               "te_tjera_":form_data['te_tjera'],
	               "perkufizime_te_tjera_":form_data['perkufizime_te_tjera'],
	               "te_tjera_2_":form_data['te_tjera_2'],
	               "Perkufizime_2_te_tjera_":form_data['Perkufizime_2_te_tjera'],
	               "komente_":form_data['komentet']
	     }, #************hapi 4******
		 "Llojet_e_Linjave_me_qira_shperndara_perdoruesit_pakice":{
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
			     "34Mbps_deri_140_MBPS":{
			            "Njesia": form_data['njesia_140mbps'],
			            "10KM":form_data['10km_140mbps'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_140mbps'],
			            "51_deri_100km":form_data['51KM_deri_100km_140mbps'],
			            "100km":form_data['100km_140mbps'],
			            "komente":form_data['komente_140mbps']
			      },
				  "140_Mbps": {
  			            "Njesia": form_data['njesia140mbps'],
  			            "10KM":form_data['10km140mbps'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km140mbps'],
  			            "51_deri_100km":form_data['51KM_deri_100km140mbps'],
  			            "100km":form_data['100km140mbps'],
  			            "komente":form_data['komente140mbps']
  			      },
				  "stm_1": {
  			            "Njesia": form_data['njesia_stm1'],
  			            "10KM":form_data['10km_stm1'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm1'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm1'],
  			            "100km":form_data['100km_stm1'],
  			            "komente":form_data['komente_stm1']
  			      },
				  "stm_16": {
  			            "Njesia": form_data['njesia_stm16'],
  			            "10KM":form_data['10km_stm16'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm16'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm16'],
  			            "100km":form_data['100km_stm16'],
  			            "komente":form_data['komente_stm16']
  			      },
				  "stm_64": {
  			            "Njesia": form_data['njesia_stm64'],
  			            "10KM":form_data['10km_stm64'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm64'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm64'],
  			            "100km":form_data['100km_stm64'],
  			            "komente":form_data['komente_stm64']
  			      },
				  "linja_tjera_meqera_ofruara": {
  			            "Njesia": form_data['njesia_meqera'],
  			            "10KM":form_data['10km_meqera'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_meqera'],
  			            "51_deri_100km":form_data['51KM_deri_100km_meqera'],
  			            "100km":form_data['100km_meqera'],
  			            "komente":form_data['komente_meqera']
  			      }
		 }, #************hapi 5*****************
		 "Llojet_e_Linjave_me_qira_shperndara_perdoruesit_shumice":{
			       "Linja_Analoge_me_qira_shumice":{
			            "Njesia": form_data['njesia_analoge_shumice'],
			            "10KM":form_data['10km_analoge_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_analoge_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_analoge_shumice'],
			            "100km":form_data['100km_analoge_shumice'],
			            "komente":form_data['komente_analoge_shumice']
			      },
			       "Linja_digjitale_shumice":{
					    "Njesia": form_data['njesia_digjitale_shumice'],
			            "10KM":form_data['10km_digjitale_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_digjitale_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_digjitale_shumice'],
			            "100km":form_data['100km_digjitale_shumice'],
			            "komente":form_data['komente_digjitale_shumice']
			      },
			      "Deri_ne_64_kbps_shumice":{
				        "Njesia": form_data['njesia_64kbps_shumice'],
			            "10KM":form_data['10km_64kbps_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_64kbps_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_64kbps_shumice'],
			            "100km":form_data['100km_64kbps_shumice'],
			            "komente":form_data['komente_64kbps_shumice']
			     },
			     "64_kbps_deri_ne_2mbps_shumice":{
			            "Njesia": form_data['njesia_2mbps_shumice'],
			            "10KM":form_data['10km_2mbps_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_2mbps_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_2mbps_shumice'],
			            "100km":form_data['100km_2mbps_shumice'],
			            "komente":form_data['komente_2mbps_shumice']
			      },
			      "2Mbits_deri_ne_34Mbps_shumice":{
			  	        "Njesia":form_data['njesia_34mbps_shumice'],
			            "10KM":form_data['10km_34mbps_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_34mbps_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_34mbps_shumice'],
			            "100km":form_data['100km_34mbps_shumice'],
			            "komente":form_data['komente_34mbps_shumice']
			      },
			     "34Mbps_deri_140_MBPS_shumice":{
			            "Njesia": form_data['njesia_140mbps_shumice'],
			            "10KM":form_data['10km_140mbps_shumice'],
			            "10KM_deri_50km":form_data['10KM_deri_50km_140mbps_shumice'],
			            "51_deri_100km":form_data['51KM_deri_100km_140mbps_shumice'],
			            "100km":form_data['100km_140mbps_shumice'],
			            "komente":form_data['komente_140mbps_shumice']
			      },
				  "140_Mbps_shumice": {
  			            "Njesia": form_data['njesia140mbps_shumice'],
  			            "10KM":form_data['10km140mbps_shumice'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km140mbps_shumice'],
  			            "51_deri_100km":form_data['51KM_deri_100km140mbps_shumice'],
  			            "100km":form_data['100km140mbps_shumice'],
  			            "komente":form_data['komente140mbps_shumice']
  			      },
				  "stm_1_shumice": {
  			            "Njesia": form_data['njesia_stm1_shumice'],
  			            "10KM":form_data['10km_stm1_shumice'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm1_shumice'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm1_shumice'],
  			            "100km":form_data['100km_stm1_shumice'],
  			            "komente":form_data['komente_stm1_shumice']
  			      },
				  "stm_16_shumice": {
  			            "Njesia": form_data['njesia_stm16_shumice'],
  			            "10KM":form_data['10km_stm16_shumice'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm16_shumice'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm16_shumice'],
  			            "100km":form_data['100km_stm16_shumice'],
  			            "komente":form_data['komente_stm16_shumice']
  			      },
				  "stm_64_shumice": {
  			            "Njesia": form_data['njesia_stm64_shumice'],
  			            "10KM":form_data['10km_stm64_shumice'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_stm64_shumice'],
  			            "51_deri_100km":form_data['51KM_deri_100km_stm64_shumice'],
  			            "100km":form_data['100km_stm64_shumice'],
  			            "komente":form_data['komente_stm64_shumice']
  			      },
				  "linja_tjera_meqera_ofruara_shumice": {
  			            "Njesia": form_data['njesia_meqera_shumice'],
  			            "10KM":form_data['10km_meqera_shumice'],
  			            "10KM_deri_50km":form_data['10KM_deri_50km_meqera_shumice'],
  			            "51_deri_100km":form_data['51KM_deri_100km_meqera_shumice'],
  			            "100km":form_data['100km_meqera_shumice'],
  			            "komente":form_data['komente_meqera_shumice']
  			      }
		 },#*********************Hapi 6***************
		 "te_ardhuratnga_linjat_me_qera":{
		         "te_ardhurat_nga_sherbimet_me_pakice":{
			            "euro":form_data['euro_ardhurat_pakice'],
				        "komente":form_data['komente_ardhurat_pakice']
		          },
                  "te_ardhurat_nga_sherbimet_me_shumice": {
					    "euro":form_data['euro_ardhurat_shumice'],
					    "komente":form_data['komente_ardhurat_shumice']
                  },
                 "te_ardhurat_nga_sherbimet_totali": {
					    "euro":form_data['euro_ardhurat_totali'],
					    "komente":form_data['komente_ardhurat_totali']
                  }
         },#**********************hapi 7******************
		 "tarifat_e_linjav_me_qera_pakice":{
                "2mbps-2km":{
                        "euro":form_data['euro_tarifat_2mbps_2km_pakice'],
                        "Komente":form_data['komente_tarifat_2mbps_2km_pakice']
                },
                "34mbps-2km":{
                        "euro":form_data['euro_tarifat_34mbps_2km_pakice'],
                        "Komente":form_data['komente_tarifat_34mbps_2km_pakice']
                },
                "2mbps-50":{
                        "euro":form_data['euro_tarifat_2mbps_50_pakice'],
                        "Komente":form_data['komente_tarifat_2mbps_50_pakice']
                },
                "34mbps-50":{
                        "euro":form_data['euro_tarifat_34mbps_50_pakice'],
                        "Komente":form_data['komente_tarifat_34mbps_50_pakice']
                },
                "2mbps-kufi":{
                        "euro":form_data['euro_tarifat_2mbps_kufi_pakice'],
                        "Komente":form_data['komente_tarifat_2mbps_kufi_pakice']
                },
                "34mbps-kufi":{
                        "euro":form_data['euro_tarifat_34mbps_kufi_pakice'],
                        "Komente":form_data['komente_tarifat_34mbps_kufi_pakice']
                },
                "2mbps-UK":{
                        "euro":form_data['euro_tarifat_2mbps_UK_pakice'],
                        "Komente":form_data['komente_tarifat_2mbps_UK_pakice']
                },
                "34mbps-deri-UK":{
                        "euro":form_data['euro_tarifat_34mbps_UK_pakice'],
                        "Komente":form_data['komente_tarifat_34mbps_UK_pakice']
                }
        },#**********************hapi8******************
		"tarifat_e_linjav_me_qera_shumice":{
			   "2mbps-2km":{
					   "euro":form_data['euro_tarifat_2mbps_2km_shumice'],
					   "Komente":form_data['komente_tarifat_2mbps_2km_shumice']
			   },
			   "34mbps-2km":{
					   "euro":form_data['euro_tarifat_34mbps_2km_shumice'],
					   "Komente":form_data['komente_tarifat_34mbps_2km_shumice']
			   },
			   "2mbps-50":{
					   "euro":form_data['euro_tarifat_2mbps_50_shumice'],
					   "Komente":form_data['komente_tarifat_2mbps_50_shumice']
			   },
			   "34mbps-50":{
					   "euro":form_data['euro_tarifat_34mbps_50_shumice'],
					   "Komente":form_data['komente_tarifat_34mbps_50_shumice']
			   },
			   "2mbps-kufi":{
					   "euro":form_data['euro_tarifat_2mbps_kufi_shumice'],
					   "Komente":form_data['komente_tarifat_2mbps_kufi_shumice']
			   },
			   "34mbps-kufi":{
					   "euro":form_data['euro_tarifat_34mbps_kufi_shumice'],
					   "Komente":form_data['komente_tarifat_34mbps_kufi_shumice']
			   },
			   "2mbps-UK":{
					   "euro":form_data['euro_tarifat_2mbps_UK_shumice'],
					   "Komente":form_data['komente_tarifat_2mbps_UK_shumice']
			   },
			   "34mbps-deri-UK":{
					   "euro":form_data['euro_tarifat_34mbps_UK_shumice'],
					   "Komente":form_data['komente_tarifat_34mbps_UK_shumice']
			   }
	   },#**********************hapi9****************
	   "Detaje_te_linjave_me_qera_teperdorura_tedhena":{
			   "9_1":{
					   "kapaciteti":form_data['detaje_kapaciteti_9_1'],
					   "tipi_kombetare/nderkombetare":form_data['detaje_kombetare_nderkombetare_9_1'],
			           "operatori_furnizues_emri_operatorit":form_data['detaje_emri_9_1'],
			           "lloji_pageses":form_data['detaje_pagesa_9_1'],
			           "euro":form_data['detaje_euro_9_1'],
				       "komente":form_data['detaje_komente_9_1']
			   },
			   "9_2":{
					   "kapaciteti":form_data['detaje_kapaciteti_9_2'],
					   "tipi_kombetare/nderkombetare":form_data['detaje_kombetare_nderkombetare_9_2'],
			           "operatori_furnizues_emri_operatorit":form_data['detaje_emri_9_2'],
			           "lloji_pageses":form_data['detaje_pagesa_9_2'],
			           "euro":form_data['detaje_euro_9_2'],
				       "komente":form_data['detaje_komente_9_2']
	           },
			   "9_3":{
					   "kapaciteti":form_data['detaje_kapaciteti_9_3'],
					   "tipi_kombetare/nderkombetare":form_data['detaje_kombetare_nderkombetare_9_3'],
			           "operatori_furnizues_emri_operatorit":form_data['detaje_emri_9_3'],
			           "lloji_pageses":form_data['detaje_pagesa_9_3'],
			           "euro":form_data['detaje_euro_9_3'],
				       "komente":form_data['detaje_komente_9_3']
	           },
			   "9_4_pagesa_totale":{
					   "kapaciteti":form_data['detaje_kapaciteti_9_4'],
					   "tipi_kombetare/nderkombetare":form_data['detaje_kombetare_nderkombetare_9_4'],
			           "operatori_furnizues_emri_operatorit":form_data['detaje_emri_9_4'],
			           "lloji_pageses":form_data['detaje_pagesa_9_4'],
			           "euro":form_data['detaje_euro_9_4'],
				       "komente":form_data['detaje_komente_9_4']
	           }

       },
	   "data_plotesimit_formularit_fund":{
		       "data_fund":form_data['data_fund'],
		       "emridorezuesit":form_data['emri_dorezuesit']
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
