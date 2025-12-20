# ModelHoleThreadNote Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelHoleThreadNote Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelHoleThreadNote/ModelHoleThreadNote_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelHoleThreadNote/ModelHoleThreadNote_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelHoleThreadNote/ModelHoleThreadNote_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelHoleThreadNote/ModelHoleThreadNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelHoleThreadNote/ModelHoleThreadNote_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelHoleThreadNote/ModelHoleThreadNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelHoleThreadNote/ModelHoleThreadNote_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelHoleThreadNote/ModelHoleThreadNote_Definition.md) | Gets and sets the hole/thread defintion associated with the note. |
| [Faces](../ModelHoleThreadNote/ModelHoleThreadNote_Faces.md) | Returns the model hole or thread feature faces associated with the hole or thread note. |
| [HealthStatus](../ModelHoleThreadNote/ModelHoleThreadNote_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelHoleThreadNote/ModelHoleThreadNote_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelHoleThreadNote/ModelHoleThreadNote_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelHoleThreadNote/ModelHoleThreadNote_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelHoleThreadNote/ModelHoleThreadNote_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelHoleThreadNote/ModelHoleThreadNote_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelHoleThreadNote/ModelHoleThreadNote_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelHoleThreadNote/ModelHoleThreadNote_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelHoleThreadNote/ModelHoleThreadNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelHoleThreadNote/ModelHoleThreadNote_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelHoleThreadNoteProxy.NativeObject](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_NativeObject.md), [ModelHoleThreadNotes.Add](../ModelHoleThreadNotes/ModelHoleThreadNotes_Add.md), [ModelHoleThreadNotes.Item](../ModelHoleThreadNotes/ModelHoleThreadNotes_Item.md)

## Derived Classes

[ModelHoleThreadNoteProxy](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |