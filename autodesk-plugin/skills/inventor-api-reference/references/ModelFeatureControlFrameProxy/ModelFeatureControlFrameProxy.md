# ModelFeatureControlFrameProxy Object

Derived from: [ModelFeatureControlFrame](../ModelFeatureControlFrame/ModelFeatureControlFrame.md) Object

## Description

ModelFeatureControlFrameProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. |
| [HealthStatus](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |