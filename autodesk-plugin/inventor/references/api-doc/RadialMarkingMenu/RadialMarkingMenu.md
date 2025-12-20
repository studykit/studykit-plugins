# RadialMarkingMenu Object

## Description

The RadialMarkingMenu object provides access to the contents of the radial marking menu (displayed when the user right clicks).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Clear](../RadialMarkingMenu/RadialMarkingMenu_Clear.md) | Method that clears the all of the controls for this radial marking menu. This is equivalent to assigning Nothing to each control. When no controls are defined, the radial marking menu is not displayed. |
| [CreateRadialSubMenu](../RadialMarkingMenu/RadialMarkingMenu_CreateRadialSubMenu.md) | Method that creates a transient RadialMarkingMenu. This object can then be assigned to any of the radial menu controls to create a sub-menu. Controls within the sub-menu can be left un-assigned to indicate the absence of those controls. |
| [Delete](../RadialMarkingMenu/RadialMarkingMenu_Delete.md) | Method that deletes this radial marking menu. Standard Inventor radial marking menus cannot be deleted, so this method is only valid for radial marking menus where the BuiltIn property returns False. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RadialMarkingMenu/RadialMarkingMenu_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../RadialMarkingMenu/RadialMarkingMenu_BuiltIn.md) | Read-only property that indicates if this radial marking menu is a standard Inventor marking menu or one created by an add-in. Returns True in the case where it’s an Inventor marking menu. |
| [ClientId](../RadialMarkingMenu/RadialMarkingMenu_ClientId.md) | Read-only property that returns the string that uniquely identifies the client that created this radial marking menu. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}".  If the menu is built-in, an empty string is returned. |
| [EastControl](../RadialMarkingMenu/RadialMarkingMenu_EastControl.md) | Gets and sets the command to display in the east control. |
| [InternalName](../RadialMarkingMenu/RadialMarkingMenu_InternalName.md) | Read-only property that returns the internal name of the radial marking menu. This is a unique name with respect to all other radial marking menus and can be used to access a specific radial marking menu. |
| [Name](../RadialMarkingMenu/RadialMarkingMenu_Name.md) | Read-write property that gets and sets the name of the radial marking menu. |
| [NorthControl](../RadialMarkingMenu/RadialMarkingMenu_NorthControl.md) | Gets and sets the command to display in the north control. |
| [NortheastControl](../RadialMarkingMenu/RadialMarkingMenu_NortheastControl.md) | Gets and sets the command to display in the north-east control. |
| [NorthwestControl](../RadialMarkingMenu/RadialMarkingMenu_NorthwestControl.md) | Gets and sets the command to display in the north-west control. |
| [SouthControl](../RadialMarkingMenu/RadialMarkingMenu_SouthControl.md) | Gets and sets the command to display in the south control. |
| [SoutheastControl](../RadialMarkingMenu/RadialMarkingMenu_SoutheastControl.md) | Gets and sets the command to display in the south-east control. |
| [SouthwestControl](../RadialMarkingMenu/RadialMarkingMenu_SouthwestControl.md) | Gets and sets the command to display in the south-west control. |
| [Type](../RadialMarkingMenu/RadialMarkingMenu_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WestControl](../RadialMarkingMenu/RadialMarkingMenu_WestControl.md) | Gets and sets the command to display in the west control. |

## Accessed From

[Environment.GetRadialMarkingMenu](../Environment/Environment_GetRadialMarkingMenu.md), [RadialMarkingMenu.CreateRadialSubMenu](../RadialMarkingMenu/RadialMarkingMenu_CreateRadialSubMenu.md), [RadialMarkingMenus.Add](../RadialMarkingMenus/RadialMarkingMenus_Add.md), [RadialMarkingMenus.Item](../RadialMarkingMenus/RadialMarkingMenus_Item.md)

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |