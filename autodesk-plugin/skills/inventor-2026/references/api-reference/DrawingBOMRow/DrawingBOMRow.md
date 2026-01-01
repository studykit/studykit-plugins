# DrawingBOMRow Object

## Description

The DrawingBOMRow object represents a row within the drawing BOM.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingBOMRow/DrawingBOMRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Ballooned](../DrawingBOMRow/DrawingBOMRow_Ballooned.md) | Property that returns whether the item represented by this row in the drawing BOM has been ballooned in the drawing. |
| [BOMRow](../DrawingBOMRow/DrawingBOMRow_BOMRow.md) | Property that returns the corresponding BOMRow from the model. |
| [Count](../DrawingBOMRow/DrawingBOMRow_Count.md) | Property that specifies the number of items in the collection. |
| [Custom](../DrawingBOMRow/DrawingBOMRow_Custom.md) | Property that returns whether this row is a custom row. |
| [Item](../DrawingBOMRow/DrawingBOMRow_Item.md) |  |
| [Parent](../DrawingBOMRow/DrawingBOMRow_Parent.md) | Property that returns the parent DrawingBOM object. |
| [Type](../DrawingBOMRow/DrawingBOMRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Virtual](../DrawingBOMRow/DrawingBOMRow_Virtual.md) | Property that returns whether this row references a virtual component in the assembly. |

## Accessed From

[BalloonValueSet.ReferencedRow](../BalloonValueSet/BalloonValueSet_ReferencedRow.md), [DrawingBOMRows.Item](../DrawingBOMRows/DrawingBOMRows_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |

## Version

Introduced in version 2009
