# AssetValue Object

## Description

The AssetValue object represents a specific value within an asset. The AssetValue class is the base class for the various types of asset values.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssetValue/AssetValue_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DisplayName](../AssetValue/AssetValue_DisplayName.md) | Gets the name of this value as seen in the Material or Appearance Browser. This can change based on the current Inventor language. |
| [IsReadOnly](../AssetValue/AssetValue_IsReadOnly.md) | Gets the boolean flag that indicates if this asset value is read-only. If True any attempted edits will fail. |
| [Name](../AssetValue/AssetValue_Name.md) | Gets the key name of the value. This name will remain constant for all languages and is the name used as input to the Item property or the Asset object. |
| [Parent](../AssetValue/AssetValue_Parent.md) | Read-only property that returns the parent Asset object. |
| [Type](../AssetValue/AssetValue_Type.md) | Read-only property returning kAssetValueObject indicating this object’s type. |
| [ValueType](../AssetValue/AssetValue_ValueType.md) | Read-only property that returns the data type that the Value property for this AssetValue object will return. |

## Accessed From

[Asset.Item](../Asset/Asset_Item.md), [AssetTexture.Item](../AssetTexture/AssetTexture_Item.md), [MaterialAsset.Item](../MaterialAsset/MaterialAsset_Item.md)

## Derived Classes

[BooleanAssetValue](../BooleanAssetValue/BooleanAssetValue.md), [ChoiceAssetValue](../ChoiceAssetValue/ChoiceAssetValue.md), [ColorAssetValue](../ColorAssetValue/ColorAssetValue.md), [FilenameAssetValue](../FilenameAssetValue/FilenameAssetValue.md), [FloatAssetValue](../FloatAssetValue/FloatAssetValue.md), [IntegerAssetValue](../IntegerAssetValue/IntegerAssetValue.md), [ReferenceAssetValue](../ReferenceAssetValue/ReferenceAssetValue.md), [StringAssetValue](../StringAssetValue/StringAssetValue.md), [TextureAssetValue](../TextureAssetValue/TextureAssetValue.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |
| [Write out all document physical properties to a file.](../../sample-programs/DumpDocumentPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a physical property |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |