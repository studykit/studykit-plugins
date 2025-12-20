# RadiusModelDimensionProxy Object

Derived from: [RadiusModelDimension](../RadiusModelDimension/RadiusModelDimension.md) Object

## Description

RadiusModelDimensionProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [HealthStatus](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |