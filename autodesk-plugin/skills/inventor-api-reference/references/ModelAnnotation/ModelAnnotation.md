# ModelAnnotation Object

## Description

ModelAnnotation Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelAnnotation/ModelAnnotation_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelAnnotation/ModelAnnotation_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelAnnotation/ModelAnnotation_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelAnnotation/ModelAnnotation_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelAnnotation/ModelAnnotation_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelAnnotation/ModelAnnotation_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelAnnotation/ModelAnnotation_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [HealthStatus](../ModelAnnotation/ModelAnnotation_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelAnnotation/ModelAnnotation_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelAnnotation/ModelAnnotation_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelAnnotation/ModelAnnotation_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelAnnotation/ModelAnnotation_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelAnnotation/ModelAnnotation_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelAnnotation/ModelAnnotation_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelAnnotation/ModelAnnotation_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelAnnotation/ModelAnnotation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelAnnotation/ModelAnnotation_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelAnnotations.Item](../ModelAnnotations/ModelAnnotations_Item.md), [ModelAnnotationsEnumerator.Item](../ModelAnnotationsEnumerator/ModelAnnotationsEnumerator_Item.md), [ModelAnnotationText.Parent](../ModelAnnotationText/ModelAnnotationText_Parent.md), [ModelCompositeAnnotationDefinition.BaseAnnotation](../ModelCompositeAnnotationDefinition/ModelCompositeAnnotationDefinition_BaseAnnotation.md), [ModelGeneralNoteDefinition.Parent](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Parent.md), [ModelHoleThreadNoteDefinition.Parent](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Parent.md), [ModelLeaderNoteDefinition.Parent](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Parent.md)

## Derived Classes

[ModelCompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation.md), [ModelDatumIdentifier](../ModelDatumIdentifier/ModelDatumIdentifier.md), [ModelDatumTarget](../ModelDatumTarget/ModelDatumTarget.md), [ModelDimension](../ModelDimension/ModelDimension.md), [ModelFeatureControlFrame](../ModelFeatureControlFrame/ModelFeatureControlFrame.md), [ModelGeneralNote](../ModelGeneralNote/ModelGeneralNote.md), [ModelHoleThreadNote](../ModelHoleThreadNote/ModelHoleThreadNote.md), [ModelLeaderNote](../ModelLeaderNote/ModelLeaderNote.md), [ModelSurfaceTextureSymbol](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol.md), [ModelWeldingSymbol](../ModelWeldingSymbol/ModelWeldingSymbol.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |