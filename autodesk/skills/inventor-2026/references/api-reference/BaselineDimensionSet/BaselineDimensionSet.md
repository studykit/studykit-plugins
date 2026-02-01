# BaselineDimensionSet Object

## Description

The BaselineDimensionSet object represents a baseline dimension set placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddMember](../BaselineDimensionSet/BaselineDimensionSet_AddMember.md) | Method that adds a member to the baseline set and returns a LinearGeneralDimension object. If an existing LinearGeneralDimension is input into the method, the same object is returned. |
| [ArrangeText](../BaselineDimensionSet/BaselineDimensionSet_ArrangeText.md) | Method that automatically arranges the text of all members. |
| [Delete](../BaselineDimensionSet/BaselineDimensionSet_Delete.md) | Method that deletes the BaselineDimensionSet. |
| [DetachMember](../BaselineDimensionSet/BaselineDimensionSet_DetachMember.md) | Method that detaches the member from the set. The member is not deleted, it is merely converted into a vanilla linear general dimension. |
| [GetReferenceKey](../BaselineDimensionSet/BaselineDimensionSet_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BaselineDimensionSet/BaselineDimensionSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BaselineDimensionSet/BaselineDimensionSet_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionType](../BaselineDimensionSet/BaselineDimensionSet_DimensionType.md) | Property that returns the dimension type of the baseline set. Possible values are kAlignedDimensionType, kHorizontalDimensionType and kVerticalDimensionType. |
| [Layer](../BaselineDimensionSet/BaselineDimensionSet_Layer.md) | Gets and sets the layer for the dimension set. |
| [Members](../BaselineDimensionSet/BaselineDimensionSet_Members.md) | Property that returns all the member LinearGeneralDimension objects. |
| [Origin](../BaselineDimensionSet/BaselineDimensionSet_Origin.md) | Gets and sets the origin for the baseline dimension set. |
| [Parent](../BaselineDimensionSet/BaselineDimensionSet_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../BaselineDimensionSet/BaselineDimensionSet_Precision.md) | Gets and sets the number of decimal places displayed for all the members in this set. |
| [Style](../BaselineDimensionSet/BaselineDimensionSet_Style.md) | Gets and sets the dimension style used for this dimension set. |
| [Type](../BaselineDimensionSet/BaselineDimensionSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BaselineDimensionSets.Add](../BaselineDimensionSets/BaselineDimensionSets_Add.md), [BaselineDimensionSets.Item](../BaselineDimensionSets/BaselineDimensionSets_Item.md), [LinearGeneralDimension.BaselineDimensionSet](../LinearGeneralDimension/LinearGeneralDimension_BaselineDimensionSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |

## Version

Introduced in version 2010
