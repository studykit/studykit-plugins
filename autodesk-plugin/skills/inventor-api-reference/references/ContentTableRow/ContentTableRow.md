# ContentTableRow Object

## Description

The ContentTableRow object represents the row of the table associated with a particular content center family.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ContentTableRow/ContentTableRow_Delete.md) | Method that deletes this row from the table. Any changes to the table are not actually applied until the ContentFamily.Save method is called. |
| [GetCellValue](../ContentTableRow/ContentTableRow_GetCellValue.md) | This method returns value of cell specified by given index. Caller can specify particular custom parameters which will be used for expression evaluation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentTableRow/ContentTableRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContentIdentifier](../ContentTableRow/ContentTableRow_ContentIdentifier.md) | Property that returns the identifier for this object. This can be used with the GetContentObject method of the ContentCenter object to obtain this object at a later time. |
| [Count](../ContentTableRow/ContentTableRow_Count.md) | Property that returns the number of ContentTableCell objects in the collection. |
| [Index](../ContentTableRow/ContentTableRow_Index.md) | Property that returns the index of this row within the table. |
| [InternalName](../ContentTableRow/ContentTableRow_InternalName.md) | Property that returns the internal name of the ContentTableRow. The internal name uniquely identifies this row with respect to other rows in the family and it cannot be changed so it will remain consistent. |
| [IsSuppressed](../ContentTableRow/ContentTableRow_IsSuppressed.md) | Gets/sets the suppressed state of this row. |
| [Item](../ContentTableRow/ContentTableRow_Item.md) | Returns the specified ContentTableCell object from the collection. |
| [Parent](../ContentTableRow/ContentTableRow_Parent.md) | Property that returns the parent ContentFamily object. |
| [Type](../ContentTableRow/ContentTableRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContentTableRows.Add](../ContentTableRows/ContentTableRows_Add.md), [ContentTableRows.Item](../ContentTableRows/ContentTableRows_Item.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |