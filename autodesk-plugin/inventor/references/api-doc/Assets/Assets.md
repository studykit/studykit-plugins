# Assets Object

## Description

The Assets collection object provides access to assets within a library and supports the creation of new assets. Depending on where the Assets object was obtained from it will provide access to different types of assets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../Assets/Assets_Add.md) | Method that creates a new asset. The new created Asset object is returned. Currently only material and appearance assets can be created. When a material asset is created a physical asset is automatically created that is associated with it that you can edit. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Assets/Assets_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Assets/Assets_Count.md) | Gets the number of items in this collection. |
| [Item](../Assets/Assets_Item.md) | Read-only property that returns the specified Asset object from the collection. |
| [Type](../Assets/Assets_Type.md) | Read-only property returning kAssetsObject indicating this object’s type. |

## Accessed From

[AssemblyDocument.Assets](../AssemblyDocument/AssemblyDocument_Assets.md), [PartDocument.Assets](../PartDocument/PartDocument_Assets.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |
| [Set the appearance of an occurrence.](../../sample-programs/SetOccurrenceAppearance_Sample.md) | Sets the appearance of a selected occurrence in an assembly. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |