# Centermarks Object

## Description

The Centermarks collection object provides access to all the center marks on a sheet and provides functionality to create new center marks.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../Centermarks/Centermarks_Add.md) | Method that creates a center mark relative to drawing geometry. This can result in a center mark at the origin of a punch center if the specified geometry is the edge of a punch and the AtPunchCenter argument is true. |
| [AddByCenterOfGravity](../Centermarks/Centermarks_AddByCenterOfGravity.md) | Method that creates a center mark at the center of gravity of the model in the input drawing view. This will fail in the case where the view does not contain any solid parts. |
| [AddByWorkFeature](../Centermarks/Centermarks_AddByWorkFeature.md) | Method that creates a center mark that represents the work feature within the drawing view. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Centermarks/Centermarks_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Centermarks/Centermarks_Count.md) | Property that returns the number of items in the collection. |
| [Item](../Centermarks/Centermarks_Item.md) | Method that returns the specified Centermark object from the collection. |
| [Type](../Centermarks/Centermarks_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.Centermarks](../Sheet/Sheet_Centermarks.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |