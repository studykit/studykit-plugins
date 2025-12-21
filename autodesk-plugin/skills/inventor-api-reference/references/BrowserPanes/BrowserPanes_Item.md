# BrowserPanes.Item Property

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Returns the specified object from the collection.

## Syntax

BrowserPanes.**Item**( ***Index*** As Variant ) As [BrowserPane](../BrowserPane/BrowserPane.md)

## Property Value

This is a read only property whose value is a [BrowserPane](../BrowserPane/BrowserPane.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant that specifies the object within the collection to return. This can be either a Long to indicate the index of the item within the collection or a String indicating the name of the . If there is no BrowserPane with this name currently, the function further checks to see if the string supplied is an InternalName of any BrowserPane. If no BrowserPane can be identified, a failure occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |

## Version

Introduced in version 5
