from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="EducationRead")


@_attrs_define
class EducationRead:
    """A constituent’s education history provides important insight into who they are and often helps determine which
    causes the constituent will invest time and money into.

        Attributes:
            id (str | Unset): The immutable system record ID of the education.
            campus (str | Unset): The campus.
            class_of (str | Unset): The year the constituent graduated.
            class_of_degree (str | Unset): The class of degree. Available values are the entries in the <a href="https://dev
                eloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationDegreeClasses"><b>Class
                of Degree</b></a> table. For the UK only.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the education.
            date_added (datetime.datetime | Unset): The date when the education was created. Includes an offset from UTC in
                <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_entered (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            date_graduated (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            date_left (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            date_modified (datetime.datetime | Unset): The date when the education was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            degree (str | Unset): The degree received. Available values are the entries in the <a href="https://developer.sk
                y.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationDegrees"><b>Degrees</b></a>
                table.
            department (str | Unset): The name of the education department. Available values are the entries in the <a href=
                "https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationDepartments"
                ><b>Departments</b></a> table. For the UK only.
            faculty (str | Unset): The name of the faculty. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationFaculties"><b>Faculties</b><
                /a> table. For the UK only.
            gpa (float | Unset): The grade point average.
            import_id (str | Unset): The import id.
            known_name (str | Unset): The known name.
            majors (list[str] | Unset): The major courses of study. Available values are the entries in the <a href="https:/
                /developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationSubjects"><b>Major/M
                inor</b></a> table.
            minors (list[str] | Unset): The minor courses of study. Available values are the entries in the <a href="https:/
                /developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationSubjects"><b>Major/M
                inor</b></a> table.
            notes (str | Unset): The notes.
            primary (bool | Unset): Indicates whether this is the constituent's primary school association.
            registration_number (str | Unset): The registration number. For the UK only.
            school (str | Unset): The school name. Available values are the entries in the <a href="https://developer.sky.bl
                ackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationSchools"><b>Schools</b></a> table.
                For the UK, this property is for the establishment name, and available values are the entries in the <a href="ht
                tps://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationSchools"><b>Est
                ablishments</b></a> table.
            social_organization (str | Unset): The social organization.
            status (str | Unset): The status of the education. Available values are the entries in the <a href="https://deve
                loper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationStatuses"><b>Education
                Status</b></a> table.
            subject_of_study (str | Unset): The subject of study. Available values are the entries in the <a href="https://d
                eveloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationSubjects"><b>Subject
                of Study</b></a> table. For the UK only.
            type_ (str | Unset): The type of education. Available values are the entries in the <a href="https://developer.s
                ky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEducationTypes"><b>School Types</b></a>
                table.
    """

    id: str | Unset = UNSET
    campus: str | Unset = UNSET
    class_of: str | Unset = UNSET
    class_of_degree: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_entered: FuzzyDate | Unset = UNSET
    date_graduated: FuzzyDate | Unset = UNSET
    date_left: FuzzyDate | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    degree: str | Unset = UNSET
    department: str | Unset = UNSET
    faculty: str | Unset = UNSET
    gpa: float | Unset = UNSET
    import_id: str | Unset = UNSET
    known_name: str | Unset = UNSET
    majors: list[str] | Unset = UNSET
    minors: list[str] | Unset = UNSET
    notes: str | Unset = UNSET
    primary: bool | Unset = UNSET
    registration_number: str | Unset = UNSET
    school: str | Unset = UNSET
    social_organization: str | Unset = UNSET
    status: str | Unset = UNSET
    subject_of_study: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        campus = self.campus

        class_of = self.class_of

        class_of_degree = self.class_of_degree

        constituent_id = self.constituent_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_entered: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_entered, Unset):
            date_entered = self.date_entered.to_dict()

        date_graduated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_graduated, Unset):
            date_graduated = self.date_graduated.to_dict()

        date_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_left, Unset):
            date_left = self.date_left.to_dict()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        degree = self.degree

        department = self.department

        faculty = self.faculty

        gpa = self.gpa

        import_id = self.import_id

        known_name = self.known_name

        majors: list[str] | Unset = UNSET
        if not isinstance(self.majors, Unset):
            majors = self.majors

        minors: list[str] | Unset = UNSET
        if not isinstance(self.minors, Unset):
            minors = self.minors

        notes = self.notes

        primary = self.primary

        registration_number = self.registration_number

        school = self.school

        social_organization = self.social_organization

        status = self.status

        subject_of_study = self.subject_of_study

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if campus is not UNSET:
            field_dict["campus"] = campus
        if class_of is not UNSET:
            field_dict["class_of"] = class_of
        if class_of_degree is not UNSET:
            field_dict["class_of_degree"] = class_of_degree
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_entered is not UNSET:
            field_dict["date_entered"] = date_entered
        if date_graduated is not UNSET:
            field_dict["date_graduated"] = date_graduated
        if date_left is not UNSET:
            field_dict["date_left"] = date_left
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if degree is not UNSET:
            field_dict["degree"] = degree
        if department is not UNSET:
            field_dict["department"] = department
        if faculty is not UNSET:
            field_dict["faculty"] = faculty
        if gpa is not UNSET:
            field_dict["gpa"] = gpa
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if known_name is not UNSET:
            field_dict["known_name"] = known_name
        if majors is not UNSET:
            field_dict["majors"] = majors
        if minors is not UNSET:
            field_dict["minors"] = minors
        if notes is not UNSET:
            field_dict["notes"] = notes
        if primary is not UNSET:
            field_dict["primary"] = primary
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if school is not UNSET:
            field_dict["school"] = school
        if social_organization is not UNSET:
            field_dict["social_organization"] = social_organization
        if status is not UNSET:
            field_dict["status"] = status
        if subject_of_study is not UNSET:
            field_dict["subject_of_study"] = subject_of_study
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        campus = d.pop("campus", UNSET)

        class_of = d.pop("class_of", UNSET)

        class_of_degree = d.pop("class_of_degree", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_entered = d.pop("date_entered", UNSET)
        date_entered: FuzzyDate | Unset
        if isinstance(_date_entered, Unset):
            date_entered = UNSET
        else:
            date_entered = FuzzyDate.from_dict(_date_entered)

        _date_graduated = d.pop("date_graduated", UNSET)
        date_graduated: FuzzyDate | Unset
        if isinstance(_date_graduated, Unset):
            date_graduated = UNSET
        else:
            date_graduated = FuzzyDate.from_dict(_date_graduated)

        _date_left = d.pop("date_left", UNSET)
        date_left: FuzzyDate | Unset
        if isinstance(_date_left, Unset):
            date_left = UNSET
        else:
            date_left = FuzzyDate.from_dict(_date_left)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        degree = d.pop("degree", UNSET)

        department = d.pop("department", UNSET)

        faculty = d.pop("faculty", UNSET)

        gpa = d.pop("gpa", UNSET)

        import_id = d.pop("import_id", UNSET)

        known_name = d.pop("known_name", UNSET)

        majors = cast(list[str], d.pop("majors", UNSET))

        minors = cast(list[str], d.pop("minors", UNSET))

        notes = d.pop("notes", UNSET)

        primary = d.pop("primary", UNSET)

        registration_number = d.pop("registration_number", UNSET)

        school = d.pop("school", UNSET)

        social_organization = d.pop("social_organization", UNSET)

        status = d.pop("status", UNSET)

        subject_of_study = d.pop("subject_of_study", UNSET)

        type_ = d.pop("type", UNSET)

        education_read = cls(
            id=id,
            campus=campus,
            class_of=class_of,
            class_of_degree=class_of_degree,
            constituent_id=constituent_id,
            date_added=date_added,
            date_entered=date_entered,
            date_graduated=date_graduated,
            date_left=date_left,
            date_modified=date_modified,
            degree=degree,
            department=department,
            faculty=faculty,
            gpa=gpa,
            import_id=import_id,
            known_name=known_name,
            majors=majors,
            minors=minors,
            notes=notes,
            primary=primary,
            registration_number=registration_number,
            school=school,
            social_organization=social_organization,
            status=status,
            subject_of_study=subject_of_study,
            type_=type_,
        )

        education_read.additional_properties = d
        return education_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
