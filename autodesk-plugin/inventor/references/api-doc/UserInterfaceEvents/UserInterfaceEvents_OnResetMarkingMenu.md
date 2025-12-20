# UserInterfaceEvents.OnResetMarkingMenu Event

Parent Object: [UserInterfaceEvents](../UserInterfaceEvents/UserInterfaceEvents.md)

## Description

Event that is fired when the user resets an individual or all radial marking menus.

## Syntax

UserInterfaceEvents.**OnResetMarkingMenu**( ***MarkingMenuInternalName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MarkingMenuInternalName | String | The internal name of the radial marking menu that was reset. In the case of an add-in created radial marking menu, the marking menu is deleted by Inventor and will need to be re-created by the add-in in response to this event. For built-in marking menus, this name can be used to obtain the existing marking menu and apply any desired modifications.  If the user has chosen to reset all marking menus then this argument will be an empty String. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about the event. No additional information is currently provided for this event. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |