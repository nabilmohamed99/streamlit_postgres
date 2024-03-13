# app.py

import streamlit as st
from db import create_user, get_users, update_user, delete_user

# Titre de l'application
st.title("Gestion des utilisateurs")

# Fonction pour afficher la liste des utilisateurs
def display_users():
    users = get_users()
    st.write("Liste des utilisateurs :")
    for user in users:
        st.write(user)

# Interface utilisateur
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Choisir une option :", ["Accueil", "Ajouter Utilisateur", "Modifier Utilisateur", "Supprimer Utilisateur"])

    if menu == "Accueil":
        st.write("Bienvenue dans l'application de gestion des utilisateurs !")
        display_users()

    elif menu == "Ajouter Utilisateur":
        st.subheader("Ajouter un nouvel utilisateur")
        name = st.text_input("Nom")
        email = st.text_input("Email")
        if st.button("Ajouter"):
            create_user(name, email)
            st.success("Utilisateur ajouté avec succès !")
            display_users()

    elif menu == "Modifier Utilisateur":
        st.subheader("Modifier un utilisateur existant")
        users = get_users()
        user_names = [user['name'] for user in users]
        selected_user = st.selectbox("Choisir un utilisateur :", user_names)
        new_email = st.text_input("Nouvel email")
        if st.button("Modifier"):
            update_user(selected_user, new_email)
            st.success("Utilisateur modifié avec succès !")
            display_users()

    elif menu == "Supprimer Utilisateur":
        st.subheader("Supprimer un utilisateur")
        users = get_users()
        user_names = [user['name'] for user in users]
        selected_user = st.selectbox("Choisir un utilisateur :", user_names)
        if st.button("Supprimer"):
            delete_user(selected_user)
            st.success("Utilisateur supprimé avec succès !")
            display_users()

if __name__ == "__main__":
    main()
