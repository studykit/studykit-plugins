# DerivedAssemblyOccurrence Object

## Description

The DerivedAssemblyOccurrence object defines the behavior of an occurrence within a derived assembly.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FailedBooleanOperation](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_FailedBooleanOperation.md) | Read-only property that returns whether this occurrence failed the Boolean operation resulting in creation of separate, independent bodies. This occurs only if the IndependentSolidsOnFailedBoolean property on DerivedAssemblyDefinition is set to true. |
| [InclusionOption](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_InclusionOption.md) | Property that defines if this occurrence is included and if it is how it is used in the derived assembly. Valid values for this property are kDerivedIncludeAll, kDerivedSubtractAll, kDerivedExcludeAll, kDerivedBoundingBox, kDerivedIntersect and kDerivedIndividualDefined. |
| [IsAssembly](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_IsAssembly.md) | Property that specifies whether this DerivedAssemblyOccurrence object represents a subassembly or a leaf part. This property is True in the case where it represents a subassembly. When it is a subassembly, the SubOccurrences property can be used to access the occurrences within this subassembly. |
| [Name](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_Name.md) | Property that returns the name of the derived occurrence. |
| [ReferencedOccurrence](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_ReferencedOccurrence.md) | Property that returns the in the assembly document. This can be used to perform additional queries to help to determine whether to include this occurrence or not. |
| [SubOccurrences](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_SubOccurrences.md) | Property that returns the in the top-level of the assembly this DerivedAssemblyOccurrence object represents. This property is only valid in the case where the IsAssembly property is True. |
| [Type](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedAssemblyOccurrences.Item](../DerivedAssemblyOccurrences/DerivedAssemblyOccurrences_Item.md)

## Version

Introduced in version 5.3
