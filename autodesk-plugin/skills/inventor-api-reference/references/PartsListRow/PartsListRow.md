# PartsListRow Object

## Description

The PartsListRow object represents a row in a parts list table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Remove](../PartsListRow/PartsListRow_Remove.md) | Method that removes this row from the parts list. This method works only for custom rows. |
| [Reposition](../PartsListRow/PartsListRow_Reposition.md) | Method that repositions the row within the parts list. |
| [SaveItemOverridesToBOM](../PartsListRow/PartsListRow_SaveItemOverridesToBOM.md) | Saves any overrides to the item values in the balloon to the model BOM. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartsListRow/PartsListRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Ballooned](../PartsListRow/PartsListRow_Ballooned.md) | Property that returns whether the item represented by this row in the parts list has been ballooned. |
| [Count](../PartsListRow/PartsListRow_Count.md) | Property that returns the number of items in this collection. |
| [Custom](../PartsListRow/PartsListRow_Custom.md) | Property that returns whether this row is a custom row. |
| [Expandable](../PartsListRow/PartsListRow_Expandable.md) | Property that returns whether this row is a nested one. (i.e. it references an assembly.) |
| [Expanded](../PartsListRow/PartsListRow_Expanded.md) | Gets or sets whether this row is expanded if this row is a nested one i.e. it references an assembly. |
| [Height](../PartsListRow/PartsListRow_Height.md) | Gets and sets the height of the parts list row. |
| [Item](../PartsListRow/PartsListRow_Item.md) | Returns the specified PartsListCells object from the collection. This is the default property of the PartsListCells collection object. |
| [Parent](../PartsListRow/PartsListRow_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [ReferencedRows](../PartsListRow/PartsListRow_ReferencedRows.md) | Property that returns an enumerator of DrawingBOMRow objects. |
| [Type](../PartsListRow/PartsListRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../PartsListRow/PartsListRow_Visible.md) | Gets and sets whether the row is visible. |

## Accessed From

[PartsListRows.Add](../PartsListRows/PartsListRows_Add.md), [PartsListRows.Item](../PartsListRows/PartsListRows_Item.md)

## Version

Introduced in version 5.3
