# CutDefinition.SetThroughAllExtent Method

Parent Object: [CutDefinition](../CutDefinition/CutDefinition.md)

## Description

Method that changes the extent to be a 'to next' extent.

## Remarks

Calling this method for a CutDefinition object that was obtained from an existing cut feature will cause the cut feature to update with the change.

## Syntax

CutDefinition.**SetThroughAllExtent**( ***Direction*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Direction | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input PartFeatureExtentDirectionEnum value to indicate which side of the sketch the cut should be. The value kPositiveExtentDirection defines the cut direction to be in the same direction as the normal of the sketch plane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |