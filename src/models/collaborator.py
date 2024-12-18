from dataclasses import dataclass
from typing import List

@dataclass
class Collaborator:
    id: str
    name: str
    type: str  # 'human' or 'robot'
    strength: int  # scale 1-5
    precision: int  # scale 1-5
    available_tools: List[str]
    constraints: List[str]
    
    def can_use_tools(self, required_tools: List[str]) -> bool:
        return all(tool in self.available_tools for tool in required_tools)
    
    def get_fitness_score(self, force_required: int, precision_required: int) -> float:
        strength_match = min(self.strength / force_required, 1)
        precision_match = min(self.precision / precision_required, 1)
        return (strength_match + precision_match) / 2
