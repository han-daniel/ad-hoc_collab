from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AssemblyStep:
    id: str
    description: str
    required_tools: List[str]
    estimated_time: int  # in minutes
    force_required: int  # scale 1-5
    precision_required: int  # scale 1-5
    predecessors: List[str]

class FurnitureAssembly:
    def __init__(self, name: str):
        self.name = name
        self.steps: Dict[str, AssemblyStep] = {}
        
    def add_step(self, step: AssemblyStep):
        self.steps[step.id] = step
        
    def get_step(self, step_id: str) -> AssemblyStep:
        return self.steps.get(step_id)
    
    def get_all_steps(self) -> Dict[str, AssemblyStep]:
        return self.steps
