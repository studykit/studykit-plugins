# RevitExportDefinition Object

## Description

RevitExportDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../RevitExportDefinition/RevitExportDefinition_Copy.md) | Method that creates a copy of this RevitExportDefinition object. The new RevitExportDefinition is independent of any RevitExport. It can be edited and used as input to edit an existing RevitExport or to create a new RevitExport. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../RevitExportDefinition/RevitExportDefinition_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the RevitExport. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../RevitExportDefinition/RevitExportDefinition_ActiveModelState.md) | Read-write property that gets and sets the name of the active model state for the RevitExport. |
| [ActivePositionalRepresentation](../RevitExportDefinition/RevitExportDefinition_ActivePositionalRepresentation.md) | Read-write property that gets and sets the name of the active Positional Representation for the RevitExport. |
| [AdditionalExcludedOccurrences](../RevitExportDefinition/RevitExportDefinition_AdditionalExcludedOccurrences.md) | Read-write property that gets and sets the occurrences being excluded for the RevitExport. |
| [AdditionalIncludedOccurrences](../RevitExportDefinition/RevitExportDefinition_AdditionalIncludedOccurrences.md) | Read-write property that gets and sets the occurrences being included for the RevitExport. |
| [Application](../RevitExportDefinition/RevitExportDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [EnableUpdating](../RevitExportDefinition/RevitExportDefinition_EnableUpdating.md) | Read-write property that controls whether or not a RevitExport object is created. If set to True, then an updateable RevitExport object is created. If set to False, then no RevitExport object is created, and no subsequent updates can be done. |
| [EnvelopesReplaceStyle](../RevitExportDefinition/RevitExportDefinition_EnvelopesReplaceStyle.md) | Read-write property that gets and sets envelopes replace style. When a new definition is created, this defaults to kNoneReplaceStyle. |
| [FileName](../RevitExportDefinition/RevitExportDefinition_FileName.md) | Read-write property that gets and sets the filename of the RevitExport. This cannot be modified after the Revit model has been created. |
| [IsAssociativeDesignView](../RevitExportDefinition/RevitExportDefinition_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. When creating a new RevitExport, setting this property to True will create a derivation that is associative to the design view. |
| [Location](../RevitExportDefinition/RevitExportDefinition_Location.md) | Read-write property that gets and sets the location of the RevitExport. This cannot be modified after the Revit model has been created. |
| [Parent](../RevitExportDefinition/RevitExportDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PreservedFeatures](../RevitExportDefinition/RevitExportDefinition_PreservedFeatures.md) | Read-write property that gets and sets the features to preserve from remove. For each preserved feature a Face from the feature is required to indicate it. |
| [RemoveAllInternalVoids](../RevitExportDefinition/RevitExportDefinition_RemoveAllInternalVoids.md) | Read-write property that gets and sets whether remove all the internal voids or not. Set this to True will fill all the internal void shells in the RevitExport solid. |
| [RemoveChamfersDistanceRange](../RevitExportDefinition/RevitExportDefinition_RemoveChamfersDistanceRange.md) | Read-write property that gets and sets the distance of chamfers in centimeters to remove for the RevitExport. This is only applicable when the RemoveChamfersStyle is set to kRevitExportRemoveByRange. |
| [RemoveChamfersStyle](../RevitExportDefinition/RevitExportDefinition_RemoveChamfersStyle.md) | Read-write property that gets and sets the style to remove chamfers for the RevitExport. |
| [RemoveEmbossMaxHeightRange](../RevitExportDefinition/RevitExportDefinition_RemoveEmbossMaxHeightRange.md) | Read-write property that gets and sets the max height of embosses in centimeters to remove for the RevitExport. This is only applicable when the RemoveEmbossesStyle is set to kRevitExportRemoveByRange. |
| [RemoveFilletsRadiusRange](../RevitExportDefinition/RevitExportDefinition_RemoveFilletsRadiusRange.md) | Read-write property that gets and sets the radius of fillets in centimeters to remove for the RevitExport. This is only applicable when the RemoveFilletsStyle is set to kRevitExportRemoveByRange. |
| [RemoveFilletsStyle](../RevitExportDefinition/RevitExportDefinition_RemoveFilletsStyle.md) | Read-write property that gets and sets the style to remove fillets for the RevitExport. |
| [RemoveHolesDiameterRange](../RevitExportDefinition/RevitExportDefinition_RemoveHolesDiameterRange.md) | Read-write property that gets and sets the diameter of holes in centimeters to remove for the RevitExport. This is only applicable when the RemoveHolesStyle is set to kRevitExportRemoveByRange. |
| [RemoveHolesStyle](../RevitExportDefinition/RevitExportDefinition_RemoveHolesStyle.md) | Read-write property that gets and sets the style to remove holes for the RevitExport. |
| [RemoveInternalParts](../RevitExportDefinition/RevitExportDefinition_RemoveInternalParts.md) | Read-write property that gets and sets whether to remove internal parts or not. |
| [RemovePartsBySize](../RevitExportDefinition/RevitExportDefinition_RemovePartsBySize.md) | Read-write property that gets and sets whether remove parts by size or not. |
| [RemovePartsSize](../RevitExportDefinition/RevitExportDefinition_RemovePartsSize.md) | Read-write property that gets and sets the bounding box diagonal length in centimeters of the parts being removed. |
| [RemovePocketsMaxDepthRange](../RevitExportDefinition/RevitExportDefinition_RemovePocketsMaxDepthRange.md) | Read-write property that gets and sets the max depth of pockets in centimeters to remove for the RevitExport. This is only applicable when the RemovePocketsStyle is set to kRevitExportRemoveByRange. |
| [RemovePocketsStyle](../RevitExportDefinition/RevitExportDefinition_RemovePocketsStyle.md) | Read-write property that gets and sets the style to remove pockets for the RevitExport. |
| [RemoveTunnelsStyle](../RevitExportDefinition/RevitExportDefinition_RemoveTunnelsStyle.md) | Read-write property that gets and sets the style to remove tunnels for the RevitExport. Valid values for this property are kSimplificationRemoveNone and kSimplificationRemoveAll. |
| [RevitTemplate](../RevitExportDefinition/RevitExportDefinition_RevitTemplate.md) | Read-write property that gets and sets the Revit template file used to create the RevitExport. |
| [RevitVersion](../RevitExportDefinition/RevitExportDefinition_RevitVersion.md) | Read-write property that gets and sets the Revit version. Use the FileManager.GetRevitEngineInstallationStatus to get the Revit versions that can be used to create RevitExport objects. |
| [Structure](../RevitExportDefinition/RevitExportDefinition_Structure.md) | Read-write property that gets and sets the structure. |
| [Type](../RevitExportDefinition/RevitExportDefinition_Type.md) | Gets the constant that indicates the type of this object. |
| [UseColorOverrideFromSourceComponent](../RevitExportDefinition/RevitExportDefinition_UseColorOverrideFromSourceComponent.md) | Read-write property that gets and sets whether use the color override from source component. |

## Accessed From

[RevitExport.Definition](../RevitExport/RevitExport_Definition.md), [RevitExportDefinition.Copy](../RevitExportDefinition/RevitExportDefinition_Copy.md), [RevitExports.CreateDefinition](../RevitExports/RevitExports_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Revit Export sample](../../sample-programs/CreateRevitExportSample_Sample.md) | This sample demonstrates how to create a RevitExport object. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |