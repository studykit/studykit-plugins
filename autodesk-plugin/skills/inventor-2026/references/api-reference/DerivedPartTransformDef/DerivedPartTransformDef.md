# DerivedPartTransformDef Object

Derived from: [DerivedPartDefinition](../DerivedPartDefinition/DerivedPartDefinition.md) Object

## Description

The DerivedPartCoordinateSystemDef object allows you to define the transformation for a derived part, as well as to include and exclude elements from the base part to the part to be derived.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExcludeAll](../DerivedPartTransformDef/DerivedPartTransformDef_ExcludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedExcludeAll. Description This method should exclude all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |
| [GetTransformation](../DerivedPartTransformDef/DerivedPartTransformDef_GetTransformation.md) | Method that gets the matrix describing the transform that should be applied to the entities being derived. |
| [IncludeAll](../DerivedPartTransformDef/DerivedPartTransformDef_IncludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedIncludeAll. |
| [SetTransformation](../DerivedPartTransformDef/DerivedPartTransformDef_SetTransformation.md) | Method that sets the matrix describing the transform that should be applied to the entities being derived. Operations allowed in the transform are: translation, rotation, non-uniform scale and mirror. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedPartTransformDef/DerivedPartTransformDef_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../DerivedPartTransformDef/DerivedPartTransformDef_ActiveModelState.md) | Read-write property that gets or sets the name of active model state for the derived part. |
| [Application](../DerivedPartTransformDef/DerivedPartTransformDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStyle](../DerivedPartTransformDef/DerivedPartTransformDef_DeriveStyle.md) | Gets and sets how bodies are derived. Valid options are kDeriveAsSingleBodyWithSeams, kDeriveAsSingleBodyNoSeams, kDeriveAsMultipleBodies and kDeriveAsWorkSurface. |
| [Finishes](../DerivedPartTransformDef/DerivedPartTransformDef_Finishes.md) | Gets the collection of FinishFeatures available in the selected part along with the inclusion option for each FinishFeature. |
| [iMateDefinitions](../DerivedPartTransformDef/DerivedPartTransformDef_iMateDefinitions.md) | Property that gets the collection of iMates available in the selected part along with the inclusion option for each iMate. |
| [IncludeAlliMateDefinitions](../DerivedPartTransformDef/DerivedPartTransformDef_IncludeAlliMateDefinitions.md) | Gets and sets whether all iMates are included in the derived part. |
| [IncludeAllParameters](../DerivedPartTransformDef/DerivedPartTransformDef_IncludeAllParameters.md) | Property that defines whether exported parameters are included in the derived part. This property is initialized to True when the DerivedPartDefinition object is created. |
| [IncludeAllSolids](../DerivedPartTransformDef/DerivedPartTransformDef_IncludeAllSolids.md) | Gets and sets whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllSurfaces](../DerivedPartTransformDef/DerivedPartTransformDef_IncludeAllSurfaces.md) | Property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IsAssociativeDesignView](../DerivedPartTransformDef/DerivedPartTransformDef_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. |
| [LinkFaceColorFromSource](../DerivedPartTransformDef/DerivedPartTransformDef_LinkFaceColorFromSource.md) | Read-write Boolean property that specifies whether to link face color from source component or not. |
| [LinkSheetMetalStyles](../DerivedPartTransformDef/DerivedPartTransformDef_LinkSheetMetalStyles.md) | Read-write Boolean property that specifies whether to link sheet metal styles or not. This is applicable only when derive another sheet metal document to current sheet metal document. |
| [LinkSketchFormattingFromSource](../DerivedPartTransformDef/DerivedPartTransformDef_LinkSketchFormattingFromSource.md) | Read-write Boolean property that specifies whether to link sketch formatting from source component or not. |
| [Parameters](../DerivedPartTransformDef/DerivedPartTransformDef_Parameters.md) | Property that gets the collection of parameters available in the selected part along with the inclusion option for each parameter. |
| [ReducedMemoryMode](../DerivedPartTransformDef/DerivedPartTransformDef_ReducedMemoryMode.md) | Read-write property that gets and sets the Reduced Memory Mode. |
| [Solids](../DerivedPartTransformDef/DerivedPartTransformDef_Solids.md) | Property that gets the collection of solids available in the selected part along with the inclusion option for each solid. |
| [Surfaces](../DerivedPartTransformDef/DerivedPartTransformDef_Surfaces.md) | Property that gets the collection of surfaces available in the selected part along with the inclusion option for each surface. |
| [Type](../DerivedPartTransformDef/DerivedPartTransformDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseOrientedMinimumBoundingBox](../DerivedPartTransformDef/DerivedPartTransformDef_UseOrientedMinimumBoundingBox.md) | Read-write Boolean property that specifies whether to use the oriented minimum bounding box or orthogonal bounding box for the components that are included as bounding box. |

## Accessed From

[DerivedPartComponents.CreateTransformDef](../DerivedPartComponents/DerivedPartComponents_CreateTransformDef.md)

## Version

Introduced in version 6
