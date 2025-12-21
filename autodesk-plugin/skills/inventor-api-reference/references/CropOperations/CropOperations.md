# CropOperations Object

## Description

CropOperations object represents all crop operations applied to a drawing view.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../CropOperations/CropOperations_Add.md) | Method that adds a crop to a drawing view. The newly created CropOperation object is returned. |
| [AddBySketch](../CropOperations/CropOperations_AddBySketch.md) | Method that adds a crop to a drawing view. The newly created CropOperation object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CropOperations/CropOperations_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../CropOperations/CropOperations_Count.md) | Gets the number of items in this collection. |
| [Item](../CropOperations/CropOperations_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../CropOperations/CropOperations_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DetailDrawingView.CropOperations](../DetailDrawingView/DetailDrawingView_CropOperations.md), [DrawingView.CropOperations](../DrawingView/DrawingView_CropOperations.md), [SectionDrawingView.CropOperations](../SectionDrawingView/SectionDrawingView_CropOperations.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CropOperation creation sample](../../sample-programs/CropOperationCreationSample_Sample.md) | This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view. |

## Version

Introduced in version 2025.1
