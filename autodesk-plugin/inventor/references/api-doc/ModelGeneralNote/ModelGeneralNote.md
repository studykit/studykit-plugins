# ModelGeneralNote Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelGeneralNote Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelGeneralNote/ModelGeneralNote_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelGeneralNote/ModelGeneralNote_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelGeneralNote/ModelGeneralNote_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelGeneralNote/ModelGeneralNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelGeneralNote/ModelGeneralNote_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelGeneralNote/ModelGeneralNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelGeneralNote/ModelGeneralNote_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelGeneralNote/ModelGeneralNote_Definition.md) | Gets and sets the definition associated with this symbol. |
| [HealthStatus](../ModelGeneralNote/ModelGeneralNote_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelGeneralNote/ModelGeneralNote_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelGeneralNote/ModelGeneralNote_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelGeneralNote/ModelGeneralNote_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelGeneralNote/ModelGeneralNote_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelGeneralNote/ModelGeneralNote_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelGeneralNote/ModelGeneralNote_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelGeneralNote/ModelGeneralNote_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelGeneralNote/ModelGeneralNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelGeneralNote/ModelGeneralNote_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelGeneralNoteProxy.NativeObject](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_NativeObject.md), [ModelGeneralNotes.Add](../ModelGeneralNotes/ModelGeneralNotes_Add.md), [ModelGeneralNotes.Item](../ModelGeneralNotes/ModelGeneralNotes_Item.md)

## Derived Classes

[ModelGeneralNoteProxy](../ModelGeneralNoteProxy/ModelGeneralNoteProxy.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |