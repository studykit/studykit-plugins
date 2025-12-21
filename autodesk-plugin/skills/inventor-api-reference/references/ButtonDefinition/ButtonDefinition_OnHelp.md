# ButtonDefinition.OnHelp Event

Parent Object: [ButtonDefinition](../ButtonDefinition/ButtonDefinition.md)

## Description

Event that is fired when the user selects F1 while the progressive tooltip of this command is being displayed in the ribbon interface.

## Syntax

ButtonDefinition.**OnHelp**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Setting the value of the HandlingCode argument specifies how Inventor is to handle displaying help. If you set this argument to kEventNotHandled or kEventCanceled, Inventor will display some general help. Setting the value of this argument to kEventHandled will allow you to handle displaying help to the end-user and Inventor will not display anything. To display help to the end-user you can choose to use whatever help system you want. Inventor's API does not provide support for the actual display of the clients help. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |