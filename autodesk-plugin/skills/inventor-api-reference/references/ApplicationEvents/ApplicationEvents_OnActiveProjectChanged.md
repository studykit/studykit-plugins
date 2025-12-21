# ApplicationEvents.OnActiveProjectChanged Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Fires just before and soon after the active project is changed, supplying the context in which this action is being taken.

## Remarks

The OnActiveProjectChanged event notifies a client when a change has been made to the active project. The notification is sent for two different actions that are related to projects; a new project is activated and the active project is saved. This event provides the DesignProject object as a representative of the project. At this time, the DesignProject object is limited in the functionality it provides. In cases where you need more information about the project you may want to use the FileLocations object.

## Syntax

ApplicationEvents.**OnActiveProjectChanged**( ***ProjectObject*** As [DesignProject](../DesignProject/DesignProject.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ProjectObject | [DesignProject](../DesignProject/DesignProject.md) | The object that has been activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the document is activated. Notification is sent before and after the active project is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. This event provides additional information through the Context argument as described below: Name = "FileName". Value = Full filename of the ipj file that is being activated. Name = "Reason". Value = The reason the notification was made. Can be one of the following values: "ProjectActivated" or "ProjectSaved". |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 7
