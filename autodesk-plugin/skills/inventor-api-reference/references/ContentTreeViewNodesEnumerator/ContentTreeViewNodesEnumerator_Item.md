# ContentTreeViewNodesEnumerator.Item Property

Parent Object: [ContentTreeViewNodesEnumerator](../ContentTreeViewNodesEnumerator/ContentTreeViewNodesEnumerator.md)

## Description

Returns the specified ContentTreeViewNode object from the collection.

## Syntax

ContentTreeViewNodesEnumerator.**Item**( ***Index*** As Variant ) As [ContentTreeViewNode](../ContentTreeViewNode/ContentTreeViewNode.md)

## Property Value

This is a read only property whose value is a [ContentTreeViewNode](../ContentTreeViewNode/ContentTreeViewNode.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or String that that specifies the ContentTreeViewNode object within the collection to return. A Long indicates the index of the item within the collection to return. A String indicates the name of the node to return. You can use either the display or internal name. In the case where there are two nodes with the same name the first node will be returned. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
