# RadialMarkingMenus.Add Method

Parent Object: [RadialMarkingMenus](../RadialMarkingMenus/RadialMarkingMenus.md)

## Description

Method that creates a new radial marking menu. The newly created marking menu is returned.

## Syntax

RadialMarkingMenus.**Add**( ***Name*** As String, ***InternalName*** As String, ***ClientId*** As String ) As [RadialMarkingMenu](../RadialMarkingMenu/RadialMarkingMenu.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name of the radial marking menu. This is the name that the user will see in the Customize dialog. |
| InternalName | String | Input String that specifies the unique identifier for this radial marking menu. The name specified must be unique with respect to all other radial marking menus or an error will occur. |
| ClientId | String | Input string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |