# TransactionEvents Object

## Description

Inventor::TransactionEventsSink

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TransactionEvents/TransactionEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../TransactionEvents/TransactionEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../TransactionEvents/TransactionEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnAbort](../TransactionEvents/TransactionEvents_OnAbort.md) | The OnAbort event notifies the client when a transaction has been aborted. |
| [OnCommit](../TransactionEvents/TransactionEvents_OnCommit.md) | The OnCommit event notifies the client when a transaction has been committed. |
| [OnDelete](../TransactionEvents/TransactionEvents_OnDelete.md) | The OnDelete event notifies the client when a transaction has been deleted from the transaction stack. |
| [OnRedo](../TransactionEvents/TransactionEvents_OnRedo.md) | The OnRedo event notifies the client when a redo operation is being performed. |
| [OnUndo](../TransactionEvents/TransactionEvents_OnUndo.md) | The OnUndo event notifies a client when an undo operation is being performed. |

## Accessed From

[TransactionManager.TransactionEvents](../TransactionManager/TransactionManager_TransactionEvents.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |