# SearchBoxEvents.OnStopSearch Event

Parent Object: [SearchBoxEvents](../SearchBoxEvents/SearchBoxEvents.md)

## Description

Event that fires just after the search is stopped.

## Syntax

SearchBoxEvents.**OnStopSearch**( ***SearchResult*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SearchResult | [NameValueMap](../NameValueMap/NameValueMap.md) | Output Variant that indicates the search result. This is ignored if the HandlingCode is not set to kEventHandled. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. |

## Version

Introduced in version 2018
