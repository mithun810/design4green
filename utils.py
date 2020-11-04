import models

def get_data(filters=None):
    Final_result=[]
    data={"commune":"","code_iris":0,"rank":0,"nom_iris":"","population":0}
    if filters:
        print("data")
    else:
        result=models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales=="Non").order_by(models.data_indexed.score_global_region).all()
        i=1
        for r in result:
            data["commune"]=r.Commune
            data["code_iris"]=r.code_iris
            data["rank"]=i
            data["nom_iris"]=r.nom_iris
            data["population"]=r.population
            data["score_global"]=r.score_global_region # filter based on Choix de Point Reference
            data["access_aux_interfaces_numeriques"]=r.access_aux_interfaces_numeriques_region # filter based on Choix de Point Reference
            data["access_al_information"]=r.access_al_information_region  # filter based on Choix de Point Reference
            data["competences_administative"]=r.competences_administative_region # filter based on Choix de Point Reference
            data["competence_numeriques"]=r.competence_numeriques_region # filter based on Choix de Point Reference
            data["global_access"]=r.global_access_region # filter based on Choix de Point Reference
            data["global_competence"]=r.global_competence_region # filter based on Choix de Point Reference
            i=i+1
            Final_result.append(data)
    # print("final\n",Final_result)
    return Final_result


def get_filters(filters=None):
    if filters:
        department=filters["department"]
        region=filters["region"]
        intercommunalities=filters["intercommunalities"]
        commune=filters["commune"]
        point_reference=filters["Choix de Point Reference"]
        infra_communales=filters["donnees infra-communales"]
        if commune == "All":
            filters["commune"]=[i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Commune).distinct().all()]
    else:
        filters={"region":[],"department":[],"intercommunalities":[],"commune":[],"Choix de Point Reference":[],"donnees infra-communales":[]}
        filters["region"]=[i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.region).distinct().all()]
        filters["department"]=[i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Department).distinct().all()]
        filters["intercommunalities"]=[i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.intercommunalite).distinct().all()]
        filters["commune"]=[i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Commune).distinct().all()]
        filters["Choix de Point Reference"]=["Tout","Region","Department","Intercommunalite"]
        filters["donnees infra-communales"]=["Oui","Non"]

    return filters