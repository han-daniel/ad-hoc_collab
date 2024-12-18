from ..models.assembly import FurnitureAssembly, AssemblyStep
from ..models.collaborator import Collaborator
from ..utils.graph_utils import create_assembly_graph, assign_tasks

def create_chair_assembly() -> FurnitureAssembly:
    chair = FurnitureAssembly("Basic Chair")
    
    steps = [
        AssemblyStep(
            id="START",
            description="Begin assembly",
            required_tools=[],
            estimated_time=0,
            force_required=1,
            precision_required=1,
            predecessors=[]
        ),
        AssemblyStep(
            id="attach_legs",
            description="Attach legs to seat base",
            required_tools=["screwdriver", "allen_key"],
            estimated_time=15,
            force_required=3,
            precision_required=4,
            predecessors=["START"]
        ),
        AssemblyStep(
            id="attach_backrest",
            description="Attach backrest to seat base",
            required_tools=["screwdriver", "allen_key"],
            estimated_time=20,
            force_required=4,
            precision_required=5,
            predecessors=["attach_legs"]
        ),
        AssemblyStep(
            id="add_cushion",
            description="Add seat cushion",
            required_tools=[],
            estimated_time=5,
            force_required=1,
            precision_required=2,
            predecessors=["attach_backrest"]
        ),
        AssemblyStep(
            id="END",
            description="Complete assembly",
            required_tools=[],
            estimated_time=0,
            force_required=1,
            precision_required=1,
            predecessors=["add_cushion"]
        )
    ]
    
    for step in steps:
        chair.add_step(step)
    
    return chair

def create_sample_collaborators() -> List[Collaborator]:
    return [
        Collaborator(
            id="human1",
            name="John",
            type="human",
            strength=4,
            precision=4,
            available_tools=["screwdriver", "allen_key", "hammer"],
            constraints=["no_heavy_lifting"]
        ),
        Collaborator(
            id="robot1",
            name="AssemblyBot",
            type="robot",
            strength=5,
            precision=5,
            available_tools=["screwdriver", "allen_key"],
            constraints=["limited_mobility"]
        ),
        Collaborator(
            id="human2",
            name="Sarah",
            type="human",
            strength=3,
            precision=5,
            available_tools=["screwdriver", "allen_key"],
            constraints=[]
        )
    ]
