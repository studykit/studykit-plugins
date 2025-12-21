# ContentTreeViewNode Object

## Description

The ContentTreeViewNode object represents nodes within the Content Center tree structure.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentTreeViewNode/ContentTreeViewNode_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChildNodes](../ContentTreeViewNode/ContentTreeViewNode_ChildNodes.md) | Property that returns a collection containing the child ContentTreeViewNode objects of this node. |
| [DisplayName](../ContentTreeViewNode/ContentTreeViewNode_DisplayName.md) | Property that returns the display name of this node. This is the name that the end-user sees and is localized for different languages. |
| [Families](../ContentTreeViewNode/ContentTreeViewNode_Families.md) | Property that returns the set of families associated with this node. The collection returned may have a count of zero indicating there aren't any families associated with this node. |
| [FullTreeViewPath](../ContentTreeViewNode/ContentTreeViewNode_FullTreeViewPath.md) | Property that provides the full path in the tree view for this node. For example, this can return 'Fasteners:Bolts:Countersunk:Oval Countersunk Head Metric Machine Screws' where a colon is used as the delimiter. |
| [Icon](../ContentTreeViewNode/ContentTreeViewNode_Icon.md) | Property that returns the icon used for this node. |
| [InternalName](../ContentTreeViewNode/ContentTreeViewNode_InternalName.md) | Property that returns the internal name of this node. This will be consistent regardless of the language version of Inventor. |
| [ParentNode](../ContentTreeViewNode/ContentTreeViewNode_ParentNode.md) | Property that returns the parent ContentTreeViewNode object. This property will return Nothing for the top node. |
| [Type](../ContentTreeViewNode/ContentTreeViewNode_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContentCenter.TreeViewTopNode](../ContentCenter/ContentCenter_TreeViewTopNode.md), [ContentTreeViewNode.ParentNode](../ContentTreeViewNode/ContentTreeViewNode_ParentNode.md), [ContentTreeViewNodesEnumerator.Item](../ContentTreeViewNodesEnumerator/ContentTreeViewNodesEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
