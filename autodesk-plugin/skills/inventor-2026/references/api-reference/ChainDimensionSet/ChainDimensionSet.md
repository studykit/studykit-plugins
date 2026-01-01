# ChainDimensionSet Object

## Description

The ChainDimensionSet object represents a chain dimension set placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddMembers](../ChainDimensionSet/ChainDimensionSet_AddMembers.md) | Method that adds member(s) to the chain set based on the input geometry or dimension and returns the newly created member(s). |
| [Arrange](../ChainDimensionSet/ChainDimensionSet_Arrange.md) | Method that resets the chain dimension set such that all members are equidistant from the view boundary. Dimensions are aligned to the specified base dimension. |
| [Delete](../ChainDimensionSet/ChainDimensionSet_Delete.md) | Method that deletes the ChainDimensionSet. |
| [GetReferenceKey](../ChainDimensionSet/ChainDimensionSet_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MergeMembers](../ChainDimensionSet/ChainDimensionSet_MergeMembers.md) | Method that merges two members of the set by deleting the second member and healing (modifying) the first member to fill the gap. The input members must be contiguous, else the method will fail. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ChainDimensionSet/ChainDimensionSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ChainDimensionSet/ChainDimensionSet_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionType](../ChainDimensionSet/ChainDimensionSet_DimensionType.md) | Property that returns the dimension type of the chain set. Possible values are kAlignedDimensionType, kHorizontalDimensionType and kVerticalDimensionType. |
| [Layer](../ChainDimensionSet/ChainDimensionSet_Layer.md) | Read-write property that gets and sets the layer for the dimension set. |
| [Locked](../ChainDimensionSet/ChainDimensionSet_Locked.md) | Read-write property that gets and sets the lock status of the dimension set. |
| [Members](../ChainDimensionSet/ChainDimensionSet_Members.md) | Property that returns all the member LinearGeneralDimension objects. |
| [Parent](../ChainDimensionSet/ChainDimensionSet_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../ChainDimensionSet/ChainDimensionSet_Precision.md) | Read-write property that gets and sets the number of decimal places displayed for all the members in this set. Valid range of values is 0 to 8. |
| [Style](../ChainDimensionSet/ChainDimensionSet_Style.md) | Read-write property that gets and sets the dimension style used for this dimension set. |
| [Type](../ChainDimensionSet/ChainDimensionSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ChainDimensionSets.Add](../ChainDimensionSets/ChainDimensionSets_Add.md), [ChainDimensionSets.AddUsingBaseDimension](../ChainDimensionSets/ChainDimensionSets_AddUsingBaseDimension.md), [ChainDimensionSets.Item](../ChainDimensionSets/ChainDimensionSets_Item.md), [LinearGeneralDimension.ChainDimensionSet](../LinearGeneralDimension/LinearGeneralDimension_ChainDimensionSet.md)

## Version

Introduced in version 2011
