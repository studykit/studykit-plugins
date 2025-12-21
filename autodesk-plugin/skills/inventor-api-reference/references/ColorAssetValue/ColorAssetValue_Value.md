# ColorAssetValue.Value Property

Parent Object: [ColorAssetValue](../ColorAssetValue/ColorAssetValue.md)

## Description

Gets and sets this asset value. The value of this property should be ignored if the HasConnectedTexture property is ture. Setting this will remove any associated texture, if there is one.

## Syntax

ColorAssetValue.**Value**() As [Color](../Color/Color.md)

## Property Value

This is a read/write property whose value is a [Color](../Color/Color.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |