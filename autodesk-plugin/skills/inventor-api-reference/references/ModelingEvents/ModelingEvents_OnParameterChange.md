# ModelingEvents.OnParameterChange Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

The OnParameterChange event notifies the client when a parameter is changed.

## Remarks

A parameter's value can be changed in many ways. This notification is sent for any change, regardless of what caused it. For example some ways that a parameter value can change are:

* An explicit edit by the end-user by editing the value in the Parameters dialog or editing the value of the associated dimension.
* Being driven through an adaptive assembly. For example, if the length of a part changes as other parts in an assembly are modified, a notification is sent when the parameter controlling the length is changed as a result of the adaptivity.
* Being changed as the result of an equation. For example, if there is a parameter A whose equation is "1.0" and parameter B whose equation is "A \* 2", any change to A will also cause B to change. In this case a notification will be sent for A and also for B since both of them will have changed.

## Syntax

ModelingEvents.**OnParameterChange**( ***DocumentObject*** As [Document](../Document/Document.md), ***Parameter*** As [Parameter](../Parameter/Parameter.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the parameter is contained within. |
| Parameter | [Parameter](../Parameter/Parameter.md) | The Parameter object that is being changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the value of the parameter is changed. Using the kBefore timing you can examine the parameter to determine its state before the change is applied and then compare it to the state when the timing is kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. When BeforeOrAfter is kBefore one of the following values is provided depending on what information associated with the parameter is changing:  * Name = "Value". Value = A String containing the new value of the parameter. This is provided if the value of the parameter is changed. This is the equivalent of the Value property of the parameter converted to a String, so it is in internal units. * Name = "Unit". Value = The String containing the new units of the parameter. This indicates that the unit of the parameter has been changed. * Name = "Name". Value = A String containing the new name of the parameter. This is provided if the name of the parameter is changed. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
