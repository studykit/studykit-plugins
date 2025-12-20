# BOM Object

## Description

The BOM object represents the Bill Of Materials (BOM) data of a document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExportBOMCustomization](../BOM/BOM_ExportBOMCustomization.md) | Export BOM column customization as XML file. |
| [GetPartNumberMergeSettings](../BOM/BOM_GetPartNumberMergeSettings.md) | Method that gets the part number row merge settings for the BOM. |
| [GetPartNumberMergeSettings2](../BOM/BOM_GetPartNumberMergeSettings2.md) | Gets the part number row merge settings for the BOM. |
| [ImportBOMCustomization](../BOM/BOM_ImportBOMCustomization.md) | Import BOM column customization as XML file. |
| [SetPartNumberMergeSettings](../BOM/BOM_SetPartNumberMergeSettings.md) | Method that sets the part number row merge settings for the BOM. |
| [SetPartNumberMergeSettings2](../BOM/BOM_SetPartNumberMergeSettings2.md) | Sets the part number row merge settings for the BOM. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BOM/BOM_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BOMViews](../BOM/BOM_BOMViews.md) | Property that gets the BOMViews collection object. |
| [HideSuppressedComponentsInBOM](../BOM/BOM_HideSuppressedComponentsInBOM.md) | Gets and sets whether to hide the suppressed components in BOM. |
| [Parent](../BOM/BOM_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [PartsOnlyViewEnabled](../BOM/BOM_PartsOnlyViewEnabled.md) | Gets and sets whether the parts only BOM view is enabled. |
| [PartsOnlyViewMinimumDigits](../BOM/BOM_PartsOnlyViewMinimumDigits.md) | Gets and sets the minimum number of digits displayed in a parts only view with the PartsOnlyViewNumberingScheme set to kNumericNumbering. |
| [PartsOnlyViewNumberingScheme](../BOM/BOM_PartsOnlyViewNumberingScheme.md) | gets and sets the numbering scheme for a 'Parts Only' view. |
| [RenumberItemsSequentially](../BOM/BOM_RenumberItemsSequentially.md) | Gets and sets whether to renumber the items sequentially or not. |
| [RequiresUpdate](../BOM/BOM_RequiresUpdate.md) | Determines whether the BOM requires an update. |
| [RevisionId](../BOM/BOM_RevisionId.md) | Property that returns the GUID that represents the last saved revision of this BOM. |
| [StructuredViewDelimiter](../BOM/BOM_StructuredViewDelimiter.md) | Gets and sets the delimiter to use for numbering. This property applies only for an all-level structured view. |
| [StructuredViewEnabled](../BOM/BOM_StructuredViewEnabled.md) | Gets and sets whether the structured BOM view is enabled. |
| [StructuredViewFirstLevelOnly](../BOM/BOM_StructuredViewFirstLevelOnly.md) | Gets and sets whether the structured view is an 'all-level' or a 'first level only' view. |
| [StructuredViewMinimumDigits](../BOM/BOM_StructuredViewMinimumDigits.md) | Gets and sets the minimum number of digits displayed in a 'first level only' structured view. |
| [Type](../BOM/BOM_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.BOM](../AssemblyComponentDefinition/AssemblyComponentDefinition_BOM.md), [BOMView.Parent](../BOMView/BOMView_Parent.md), [WeldmentComponentDefinition.BOM](../WeldmentComponentDefinition/WeldmentComponentDefinition_BOM.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |