# ModelAnnotations Object

## Description

The ModelAnnotations collection object provides access to all of the annotations in a part or assembly. This includes dimensions and other types of annotations.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateAnnotationPlaneDefinitionUsingIntents](../ModelAnnotations/ModelAnnotations_CreateAnnotationPlaneDefinitionUsingIntents.md) | Method that determines all of the valid annotation planes for the given input. The definitions for these annotation planes is returned as a collection, allowing you to select the desired annotation plane to use when creating annotation. |
| [CreateAnnotationPlaneDefinitionUsingPlane](../ModelAnnotations/ModelAnnotations_CreateAnnotationPlaneDefinitionUsingPlane.md) | Method that returns an annotation plane definition for the given planar entity. The object returned is not an annotation plane, but is the information that defines a plane and can be used to create an annotation plane when an annotation is created. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelAnnotations/ModelAnnotations_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ModelAnnotations/ModelAnnotations_Count.md) | Gets the number of items in this collection. |
| [Item](../ModelAnnotations/ModelAnnotations_Item.md) | Method that returns the specified model annotation object from the collection. |
| [ModelCompositeAnnotations](../ModelAnnotations/ModelAnnotations_ModelCompositeAnnotations.md) | Read-only property that returns ModelCompositeAnnotations collection object. |
| [ModelDatumIdentifiers](../ModelAnnotations/ModelAnnotations_ModelDatumIdentifiers.md) | Read-only property that returns the ModelDatumIdentifiers collection object. This object provides access to all of the datum ID’s in the part or assembly. |
| [ModelDatums](../ModelAnnotations/ModelAnnotations_ModelDatums.md) | Returns the ModelDatums collection object. |
| [ModelDimensions](../ModelAnnotations/ModelAnnotations_ModelDimensions.md) | Read-only property that returns the ModelDimensions collection object. This object provides access to all of the model dimensions in the part or assembly. |
| [ModelFeatureControlFrames](../ModelAnnotations/ModelAnnotations_ModelFeatureControlFrames.md) | Read-only property that returns the ModelFeatureControlFrames collection object. This object provides access to all of the feature controls frames in the part or assembly. |
| [ModelGeneralNotes](../ModelAnnotations/ModelAnnotations_ModelGeneralNotes.md) | Returns ModelGeneralNotes collection object. |
| [ModelHoleThreadNotes](../ModelAnnotations/ModelAnnotations_ModelHoleThreadNotes.md) | Read-only property that returns the ModelHoleThreadNotes collection object. This object provides access to all of the model dimensions in the part or assembly. |
| [ModelLeaderNotes](../ModelAnnotations/ModelAnnotations_ModelLeaderNotes.md) | Read-only property that returns the ModelLeaderNotes collection object. This object provides access to all of the model dimensions in the part or assembly. |
| [ModelSurfaceTextureSymbols](../ModelAnnotations/ModelAnnotations_ModelSurfaceTextureSymbols.md) | Read-only property that returns the ModelSurfaceTextureSymbols collection object. This object provides access to all of the surface texture symbols in the part or assembly. |
| [ModelWeldingSymbols](../ModelAnnotations/ModelAnnotations_ModelWeldingSymbols.md) | Returns the ModelWeldingSymbols collection object. |
| [Type](../ModelAnnotations/ModelAnnotations_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[AssemblyComponentDefinition.ModelAnnotations](../AssemblyComponentDefinition/AssemblyComponentDefinition_ModelAnnotations.md), [FlatPattern.ModelAnnotations](../FlatPattern/FlatPattern_ModelAnnotations.md), [PartComponentDefinition.ModelAnnotations](../PartComponentDefinition/PartComponentDefinition_ModelAnnotations.md), [SheetMetalComponentDefinition.ModelAnnotations](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelAnnotations.md), [WeldmentComponentDefinition.ModelAnnotations](../WeldmentComponentDefinition/WeldmentComponentDefinition_ModelAnnotations.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |