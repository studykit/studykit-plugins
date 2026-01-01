# ContentCenter Object

## Description

The ContentCenter object provides the API interface to the Content Center functionality.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetContentObject](../ContentCenter/ContentCenter_GetContentObject.md) | Property that returns the specified content center object specified by the content identifier. If the object cannot be found then Nothing is returned. This can return a ContentFamily or ContentRow depending on what the identifier represents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentCenter/ContentCenter_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [TreeViewTopNode](../ContentCenter/ContentCenter_TreeViewTopNode.md) | Property that returns the top-most node in the Content Center tree. The entire tree can be accessed by traversing the tree beginning at this node. |
| [Type](../ContentCenter/ContentCenter_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.ContentCenter](../Application/Application_ContentCenter.md), [InventorServer.ContentCenter](InventorServer_ContentCenter.md), [InventorServerObject.ContentCenter](InventorServerObject_ContentCenter.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
