# DerivedAssemblyOccurrences Object

## Description

The DerivedAssemblyOccurrences collection object provides access to the objects associated with a specific DerivedAssemblyDefinition object. The DerivedAssemblyOccurrence objects contained within the collection represent the top-level occurrences within the assembly you obtained the collection from.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAssemblyOccurrences/DerivedAssemblyOccurrences_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DerivedAssemblyOccurrences/DerivedAssemblyOccurrences_Count.md) | Property that returns the number of items in the collection. |
| [Item](../DerivedAssemblyOccurrences/DerivedAssemblyOccurrences_Item.md) | Returns the specified object from the collection. |
| [Type](../DerivedAssemblyOccurrences/DerivedAssemblyOccurrences_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedAssemblyDefinition.Occurrences](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_Occurrences.md), [DerivedAssemblyOccurrence.SubOccurrences](../DerivedAssemblyOccurrence/DerivedAssemblyOccurrence_SubOccurrences.md)

## Version

Introduced in version 5.3
