# DerivedFutureAssemblyOccurrence Object

## Description

The DerivedFutureAssemblyOccurrence object defines the behavior of an occurrence within a derived future assembly. This object is derived from the ReferenceComponent object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [InclusionOption](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_InclusionOption.md) | Read-write property that defines if this occurrence is included and if it is how it is used in the derived assembly. Valid values for this property are kDerivedIncludeAll, kDerivedExcludeAll and kDerivedIndividualDefined.   If this occurrence represents a subassembly, setting to kDerivedIncludeAll will cause all sub occurrences to add material to the solid body. If setting to kDerivedIndividualDefined, the sub occurrence’s define their behavior. An important distinction between “All” and “IndividualDefined” switches is that as occurrences are added to the subassembly they will automatically be included if any of the “All” switches are used. If the “InidividualDefined” switch is used, new components added to the assembly will be set to kDerivedExludeAll. If this occurrence represents a leaf part, then valid options are kDerivedIncludeAll or kDerivedExcludeAll. |
| [IsAssembly](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_IsAssembly.md) | Read-only property that specifies whether this DerivedFutureAssemblyOccurrence object represents a subassembly or a leaf part. This property is True in the case where it represents a subassembly. When it is a subassembly, the SubOccurrences property can be used to access the occurrences within this subassembly. |
| [Name](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_Name.md) | Gets the name of this DerivedFutureAssemblyOccurrence within the scope of this Document. |
| [SubOccurrences](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_SubOccurrences.md) | Read-only property that returns the occurrences in the top-level of the assembly this DerivedFutureAssemblyOccurrence object represents. This property is only valid in the case where the IsAssembly property is True. . |
| [Type](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DerivedFutureAssemblyOccurrences.Item](../DerivedFutureAssemblyOccurrences/DerivedFutureAssemblyOccurrences_Item.md)

## Version

Introduced in version 2018
