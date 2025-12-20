# CutDefinition.SetToNextExtent Method

Parent Object: [CutDefinition](../CutDefinition/CutDefinition.md)

## Description

Method that changes the extent to be a 'to next' extent.

## Remarks

Calling this method for a CutDefinition object that was obtained from an existing cut feature will cause the cut feature to update with the change.

## Syntax

CutDefinition.**SetToNextExtent**( ***Direction*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Direction | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input PartFeatureExtentDirectionEnum value to indicate which side of the sketch the cut should be. kPositiveExtentDirection and kNegativeExtentDirection are valid values. The value kPositiveExtentDirection defines the cut direction to be in the same direction as the normal of the sketch plane. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |