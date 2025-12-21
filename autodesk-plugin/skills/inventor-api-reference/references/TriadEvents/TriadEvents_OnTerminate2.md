# TriadEvents.OnTerminate2 Event

Parent Object: [TriadEvents](../TriadEvents/TriadEvents.md)

## Description

Fires when the triad is terminated.

## Syntax

TriadEvents.**OnTerminate2**( ***Cancelled*** As Boolean, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Cancelled | Boolean | Returns a Boolean indicating whether this sequence of moves was cancelled by the user. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |