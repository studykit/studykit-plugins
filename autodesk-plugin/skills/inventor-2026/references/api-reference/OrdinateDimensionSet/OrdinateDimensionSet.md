# OrdinateDimensionSet Object

## Description

The OrdinateDimensionSet object represents an ordinate dimension set placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddMember](../OrdinateDimensionSet/OrdinateDimensionSet_AddMember.md) | Method that adds a member to the ordinate set and returns an OrdinateDimension object that represents the member. |
| [Delete](../OrdinateDimensionSet/OrdinateDimensionSet_Delete.md) | Method that deletes the OrdinateDimensionSet. |
| [GetReferenceKey](../OrdinateDimensionSet/OrdinateDimensionSet_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlignMembers](../OrdinateDimensionSet/OrdinateDimensionSet_AlignMembers.md) | Gets and sets whether to align the text and the jog points of all the members. |
| [AllowBrokenLeaders](../OrdinateDimensionSet/OrdinateDimensionSet_AllowBrokenLeaders.md) | Gets and sets whether to allow jog points (movable vertices) on the dimensions. |
| [Application](../OrdinateDimensionSet/OrdinateDimensionSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OrdinateDimensionSet/OrdinateDimensionSet_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContinuousRunning](../OrdinateDimensionSet/OrdinateDimensionSet_ContinuousRunning.md) | Gets and sets whether to display continuity line between the set members. |
| [DimensionType](../OrdinateDimensionSet/OrdinateDimensionSet_DimensionType.md) | Property that returns the dimension type of the ordinate set. Possible values are kAlignedDimensionType, kHorizontalDimensionType and kVerticalDimensionType. |
| [DirectionReversed](../OrdinateDimensionSet/OrdinateDimensionSet_DirectionReversed.md) | Gets and sets whether to reverse the direction of positive numbers. |
| [Layer](../OrdinateDimensionSet/OrdinateDimensionSet_Layer.md) | Gets and sets the layer for the dimension set. |
| [Members](../OrdinateDimensionSet/OrdinateDimensionSet_Members.md) | Property that returns all the member OrdinateDimension objects. |
| [OriginArrowheadType](../OrdinateDimensionSet/OrdinateDimensionSet_OriginArrowheadType.md) | Read-write property that gets and sets the arrowhead type for the origin member of the ordinate dimension set. |
| [OriginMember](../OrdinateDimensionSet/OrdinateDimensionSet_OriginMember.md) | Gets and sets the origin for the ordinate dimension set. |
| [Parent](../OrdinateDimensionSet/OrdinateDimensionSet_Parent.md) | Property that returns the parent sheet of the object. |
| [PositiveBothDirections](../OrdinateDimensionSet/OrdinateDimensionSet_PositiveBothDirections.md) | Gets and sets whether dimension values should be positive in both directions of the origin. |
| [Precision](../OrdinateDimensionSet/OrdinateDimensionSet_Precision.md) | Gets and sets the number of decimal places displayed for all the members in this set. |
| [ShowDirection](../OrdinateDimensionSet/OrdinateDimensionSet_ShowDirection.md) | Gets and sets whether to place an arrow on the origin dimension pointing in the positive direction. |
| [Style](../OrdinateDimensionSet/OrdinateDimensionSet_Style.md) | Gets and sets the dimension style used for this dimension set. |
| [Type](../OrdinateDimensionSet/OrdinateDimensionSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[OrdinateDimension.OrdinateDimensionSet](../OrdinateDimension/OrdinateDimension_OrdinateDimensionSet.md), [OrdinateDimensionSets.Add](../OrdinateDimensionSets/OrdinateDimensionSets_Add.md), [OrdinateDimensionSets.Item](../OrdinateDimensionSets/OrdinateDimensionSets_Item.md)

## Version

Introduced in version 2010
