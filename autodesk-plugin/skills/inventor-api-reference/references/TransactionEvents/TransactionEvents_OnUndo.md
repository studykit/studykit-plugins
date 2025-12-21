# TransactionEvents.OnUndo Event

Parent Object: [TransactionEvents](../TransactionEvents/TransactionEvents.md)

## Description

The OnUndo event notifies a client when an undo operation is being performed.

## Syntax

TransactionEvents.**OnUndo**( ***TransactionObject*** As [Transaction](../Transaction/Transaction.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransactionObject | [Transaction](../Transaction/Transaction.md) | The Transaction object being undone. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is sent before and after the transaction is undone. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |