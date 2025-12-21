# PartOptions Object

## Description

The PartOptions object provides access to properties that provide read and write access of the part related application options. This is somewhat equivalent to the Part tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartOptions/PartOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoConsumeWorkAndSurfaceFeatures](../PartOptions/PartOptions_AutoConsumeWorkAndSurfaceFeatures.md) | Enables/disables automatically consuming work and surface features when they are used as inputs for creating other features. |
| [AutoHideInLineWorkFeatures](../PartOptions/PartOptions_AutoHideInLineWorkFeatures.md) | Enables/disables the behavior of automatically hiding an in-line work feature. |
| [DefaultDesignView](../PartOptions/PartOptions_DefaultDesignView.md) | Read-write property that gets and sets the default design view representation to use when opening part documents. |
| [DefaultDesignViewIsAssociative](../PartOptions/PartOptions_DefaultDesignViewIsAssociative.md) | Read-write Boolean property that gets and sets whether the default design view representation is associative. |
| [DimensionConstraintsRelaxation](../PartOptions/PartOptions_DimensionConstraintsRelaxation.md) | Gets and Sets the preference for relaxing dimension constraints during 3D grip edit. |
| [DisplayExtendedName](../PartOptions/PartOptions_DisplayExtendedName.md) | Read-write property that gets and sets whether to display extended information after the feature name in the browser. |
| [DisplayGripsOnSelection](../PartOptions/PartOptions_DisplayGripsOnSelection.md) | Enables/disables display of glyphs for 3D grips when faces are selected. |
| [EditBaseSolidsUsingFusion](../PartOptions/PartOptions_EditBaseSolidsUsingFusion.md) | Read-write property that gets and sets whether command to edit base solids in parts launches Inventor Fusion or the legacy Solid Edit environment. This property cannot be set to True if Inventor Fusion is not installed. |
| [Enable3DGrips](../PartOptions/PartOptions_Enable3DGrips.md) | Enables/disables access to 3D grips. |
| [EnableConstructionEnvironment](../PartOptions/PartOptions_EnableConstructionEnvironment.md) | Enable/Disable Construction Environment. |
| [GeometricConstraintsBreakage](../PartOptions/PartOptions_GeometricConstraintsBreakage.md) | Gets and Sets the preference for breaking geometric constraints during 3D grip edit. |
| [LinkFaceColorFromSource](../PartOptions/PartOptions_LinkFaceColorFromSource.md) | Read-write Boolean property that specifies whether to link face color from source component or not. |
| [LinkSketchFormattingFromSource](../PartOptions/PartOptions_LinkSketchFormattingFromSource.md) | Read-write Boolean property that specifies whether to link sketch formatting from source component or not. |
| [OpaqueConstructionSurfaces](../PartOptions/PartOptions_OpaqueConstructionSurfaces.md) | Enables/disables whether construction surfaces are displayed opaque or translucent. |
| [SketchCreationOnNewPart](../PartOptions/PartOptions_SketchCreationOnNewPart.md) | Gets and sets the preference for creating a sketch when a new part file is created. |
| [Type](../PartOptions/PartOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.PartOptions](../Application/Application_PartOptions.md), [InventorServer.PartOptions](InventorServer_PartOptions.md), [InventorServerObject.PartOptions](InventorServerObject_PartOptions.md)

## Version

Introduced in version 11
