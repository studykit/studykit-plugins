# CropOperation Object

## Description

CropOperation object represents a crop applied to a drawing view.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CropOperation/CropOperation_Delete.md) | Method that deletes the CropOperation. |
| [GetReferenceKey](../CropOperation/CropOperation_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CropOperation/CropOperation_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../CropOperation/CropOperation_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [CropBoundarySketch](../CropOperation/CropOperation_CropBoundarySketch.md) | Read-only property that returns the drawing sketch used to specify the boundary for crop operation. |
| [DisplayCropCutLine](../CropOperation/CropOperation_DisplayCropCutLine.md) | Read-write property that gets and sets whether to display the crop cut line or not. |
| [Parent](../CropOperation/CropOperation_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Style](../CropOperation/CropOperation_Style.md) | Read-write property that gets and sets the view annotation style for this CropOperation. |
| [Type](../CropOperation/CropOperation_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[CropOperations.Add](../CropOperations/CropOperations_Add.md), [CropOperations.AddBySketch](../CropOperations/CropOperations_AddBySketch.md), [CropOperations.Item](../CropOperations/CropOperations_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CropOperation creation sample](../../sample-programs/CropOperationCreationSample_Sample.md) | This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |