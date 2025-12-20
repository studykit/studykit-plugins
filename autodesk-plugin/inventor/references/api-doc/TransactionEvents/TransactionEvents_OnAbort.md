# TransactionEvents.OnAbort Event

Parent Object: [TransactionEvents](../TransactionEvents/TransactionEvents.md)

## Description

The OnAbort event notifies the client when a transaction has been aborted.

## Remarks

An abort can happen in the case where a command has started a transaction and performed operations within that transaction but decides to abort the process rather than commit it.

## Syntax

TransactionEvents.**OnAbort**( ***TransactionObject*** As [Transaction](../Transaction/Transaction.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransactionObject | [Transaction](../Transaction/Transaction.md) | The Transaction object being aborted. When the BeforeOrAfter argument is kBefore this is the Transaction being aborted and it supports the full functionality of a Transaction object. When the BeforeOrAfter argument is kAfter the Transaction object no longer exists so the object provided by this argument is not functional except to compare its identity to another Transaction object. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is sent before and after the transaction is aborted. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |