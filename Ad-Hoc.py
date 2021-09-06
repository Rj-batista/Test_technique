import pandas as pd  
import json 


def get_keys_pubmed(data): 
    """Prends en entrée un fichier JSON produit par le DataPipeline.

    Returns
    -------
    set_pubmed
        Dictionnaire contenant les journaux en clés (keys).

    """
    liste_pubmed = []
    for i in data["Pubmed"]:
        liste_pubmed.append(i["journal"]) 
    set_pubmed = dict.fromkeys(liste_pubmed, "") 
    return(set_pubmed)


def get_keys_trials(data): 
    """Prends en entrée un fichier JSON produit par le DataPipeline.

    Returns
    -------
    set_trials
        Dictionnaire contenant les journaux en clés (keys).

    """
    liste_trial = []
    for i in data["Clinical_trials"]:
        liste_trial.append(i["journal"]) 
    set_trials = dict.fromkeys(liste_trial, "") 
    return(set_trials)


def dict_pubmed(set_pubmed, data): 
    """Prends en entrée un fichier JSON produit par le DataPipeline (set_pubmed)
        et le dictionnaire de clés (data).

    Returns
    -------
    set_pubmed
        Dictionnaire contenant les journaux en clés et les articles en valeurs pour la 
        partie Pubmed.

    """
    test = ''
    for key, value in set_pubmed.items():
        for j in data["Pubmed"]:
            if j["journal"] == key:
                test = test + j["title"] 
            else:
                continue
        set_pubmed[key] = test 
        test = ''  
    return(set_pubmed)


def dict_trial(set_trials, data): 
    """Prends en entrée un fichier JSON produit par le DataPipeline (set_trials) et le 
    	dictionnaire de clés (data).

    Returns
    -------
    pubmed_tri
        Dictionnaire contenant les journaux en clés et les articles en valeurs pour la 
        partie Clinical_trials.

    """
    test = ''
    for key, value in set_trials.items():
        for j in data["Clinical_trials"]:
            if j["journal"] == key:
                test = test + j["scientific_title"] 
            else:
                continue
        set_trials[key] = test 
        test = '' 
    return(set_trials)


def dict_final(set_pubmed, set_trials):  
    """Prends en entrée les deux dictionnaires précedemments créés.

    Returns
    -------
    pubmed_tri
        Dictionnaire contenant les journaux en clés (keys) et les articles en valeurs 
        (values) provenant des deux parties du JSON.

    """
    for ikey, ivalue in set_pubmed.items():
        for jkey, jvalue in set_trials.items():
            if ikey == jkey:
                ivalue = ivalue + jvalue 
                set_pubmed[ikey] = ivalue
            else: 
                set_pubmed.setdefault(jkey, jvalue)
    return(set_pubmed)


def count_drug(set_pubmed_tri, list_drug): 
    """Prends en entrée un dictionnaire (set_pubmed_tri) et la liste de drug (list_drug).

    Print
    -------
        Le nombre de molécules différentes par journaux.

    """
    compteur = 0  
    for key, value in set_pubmed_tri.items():  
        for elm in range(len(list_drug)):  
            values = value.lower()
            if list_drug[elm] in values: 
                compteur = compteur + 1 
                compteur_final = 0
            else:  
                compteur_final = compteur_final + compteur
                compteur = 0  
        print("Le journal {} a {} de molécules différentes".format(key,compteur_final))



if __name__ == "__main__":   
    drug = pd.read_csv("drugs.csv") 
    list_drug = drug["drug"].tolist() 
    list_drug = [x.lower() for x in list_drug]
    Question = input("Ecrivez le nom du fichier JSON : ") 
    Reponse = str(Question)
    files = open(Reponse) 
    data = json.load(files) 
    keys_pubmed = get_keys_pubmed(data)
    keys_trials = get_keys_trials(data) 
    pub_dict = dict_pubmed(keys_pubmed, data)
    tria_dict = dict_trial(keys_trials, data) 
    dict_fin = dict_final(pub_dict, tria_dict)  
    count = count_drug(dict_fin, list_drug) 
    





