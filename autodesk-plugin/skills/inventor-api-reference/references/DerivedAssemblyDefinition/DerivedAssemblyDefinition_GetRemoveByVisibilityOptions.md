# DerivedAssemblyDefinition.GetRemoveByVisibilityOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that returns the simplification options specifying geometry to remove based on visibility.

## Syntax

DerivedAssemblyDefinition.**GetRemoveByVisibilityOptions**( ***GeometryToRemove*** As [DerivedGeometryRemovalEnum](../DerivedGeometryRemovalEnum.md), ***VisibilityPercentage*** As Long, ***IgnoreSurfaceFeatures*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometryToRemove | [DerivedGeometryRemovalEnum](../DerivedGeometryRemovalEnum.md) | Output that specifies what geometry to remove. Valid values are kDerivedRemoveNone, kDerivedRemovePartsOnly and kDerivedRemovePartsAndFaces. |
| VisibilityPercentage | Long | Output Long that specifies the visibility percentage value of parts/faces to be removed. For instance, a value of 0 indicates that parts/faces not visible in any view are to be removed. Valid range is 0 to 100. This value returns 0 and should be ignored if GeometryToRemove returns kDerivedRemoveNone. |
| IgnoreSurfaceFeatures | Boolean | Output Boolean that specifies whether to ignore surfaces in visibility detection and removal. This value returns True and should be ignored if GeometryToRemove returns kDerivedRemoveNone. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |