# CommandCategory Object

## Description

The CommandCategory object represents the list of commands that are displayed in the Customize dialog. Command categories serve as a logical grouping of commands to allow the user to more easily find a specific command. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../CommandCategory/CommandCategory_Add.md) | Method that adds a control definition or a command bar to the command category. |
| [Delete](../CommandCategory/CommandCategory_Delete.md) | Method that deletes the command category. If this category contains commands, these are moved to the default command category. This method fails for built-in categories. |
| [Remove](../CommandCategory/CommandCategory_Remove.md) | Method that removes a control definition or a command bar from the command category. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CommandCategory/CommandCategory_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../CommandCategory/CommandCategory_BuiltIn.md) | Property that specifies if the control or definition is a standard Autodesk Inventor control or definition. Built-in ones have restrictions in the edits that can be performed. |
| [ClientId](../CommandCategory/CommandCategory_ClientId.md) | Property that returns the string that uniquely identifies the client. |
| [Count](../CommandCategory/CommandCategory_Count.md) | Property that returns the number of commands in this category. |
| [DisplayName](../CommandCategory/CommandCategory_DisplayName.md) | Property that returns the display name of the command category. This is the name displayed to the user and can vary between locales. |
| [InternalName](../CommandCategory/CommandCategory_InternalName.md) | Property that returns the name of the command category. The name is the internal English name of the command category. This name will remain constant and is not affected by locale. The name is never displayed to the user. The display name is what's shown to the user. |
| [Item](../CommandCategory/CommandCategory_Item.md) | Returns the specified object in the collection. |
| [ItemByName](../CommandCategory/CommandCategory_ItemByName.md) | Returns the specified ControlDefinition or CommandBar object. |
| [Parent](../CommandCategory/CommandCategory_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../CommandCategory/CommandCategory_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CommandCategories.Add](../CommandCategories/CommandCategories_Add.md), [CommandCategories.Item](../CommandCategories/CommandCategories_Item.md)

## Version

Introduced in version 9
