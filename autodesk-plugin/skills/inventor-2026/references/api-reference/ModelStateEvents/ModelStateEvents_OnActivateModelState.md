# ModelStateEvents.OnActivateModelState Event

Parent Object: [ModelStateEvents](../ModelStateEvents/ModelStateEvents.md)

## Description

Event that fires when a model state is activated.

## Remarks

OnActivateModelState won't be triggered when activate or deactivate a substitute model state but the OnActivateDocument should be used to monitor this action instead. Please refer to [ModelStates](ModelStates_Overview.md) for more info about model states behavior.

## Syntax

ModelStateEvents.**OnActivateModelState**( ***DocumentObject*** As [Document](../Document/Document.md), ***ModelState*** As [ModelState](../ModelState/ModelState.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the model state is being activated within. |
| ModelState | [ModelState](../ModelState/ModelState.md) | The model state that is being activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the model state has been activated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2022
