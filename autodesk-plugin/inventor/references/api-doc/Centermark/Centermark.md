# Centermark Object

## Description

The Centermark object represents a center mark on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Centermark/Centermark_Delete.md) | Method that deletes the Centermark. |
| [GetReferenceKey](../Centermark/Centermark_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Centermark/Centermark_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../Centermark/Centermark_Attached.md) | Property that returns whether the centermark is sick. Returns False if the centermark is sick. |
| [AttachedEntity](../Centermark/Centermark_AttachedEntity.md) | Property that returns the entity the center mark is associated with. |
| [AttributeSets](../Centermark/Centermark_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Centerlines](../Centermark/Centermark_Centerlines.md) | Property that returns the a collection of associated Centerline objects. |
| [CentermarkType](../Centermark/Centermark_CentermarkType.md) | Property that gets the centermark type. |
| [ExtensionLinesVisible](../Centermark/Centermark_ExtensionLinesVisible.md) | Read-write property that gets and sets whether the extension lines associated with this center mark are visible or not. |
| [ExtensionPointFour](../Centermark/Centermark_ExtensionPointFour.md) | Read-write property that gets and sets the position of the center mark extension point. This property can return Nothing in the case where the extension lines have been turned off or the end of the extension line is clipped of as the result of a broken view. |
| [ExtensionPointFourDirection](../Centermark/Centermark_ExtensionPointFourDirection.md) | Property that returns the direction of the extension point. This can be used to understand the direction the fourth extension point can be moved. |
| [ExtensionPointOne](../Centermark/Centermark_ExtensionPointOne.md) | Read-write property that gets and sets the position of the center mark extension point. This property can return Nothing in the case where the extension lines have been turned off or the end of the extension line is clipped of as the result of a broken view. |
| [ExtensionPointOneDirection](../Centermark/Centermark_ExtensionPointOneDirection.md) | Property that returns the direction of the extension point. This can be used to understand the direction the first extension point can be moved. |
| [ExtensionPointThree](../Centermark/Centermark_ExtensionPointThree.md) | Read-write property that gets and sets the position of the center mark extension point. This property can return Nothing in the case where the extension lines have been turned off or the end of the extension line is clipped of as the result of a broken view. |
| [ExtensionPointThreeDirection](../Centermark/Centermark_ExtensionPointThreeDirection.md) | Property that returns the direction of the extension point. This can be used to understand the direction the third extension point can be moved. |
| [ExtensionPointTwo](../Centermark/Centermark_ExtensionPointTwo.md) | Read-write property that gets and sets the position of the center mark extension point. This property can return Nothing in the case where the extension lines have been turned off or the end of the extension line is clipped of as the result of a broken view. |
| [ExtensionPointTwoDirection](../Centermark/Centermark_ExtensionPointTwoDirection.md) | Property that returns the direction of the extension point. This can be used to understand the direction the second extension point can be moved. |
| [Layer](../Centermark/Centermark_Layer.md) | Gets and sets the layer associated with this object. |
| [Parent](../Centermark/Centermark_Parent.md) | Property that returns the parent Sheet object. |
| [Position](../Centermark/Centermark_Position.md) | Property that returns the position of the center of the center mark on the sheet. |
| [Style](../Centermark/Centermark_Style.md) | Gets and sets the style associated with this center mark. |
| [Type](../Centermark/Centermark_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../Centermark/Centermark_Visible.md) | Read-write property that gets and sets whether the center mark is visible. |

## Accessed From

[Centermarks.Add](../Centermarks/Centermarks_Add.md), [Centermarks.AddByCenterOfGravity](../Centermarks/Centermarks_AddByCenterOfGravity.md), [Centermarks.AddByWorkFeature](../Centermarks/Centermarks_AddByWorkFeature.md), [Centermarks.Item](../Centermarks/Centermarks_Item.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |