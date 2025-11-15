import streamlit as st

# Configuration de la page (titre de l'onglet et icône)
st.set_page_config(page_title="Chasse au Trésor", page_icon="🎁")

# --- INITIALISATION DE L'ÉTAT ---
# Nous devons "souvenir" si la première étape est résolue.
# On initialise 'etape1_resolue' à False s'il n'existe pas encore.
if 'etape1_resolue' not in st.session_state:
    st.session_state.etape1_resolue = False

# --- TITRE PRINCIPAL ---
st.title("🎂Chasse au trésor d'anniversaire !")
st.write("Pour trouver ton cadeau, tu dois d'abord résoudre ces énigmes... Mais attention aux fautes d'orthographe !")

st.markdown("---")

# --- ÉTAPE 1 : L'ÉNIGME D'ACCÈS ---
# Cette partie est toujours visible
st.header("Étape 1 : L'énigme d'accès")
st.info("Je renvoie sans trahir.")
reponse_acces = st.text_input("Ta réponse pour l'étape 1 :", key="acces")

# La réponse correcte (en minuscules pour être robuste)
REPONSE_ACCES_COURTE = "miroir"
REPONSE_ACCES_LONGUE = "un miroir"

# Bouton pour valider l'étape 1
if st.button("Déverrouiller la suite"):
    reponse_propre = reponse_acces.lower().strip()
    if (reponse_propre == REPONSE_ACCES_COURTE or reponse_propre == REPONSE_ACCES_LONGUE):
        st.success("Correct ! La voie est libre...")
        # On met à jour l'état pour dire que l'étape 1 est résolue
        st.session_state.etape1_resolue = True
        # st.rerun() force l'application à se recharger avec le nouvel état
        st.rerun()
        
    else:
        st.error("Ce n'est pas ça... Réfléchis bien !")


# --- LA SUITE DE LA CHASSE (ÉTAPE 2 ET 3) ---
# Le code suivant ne s'exécute QUE SI 'etape1_resolue' est True
if st.session_state.etape1_resolue:

    st.markdown("---")

    # --- ÉTAPE 2 (Anciennement Énigme 1) ---
    st.header("Étape 2 : Énigme 1")
    st.info("Mon mythe fondateur dit que j'ai été bâtie par un exilé troyen.")
    reponse1 = st.text_input("Ta réponse pour l'énigme 1 :", key="enigme1")

    st.markdown("---")

    # --- ÉTAPE 3 (Anciennement Énigme 2) ---
    st.header("Étape 3 : Énigme 2")
    st.info("Je suis le point de convergence involontaire de deux lignées rivales.")
    reponse2 = st.text_input("Ta réponse pour l'énigme 2 :", key="enigme2")

    st.markdown("---")

    # --- BOUTON DE VALIDATION FINAL ---
    REPONSE_CORRECTE_1 = "londres"
    REPONSE_CORRECTE_2 = "harry potter"

    if st.button("Vérifier mes réponses !"):
        
        if (reponse1.lower().strip() == REPONSE_CORRECTE_1 and 
            reponse2.lower().strip() == REPONSE_CORRECTE_2):
            
            st.balloons()
            st.success("BRAVO ! Tu as trouvé les bonnes réponses !")
            
            st.subheader("Ton cadeau se trouve...")
            st.write("Nous partons à Londres du 21 au 23 mars pour visiter Warner Bros Studios : The Making of Harry Potter. J'espère que cela te plaira. 🙃")

            st.write("Voici un aperçu de ce qui t'attend :")
            
            st.image("londres.jpg", caption="La magnifique ville de Londres")
            st.image("rue.jpg", caption="Bienvenue au Chemin de Traverse !")
            st.image("train.jpg", caption="Le majestueux Poudlard Express")
            
        else:
            st.error("Oups... au moins une des réponses est incorrecte. Essaie encore !")
