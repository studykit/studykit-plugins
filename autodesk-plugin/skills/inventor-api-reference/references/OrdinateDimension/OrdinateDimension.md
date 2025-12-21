# OrdinateDimension Object

Derived from: [DrawingDimension](../DrawingDimension/DrawingDimension.md) Object

## Description

The OrdinateDimension object represents an ordinate dimension placed on a sheet. The properties and methods listed below are in addition to those supported by the DrawingDimension object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OrdinateDimension/OrdinateDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../OrdinateDimension/OrdinateDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../OrdinateDimension/OrdinateDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetInspectionDimensionData](../OrdinateDimension/OrdinateDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OrdinateDimension/OrdinateDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../OrdinateDimension/OrdinateDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../OrdinateDimension/OrdinateDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../OrdinateDimension/OrdinateDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [DimensionType](../OrdinateDimension/OrdinateDimension_DimensionType.md) | Property that returns the dimension type. |
| [HideValue](../OrdinateDimension/OrdinateDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [Intent](../OrdinateDimension/OrdinateDimension_Intent.md) | Read-write property that gets and sets the geometry associated with the dimension. |
| [IsInspectionDimension](../OrdinateDimension/OrdinateDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [IsOrdinateSetMember](../OrdinateDimension/OrdinateDimension_IsOrdinateSetMember.md) | Property that returns whether this dimension is a member of an ordinate dimension set. If this property returns True, the OrdinateDimensionSet object is returned by the OrdinateDimensionSet property. |
| [JogPointOne](../OrdinateDimension/OrdinateDimension_JogPointOne.md) | Read-write property that gets and sets the first jog point for the ordinate dimension. |
| [JogPointTwo](../OrdinateDimension/OrdinateDimension_JogPointTwo.md) | Read-write property that gets and sets the second jog point for the ordinate dimension. |
| [Layer](../OrdinateDimension/OrdinateDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [ModelValue](../OrdinateDimension/OrdinateDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../OrdinateDimension/OrdinateDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OrdinateDimensionSet](../OrdinateDimension/OrdinateDimension_OrdinateDimensionSet.md) | Property that returns the OrdinateDimensionSet that owns this dimension. This property returns nothing if this dimension is not an ordinate dimension set member. This can be checked using the IsOrdinateSetMember property. |
| [OverrideModelValue](../OrdinateDimension/OrdinateDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../OrdinateDimension/OrdinateDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../OrdinateDimension/OrdinateDimension_Precision.md) | Gets and sets the Precision setting. |
| [Style](../OrdinateDimension/OrdinateDimension_Style.md) | Read-write property that gets and sets the dimension style used for this dimension. |
| [Text](../OrdinateDimension/OrdinateDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../OrdinateDimension/OrdinateDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../OrdinateDimension/OrdinateDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../OrdinateDimension/OrdinateDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[OrdinateDimensions.Add](../OrdinateDimensions/OrdinateDimensions_Add.md), [OrdinateDimensions.Item](../OrdinateDimensions/OrdinateDimensions_Item.md), [OrdinateDimensionsEnumerator.Item](../OrdinateDimensionsEnumerator/OrdinateDimensionsEnumerator_Item.md), [OrdinateDimensionSet.AddMember](../OrdinateDimensionSet/OrdinateDimensionSet_AddMember.md), [OrdinateDimensionSet.OriginMember](../OrdinateDimensionSet/OrdinateDimensionSet_OriginMember.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |