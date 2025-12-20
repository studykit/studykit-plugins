# VisibleOccurrenceFinder Object

## Description

The VisibleOccurrenceFinder object is a utility object created using the AssemblyComponentDefinition.CreateVisibleOccurrenceFinder method. It is used to find occurrences in the assembly based on their visibility. It is equivalent to the “Select Internal Components”, “Select External Components”, and “Select All in Camera” commands in Inventor.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CompactResult](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_CompactResult.md) | Read-write property Boolean that defines if all components that are found within an assembly will be consolidated so that their paraent assembly is returned instead of each one of the child components. |
| [FoundOccurrences](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_FoundOccurrences.md) | Read-only property that returns the occurrences that meet the current criteria defined by the other properties on the VisibleOccurrenceFinder object. |
| [PercentageVisible](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_PercentageVisible.md) | Read-write property Double that defines the percentage of the component that can be visible or hidden. |
| [Type](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../VisibleOccurrenceFinder/VisibleOccurrenceFinder_Visible.md) | Read-write property that defines if visible or hidden objects should be found. |

## Accessed From

[AssemblyComponentDefinition.CreateVisibleOccurrenceFinder](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateVisibleOccurrenceFinder.md), [WeldmentComponentDefinition.CreateVisibleOccurrenceFinder](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateVisibleOccurrenceFinder.md)

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |