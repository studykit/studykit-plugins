# BOMView Object

## Description

The BOMView object represents a view (or an ordering scheme) of the BOM.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Export](../BOMView/BOMView_Export.md) | Method that saves the BOM as viewed in this BOM view to an external file. |
| [Renumber](../BOMView/BOMView_Renumber.md) | Method that renumbers all rows in the BOM view. If the BOMRowsToRenumber argument is provided, only those rows are renumbered. Applies only to structured and parts only views. This method returns a failure for the model data BOM view. |
| [Sort](../BOMView/BOMView_Sort.md) | Method that changes the sort order of items in the BOM view. Applies only to structured and parts only views. This method returns a failure for the model data BOM view. |
| [Sort2](../BOMView/BOMView_Sort2.md) | Method that changes the sort order of items in the BOM view. Applies only to structured and parts only views. This method returns a failure for the model data BOM view. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BOMView/BOMView_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BOMRows](../BOMView/BOMView_BOMRows.md) | Property that gets the BOMRows enumerator object containing the top level BOM rows. |
| [iAssemblyMemberName](../BOMView/BOMView_iAssemblyMemberName.md) | Gets and sets the name of the iAssembly member that the BOM view is based on. |
| [ModelStateMemberName](../BOMView/BOMView_ModelStateMemberName.md) | Gets the name of the model state member that the BOM view is based on. |
| [Name](../BOMView/BOMView_Name.md) | Property that gets the name of the BOMView. |
| [Parent](../BOMView/BOMView_Parent.md) | Property that returns the parent BOM object. |
| [RevisionId](../BOMView/BOMView_RevisionId.md) | Property that returns the GUID that represents the last saved revision of this BOMView. |
| [Type](../BOMView/BOMView_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [ViewType](../BOMView/BOMView_ViewType.md) | Property that returns the BOM View type. Possible return values are kModelDataBOMViewType (for the 'raw' view), kStructuredBOMViewType (for the structured view) and kPartsOnlyBOMViewType (for the parts-only view). |

## Accessed From

[BOMViews.Item](../BOMViews/BOMViews_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |

## Version

Introduced in version 10
