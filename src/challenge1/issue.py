from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any


class IssueStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IssueObserver(ABC):
    @abstractmethod
    def update(self, issue: 'Issue', changed_fields: Dict[str, Any]) -> None:
        """Called when the observed issue is updated."""
        pass


@dataclass
class Issue:
    title: str
    description: str
    status: IssueStatus = IssueStatus.OPEN
    created_at: datetime = None
    updated_at: datetime = None
    assigned_to: str = None
    
    def __post_init__(self):
        self._observers: List[IssueObserver] = []
        if self.created_at is None:
            self.created_at = datetime.now()
        self.updated_at = self.created_at

    def attach(self, observer: IssueObserver) -> None:
        """Add an observer to the issue."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: IssueObserver) -> None:
        """Remove an observer from the issue."""
        self._observers.remove(observer)

    def _notify(self, changed_fields: Dict[str, Any]) -> None:
        """Notify all observers about changes."""
        for observer in self._observers:
            observer.update(self, changed_fields)

    def update_status(self, new_status: IssueStatus) -> None:
        """Update the issue status and notify observers."""
        if new_status != self.status:
            old_status = self.status
            self.status = new_status
            self.updated_at = datetime.now()
            self._notify({"status": {"old": old_status, "new": new_status}})

    def assign_to(self, assignee: str) -> None:
        """Assign the issue to someone and notify observers."""
        if assignee != self.assigned_to:
            old_assignee = self.assigned_to
            self.assigned_to = assignee
            self.updated_at = datetime.now()
            self._notify({"assigned_to": {"old": old_assignee, "new": assignee}}) 