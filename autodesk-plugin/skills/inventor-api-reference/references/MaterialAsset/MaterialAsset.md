# MaterialAsset Object

Derived from: [Asset](../Asset/Asset.md) Object

## Description

The MaterialAsset object is derived from the Asset object and represents a material. A material is a simple asset that references an appearance and a physical properties asset.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../MaterialAsset/MaterialAsset_CopyTo.md) | Method that copies this asset to the specified target and returns the new asset. A failure will occur if you attempt to replace the asset itself.. |
| [Delete](../MaterialAsset/MaterialAsset_Delete.md) | Method that deletes this asset from the library. An asset can only be deleted if it is not currently being used, which you can determine using the IsUsed property. |
| [Duplicate](../MaterialAsset/MaterialAsset_Duplicate.md) | Method that creates a copy of this asset within the document using a new display name. This method is only valid when called on an asset that is owned by a document. A failure will occur if you attempt to copy an asset that isn’t owned by a document and if the. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AppearanceAsset](../MaterialAsset/MaterialAsset_AppearanceAsset.md) | Gets and sets the appearance associated with the material. When assigning an appearance, the appearance must exist in the same document as the material. |
| [Application](../MaterialAsset/MaterialAsset_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssetType](../MaterialAsset/MaterialAsset_AssetType.md) | Gets the data type that returns whether this is an appearance, physical properties, or material asset. |
| [Category](../MaterialAsset/MaterialAsset_Category.md) | Gets the category that this asset is a member of. A value of Nothing indicates this asset is not a member of a category. A value of Nothing is also returned when an Asset is associated with a document, rather than a library. Categories don’t exist in a documen. |
| [CategoryName](../MaterialAsset/MaterialAsset_CategoryName.md) | Gets the name of the category this Asset is designated to be in. This can include the the category and subcategories which are delimited by a colon. |
| [Count](../MaterialAsset/MaterialAsset_Count.md) | Gets the number of items in this collection. |
| [DisplayName](../MaterialAsset/MaterialAsset_DisplayName.md) | Gets and sets the name of this asset as seen in the Material or Appearance Browser. |
| [HasTexture](../MaterialAsset/MaterialAsset_HasTexture.md) | Gets the flag that indicates if this asset has texture. |
| [IsReadOnly](../MaterialAsset/MaterialAsset_IsReadOnly.md) | Gets the boolean flag that indicates if this asset is read-only. If True any attempted edits will fail. |
| [IsUsed](../MaterialAsset/MaterialAsset_IsUsed.md) | Gets the boolean flag that indicates if this asset is being used in the document or in a material definition. |
| [Item](../MaterialAsset/MaterialAsset_Item.md) | Allows integer-indexed access to items in the collection. |
| [LocalType](../MaterialAsset/MaterialAsset_LocalType.md) | Returns the local type of this asset. This is applicable to appearance asset. |
| [Name](../MaterialAsset/MaterialAsset_Name.md) | Gets the key name of the asset. This name will remain constant for all languages and is the name used as input to the Item property. |
| [Parent](../MaterialAsset/MaterialAsset_Parent.md) | Read-only property that returns the parent object of this asset. This can return an AssetLibrary, or Document object. |
| [PhysicalPropertiesAsset](../MaterialAsset/MaterialAsset_PhysicalPropertiesAsset.md) | Gets and sets the physical properties associated with the material. When assigning physical properties, the physical properties asset must exist in the same document as the material. |
| [Type](../MaterialAsset/MaterialAsset_Type.md) | Gets the constant that indicates the type of this object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |