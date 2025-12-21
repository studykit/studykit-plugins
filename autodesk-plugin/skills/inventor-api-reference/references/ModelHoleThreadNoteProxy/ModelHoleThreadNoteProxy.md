# ModelHoleThreadNoteProxy Object

Derived from: [ModelHoleThreadNote](../ModelHoleThreadNote/ModelHoleThreadNote.md) Object

## Description

ModelHoleThreadNoteProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Definition.md) | Gets and sets the hole/thread defintion associated with the note. |
| [Faces](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Faces.md) | Returns the model hole or thread feature faces associated with the hole or thread note. |
| [HealthStatus](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |