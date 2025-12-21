# ReferenceAssetValue Object

Derived from: [AssetValue](../AssetValue/AssetValue.md) Object

## Description

The ReferenceAssetValue object represents an asset value that consists of a reference to another asset. The Value property will return an asset that exists within the same library. When setting the value, the Asset you’re setting and the one you’re assigning must exist within a document.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ReferenceAssetValue/ReferenceAssetValue_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DisplayName](../ReferenceAssetValue/ReferenceAssetValue_DisplayName.md) | Gets the name of this value as seen in the Material or Appearance Browser. This can change based on the current Inventor language. |
| [HasMultipleValues](../ReferenceAssetValue/ReferenceAssetValue_HasMultipleValues.md) | Gets the boolean flag that indicates if this value has multiple values or not. |
| [IsReadOnly](../ReferenceAssetValue/ReferenceAssetValue_IsReadOnly.md) | Gets the boolean flag that indicates if this asset value is read-only. If True any attempted edits will fail. |
| [Name](../ReferenceAssetValue/ReferenceAssetValue_Name.md) | Gets the key name of the value. This name will remain constant for all languages and is the name used as input to the Item property or the Asset object. |
| [Parent](../ReferenceAssetValue/ReferenceAssetValue_Parent.md) | Read-only property that returns the parent Asset object. |
| [Type](../ReferenceAssetValue/ReferenceAssetValue_Type.md) | Read-only property returning kAssetValueObject indicating this object’s type. |
| [Value](../ReferenceAssetValue/ReferenceAssetValue_Value.md) | Gets and sets this asset value. |
| [Values](../ReferenceAssetValue/ReferenceAssetValue_Values.md) | Gets and sets the values associated with this asset value. HasMultipleValues property indicates if this property will be returning more than one value. |
| [ValueType](../ReferenceAssetValue/ReferenceAssetValue_ValueType.md) | Read-only property that returns the data type that the Value property for this AssetValue object will return. |

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
