from enum import Enum


class ParticipantListEntryOnlineDataHealth(str, Enum):
    FORMERPOSSIBLEDUPLICATE = "FormerPossibleDuplicate"
    MANUALLYCHANGED = "ManuallyChanged"
    MATCHED = "Matched"
    NEWCONSTITUENT = "NewConstituent"
    NEWNAMEDGUEST = "NewNamedGuest"
    POSSIBLEDUPLICATE = "PossibleDuplicate"

    def __str__(self) -> str:
        return str(self.value)
