# AssetTexture Object

## Description

The AssetTexture object represents a texture that’s associated with an asset value.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ChangeTextureType](../AssetTexture/AssetTexture_ChangeTextureType.md) | Method that changes the type of of this texture. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssetTexture/AssetTexture_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AssetTexture/AssetTexture_Count.md) | Read-only property that returns the number of asset values associated with this texture. |
| [Item](../AssetTexture/AssetTexture_Item.md) | Read-only property that returns the specified AssetValue object from the asset. |
| [TextureType](../AssetTexture/AssetTexture_TextureType.md) | Gets the current texture type. |
| [Type](../AssetTexture/AssetTexture_Type.md) | Read-only property returning kAssetTextureObject indicating this object’s type. |

## Accessed From

[ColorAssetValue.ConnectedTexture](../ColorAssetValue/ColorAssetValue_ConnectedTexture.md), [FloatAssetValue.ConnectedTexture](../FloatAssetValue/FloatAssetValue_ConnectedTexture.md), [TextureAssetValue.Value](../TextureAssetValue/TextureAssetValue_Value.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |

## Version

Introduced in version 2014
