# DerivedPartCoordinateSystemDef Object

Derived from: [DerivedPartDefinition](../DerivedPartDefinition/DerivedPartDefinition.md) Object

## Description

The DerivedPartCoordinateSystemDef object allows you to query and define the coordinate system for a derived part, as well as to include and exclude elements and characteristics from the base part to the part to be derived.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExcludeAll](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_ExcludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedExcludeAll. Description This method should exclude all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |
| [GetCoordinateSystem](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_GetCoordinateSystem.md) | Method that returns the coordinate system. |
| [GetScale](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_GetScale.md) | Method that returns the scale factors along the x, y and z directions. |
| [IncludeAll](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IncludeAll.md) | Method that causes all entities within the derived part component to be set to kDerivedIncludeAll. |
| [SetCoordinateSystem](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_SetCoordinateSystem.md) | Method that sets the coordinate system. |
| [SetScale](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_SetScale.md) | Method that sets the scale factors along the x, y and z directions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_ActiveModelState.md) | Read-write property that gets or sets the name of active model state for the derived part. |
| [Application](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStyle](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_DeriveStyle.md) | Gets and sets how bodies are derived. Valid options are kDeriveAsSingleBodyWithSeams, kDeriveAsSingleBodyNoSeams, kDeriveAsMultipleBodies and kDeriveAsWorkSurface. |
| [Finishes](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Finishes.md) | Gets the collection of FinishFeatures available in the selected part along with the inclusion option for each FinishFeature. |
| [iMateDefinitions](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_iMateDefinitions.md) | Property that gets the collection of iMates available in the selected part along with the inclusion option for each iMate. |
| [IncludeAlliMateDefinitions](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IncludeAlliMateDefinitions.md) | Gets and sets whether all iMates are included in the derived part. |
| [IncludeAllParameters](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IncludeAllParameters.md) | Property that defines whether exported parameters are included in the derived part. This property is initialized to True when the DerivedPartDefinition object is created. |
| [IncludeAllSolids](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IncludeAllSolids.md) | Gets and sets whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IncludeAllSurfaces](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IncludeAllSurfaces.md) | Property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. |
| [IsAssociativeDesignView](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. |
| [LinkFaceColorFromSource](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_LinkFaceColorFromSource.md) | Read-write Boolean property that specifies whether to link face color from source component or not. |
| [LinkSheetMetalStyles](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_LinkSheetMetalStyles.md) | Read-write Boolean property that specifies whether to link sheet metal styles or not. This is applicable only when derive another sheet metal document to current sheet metal document. |
| [LinkSketchFormattingFromSource](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_LinkSketchFormattingFromSource.md) | Read-write Boolean property that specifies whether to link sketch formatting from source component or not. |
| [MirrorPlane](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_MirrorPlane.md) | Sets the plane about which the base part will be mirrored to create the derived part. |
| [Parameters](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Parameters.md) | Property that gets the collection of parameters available in the selected part along with the inclusion option for each parameter. |
| [ReducedMemoryMode](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_ReducedMemoryMode.md) | Read-write property that gets and sets the Reduced Memory Mode. |
| [Solids](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Solids.md) | Property that gets the collection of solids available in the selected part along with the inclusion option for each solid. |
| [Surfaces](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Surfaces.md) | Property that gets the collection of surfaces available in the selected part along with the inclusion option for each surface. |
| [Type](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseOrientedMinimumBoundingBox](../DerivedPartCoordinateSystemDef/DerivedPartCoordinateSystemDef_UseOrientedMinimumBoundingBox.md) | Read-write Boolean property that specifies whether to use the oriented minimum bounding box or orthogonal bounding box for the components that are included as bounding box. |

## Accessed From

[DerivedPartComponents.CreateCoordinateSystemDef](../DerivedPartComponents/DerivedPartComponents_CreateCoordinateSystemDef.md)

## Version

Introduced in version 6
