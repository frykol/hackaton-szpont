from fastapi import HTTPException
from database import session
from sqlmodel import select
from role import role

def get_roles(session: session.SessionDep) -> list[role.Role]:
    roles = session.exec(select(role.Role)).all()
    return roles

def get_role(role_id: int, session: session.SessionDep) -> role.Role:
    role_get = session.get(role.Role, role_id)
    if not role_get:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_get

def create_role(role_create: role.RolePost, session: session.SessionDep) -> role.Role:
    db_role = role.Role.model_validate(role_create)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

def update_role(role_id: int, role_update: role.RoleUpdate, session: session.SessionDep) -> role.Role:
    role_to_update = get_role(role_id, session)
    role_data = role_update.model_dump(exclude_unset=True)
    role_to_update.sqlmodel_update(role_data)
    session.add(role_to_update)
    session.commit()
    session.refresh(role_to_update)
    return role_to_update

def delete_role(role_id: int, session: session.SessionDep):
    role_delete = get_role(role_id, session)
    role_delete.users.clear()
    session.delete(role_delete)
    session.commit()
    return {"deleted": role_id}