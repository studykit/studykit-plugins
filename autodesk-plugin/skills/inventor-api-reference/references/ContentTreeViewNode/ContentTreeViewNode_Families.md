# ContentTreeViewNode.Families Property

Parent Object: [ContentTreeViewNode](../ContentTreeViewNode/ContentTreeViewNode.md)

## Description

Property that returns the set of families associated with this node. The collection returned may have a count of zero indicating there aren't any families associated with this node.

## Syntax

ContentTreeViewNode.**Families**() As [ContentFamiliesEnumerator](../ContentFamiliesEnumerator/ContentFamiliesEnumerator.md)

## Property Value

This is a read only property whose value is a [ContentFamiliesEnumerator](../ContentFamiliesEnumerator/ContentFamiliesEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
