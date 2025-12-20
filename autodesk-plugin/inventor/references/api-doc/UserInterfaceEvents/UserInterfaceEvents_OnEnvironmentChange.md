# UserInterfaceEvents.OnEnvironmentChange Event

Parent Object: [UserInterfaceEvents](../UserInterfaceEvents/UserInterfaceEvents.md)

## Description

The OnEnvironmentChange event notifies the client when the active environment switches from one environment to another.

## Remarks

Many end-user actions can cause the environment to change. This notification is sent regardless of what triggered the environment change. When the environment changes, this notification will be sent four times; a before and after notification for the environment that was active before the change and is being suspended or terminated and a before and after notification for the environment that is becoming the active environment. In the context of environment change, Inventor considers an environment to be tied with a particular document. For example, Inventor defines a single Part environment but if you have two part documents open there is a unique Part environment associated with each document. This means that the OnEnvironmentChange event notification is sent if the end-user should switch between the two part documents.

## Syntax

UserInterfaceEvents.**OnEnvironmentChange**( ***Environment*** As [Environment](../Environment/Environment.md), ***EnvironmentState*** As [EnvironmentStateEnum](../EnvironmentStateEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Environment | [Environment](../Environment/Environment.md) | The environment object whose state is changing. |
| EnvironmentState | [EnvironmentStateEnum](../EnvironmentStateEnum.md) | Indicates the transition state the environment is going through. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the environment change. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about the event. Name = "Document". Value = The Document object this environment is associated with. Name = "Reason for event". Value = "Undo" or "Redo". The activation of environments is transacted so environments can be activated as a result of an undo or redo operation. If this value is " " then the activation is occurring from an explicit action either from the end-user or through the API. If this value is "Undo" then the activation occurred as the result of an undo operation and if it is "Redo" then it is the result of a redo operation. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. You can cancel the environment change by changing this value to kEventCanceled. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |