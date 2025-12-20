# CheckPoint Object

## Description

The CheckPoint object serves as a bookmark within a transaction. See the article in the overviews section.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CheckPoint/CheckPoint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContainingTransaction](../CheckPoint/CheckPoint_ContainingTransaction.md) | Gets the transaction in which this check point is defined. |
| [DisplayName](../CheckPoint/CheckPoint_DisplayName.md) | Gets the user-friendly display name of this check point. |
| [Id](../CheckPoint/CheckPoint_Id.md) | Gets the numeric identifier of this check point. |
| [Parent](../CheckPoint/CheckPoint_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../CheckPoint/CheckPoint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CheckPointsEnumerator.Item](../CheckPointsEnumerator/CheckPointsEnumerator_Item.md), [TransactionManager.SetCheckPoint](../TransactionManager/TransactionManager_SetCheckPoint.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |