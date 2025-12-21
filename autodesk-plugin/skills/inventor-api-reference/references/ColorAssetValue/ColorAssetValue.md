# ColorAssetValue Object

Derived from: [AssetValue](../AssetValue/AssetValue.md) Object

## Description

The ColorAssetValue object represents an asset value that consists of a color. The Value property will return and must be set with a Color object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ColorAssetValue/ColorAssetValue_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConnectedTexture](../ColorAssetValue/ColorAssetValue_ConnectedTexture.md) | Gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If the library is writable you can edit the texture. If not texture exists, this property will return Nothing. |
| [DisplayName](../ColorAssetValue/ColorAssetValue_DisplayName.md) | Gets the name of this value as seen in the Material or Appearance Browser. This can change based on the current Inventor language. |
| [HasConnectedTexture](../ColorAssetValue/ColorAssetValue_HasConnectedTexture.md) | Read-write property that indicates if the color has been overridden using a texture. Setting this property to False will remove the texture so that a basic color is used. Setting this property to True will connect a texture to this color which you can then edit to create the desired texture. |
| [HasMultipleValues](../ColorAssetValue/ColorAssetValue_HasMultipleValues.md) | Gets the boolean flag that indicates if this value has multiple values or not. |
| [IsReadOnly](../ColorAssetValue/ColorAssetValue_IsReadOnly.md) | Gets the boolean flag that indicates if this asset value is read-only. If True any attempted edits will fail. |
| [Name](../ColorAssetValue/ColorAssetValue_Name.md) | Gets the key name of the value. This name will remain constant for all languages and is the name used as input to the Item property or the Asset object. |
| [Parent](../ColorAssetValue/ColorAssetValue_Parent.md) | Read-only property that returns the parent Asset object. |
| [Type](../ColorAssetValue/ColorAssetValue_Type.md) | Read-only property returning kAssetValueObject indicating this object’s type. |
| [Value](../ColorAssetValue/ColorAssetValue_Value.md) | Gets and sets this asset value. The value of this property should be ignored if the HasConnectedTexture property is ture. Setting this will remove any associated texture, if there is one. |
| [Values](../ColorAssetValue/ColorAssetValue_Values.md) | Gets and sets the values associated with this asset value. HasMultipleValues property indicates if this property will be returning more than one value. |
| [ValueType](../ColorAssetValue/ColorAssetValue_ValueType.md) | Read-only property that returns the data type that the Value property for this AssetValue object will return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |