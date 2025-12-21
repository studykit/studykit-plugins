# ApplicationEvents.OnRestart32BitHost Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

This event is fired when the 32BitHost process is restarted. This process is used to host 32-bit processes when running 64-bit Inventor. The primary use of this is to host VBA, which is currently only a 32-bit process.

## Remarks

This event is primarily used for internal needs. It is not implemented in the 32-bit version of Inventor.

## Syntax

ApplicationEvents.**OnRestart32BitHost**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) |  |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) |  |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) |  |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |