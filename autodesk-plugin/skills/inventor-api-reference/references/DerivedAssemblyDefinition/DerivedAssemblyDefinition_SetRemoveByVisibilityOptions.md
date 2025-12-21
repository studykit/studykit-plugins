# DerivedAssemblyDefinition.SetRemoveByVisibilityOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that sets the simplification options specifying geometry to remove based on visibility.

## Syntax

DerivedAssemblyDefinition.**SetRemoveByVisibilityOptions**( ***GeometryToRemove*** As [DerivedGeometryRemovalEnum](../DerivedGeometryRemovalEnum.md), [***VisibilityPercentage***] As Long, [***IgnoreSurfaceFeatures***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometryToRemove | [DerivedGeometryRemovalEnum](../DerivedGeometryRemovalEnum.md) | Input that specifies what geometry to remove. Valid values are kDerivedRemoveNone, kDerivedRemovePartsOnly and kDerivedRemovePartsAndFaces. |
| VisibilityPercentage | Long | Optional input Long that specifies the visibility percentage value of parts/faces to be removed. For instance, a value of 0 indicates that parts/faces not visible in any view are to be removed. Valid range is 0 to 100. This input is required if GeometryToRemove is specified to be kDerivedRemovePartsOnly or kDerivedRemovePartsAndFaces. |
| IgnoreSurfaceFeatures | Boolean | Optional input Boolean that specifies whether to ignore surfaces in visibility detection and removal. If not specified, a default of True is assumed indicating that surfaces will be ignored.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |