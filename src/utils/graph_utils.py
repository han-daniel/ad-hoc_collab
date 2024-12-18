import networkx as nx
from typing import Dict, List
from ..models.assembly import FurnitureAssembly
from ..models.collaborator import Collaborator

def create_assembly_graph(assembly: FurnitureAssembly) -> nx.DiGraph:
    G = nx.DiGraph()
    
    # Add nodes for each step
    for step_id, step in assembly.steps.items():
        G.add_node(step_id, **step.__dict__)
    
    # Add edges based on predecessors
    for step_id, step in assembly.steps.items():
        for pred in step.predecessors:
            G.add_edge(pred, step_id)
    
    return G

def assign_tasks(G: nx.DiGraph, assembly: FurnitureAssembly, 
                collaborators: List[Collaborator]) -> Dict[str, List[str]]:
    assignments = {c.id: [] for c in collaborators}
    
    # Sort steps topologically to respect dependencies
    steps = list(nx.topological_sort(G))
    
    for step in steps:
        if step in ["START", "END"]:
            continue
            
        step_data = assembly.get_step(step)
        best_collaborator = None
        best_score = -1
        
        for collaborator in collaborators:
            if not collaborator.can_use_tools(step_data.required_tools):
                continue
                
            score = collaborator.get_fitness_score(
                step_data.force_required,
                step_data.precision_required
            )
            
            if score > best_score:
                best_score = score
                best_collaborator = collaborator
        
        if best_collaborator:
            assignments[best_collaborator.id].append(step)
    
    return assignments
