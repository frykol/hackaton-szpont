from fastapi import APIRouter
from database import session
from role import role_service, role

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model=list[role.RolePublic])
def get_roles(session: session.SessionDep):
    roles_return = role_service.get_roles(session)
    return roles_return

@router.get("/withUsers", response_model=list[role.RoleWithUsersPublic])
def get_roles_with_users(session: session.SessionDep):
    roles_return = role_service.get_roles(session)
    return roles_return

@router.get("/{role_id}", response_model=role.RolePublic)
def get_roles(role_id: int, session: session.SessionDep):
    roles_return = role_service.get_role(role_id, session)
    return roles_return

@router.post("/", response_model=role.RolePublic)
def create_role(role_create: role.RolePost, session: session.SessionDep):
    role_return = role_service.create_role(role_create, session)
    return role_return

@router.patch("/{role_id}", response_model=role.RolePublic)
def update_role(role_id: int, role_update: role.RoleUpdate, session: session.SessionDep):
    role_return = role_service.update_role(role_id, role_update, session)
    return role_return
