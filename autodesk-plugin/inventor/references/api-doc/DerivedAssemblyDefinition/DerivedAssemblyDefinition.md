# DerivedAssemblyDefinition Object

## Description

The DerivedAssemblyDefinition object is used to describe which parts in an assembly will be used during the creation of the DerivedAssemblyComponent. It is also used when querying and editing an existing derived assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetHolePatchingOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_GetHolePatchingOptions.md) | Method that returns the hole patching options for the derived assembly. |
| [GetRemoveBySizeOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_GetRemoveBySizeOptions.md) | Method that returns the simplification options specifying geometry to remove based on size. |
| [GetRemoveByVisibilityOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_GetRemoveByVisibilityOptions.md) | Method that returns the simplification options specifying geometry to remove based on visibility. |
| [IncludeAllParameters](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllParameters.md) | Method that includes all parameters from the source assembly. This includes top level parameters in the source assembly as well as parameters in sub-assemblies and parts. |
| [IncludeAllSketches](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllSketches.md) | Method that includes all sketches from the source assembly. This includes top level sketches in the source assembly as well as sketches in sub-assemblies and parts. |
| [IncludeAllWorkFeatures](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllWorkFeatures.md) | Method that includes all work features from the source assembly. This includes top level work features in the source assembly as well as work features in sub-assemblies and parts. |
| [SetHolePatchingOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_SetHolePatchingOptions.md) | Method that sets the hole patching options for the derived assembly. |
| [SetRemoveBySizeOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_SetRemoveBySizeOptions.md) | Method that sets the simplification options specifying geometry to remove based on size. |
| [SetRemoveByVisibilityOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_SetRemoveByVisibilityOptions.md) | Method that sets the simplification options specifying geometry to remove based on visibility. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActiveModelState](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_ActiveModelState.md) | Read-write property that gets or sets the name of active model state for the derived assembly. |
| [ActivePositionalRepresentation](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_ActivePositionalRepresentation.md) | Gets and sets the name of the active Positional Representation for the derived assembly. |
| [Application](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStyle](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_DeriveStyle.md) | Gets and sets how bodies are derived. Valid options are kDeriveAsSingleBodyWithSeams, kDeriveAsSingleBodyNoSeams and kDeriveAsMultipleBodies. kDeriveAsWorkSurface is not a valid option for derived assemblies. |
| [IncludeAllTopLeveliMateDefinitions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllTopLeveliMateDefinitions.md) | Read-write property that defines whether all top level iMates in the source assembly are included in the derived assembly. |
| [IncludeAllTopLevelParameters](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllTopLevelParameters.md) | Read-write property that defines whether all top level parameters in the source assembly are included in the derived assembly. |
| [IncludeAllTopLevelSketches](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllTopLevelSketches.md) | Read-write property that defines whether all top level sketches in the source assembly are included in the derived assembly. |
| [IncludeAllTopLevelWorkFeatures](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IncludeAllTopLevelWorkFeatures.md) | Read-write property that defines whether all top level work features in the source assembly are included in the derived assembly. |
| [InclusionOption](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_InclusionOption.md) | Property that defines the inclusion status for all of the occurrences in the assembly. Valid options are kDerivedIncludeAll, kDerivedSubtractAll, kDerivedExcludeAll, kDerivedBoundingBox, kDerivedIntersect and kDerivedIndividualDefined. |
| [IndependentSolidsOnFailedBoolean](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IndependentSolidsOnFailedBoolean.md) | Read-write property that gets and sets whether to create independent solids in the derived part when a Boolean operation fails. |
| [IsAssociativeDesignView](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. |
| [LinkFaceColorFromSource](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_LinkFaceColorFromSource.md) | Read-write property that gets and sets whether color override should be removed from the resulting derived part. |
| [LinkSketchFormattingFromSource](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_LinkSketchFormattingFromSource.md) | Read-write property that gets and sets whether color override should be removed from the resulting derived part. |
| [MirrorPlane](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_MirrorPlane.md) | Gets and sets the plane about which the base assembly will be mirrored to create the derived assembly. |
| [Occurrences](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_Occurrences.md) | Property that gets the available in the selected assembly. This returns the top-level occurrences in the assembly. You can use the SubOccurrences of the DerivedAssemblyOccurrence object to traverse through the entire occurrence tree. |
| [ReducedMemoryMode](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_ReducedMemoryMode.md) | Gets and sets reduced memory mode for the derived Assembly. |
| [RemoveInternalVoids](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_RemoveInternalVoids.md) | Read-write property that gets and sets whether internal voids should be removed from the resulting derived part. |
| [ScaleFactor](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_ScaleFactor.md) | Gets or sets the scale factor for the derived Assembly. |
| [Type](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseOrientedMinimumBoundingBox](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_UseOrientedMinimumBoundingBox.md) | Read-write Boolean property that specifies whether to use the oriented minimum bounding box or orthogonal bounding box for the components that are included as bounding box. |

## Accessed From

[DerivedAssemblyComponent.Definition](../DerivedAssemblyComponent/DerivedAssemblyComponent_Definition.md), [DerivedAssemblyComponentProxy.Definition](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Definition.md), [DerivedAssemblyComponents.CreateDefinition](../DerivedAssemblyComponents/DerivedAssemblyComponents_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |