# iFeatureTableRows.Item Property

Parent Object: [iFeatureTableRows](../iFeatureTableRows/iFeatureTableRows.md)

## Description

Method that returns the specified iFeatureTableRow object from the collection.

## Syntax

iFeatureTableRows.**Item**( ***Index*** As Variant ) As [iFeatureTableRow](../iFeatureTableRow/iFeatureTableRow.md)

## Property Value

This is a read only property whose value is an [iFeatureTableRow](../iFeatureTableRow/iFeatureTableRow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or String value that specifies the iFeatureTableRow to return. If a Long is input then it is the index of the item to return. If a String is input then it must match the member name of one of the rows. If the index is out of range or the name does not exist a failure will occur. |

## Version

Introduced in version 2009
