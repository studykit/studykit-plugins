# CropOperations.Add Method

Parent Object: [CropOperations](../CropOperations/CropOperations.md)

## Description

Method that adds a crop to a drawing view. The newly created CropOperation object is returned.

## Syntax

CropOperations.**Add**( ***UseCircularBoundaryType*** As Boolean, ***BoundaryCenterOrCornerOne*** As [Point2d](../Point2d/Point2d.md), ***BoundaryRadiusOrCornerTwo*** As Variant, [***DisplayCropCutLine***] As Boolean, [***Options***] As Variant ) As [CropOperation](../CropOperation/CropOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UseCircularBoundaryType | Boolean | Input Boolean value that specifies whether to use the circular boundary type or rectangular boundary type. |
| BoundaryCenterOrCornerOne | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the circular boundary center or rectangular boundary corner one. If the UseCircularBoundaryType is set to True then this is the circular boundary center, otherwise this is the rectangular boundary corner one. |
| BoundaryRadiusOrCornerTwo | Variant | Input double that specifies the radius of a circular boundary or input Point2d object that specifies the second corner for a rectangular boundary. If the UseCircularBoundaryType is set to True then this is the circular boundary radius, otherwise this is the rectangular boundary corner two. |
| DisplayCropCutLine | Boolean | Optional input Boolean value that specifies whether to display the crop cut line or not. If not provided this default to True. |
| Options | Variant | Reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |