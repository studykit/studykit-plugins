# Transaction Object

## Description

The Transaction object that stands for a single transaction. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Abort](../Transaction/Transaction_Abort.md) | Method that aborts this transaction. This method will fail if this transaction is not the current transaction. |
| [End](../Transaction/Transaction_End.md) | Method that ends this transaction. This method will fail if this transaction is not the current transaction. |
| [IdentifyForDocumentOpen](../Transaction/Transaction_IdentifyForDocumentOpen.md) | Identify the document open transaction. This action should precede the end of document open transaction. |
| [SuppressChangeNotifications](../Transaction/Transaction_SuppressChangeNotifications.md) | Method that sets whether the changes notifications within this transaction should be suppressed or not. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Transaction/Transaction_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CheckPoints](../Transaction/Transaction_CheckPoints.md) | Gets the enumeration of all of the check points that may be present in this transaction. |
| [ChildTransactions](../Transaction/Transaction_ChildTransactions.md) | Gets the enumeration of all of the child transactions that this transaction may contain. |
| [DisplayName](../Transaction/Transaction_DisplayName.md) | Gets the display name of this transaction. |
| [Document](../Transaction/Transaction_Document.md) | Gets the affected by this transaction. |
| [HasParentTransaction](../Transaction/Transaction_HasParentTransaction.md) | Gets the Boolean flag indicating if this transaction is a child of another transaction. |
| [Id](../Transaction/Transaction_Id.md) | Gets the unique identifier for this transaction. |
| [MergeWithPrevious](../Transaction/Transaction_MergeWithPrevious.md) | Gets and sets whether to merge this transaction with the previously committed transaction. |
| [Parent](../Transaction/Transaction_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [ParentTransaction](../Transaction/Transaction_ParentTransaction.md) | Property that returns the parent transaction, if one exists; else returns a NULL pointer. |
| [State](../Transaction/Transaction_State.md) | Property that returns a TransactionStateEnum that describes the current state of the transaction. |
| [Type](../Transaction/Transaction_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CheckPoint.ContainingTransaction](../CheckPoint/CheckPoint_ContainingTransaction.md), [Transaction.ParentTransaction](../Transaction/Transaction_ParentTransaction.md), [TransactionManager.CurrentTransaction](../TransactionManager/TransactionManager_CurrentTransaction.md), [TransactionManager.StartTransaction](../TransactionManager/TransactionManager_StartTransaction.md), [TransactionManager.StartTransactionForDocumentOpen](../TransactionManager/TransactionManager_StartTransactionForDocumentOpen.md), [TransactionsEnumerator.Item](../TransactionsEnumerator/TransactionsEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |

## Version

Introduced in version 4
