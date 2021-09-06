import matplotlib.pyplot as plt
import pandas as pd  
import json 



def search_pubmed(name_drug): 
    """Prends en entrée le nom d'une molécule et tri un DataFrame.

    Returns
    -------
    pubmed_tri
        DataFrame contenant les articles mentionnant la molécule.

    """
    pubmed = pd.read_csv("pubmed.csv")
    pubmed["title"] = pubmed["title"].str.lower() # On normalise la police des caractères pour ne pas avoir de problème dans la recherche 
    pubmed_tri = pubmed[pubmed["title"].str.contains(name_drug) == True] #On récupère uniquement les articles contenant dans leur nom la molécule
    journal_pubmed = pubmed_tri["journal"].tolist() #On garde dans une liste les journaux 
    #del pubmed_tri['journal'] #On supprime la colonne des journaux du DataFrame 

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
    #del clinical_tri['journal']
    return(clinical_tri,journal_clinical)

def json_write(pubmed_tri, clinical_tri, journal_pubmed, journal_clinical, name_drug): 
    """Prends en entrée deux DataFrame, deux listes de journaux et le nom de la molécule.

    Returns
    -------
        JSON file
        Fichier JSON avec les articles pubmed et d'essai clinique pour une molécule.

    """   
    all_journal = journal_pubmed + journal_clinical
    pubmed_dict = pubmed_tri.to_dict(orient='records') 
    clinical_dict = clinical_tri.to_dict(orient="records")  
     
    results_article = {
        "Pubmed" : pubmed_dict, 
        "Clinical_trials" : clinical_dict,  
        "Journal" : all_journal
    }
    json_article = json.dumps(results_article, indent = 4) 
    with open("{}.json".format(name_drug), "w") as outfile:  
        outfile.write(json_article)  



if __name__ == "__main__":  
    drug=pd.read_csv("drugs.csv") 
    list_drug = drug["drug"].tolist() 
    list_drug = (map(lambda d : d.lower(), list_drug))
    Question = input("Ecrivez le nom de la molécule/drug recherché: ") 
    Reponse = str(Question).lower() 
    if(Reponse in list_drug):  
        name_drug=Reponse   
    else : 
        print("Le nom de la molécule/drug n'a pas était trouvé")
    result_search_pubmed = search_pubmed(name_drug)   
    result_search_clinical = search_clinical(name_drug)
    json_write(result_search_pubmed[0], result_search_clinical[0],
                result_search_pubmed[1],result_search_clinical[1], name_drug) 
    print("{}.json a été crée".format(name_drug))





    
    


