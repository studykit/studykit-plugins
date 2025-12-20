# ModelGeneralNoteProxy Object

Derived from: [ModelGeneralNote](../ModelGeneralNote/ModelGeneralNote.md) Object

## Description

ModelGeneralNoteProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Definition.md) | Gets and sets the definition associated with this symbol. |
| [HealthStatus](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |