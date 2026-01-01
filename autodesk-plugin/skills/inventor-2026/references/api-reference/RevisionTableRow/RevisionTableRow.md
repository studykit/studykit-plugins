# RevisionTableRow Object

## Description

This object represents a row in the revision table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RevisionTableRow/RevisionTableRow_Delete.md) | Method that deletes the RevisionTableRow and any associated revision tags. |
| [Reposition](../RevisionTableRow/RevisionTableRow_Reposition.md) | Method that repositions the row within the revision table. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RevisionTableRow/RevisionTableRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../RevisionTableRow/RevisionTableRow_Count.md) | Property that returns the number of items in the collection. |
| [Custom](../RevisionTableRow/RevisionTableRow_Custom.md) | Gets whether this is a custom row. |
| [Height](../RevisionTableRow/RevisionTableRow_Height.md) | Gets/Sets the height of the RevisionTable row. |
| [IsActiveRow](../RevisionTableRow/RevisionTableRow_IsActiveRow.md) | Read-write property that gets and sets whether this is the active row of the revision table. When set this property it can only be set from False to True to make current RevisionTableRow the active row. |
| [Item](../RevisionTableRow/RevisionTableRow_Item.md) | Returns the specified Cell object from the collection. |
| [Parent](../RevisionTableRow/RevisionTableRow_Parent.md) | Property that returns the parent RevisionTable. |
| [Type](../RevisionTableRow/RevisionTableRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RevisionTableRow/RevisionTableRow_Visible.md) | Read-write property that gets and sets whether the row is visible. |

## Accessed From

[RevisionTableRows.Add](../RevisionTableRows/RevisionTableRows_Add.md), [RevisionTableRows.AddCustom](../RevisionTableRows/RevisionTableRows_AddCustom.md), [RevisionTableRows.Item](../RevisionTableRows/RevisionTableRows_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query revision table](../../sample-programs/RevisionTable_Sample.md) | This sample illustrates querying the contents of the revision table. |

## Version

Introduced in version 10
