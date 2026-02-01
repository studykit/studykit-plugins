# FloatAssetValue Object

Derived from: [AssetValue](../AssetValue/AssetValue.md) Object

## Description

The FloatAssetValue object represents a floating point value. The value is returned as a Double and a Double should be used when setting the value. This object also provides any limits that the value must meet to be valid.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetLimits](../FloatAssetValue/FloatAssetValue_GetLimits.md) | Method that returns the limits for this value. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FloatAssetValue/FloatAssetValue_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectedTexture](../FloatAssetValue/FloatAssetValue_ConnectedTexture.md) | Read-only property that returns the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If the library is writable you can edit the texture. If there isn’t a texture associated with this value, this property will return Nothing. |
| [DisplayName](../FloatAssetValue/FloatAssetValue_DisplayName.md) | Gets the name of this value as seen in the Material or Appearance Browser. This can change based on the current Inventor language. |
| [HasConnectedTexture](../FloatAssetValue/FloatAssetValue_HasConnectedTexture.md) | Gets and sets the boolean flag that indicates if the float value has been overridden using a texture. Setting this property to False will remove the texture so that a float value is used. Setting this property to True will connect a texture to this float value. |
| [HasLimits](../FloatAssetValue/FloatAssetValue_HasLimits.md) | Gets the boolean flag that indicates if this value has any limits it must be within to be valid. If True, use the GetLimits method to get the limit values. |
| [HasMultipleValues](../FloatAssetValue/FloatAssetValue_HasMultipleValues.md) | Gets the boolean flag that indicates if this value has multiple values or not. |
| [IsPercentage](../FloatAssetValue/FloatAssetValue_IsPercentage.md) | Gets the boolean flag that indicates that this value represents a percentage value so the valid values must be in the range of 0.0 to 1.0 unless they’re further limited by additional limits which can be determined with the HasLimits property. |
| [IsReadOnly](../FloatAssetValue/FloatAssetValue_IsReadOnly.md) | Gets the boolean flag that indicates if this asset value is read-only. If True any attempted edits will fail. |
| [Name](../FloatAssetValue/FloatAssetValue_Name.md) | Gets the key name of the value. This name will remain constant for all languages and is the name used as input to the Item property or the Asset object. |
| [Parent](../FloatAssetValue/FloatAssetValue_Parent.md) | Read-only property that returns the parent Asset object. |
| [Type](../FloatAssetValue/FloatAssetValue_Type.md) | Read-only property returning kAssetValueObject indicating this object’s type. |
| [Units](../FloatAssetValue/FloatAssetValue_Units.md) | Gets the units that this value is returned in. The String returned is a valid Inventor unit string that can be used with the methods on the UnitOfMeasure object. |
| [Value](../FloatAssetValue/FloatAssetValue_Value.md) | Gets and sets this asset value. If this asset value has a texture associated with it, setting the value will remove the texture and assign the static value. |
| [Values](../FloatAssetValue/FloatAssetValue_Values.md) | Gets and sets the values associated with this asset value. HasMultipleValues property indicates if this property will be returning more than one value. |
| [ValueType](../FloatAssetValue/FloatAssetValue_ValueType.md) | Read-only property that returns the data type that the Value property for this AssetValue object will return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |
| [Write out all document physical properties to a file.](../../sample-programs/DumpDocumentPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a physical property |

## Version

Introduced in version 2014
