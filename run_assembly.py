from src.examples.chair_assembly import create_chair_assembly, create_sample_collaborators
from src.utils.graph_utils import create_assembly_graph, assign_tasks
import networkx as nx
import matplotlib.pyplot as plt

def visualize_assembly_graph(G, assignments):
    plt.figure(figsize=(12, 8))
    
    # Create layout
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=2000, alpha=0.7)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', 
                          arrows=True, arrowsize=20)
    
    # Draw labels
    labels = {}
    for node in G.nodes():
        if node in ["START", "END"]:
            labels[node] = node
        else:
            step = G.nodes[node]
            labels[node] = f"{step['description']}\nTime: {step['estimated_time']}min"
    
    nx.draw_networkx_labels(G, pos, labels, font_size=8, 
                          font_weight='bold', font_family='sans-serif')
    
    # Add title and legend
    plt.title("Furniture Assembly Graph", pad=20, font_size=16)
    
    # Add assignee information
    assignee_text = "Task Assignments:\n"
    for collaborator_id, tasks in assignments.items():
        if tasks:  # only show collaborators with assigned tasks
            collaborator = next(c for c in collaborators if c.id == collaborator_id)
            assignee_text += f"\n{collaborator.name}:\n"
            for task in tasks:
                assignee_text += f"- {task}\n"
    
    plt.figtext(1.02, 0.5, assignee_text, fontsize=8, 
                bbox=dict(facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.axis('off')
    plt.show()

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
    
    # Visualize the graph
    visualize_assembly_graph(G, assignments)

if __name__ == "__main__":
    main()
