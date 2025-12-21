# DerivedPartUniformScaleDef Object

Derived from: [DerivedPartDefinition](../DerivedPartDefinition/DerivedPartDefinition.md) Object

## Description

The DerivedPartUniformScaleDef object allows you to query and define the uniform scale for a derived part, as well as to include and exclude elements and characteristics from the base part to the part to be derived.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExcludeAll](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_ExcludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedExcludeAll. Description This method should exclude all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |
| [IncludeAll](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedIncludeAll. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_ActiveModelState.md) | Read-write property that gets or sets the name of active model state for the derived part. |
| [Application](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStyle](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_DeriveStyle.md) | Gets and sets how bodies are derived. Valid options are kDeriveAsSingleBodyWithSeams, kDeriveAsSingleBodyNoSeams, kDeriveAsMultipleBodies and kDeriveAsWorkSurface. |
| [Finishes](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Finishes.md) | Gets the collection of FinishFeatures available in the selected part along with the inclusion option for each FinishFeature. |
| [iMateDefinitions](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_iMateDefinitions.md) | Property that gets the collection of iMates available in the selected part along with the inclusion option for each iMate. |
| [IncludeAlliMateDefinitions](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAlliMateDefinitions.md) | Gets and sets whether all iMates are included in the derived part. |
| [IncludeAllParameters](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllParameters.md) | Property that defines whether exported parameters are included in the derived part. This property is initialized to True when the DerivedPartDefinition object is created. |
| [IncludeAllSketchBlockDefinitions](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllSketchBlockDefinitions.md) | Gets or sets whether all sketch block definitions are included in the derived part. |
| [IncludeAllSketches](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllSketches.md) | Property that defines whether all sketches are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllSketches3D](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllSketches3D.md) | Gets or sets whether all sketches3D are included in the derived part. |
| [IncludeAllSolids](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllSolids.md) | Gets and sets whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllSurfaces](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllSurfaces.md) | Property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllWorkFeatures](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IncludeAllWorkFeatures.md) | Property that defines whether all work features are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IsAssociativeDesignView](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. |
| [LinkFaceColorFromSource](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_LinkFaceColorFromSource.md) | Read-write Boolean property that specifies whether to link face color from source component or not. |
| [LinkSheetMetalStyles](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_LinkSheetMetalStyles.md) | Read-write Boolean property that specifies whether to link sheet metal styles or not. This is applicable only when derive another sheet metal document to current sheet metal document. |
| [LinkSketchFormattingFromSource](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_LinkSketchFormattingFromSource.md) | Read-write Boolean property that specifies whether to link sketch formatting from source component or not. |
| [MirrorPlane](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_MirrorPlane.md) | Property that gets and sets the plane about which the base part will be mirrored to create the derived part. This property is initialized to kDerivedPartNoMirrorPlane when the DerivedPartDefinition object is created. |
| [Parameters](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Parameters.md) | Property that gets the collection of parameters available in the selected part along with the inclusion option for each parameter. |
| [ReducedMemoryMode](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_ReducedMemoryMode.md) | Read-write property that gets and sets the Reduced Memory Mode. |
| [ScaleFactor](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_ScaleFactor.md) | Property that gets and sets the scale factor for the Derived Part. The base part will be scaled by this factor to create the Derived Part. This property is initialized to 1.0 when the DerivedPartDefinition object is created. |
| [SketchBlockDefinitions](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_SketchBlockDefinitions.md) | Property that gets the collection of sketch block definitions available in the selected part along with the inclusion option for each sketch block definition. |
| [SketchBlocks](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_SketchBlocks.md) | Property that gets the collection of sketch blocks available in the selected part along with the inclusion option for each sketch block. |
| [Sketches](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Sketches.md) | Property that returns the collection of sketches available in the selected part along with the inclusion option for each sketch. |
| [Sketches3D](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Sketches3D.md) | Property that gets the collection of 3D sketches available in the selected part along with the inclusion option for each sketch. |
| [Solids](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Solids.md) | Property that gets the collection of solids available in the selected part along with the inclusion option for each solid. |
| [Surfaces](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Surfaces.md) | Property that gets the collection of surfaces available in the selected part along with the inclusion option for each surface. |
| [Type](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseOrientedMinimumBoundingBox](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_UseOrientedMinimumBoundingBox.md) | Read-write Boolean property that specifies whether to use the oriented minimum bounding box or orthogonal bounding box for the components that are included as bounding box. |
| [WorkFeatures](../DerivedPartUniformScaleDef/DerivedPartUniformScaleDef_WorkFeatures.md) | Property that returns the collection of work features available in the selected part along with the inclusion option for each work feature. |

## Accessed From

[DerivedPartComponents.CreateUniformScaleDef](../DerivedPartComponents/DerivedPartComponents_CreateUniformScaleDef.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |

## Version

Introduced in version 6
