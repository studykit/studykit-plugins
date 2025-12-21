# AssemblyOptions Object

## Description

The AssemblyOptions object provides access to properties that provide read and write access of the assembly related application options. This is somewhat equivalent to the Assembly tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssemblyOptions/AssemblyOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssemblyExpressMinimumUniqueDocument](../AssemblyOptions/AssemblyOptions_AssemblyExpressMinimumUniqueDocument.md) | Gets and sets the minimum number of unique documents to open in assembly Express mode by default. |
| [ConstraintAudioNotification](../AssemblyOptions/AssemblyOptions_ConstraintAudioNotification.md) | Enables or Disables audio notifications when creating constraints. |
| [DeferUpdate](../AssemblyOptions/AssemblyOptions_DeferUpdate.md) | Enables or Disables updating assemblies. |
| [DeleteComponentPatternSources](../AssemblyOptions/AssemblyOptions_DeleteComponentPatternSources.md) | Gets/Sets the behavior when deleting pattern elements. |
| [DisplayComponentNamesInConstraints](../AssemblyOptions/AssemblyOptions_DisplayComponentNamesInConstraints.md) | Gets and sets whether component names should be suffixed to constraint names. |
| [EnableAssemblyExpress](../AssemblyOptions/AssemblyOptions_EnableAssemblyExpress.md) | Enables or disables assembly Express workflows. |
| [EnableConstraintRedundancyAnalysis](../AssemblyOptions/AssemblyOptions_EnableConstraintRedundancyAnalysis.md) | Gets/Sets analysis of all assembly components for adaptivity adjustments. |
| [EnableCrossPartEdgeLoopProjection](../AssemblyOptions/AssemblyOptions_EnableCrossPartEdgeLoopProjection.md) | Enables or disables associative edge/loop geometry projection during in-place modeling. |
| [EnableCrossPartSketchGeometryProjection](../AssemblyOptions/AssemblyOptions_EnableCrossPartSketchGeometryProjection.md) | Enables or disables associative sketch geometry projection during in-place modeling. |
| [FromToExtentsAdaptFeature](../AssemblyOptions/AssemblyOptions_FromToExtentsAdaptFeature.md) | Enables or Disables automatically adapting the in-place feature size or position. |
| [FromToExtentsMatePlane](../AssemblyOptions/AssemblyOptions_FromToExtentsMatePlane.md) | Enables or Disables automatically creating the feature to the desired size and mating it to the plane. |
| [OnlyActiveComponentIsOpaque](../AssemblyOptions/AssemblyOptions_OnlyActiveComponentIsOpaque.md) | Gets/Sets Opaqueness of Active Component. |
| [PartFeaturesInitiallyAdaptive](../AssemblyOptions/AssemblyOptions_PartFeaturesInitiallyAdaptive.md) | Gets/Sets the default adaptive behavior when new features are created. |
| [PlaceAndGroundFirstComponentAtOrigin](../AssemblyOptions/AssemblyOptions_PlaceAndGroundFirstComponentAtOrigin.md) | Place and ground first component at origin. |
| [SectionAllParts](../AssemblyOptions/AssemblyOptions_SectionAllParts.md) | Enables or Disables sectioning of all parts including standard parts in an assembly. |
| [Type](../AssemblyOptions/AssemblyOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseLastOccurrenceOrientationForPlacement](../AssemblyOptions/AssemblyOptions_UseLastOccurrenceOrientationForPlacement.md) | Gets and sets whether the last used orientation should be applied when placing components interactively. |
| [ZoomTargetComponentWithiMate](../AssemblyOptions/AssemblyOptions_ZoomTargetComponentWithiMate.md) | Gets/Sets the default zoom behavior for the graphics window when placing components with iMates. |

## Accessed From

[Application.AssemblyOptions](../Application/Application_AssemblyOptions.md), [InventorServer.AssemblyOptions](InventorServer_AssemblyOptions.md), [InventorServerObject.AssemblyOptions](InventorServerObject_AssemblyOptions.md)

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |