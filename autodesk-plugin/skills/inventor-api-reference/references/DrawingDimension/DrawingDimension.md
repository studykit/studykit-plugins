# DrawingDimension Object

## Description

The DrawingDimension object is the base class for all dimensions placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DrawingDimension/DrawingDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../DrawingDimension/DrawingDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../DrawingDimension/DrawingDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetInspectionDimensionData](../DrawingDimension/DrawingDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingDimension/DrawingDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../DrawingDimension/DrawingDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../DrawingDimension/DrawingDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../DrawingDimension/DrawingDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [HideValue](../DrawingDimension/DrawingDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [IsInspectionDimension](../DrawingDimension/DrawingDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../DrawingDimension/DrawingDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [ModelValue](../DrawingDimension/DrawingDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../DrawingDimension/DrawingDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../DrawingDimension/DrawingDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../DrawingDimension/DrawingDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../DrawingDimension/DrawingDimension_Precision.md) | Gets and sets the Precision setting. |
| [Text](../DrawingDimension/DrawingDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../DrawingDimension/DrawingDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../DrawingDimension/DrawingDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../DrawingDimension/DrawingDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionText.Parent](../DimensionText/DimensionText_Parent.md), [DrawingDimensions.Item](../DrawingDimensions/DrawingDimensions_Item.md)

## Derived Classes

[GeneralDimension](../GeneralDimension/GeneralDimension.md), [OrdinateDimension](../OrdinateDimension/OrdinateDimension.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Center Dimension Text](../../sample-programs/AngularGeneralDimension_CenterText_Sample.md) | This sample demonstrates how to center the text of all dimensions on the active sheet in a drawing. |
| [Aligning drawing dimensions](../../sample-programs/DrawingDimension_Text_Sample.md) | This sample demonstrates aligning the selected drawing dimensions along a horizontal or vertical axis. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |