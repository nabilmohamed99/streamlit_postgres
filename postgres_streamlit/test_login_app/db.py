# db.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connexion à la base de données
DATABASE_URL = "postgresql://your_username:your_password@db/your_database_name"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclaration de la base de données
Base = declarative_base()

# Modèle de données pour la table des utilisateurs
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Créer les tables dans la base de données
def create_database():
    Base.metadata.create_all(bind=engine)

# Créer un nouvel utilisateur dans la base de données
def create_user(name: str, email: str):
    db = SessionLocal()
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()

# Récupérer tous les utilisateurs de la base de données
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return [{"name": user.name, "email": user.email} for user in users]

# Mettre à jour l'email d'un utilisateur dans la base de données
def update_user(name: str, new_email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.name == name).first()
    user.email = new_email
    db.commit()
    db.close()

# Supprimer un utilisateur de la base de données
def delete_user(name: str):
    db = SessionLocal()
    db.query(User).filter(User.name == name).delete()
    db.commit()
    db.close()

# Appel à la fonction de création de la base de données au démarrage
create_database()
