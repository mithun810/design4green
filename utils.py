import models


def get_data(filters=None):
    Final_result=[]
    if filters:
        donnees=filters["donnees_infra_communales"]
        reference=filters["Choix_de_Point_Reference"]
        distinct_filter=[]
        if filters["change"] == "region" :
            region=[filters["region"]] if filters["region"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.region).distinct().all()]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Department).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region)).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region))
        elif filters["change"] == "department" :
            region=region=[filters["region"]] if filters["region"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.region).distinct().all()]
            department=[filters["department"]] if filters["department"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Department).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region)).distinct().all()]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.intercommunalite).filter(
            models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department)).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department))
        elif filters["change"] == "intercommunalities" :
            region=region=[filters["region"]] if filters["region"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.region).distinct().all()]
            department=[filters["department"]] if filters["department"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Department).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region)).distinct().all()]
            intercommunalities=[filters["intercommunalities"]] if filters["intercommunalities"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.intercommunalite).filter(
            models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department)).distinct().all()]
            distinct_filter = [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Commune).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities)).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities))
        elif filters["change"] == "commune" :
            region=region=[filters["region"]] if filters["region"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.region).distinct().all()]
            department=[filters["department"]] if filters["department"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Department).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region)).distinct().all()]
            intercommunalities=[filters["intercommunalities"]] if filters["intercommunalities"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.intercommunalite).filter(
            models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department)).distinct().all()]
            commune=[filters["commune"]] if filters["commune"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Commune).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities)).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities),models.data_indexed.Commune.in_(commune))
        else:
            region=region=[filters["region"]] if filters["region"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.region).distinct().all()]
            department=[filters["department"]] if filters["department"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(
            models.data_indexed.Department).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region)).distinct().all()]
            intercommunalities=[filters["intercommunalities"]] if filters["intercommunalities"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.intercommunalite).filter(
            models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department)).distinct().all()]
            commune=[filters["commune"]] if filters["commune"] != "ALL" else [i[0] for i in models.data_indexed.query.with_entities(models.data_indexed.Commune).filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities)).distinct().all()]
            result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == donnees,models.data_indexed.region.in_(region),models.data_indexed.Department.in_(department),models.data_indexed.intercommunalite.in_(intercommunalities),models.data_indexed.Commune.in_(commune))
        
        # "Tout", "Region", "Department", "Intercommunalite"]
        total_count=result.count()
        if reference == "Region":
            result = result.order_by(models.data_indexed.score_global_region.desc()).limit(100).offset(0).all()
        elif reference == "Department":
            result = result.order_by(models.data_indexed.score_global_department.desc()).limit(100).offset(0).all()
        elif reference == "Intercommunalities":
            result = result.order_by(models.data_indexed.score_global_intercommunalite.desc()).limit(100).offset(0).all()
        Final_result=[]
        i = 1
        for r in result:
            data = {}
            data["Nom Com"] = r.Commune
            data["Code Iris"] = r.code_iris
            data["Rank of ScoreGlobal"] = i
            data["Nom Iris"] = r.nom_iris
            data["Population"] = r.population
            
            if reference == "Region":
                data["Score Global"] = r.score_global_region
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_region
                data["Access Al_information_intercommunalite"] = r.access_al_information_region
                data["competences_administative_intercommunalite"] = r.competences_administative_region
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_region
                data["global_access_intercommunalite"] = r.global_access_region
                data["global_competence_intercommunalite"] = r.global_competence_region
            elif reference == "Department":
                data["Score Global"] = r.score_global_department
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_departement
                data["Access Al_information_intercommunalite"] = r.access_al_information_department
                data["competences_administative_intercommunalite"] = r.competences_administative_department
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_department
                data["global_access_intercommunalite"] = r.global_access_department
                data["global_competence_intercommunalite"] = r.global_competence_department
            elif reference == "Intercommunalities":
                data["Score Global"] = r.score_global_intercommunalite
                data["Acces Aux_interfaces_numeriques_intercommunalite"] = r.access_aux_interfaces_numeriques_intercommunalite
                data["Access Al_information_intercommunalite"] = r.access_al_information_intercommunalite
                data["competences_administative_intercommunalite"] = r.competences_administative_intercommunalite
                data["competence_numeriques_intercommunalite"] = r.competence_numeriques_intercommunalite
                data["global_access_intercommunalite"] = r.global_access_intercommunalite
                data["global_competence_intercommunalite"] = r.global_competence_intercommunalite
            i = i+1
            Final_result.append(data)
        filtered_result = dict()
        filtered_result["Final_result"] = Final_result
        filtered_result["distinct_filter"] = distinct_filter
        filtered_result["total_count"] = total_count
        return filtered_result
    else:
        result = models.data_indexed.query.filter(models.data_indexed.donnes_infra_communales == "Non").order_by(
            models.data_indexed.score_global_region.desc()).limit(100).offset(0).all()
        total_result_count = models.data_indexed.query.filter(
            models.data_indexed.donnes_infra_communales == "Non").count()
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
    all_filters = dict()
    all_filters["Final_result"] = Final_result
    filtered_result["total_count"] = total_result_count
    return all_filters


def get_filters(filters=None):
    if filters:
        department = filters["department"]
        region = filters["region"]
        intercommunalities = filters["intercommunalities"]
        commune = filters["commune"]
        point_reference = filters["Choix_de_Point_Reference"]
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
        filters["Choix_de_Point_Reference"] = [
            "Tout", "Region", "Department", "Intercommunalities"]
        filters["donnees_infra_communales"] = ["Oui", "Non"]

    return filters