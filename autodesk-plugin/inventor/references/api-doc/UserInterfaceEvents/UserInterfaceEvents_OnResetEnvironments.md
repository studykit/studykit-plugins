# UserInterfaceEvents.OnResetEnvironments Event

Parent Object: [UserInterfaceEvents](../UserInterfaceEvents/UserInterfaceEvents.md)

## Description

The OnResetEnvironments event notifies the client when environments have been reset.

## Remarks

The end-user resets environments using the "Reset" and "Reset All" buttons on the Environments tab of the Customize dialog. \* The "Reset" button on the Environments tab will cause this notification to be sent for the currently selected environment. \* The "Reset All" button causes this notification to be sent where the Environments argument will contain all of the existing environments. When an environment is reset it is set back the default state, but the environment is not deleted. The primary use of this notification is to allow add-ins to reconfigure their environments after a reset has occurred. In most cases this will involved performing the same actions that the add-in performed when it was initialized and the FirstTime argument is True. The exception is the creation of the environment since they are not deleted as a result of the reset. Only the configuration of the environment needs to be performed. Event that is fired when the end user clicks the Reset button in the UI customization dialog. Typically, the client application should then perform the following actions. \* Populate custom environments. \* Populate custom toolbars. \* Modify Inventor environments. \* Modify Inventor toolbars.

## Syntax

UserInterfaceEvents.**OnResetEnvironments**( ***Environments*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Environments | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | A collection of the Environment objects that have been reset. In the case where the end-user uses the "Reset" button this collection will contain a single Environment object. If the "Reset All" button is pressed this collection contains all of the Environment objects. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about the event. No context information is provided for this event. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |