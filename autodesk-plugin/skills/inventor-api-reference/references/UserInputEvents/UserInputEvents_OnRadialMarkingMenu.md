# UserInputEvents.OnRadialMarkingMenu Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

Fires before the marking menu is displayed to the user or before the user gestures using the right mouse button.

## Syntax

UserInputEvents.**OnRadialMarkingMenu**( ***SelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***SelectionDevice*** As [SelectionDeviceEnum](../SelectionDeviceEnum.md), ***RadialMenu*** As [RadialMarkingMenu](../RadialMarkingMenu/RadialMarkingMenu.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Input ObjectsEnumerator that contains the selected entities. This is the same set of entities currently contained in the document’s SelectSet. |
| SelectionDevice | [SelectionDeviceEnum](../SelectionDeviceEnum.md) | Input constant denoting whether the menu was invoked via a click in a graphics window (kGraphicsWindowSelection) or by a click in the browser (kBrowserSelection). |
| RadialMenu | [RadialMarkingMenu](../RadialMarkingMenu/RadialMarkingMenu.md) | Input/Output RadialMarkingMenu object. This object represents the contents of the radial menu that will be displayed to the user. The radial marking menu that Inventor would usually show in the current context is passed through this argument. You can then choose to modify the contents of that marking menu. Any changes you make are transient and will only be used for that display of the marking menu.  Instead of modifying the marking menu you can instead return a different marking menu. For example, you can create a custom radial marking menu, and then in certain contexts, provide that marking menu. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about why the menu is being displayed. This is currently empty. |

## Version

Introduced in version 2012
