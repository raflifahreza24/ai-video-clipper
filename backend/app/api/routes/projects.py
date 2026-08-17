from fastapi import APIRouter
from app.schemas.project import ProjectCreate, ProjectResponse
router = APIRouter(
   prefix="/projects",
   tags=["projects"],
)
@router.get("")
def list_projects():
   return [
      {
         "id": "demo-1",
         "name": "Podcast Programmer"
      }
   ]

@router.post("", response_model=ProjectResponse, status_code=201)
def create_project(payload: ProjectCreate):
   return ProjectResponse(
      id="demo-new-project",
      name=payload.name,
      description=payload.description,
   )