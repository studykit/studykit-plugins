# ChangeDefinition Object

## Description

The ChangeDefinition object is obtained from the ChangeManager object. It's purpose is to provide a ChangeProcessor object via the CreateChangeProcessor method, according to the settings of the ChangeDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateChangeProcessor](../ChangeDefinition/ChangeDefinition_CreateChangeProcessor.md) | Creates a new ChangeProcessor object based on this definition. |
| [Delete](../ChangeDefinition/ChangeDefinition_Delete.md) | Deletes this ChangeDefinition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ChangeDefinition/ChangeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChangeType](../ChangeDefinition/ChangeDefinition_ChangeType.md) | Gets and sets the type of change (shape edit, query only, etc.) that this ChangeDefinition represents. Defaults kShapeEditCmdType. |
| [ClientId](../ChangeDefinition/ChangeDefinition_ClientId.md) | Gets the Client Id string for this definition. |
| [CommandName](../ChangeDefinition/ChangeDefinition_CommandName.md) | Gets the command name associated with this ChangeDefinition. This localized string shows up in the undo list. |
| [InternalName](../ChangeDefinition/ChangeDefinition_InternalName.md) | Gets the internal name of the ChangeDefinition. This is a unique string that may be used to reliably retrieve a ChangeDefinition object. |
| [Parent](../ChangeDefinition/ChangeDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ChangeDefinition/ChangeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnReplay](../ChangeDefinition/ChangeDefinition_OnReplay.md) | Event that is fired by Inventor in a script replay scenario. In the handler of this event (typically, written by the client who created this ChangeDefinition), it is expected that a new ChangeProcessor will be generated using the CreateChangeProcessor method of this object, followed by the client proceeding to 'hook up' its ChangeProcessor handler code, and returning this hooked-up processor back. Inventor will then use this returned ChangeProcessor to replay the scripted command. |

## Accessed From

[ChangeDefinitions.Add](../ChangeDefinitions/ChangeDefinitions_Add.md), [ChangeDefinitions.Item](../ChangeDefinitions/ChangeDefinitions_Item.md), [ChangeProcessor.Parent](../ChangeProcessor/ChangeProcessor_Parent.md)

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |