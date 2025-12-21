# ModelDimension Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelDimension Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelDimension/ModelDimension_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelDimension/ModelDimension_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelDimension/ModelDimension_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelDimension/ModelDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelDimension/ModelDimension_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelDimension/ModelDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelDimension/ModelDimension_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelDimension/ModelDimension_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [HealthStatus](../ModelDimension/ModelDimension_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelDimension/ModelDimension_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelDimension/ModelDimension_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelDimension/ModelDimension_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../ModelDimension/ModelDimension_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../ModelDimension/ModelDimension_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelDimension/ModelDimension_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelDimension/ModelDimension_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelDimension/ModelDimension_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelDimension/ModelDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelDimension/ModelDimension_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[AngularModelDimensionDefinition.Parent](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Parent.md), [DiameterModelDimensionDefinition.Parent](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Parent.md), [LinearModelDimensionDefinition.Parent](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Parent.md), [ModelDimensionDefinition.Parent](../ModelDimensionDefinition/ModelDimensionDefinition_Parent.md), [ModelDimensions.Item](../ModelDimensions/ModelDimensions_Item.md), [ModelDimensions.PromoteFrom](../ModelDimensions/ModelDimensions_PromoteFrom.md), [RadiusModelDimensionDefinition.Parent](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition_Parent.md)

## Derived Classes

[AngularModelDimension](../AngularModelDimension/AngularModelDimension.md), [DiameterModelDimension](../DiameterModelDimension/DiameterModelDimension.md), [LinearModelDimension](../LinearModelDimension/LinearModelDimension.md), [RadiusModelDimension](../RadiusModelDimension/RadiusModelDimension.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |