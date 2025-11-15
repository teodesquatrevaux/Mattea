import streamlit as st

# Configuration de la page (titre de l'onglet et icône)
st.set_page_config(page_title="Chasse au Cadeau", page_icon="🎁")

# --- INITIALISATION DE L'ÉTAT ---
# On initialise les deux verrous
if 'etape1_resolue' not in st.session_state:
    st.session_state.etape1_resolue = False
if 'etape2_resolue' not in st.session_state:
    st.session_state.etape2_resolue = False

# --- TITRE PRINCIPAL ---
st.title("🎂Chasse au cadeau d'anniversaire !")
st.write("Pour trouver ton cadeau, tu dois d'abord résoudre ces énigmes... Mais attention aux fautes d'orthographe !")

st.markdown("---")

# --- ÉTAPE 1 : L'ÉNIGME D'ACCÈS ---
st.header("Étape 1 : L'énigme d'accès")
st.info("Je renvoie sans trahir.")
reponse_acces = st.text_input("Ta réponse pour l'étape 1 :", key="acces")

REPONSE_ACCES_COURTE = "miroir"
REPONSE_ACCES_LONGUE = "un miroir"

if st.button("Déverrouiller la suite"):
    reponse_propre = reponse_acces.lower().strip()
    if (reponse_propre == REPONSE_ACCES_COURTE or reponse_propre == REPONSE_ACCES_LONGUE):
        st.success("Correct ! La voie est libre pour l'étape 2...")
        st.session_state.etape1_resolue = True
        st.rerun()
    else:
        st.error("Ce n'est pas ça... Réfléchis bien !")


# --- ÉTAPE 2 : NOUVELLE ÉNIGME ---
# Ne s'affiche que si l'étape 1 est résolue
if st.session_state.etape1_resolue:
    
    st.markdown("---")
    st.header("Étape 2 : L'énigme du coeur")
    st.info("On le porte sans le voir clairement.")
    reponse_acces_2 = st.text_input("Ta réponse pour l'étape 2 :", key="acces2")

    REPONSE_ACCES_2_COURTE = "amour"
    REPONSE_ACCES_2_LONGUE = "l'amour" # J'ajoute une variante

    # Bouton unique pour cette étape
    if st.button("Déverrouiller la suite finale"):
        reponse_propre_2 = reponse_acces_2.lower().strip()
        if (reponse_propre_2 == REPONSE_ACCES_2_COURTE or reponse_propre_2 == REPONSE_ACCES_2_LONGUE):
            st.success("Bravo ! Voici les dernières énigmes...")
            # On active le deuxième verrou
            st.session_state.etape2_resolue = True
            st.rerun()
        else:
            st.error("Non... ce n'est pas ça. Cherche bien !")


# --- LA SUITE DE LA CHASSE (ÉTAPE 3 ET 4) ---
# Ne s'exécute que si l'étape 2 est résolue
if st.session_state.etape2_resolue:

    st.markdown("---")

    # --- ÉTAPE 3 (Anciennement Énigme 1) ---
    st.header("Étape 3 : Énigme 1") # Renuméroté
    st.info("Mon mythe fondateur dit que j'ai été bâtie par un exilé troyen.")
    reponse1 = st.text_input("Ta réponse pour l'énigme 1 :", key="enigme1")

    st.markdown("---")

    # --- ÉTAPE 4 (Anciennement Énigme 2) ---
    st.header("Étape 4 : Énigme 2") # Renuméroté
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
            
            # Assurez-vous que les images sont au bon endroit !
            # (par exemple, dans le même dossier que le script)
            st.image("londres.jpg", caption="La magnifique ville de Londres")
            st.image("rue.jpg", caption="Bienvenue au Chemin de Traverse !")
            st.image("train.jpg", caption="Le majestueux Poudlard Express")
            
        else:
            st.error("Oups... au moins une des réponses est incorrecte. Essaie encore !")
