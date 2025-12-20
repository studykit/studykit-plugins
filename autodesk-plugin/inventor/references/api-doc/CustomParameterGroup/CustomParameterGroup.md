# CustomParameterGroup Object

## Description

The CustomParameterGroup object represents a grouping of certain parameters in the parameters dialog. These groups serve as a logical grouping of parameters to allow the user to more easily find a specific parameter.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../CustomParameterGroup/CustomParameterGroup_Add.md) | Method that adds a parameter to the group. Adding a parameter to a group does not remove it from group(s) that it currently resides in. |
| [Delete](../CustomParameterGroup/CustomParameterGroup_Delete.md) | Method that deletes the group and optionally deletes the parameters that it contains. |
| [Remove](../CustomParameterGroup/CustomParameterGroup_Remove.md) | Method that removes a parameter from the group. This does not delete the parameter. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CustomParameterGroup/CustomParameterGroup_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../CustomParameterGroup/CustomParameterGroup_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [Count](../CustomParameterGroup/CustomParameterGroup_Count.md) | Property that returns the number of parameters in this group. |
| [DisabledActionTypes](../CustomParameterGroup/CustomParameterGroup_DisabledActionTypes.md) | Gets and sets the disabling of certain user actions on this object. |
| [DisplayName](../CustomParameterGroup/CustomParameterGroup_DisplayName.md) | Gets the display name of the Custom Parameter Group. |
| [InternalName](../CustomParameterGroup/CustomParameterGroup_InternalName.md) | Property that returns the name of the custom group. The name is the internal English name of the group. This name will remain constant and is not affected by locale. The name is never displayed to the user. The display name is what's shown to the user. |
| [Item](../CustomParameterGroup/CustomParameterGroup_Item.md) | Returns the specified Parameter object. |
| [Type](../CustomParameterGroup/CustomParameterGroup_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CustomParameterGroups.Add](../CustomParameterGroups/CustomParameterGroups_Add.md), [CustomParameterGroups.Item](../CustomParameterGroups/CustomParameterGroups_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |