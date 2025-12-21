# ColorAssetValue.HasConnectedTexture Property

Parent Object: [ColorAssetValue](../ColorAssetValue/ColorAssetValue.md)

## Description

Read-write property that indicates if the color has been overridden using a texture. Setting this property to False will remove the texture so that a basic color is used. Setting this property to True will connect a texture to this color which you can then edit to create the desired texture.

## Syntax

ColorAssetValue.**HasConnectedTexture**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |

## Version

Introduced in version 2014
