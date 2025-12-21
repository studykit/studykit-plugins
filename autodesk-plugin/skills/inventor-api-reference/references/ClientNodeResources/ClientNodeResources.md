# ClientNodeResources Object

## Description

This object is accessible through the . But it is in fact, just the one associated with the Document. In other words, all of the ClientNodeResource objects that are used inside the various BrowserPanes of this Document are to be found here.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddNodeResource](../ClientNodeResources/ClientNodeResources_AddNodeResource.md) | Method which creates new client resource object. |
| [ItemById](../ClientNodeResources/ClientNodeResources_ItemById.md) | Returns the specified NodeResource object from the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientNodeResources/ClientNodeResources_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ClientNodeResources/ClientNodeResources_Count.md) | Property that returns the number of items in the collection. |
| [Item](../ClientNodeResources/ClientNodeResources_Item.md) | Returns the specified NodeResource object from the collection. |
| [Type](../ClientNodeResources/ClientNodeResources_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BrowserPanes.ClientNodeResources](../BrowserPanes/BrowserPanes_ClientNodeResources.md)

## Version

Introduced in version 8
