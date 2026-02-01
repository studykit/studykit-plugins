# ChangeDefinitions Object

## Description

The ChangeDefinitions collection object provides access to all the objects created by a particular client and provides a method to create additional ChangeDefinitions. See the topic in the overview section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ChangeDefinitions/ChangeDefinitions_Add.md) | Method that creates a new ChangeDefinition. The newly created ChangeDefinition is returned. |
| [Delete](../ChangeDefinitions/ChangeDefinitions_Delete.md) | Method to delete this collection and all objects contained within it. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ChangeDefinitions/ChangeDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../ChangeDefinitions/ChangeDefinitions_ClientId.md) | Property indicating the Client Id string that uniquely identifies this definitions collection. |
| [Count](../ChangeDefinitions/ChangeDefinitions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../ChangeDefinitions/ChangeDefinitions_Item.md) | Returns the specified ChangeDefinition object from the collection. |
| [Type](../ChangeDefinitions/ChangeDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ChangeManager.Add](../ChangeManager/ChangeManager_Add.md), [ChangeManager.Item](../ChangeManager/ChangeManager_Item.md)

## Version

Introduced in version 9
