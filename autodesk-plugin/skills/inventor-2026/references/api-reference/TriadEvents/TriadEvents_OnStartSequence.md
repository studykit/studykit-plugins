# TriadEvents.OnStartSequence Event

Parent Object: [TriadEvents](../TriadEvents/TriadEvents.md)

## Description

Event that fires indicating the logical start of a sequence of triad moves.

## Syntax

TriadEvents.**OnStartSequence**( ***CoordinateSystem*** As [Matrix](../Matrix/Matrix.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CoordinateSystem | [Matrix](../Matrix/Matrix.md) | Returns a Matrix object indicating the triad's current position in model space. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9
