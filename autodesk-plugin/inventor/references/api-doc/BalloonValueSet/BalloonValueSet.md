# BalloonValueSet Object

## Description

The BalloonValueSet object allows for setting and overriding of balloon content.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BalloonValueSet/BalloonValueSet_Delete.md) | Deletes this BalloonValueSet object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BalloonValueSet/BalloonValueSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ItemNumber](../BalloonValueSet/BalloonValueSet_ItemNumber.md) | Returns the associated item number. |
| [OverrideValue](../BalloonValueSet/BalloonValueSet_OverrideValue.md) | Gets and sets the override value of the balloon. |
| [Parent](../BalloonValueSet/BalloonValueSet_Parent.md) | Property returning the parent balloon. |
| [ReferencedRow](../BalloonValueSet/BalloonValueSet_ReferencedRow.md) | Property that returns the referenced DrawingBOMRow object. |
| [Static](../BalloonValueSet/BalloonValueSet_Static.md) | Gets and sets whether the Value property has been overridden. |
| [Type](../BalloonValueSet/BalloonValueSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../BalloonValueSet/BalloonValueSet_Value.md) | Gets and sets the value of the balloon. This value corresponds to the item number of a row in a parts list if any have been created. |

## Accessed From

[BalloonValueSets.Add](../BalloonValueSets/BalloonValueSets_Add.md), [BalloonValueSets.Item](../BalloonValueSets/BalloonValueSets_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Balloons - edit](../../sample-programs/Balloons_Sample.md) | This sample demonstrates the editing of balloons in a drawing. |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |