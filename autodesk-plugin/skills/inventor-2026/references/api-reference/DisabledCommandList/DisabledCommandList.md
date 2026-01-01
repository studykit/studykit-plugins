# DisabledCommandList Object

## Description

This object represents a list of commands that are disabled in the given context. For example, a DisabledCommandList collection in the document context lists all commands disabled at the document level, while a DisabledCommandList collection at the environment level list commands disabled in a given environment. This collection object compliments the Enabled property of the ControlDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DisabledCommandList/DisabledCommandList_Add.md) | Method that adds the specified command to the list. |
| [Remove](../DisabledCommandList/DisabledCommandList_Remove.md) | Method that removes the specified command from the list. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DisabledCommandList/DisabledCommandList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DisabledCommandList/DisabledCommandList_Count.md) | Read only property that returns the number of commands in the list. |
| [Item](../DisabledCommandList/DisabledCommandList_Item.md) | Returns the specified ControlDefinition from the list. |
| [Type](../DisabledCommandList/DisabledCommandList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyDocument.DisabledCommandList](../AssemblyDocument/AssemblyDocument_DisabledCommandList.md), [DrawingDocument.DisabledCommandList](../DrawingDocument/DrawingDocument_DisabledCommandList.md), [Environment.DisabledCommandList](../Environment/Environment_DisabledCommandList.md), [PartDocument.DisabledCommandList](../PartDocument/PartDocument_DisabledCommandList.md), [PresentationDocument.DisabledCommandList](../PresentationDocument/PresentationDocument_DisabledCommandList.md)

## Version

Introduced in version 10
