# iFeatures.Item Property

Parent Object: [iFeatures](../iFeatures/iFeatures.md)

## Description

Returns the specified iFeature object from the collection..

## Syntax

iFeatures.**Item**( ***Index*** As Variant ) As [iFeature](../iFeature/iFeature.md)

## Property Value

This is a read only property whose value is an [iFeature](../iFeature/iFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or String value that specifies the iFeature to return. If a Long is input then it is the index of the item to return. If a String is input then it must match the name of an existing iFeature. If the index is out of range or the name does not exist a failure will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Changing row of table driven iFeature](../../sample-programs/iFeatureTable_iFeatureTableColumns_Sample.md) | This program demonstrates the edit of a table driven iFeature to change which row of the table is being used to drive the iFeature. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |