# DerivedAssemblyDefinition.GetHolePatchingOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that returns the hole patching options for the derived assembly.

## Syntax

DerivedAssemblyDefinition.**GetHolePatchingOptions**( ***HolePatchType*** As [DerivedHolePatchEnum](../DerivedHolePatchEnum.md), ***MinimumPerimeter*** As Double, ***MaximumPerimeter*** As Double, ***Reserved*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePatchType | [DerivedHolePatchEnum](../DerivedHolePatchEnum.md) | Output DerivedHolePatchEnum that specifies the holes to patch. Valid values are kDerivedPatchNone, kDerivedPatchAll and kDerivedPatchRange. If kDerivedPatchRange is returned, the MinimumPerimeter and MaximumPerimeter values define the range. |
| MinimumPerimeter | Double | Output Double that specifies the minimum perimeter value if the HolePatchType is specified to be kDerivedPatchRange. |
| MaximumPerimeter | Double | Output Double that specifies the maximum perimeter value if the HolePatchType is specified to be kDerivedPatchRange. |
| Reserved | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | For future use. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |