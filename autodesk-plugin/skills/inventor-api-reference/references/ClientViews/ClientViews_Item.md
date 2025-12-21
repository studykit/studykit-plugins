# ClientViews.Item Property

Parent Object: [ClientViews](../ClientViews/ClientViews.md)

## Description

Returns the specified object from the collection. This is the default property of the ClientViews collection object.

## Syntax

ClientViews.**Item**( ***Index*** As Long ) As [ClientView](../ClientView/ClientView.md)

## Property Value

This is a read only property whose value is a [ClientView](../ClientView/ClientView.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the ClientView to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ClientView name. The name expected is the display name of the view. This is the name that is displayed to the user in the assembly browser. If an out-of-range index or a name of a non-existent name is provided, an error occurs. |

## Version

Introduced in version 6
