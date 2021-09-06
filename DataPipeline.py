import pandas as pd  
import json 



def search_pubmed(name_drug): 
    """Prends en entrée le nom d'une molécule et tri un DataFrame.

    Returns
    -------
    pubmed_tri
        DataFrame contenant les articles mentionnant la molécule.

    """
    
    # Nous lisons le fichier .csv.
    pubmed = pd.read_csv("pubmed.csv")
    
    # Nous normalisons la police de caractères afin de ne pas avoir de problème dans la recherche.
    pubmed["title"] = pubmed["title"].str.lower()
    
    # Permet de récupérer uniquement les articles contenant dans leur titre la molécule.
    pubmed_tri = pubmed[pubmed["title"].str.contains(name_drug) == True] 
    
    # Nous stockons dans une liste les journaux.
    journal_pubmed = pubmed_tri["journal"].tolist() 
    
    # Nous supprimons la colonne 'journal' du DataFrame 
    #del pubmed_tri['journal']

    return(pubmed_tri,journal_pubmed)
    

def search_clinical(name_drug): 
    """Prends en entrée le nom d'une molécule et tri un DataFrame.

    Returns
    -------
    clinical_tri
        DataFrame contenant les articles mentionnant la molécule.

    """ 
    clinical = pd.read_csv("clinical_trials.csv") 
    clinical["scientific_title"] = clinical["scientific_title"].str.lower() 
    clinical_tri = clinical[clinical["scientific_title"].str.contains(name_drug) == True]  
    journal_clinical = clinical_tri["journal"].tolist() 
    return(clinical_tri,journal_clinical)


def json_write(pubmed_tri, clinical_tri, journal_pubmed, journal_clinical, name_drug): 
    """Prends en entrée deux DataFrames (pubmed_tri, clinical_tri), deux listes de 
    journaux (journal_pubmed, journal_clinical) et le nom de la molécule (name_drug).

    Returns
    -------
        JSON file
        Fichier JSON avec les articles pubmed et d'essai clinique pour une molécule.

    """   
    all_journal = journal_pubmed + journal_clinical
    pubmed_dict = pubmed_tri.to_dict(orient = "records") 
    clinical_dict = clinical_tri.to_dict(orient = "records")  
     
    results_article = {
        "Pubmed" : pubmed_dict, 
        "Clinical_trials" : clinical_dict,  
        "Journal" : all_journal
    }
    json_article = json.dumps(results_article, indent = 4) 
    with open("{}.json".format(name_drug), "w") as outfile:  
        outfile.write(json_article)  



if __name__ == "__main__":  
    drug = pd.read_csv("drugs.csv") 
    list_drug = drug["drug"].tolist() 
    list_drug = [x.lower() for x in list_drug]
    Question = input("Ecrivez le nom de la molécule/drug recherché : ") 
    Reponse = str(Question).lower() 
    if(Reponse in list_drug):  
        name_drug = Reponse   
    else : 
        print("Le nom de la molécule/drug n'a pas été trouvé. ")
    result_search_pubmed = search_pubmed(name_drug)   
    result_search_clinical = search_clinical(name_drug)
    json_write(result_search_pubmed[0], result_search_clinical[0],
                result_search_pubmed[1], result_search_clinical[1], name_drug) 
    print("{}.json a été crée".format(name_drug))





    
    


