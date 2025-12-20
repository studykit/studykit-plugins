# TransactionManager Object

## Description

The TransactionManager object encapsulates all of the transaction-based functionality. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearAllTransactions](../TransactionManager/TransactionManager_ClearAllTransactions.md) | Method that clears all the transactions in the committed and undone stacks. After this method is called a user may no longer Undo/Redo until another transaction is committed. This method fails if an identified transaction is in progress. |
| [GoToCheckPoint](../TransactionManager/TransactionManager_GoToCheckPoint.md) | Aborts back up to the checkpoint specified. |
| [RedoTransaction](../TransactionManager/TransactionManager_RedoTransaction.md) | Redoes the transaction following the current (if that had been undone). |
| [SetCheckPoint](../TransactionManager/TransactionManager_SetCheckPoint.md) | Sets a bookmark in the current transaction in progress. |
| [StartTransaction](../TransactionManager/TransactionManager_StartTransaction.md) | Starts a new transaction. |
| [StartTransactionForDocumentOpen](../TransactionManager/TransactionManager_StartTransactionForDocumentOpen.md) | Start a transaction that wraps a document open or new document operation. |
| [UndoTransaction](../TransactionManager/TransactionManager_UndoTransaction.md) | Undoes the current transaction. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TransactionManager/TransactionManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CommittedTransactions](../TransactionManager/TransactionManager_CommittedTransactions.md) | Gets the collection of all committed transactions currently held by the system. These can be undone in reverse sequence. |
| [CurrentTransaction](../TransactionManager/TransactionManager_CurrentTransaction.md) | Gets the current transaction in progress. |
| [Parent](../TransactionManager/TransactionManager_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [TransactionEvents](../TransactionManager/TransactionManager_TransactionEvents.md) | Gets the object that will fire transaction events. |
| [Type](../TransactionManager/TransactionManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UndoneTransactions](../TransactionManager/TransactionManager_UndoneTransactions.md) | Gets the collection of all currently undone transactions. These can be redone in forward sequence. |

## Accessed From

[Application.TransactionManager](../Application/Application_TransactionManager.md), [CheckPoint.Parent](../CheckPoint/CheckPoint_Parent.md), [InventorServer.TransactionManager](InventorServer_TransactionManager.md), [InventorServerObject.TransactionManager](InventorServerObject_TransactionManager.md), [Transaction.Parent](../Transaction/Transaction_Parent.md), [TransactionEvents.Parent](../TransactionEvents/TransactionEvents_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |