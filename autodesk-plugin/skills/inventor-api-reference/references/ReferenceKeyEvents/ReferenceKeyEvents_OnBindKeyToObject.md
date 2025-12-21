# ReferenceKeyEvents.OnBindKeyToObject Event

Parent Object: [ReferenceKeyEvents](../ReferenceKeyEvents/ReferenceKeyEvents.md)

## Description

Event that fires when either the BindKeyToObject or CanBindKeyToObject method of the ReferenceKeyManager object is called with a custom reference key.

## Syntax

ReferenceKeyEvents.**OnBindKeyToObject**( ***ReferenceKey***() As Byte, ***Document*** As Object, ***Object*** As Object, ***MatchType*** As [SolutionNatureEnum](../SolutionNatureEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKey | Byte | Input array of Bytes that contains the reference key. |
| Document | Object | The document object that the client obtained the ReferenceKeyManager object from and called the BindKeyToObject or CanBindKeyToObject method. |
| Object | Object | Output object that was found as a result of binding the provided reference key. The initial value of this argument is Nothing. In the case of multiple matches, the client should return an ObjectCollection containing all the candidate matches. The primary match is always the first member of this collection. Except for the first element, the order is not significant. |
| MatchType | [SolutionNatureEnum](../SolutionNatureEnum.md) | Output SolutionNatureEnum that returns the nature of the solution that was found. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Not currently used. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates if you are handling the event. kEventNotHandled indicates that the reference key is not yours and you’re not handling the binding. kEventHandled indicates that the reference key is yours and you are handling the binding. Even if the binding is unsuccessful you should return kEventHandled but with a match type of kNoSolution. |

## Version

Introduced in version 2012
