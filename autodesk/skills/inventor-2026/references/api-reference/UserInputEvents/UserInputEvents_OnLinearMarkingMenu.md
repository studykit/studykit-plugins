# UserInputEvents.OnLinearMarkingMenu Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

Fires before the overflow context menu is displayed to the user.

## Syntax

UserInputEvents.**OnLinearMarkingMenu**( ***SelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***LinearMenu*** As [CommandControls](../CommandControls/CommandControls.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Input ObjectsEnumerator that contains the selected entities. This is the same set of entities currently contained in the document’s SelectSet. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) | Input constant denoting whether the menu was invoked via a click in a graphics window (kGraphicsWindowSelection) or by a click in the browser (kBrowserSelection). |
| LinearMenu | [CommandControls](../CommandControls/CommandControls.md) | Input/Output CommandControls object. This object represents the contents of the linear menu that will be displayed to the user. Using the functionality of the CommandControls object you can iterate over the current contents and add and remove items from the menu. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about why the menu is being displayed. This is currently empty. |

## Version

Introduced in version 2012
