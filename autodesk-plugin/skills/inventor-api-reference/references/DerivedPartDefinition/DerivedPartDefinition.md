# DerivedPartDefinition Object

## Description

The DerivedPartDefinition object is used to describe which entities within a part will be used during the creation of the DerivedPartComponent. It is also used when querying and editing an existing derived part.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExcludeAll](../DerivedPartDefinition/DerivedPartDefinition_ExcludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedExcludeAll. Description This method should exclude all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |
| [IncludeAll](../DerivedPartDefinition/DerivedPartDefinition_IncludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedIncludeAll. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedPartDefinition/DerivedPartDefinition_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../DerivedPartDefinition/DerivedPartDefinition_ActiveModelState.md) | Read-write property that gets or sets the name of active model state for the derived part. |
| [Application](../DerivedPartDefinition/DerivedPartDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStyle](../DerivedPartDefinition/DerivedPartDefinition_DeriveStyle.md) | Gets and sets how bodies are derived. Valid options are kDeriveAsSingleBodyWithSeams, kDeriveAsSingleBodyNoSeams, kDeriveAsMultipleBodies and kDeriveAsWorkSurface. |
| [Finishes](../DerivedPartDefinition/DerivedPartDefinition_Finishes.md) | Gets the collection of FinishFeatures available in the selected part along with the inclusion option for each FinishFeature. |
| [iMateDefinitions](../DerivedPartDefinition/DerivedPartDefinition_iMateDefinitions.md) | Property that gets the collection of iMates available in the selected part along with the inclusion option for each iMate. |
| [IncludeAlliMateDefinitions](../DerivedPartDefinition/DerivedPartDefinition_IncludeAlliMateDefinitions.md) | Gets and sets whether all iMates are included in the derived part. |
| [IncludeAllParameters](../DerivedPartDefinition/DerivedPartDefinition_IncludeAllParameters.md) | Property that defines whether exported parameters are included in the derived part. This property is initialized to True when the DerivedPartDefinition object is created. |
| [IncludeAllSolids](../DerivedPartDefinition/DerivedPartDefinition_IncludeAllSolids.md) | Gets and sets whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllSurfaces](../DerivedPartDefinition/DerivedPartDefinition_IncludeAllSurfaces.md) | Property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IsAssociativeDesignView](../DerivedPartDefinition/DerivedPartDefinition_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. |
| [LinkFaceColorFromSource](../DerivedPartDefinition/DerivedPartDefinition_LinkFaceColorFromSource.md) | Read-write Boolean property that specifies whether to link face color from source component or not. |
| [LinkSheetMetalStyles](../DerivedPartDefinition/DerivedPartDefinition_LinkSheetMetalStyles.md) | Read-write Boolean property that specifies whether to link sheet metal styles or not. This is applicable only when derive another sheet metal document to current sheet metal document. |
| [LinkSketchFormattingFromSource](../DerivedPartDefinition/DerivedPartDefinition_LinkSketchFormattingFromSource.md) | Read-write Boolean property that specifies whether to link sketch formatting from source component or not. |
| [Parameters](../DerivedPartDefinition/DerivedPartDefinition_Parameters.md) | Property that gets the collection of parameters available in the selected part along with the inclusion option for each parameter. |
| [ReducedMemoryMode](../DerivedPartDefinition/DerivedPartDefinition_ReducedMemoryMode.md) | Read-write property that gets and sets the Reduced Memory Mode. |
| [Solids](../DerivedPartDefinition/DerivedPartDefinition_Solids.md) | Property that gets the collection of solids available in the selected part along with the inclusion option for each solid. |
| [Surfaces](../DerivedPartDefinition/DerivedPartDefinition_Surfaces.md) | Property that gets the collection of surfaces available in the selected part along with the inclusion option for each surface. |
| [Type](../DerivedPartDefinition/DerivedPartDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseOrientedMinimumBoundingBox](../DerivedPartDefinition/DerivedPartDefinition_UseOrientedMinimumBoundingBox.md) | Read-write Boolean property that specifies whether to use the oriented minimum bounding box or orthogonal bounding box for the components that are included as bounding box. |

## Accessed From

[DerivedPartComponent.Definition](../DerivedPartComponent/DerivedPartComponent_Definition.md), [DerivedPartComponentProxy.Definition](../DerivedPartComponentProxy/DerivedPartComponentProxy_Definition.md)

## Derived Classes

[DerivedPartCoordinateSystemDef](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef.md), [DerivedPartTransformDef](../DerivedPartTransformDef/DerivedPartTransformDef.md), [DerivedPartUniformScaleDef](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |