# iPartTableRow Object

## Description

The iPartTableRow object represents a row in the iPart factory table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../iPartTableRow/iPartTableRow_Copy.md) | Method that creates a new row with all values equal to the original row. |
| [Delete](../iPartTableRow/iPartTableRow_Delete.md) | Method that deletes this row in the factory. |
| [GetReferenceKey](../iPartTableRow/iPartTableRow_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iPartTableRow/iPartTableRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../iPartTableRow/iPartTableRow_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Count](../iPartTableRow/iPartTableRow_Count.md) | Property that returns the number of items in the collection. |
| [Index](../iPartTableRow/iPartTableRow_Index.md) | Property that returns the index of this row within the iPart factory table. |
| [IsPartNameBasedOnMemberName](../iPartTableRow/iPartTableRow_IsPartNameBasedOnMemberName.md) | Gets whether the member's filename is based on the member name or an explicitly set filename. |
| [Item](../iPartTableRow/iPartTableRow_Item.md) | Returns the specified iPartTableCell object from the collection. This is the default property of the iPartTableRow object. |
| [MemberName](../iPartTableRow/iPartTableRow_MemberName.md) | Property that returns the member name corresponding to this row in the iPart table. |
| [Parent](../iPartTableRow/iPartTableRow_Parent.md) | Property that returns the parent iPartFactory object. |
| [PartName](../iPartTableRow/iPartTableRow_PartName.md) | Gets the filename corresponding to this row in the iPart table. |
| [PartNameModifiable](../iPartTableRow/iPartTableRow_PartNameModifiable.md) | Property that returns whether the name of the document corresponding to this member can be modified. This property also returns False if the corresponding cell in Excel contains a formula. |
| [Type](../iPartTableRow/iPartTableRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iPartFactory.DefaultRow](../iPartFactory/iPartFactory_DefaultRow.md), [iPartMember.Row](../iPartMember/iPartMember_Row.md), [iPartTableRow.Copy](../iPartTableRow/iPartTableRow_Copy.md), [iPartTableRows.Item](../iPartTableRows/iPartTableRows_Item.md)

## Version

Introduced in version 6
