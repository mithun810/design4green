import models


def get_data(filters=None):
    if filters:
        if filters["region"]["status"] is True:
            regions = models.data_indexed.query.filter(
                models.data_indexed.region == filters["region"]["name"]).distinct().all()
            dept_filters = []
            for reg in regions:
                dept_filters.append(reg.Department)
            return dept_filters
        elif filters["department"]["status"] is True:
            departments = models.data_indexed.query.filter(
                models.data_indexed.region == filters["department"]["name"]).distinct().all()
            int_comms_filters = []
            for int_comm in departments:
                int_comms_filters.append(int_comm.intercommunalite)
            return int_comms_filters
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
        filters["donnees infra-communales"] = ["Oui", "Non"]

    return filters
