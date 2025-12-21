# CropOperations.AddBySketch Method

Parent Object: [CropOperations](../CropOperations/CropOperations.md)

## Description

Method that adds a crop to a drawing view. The newly created CropOperation object is returned.

## Syntax

CropOperations.**AddBySketch**( ***CropBoundarySketch*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md), [***DisplayCropCutLine***] As Boolean, [***Reserved***] As Variant ) As [CropOperation](../CropOperation/CropOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CropBoundarySketch | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Input DrawingSketch that specifies the sketch with a loop as the boundary to crop the drawing view. |
| DisplayCropCutLine | Boolean | Optional input Boolean value that specifies whether to display the crop cut line or not. If not provided this default to True. |
| Reserved | Variant | Reserved for future use.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CropOperation creation sample](../../sample-programs/CropOperationCreationSample_Sample.md) | This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view. |

## Version

Introduced in version 2025.1
