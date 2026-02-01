# DockableWindowsEvents.OnHelp Event

Parent Object: [DockableWindowsEvents](../DockableWindowsEvents/DockableWindowsEvents.md)

## Description

Fires whenever the user clicks the help button in a dockable window.

## Syntax

DockableWindowsEvents.**OnHelp**( ***DockableWindow*** As [DockableWindow](../DockableWindow/DockableWindow.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DockableWindow | [DockableWindow](../DockableWindow/DockableWindow.md) | Input DockableWindow object that specifies the window on which the help button was pressed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Setting the value of the HandlingCode argument specifies how Inventor is to handle displaying help. If you set this argument to kEventNotHandled or kEventCanceled, Inventor will display some general help. Setting the value of this argument to kEventHandled will allow you to handle displaying help to the end-user and Inventor will not display anything. To display help to the end-user you can choose to use whatever help system you want. Inventor's API does not provide support for the actual display of the clients help. |

## Version

Introduced in version 2012
