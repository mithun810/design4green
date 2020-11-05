import models


def get_data(filters=None):
    Final_result=[]
    if filters:
        donnees=filters["donnees_infra_communales"]
        reference=filters["Choix de Point Reference"]
        distinct_filter=[]
        if filters["change"] == "region" :
            region=filters["region"]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Department).filter(models.data_indexed.region == region).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region == region)
        elif filters["change"] == "department" :
            region=filters["region"]
            department=filters["department"]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Department).filter(models.data_indexed.region == region,models.data_indexed.Department==department).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region == region,models.data_indexed.Department==department)
        elif filters["change"] == "intercommunalities" :
            region=filters["region"]
            department=filters["department"]
            intercommunalities=filters["intercommunalities"]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Department).filter(models.data_indexed.region == region,models.data_indexed.Department==department,models.data_indexed.intercommunalite==intercommunalities).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region == region,models.data_indexed.Department==department,models.data_indexed.intercommunalite==intercommunalities)
        elif filters["change"] == "commune" :
            region=filters["region"]
            department=filters["department"]
            intercommunalities=filters["intercommunalities"]
            commune=filters["commune"]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region == region,models.data_indexed.Department==department,models.data_indexed.intercommunalite==intercommunalities,models.data_indexed.Commune==commune)
        # "Tout", "Region", "Department", "Intercommunalite"]
        if reference == "Region":
            result = result.order_by(models.data_indexed.score_global_region.desc()).limit(100).offset(1*100).all()
        elif reference == "Department":
            result = result.order_by(models.data_indexed.score_global_department.desc()).limit(100).offset(1*100).all()
        elif reference == "Intercommunalite":
            result = result.order_by(models.data_indexed.score_global_intercommunalite.desc()).limit(100).offset(1*100).all()
        Final_result=[]
        i = 1
        for r in result:
            data = {}
            data["Nom Com"] = r.Commune
            data["Code Iris"] = r.code_iris
            data["Rank of ScoreGlobal"] = i
            data["Nom Iris"] = r.nom_iris
            data["Population"] = r.population
            data["geo_points_lat"]=r.geo_points.split(",")[0]
            data["geo_points_lon"]=r.geo_points.split(",")[1]
            if reference == "Region":
                data["Score Global"] = r.score_global_region
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_region
                data["Access Al_information_intercommunalite"] = r.access_al_information_region
                data["competences_administative_intercommunalite"] = r.competences_administative_region
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_region
                data["global_access_intercommunalite"] = r.global_access_region
                data["global_competence_intercommunalite"] = r.global_competence_region
            elif reference == "Department":
                data["Score Global"] = r.score_global_region
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_departement
                data["Access Al_information_intercommunalite"] = r.access_al_information_departement
                data["competences_administative_intercommunalite"] = r.competences_administative_departement
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_departement
                data["global_access_intercommunalite"] = r.global_access_departement
                data["global_competence_intercommunalite"] = r.global_competence_departement
            elif reference == "Intercommunalite":
                data["Score Global"] = r.score_global_region
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_intercommunalite
                data["Access Al_information_intercommunalite"] = r.access_al_information_intercommunalite
                data["competences_administative_intercommunalite"] = r.competences_administative_intercommunalite
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_intercommunalite
                data["global_access_intercommunalite"] = r.global_access_intercommunalite
                data["global_competence_intercommunalite"] = r.global_competence_intercommunalite
            i = i+1
            Final_result.append(data)
        return Final_result, distinct_filter
    else:
        result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == "Non").order_by(
            models.data_indexed.score_global_region.desc()).limit(100).offset(1*100).all()
        total_result_count = models.data_indexed.query.filter(
            models.data_indexed.donnes_infra_communales == "Non").count()
        print("total", total_result_count)
        i = 1
        for r in result:
            data = {}
            data["Nom Com"] = r.Commune
            data["Code Iris"] = r.code_iris
            data["Rank of ScoreGlobal"] = i
            data["Nom Iris"] = r.nom_iris
            data["Population"] = r.population
            data["geo_points_lat"]=r.geo_points.split(",")[0]
            data["geo_points_lon"]=r.geo_points.split(",")[1]
            # filter based on Choix de Point Reference
            data["Score Global"] = r.score_global_region
            # filter based on Choix de Point Reference
            data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_region
            # filter based on Choix de Point Reference
            data["Access Al_information_intercommunalite"] = r.access_al_information_region
            # filter based on Choix de Point Reference
            data["competences_administative_intercommunalite"] = r.competences_administative_region
            # filter based on Choix de Point Reference
            data["competence_numeriques_intercommunalite"] = r.competence_numeriques_region
            # filter based on Choix de Point Reference
            data["global_access_intercommunalite"] = r.global_access_region
            # filter based on Choix de Point Reference
            data["global_competence_intercommunalite"] = r.global_competence_region
            i = i+1
            Final_result.append(data)
    # print("final\n",Final_result)
    return Final_result


def get_filters(filters=None):
    if filters:
        department = filters["department"]
        region = filters["region"]
        intercommunalities = filters["intercommunalities"]
        commune = filters["commune"]
        point_reference = filters["Choix de Point Reference"]
        infra_communales = filters["donnees infra-communales"]
        if commune == "All":
            filters["commune"] = [i[0] for i in models.data_indexed.query.with_entities(
                models.data_indexed.Commune).distinct().all()]
    else:
        filters = {"region": [], "department": [], "intercommunalities": [], "commune": [
        ], "Choix de Point Reference": [], "donnees infra-communales": []}
        filters["region"] = [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.region).distinct().all()]
        filters["department"] = [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Department).distinct().all()]
        filters["intercommunalities"] = [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.intercommunalite).distinct().all()]
        filters["commune"] = [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Commune).distinct().all()]
        filters["Choix de Point Reference"] = [
            "Tout", "Region", "Department", "Intercommunalite"]
        filters["donnees_infra_communales"] = ["Oui", "Non"]

    return filters

if __name__ == '__main__':
    filters={"change":"region","region":"AUVERGNE RHONE ALPES","donnees_infra_communales":"Non","Choix de Point Reference":"Region"}
    data, dist_filters=get_data(filters)
    from pprint import pprint
    # pprint(data)
    print(dist_filters)