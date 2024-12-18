from src.examples.chair_assembly import create_chair_assembly, create_sample_collaborators
from src.utils.graph_utils import create_assembly_graph, assign_tasks
import networkx as nx

def main():
    # Create sample data
    print("Creating chair assembly...")
    chair = create_chair_assembly()
    collaborators = create_sample_collaborators()
    
    # Create assembly graph
    print("\nCreating assembly graph...")
    G = create_assembly_graph(chair)
    
    # Print graph information
    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    print("\nAssembly sequence:")
    for step in nx.topological_sort(G):
        if step not in ["START", "END"]:
            step_data = chair.get_step(step)
            print(f"- {step_data.description}")
    
    # Get and print task assignments
    print("\nAssigning tasks to collaborators...")
    assignments = assign_tasks(G, chair, collaborators)
    
    # Print results
    print("\nTask Assignments:")
    for collaborator_id, tasks in assignments.items():
        collaborator = next(c for c in collaborators if c.id == collaborator_id)
        print(f"\n{collaborator.name} ({collaborator.type}) will perform:")
        for task in tasks:
            step = chair.get_step(task)
            print(f"- {step.description} (estimated time: {step.estimated_time} min)")

if __name__ == "__main__":
    main()
