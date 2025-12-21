# RadiusModelDimension Object

Derived from: [ModelDimension](../ModelDimension/ModelDimension.md) Object

## Description

The RadiusModelDimension object represents a radius model dimension in a part or assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusModelDimension/RadiusModelDimension_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../RadiusModelDimension/RadiusModelDimension_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../RadiusModelDimension/RadiusModelDimension_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../RadiusModelDimension/RadiusModelDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RadiusModelDimension/RadiusModelDimension_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../RadiusModelDimension/RadiusModelDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../RadiusModelDimension/RadiusModelDimension_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../RadiusModelDimension/RadiusModelDimension_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [HealthStatus](../RadiusModelDimension/RadiusModelDimension_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../RadiusModelDimension/RadiusModelDimension_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../RadiusModelDimension/RadiusModelDimension_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../RadiusModelDimension/RadiusModelDimension_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../RadiusModelDimension/RadiusModelDimension_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../RadiusModelDimension/RadiusModelDimension_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../RadiusModelDimension/RadiusModelDimension_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../RadiusModelDimension/RadiusModelDimension_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../RadiusModelDimension/RadiusModelDimension_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../RadiusModelDimension/RadiusModelDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RadiusModelDimension/RadiusModelDimension_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[RadiusModelDimensionProxy.NativeObject](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_NativeObject.md), [RadiusModelDimensions.Add](../RadiusModelDimensions/RadiusModelDimensions_Add.md), [RadiusModelDimensions.Item](../RadiusModelDimensions/RadiusModelDimensions_Item.md)

## Derived Classes

[RadiusModelDimensionProxy](../RadiusModelDimensionProxy/RadiusModelDimensionProxy.md)

## Version

Introduced in version 2018
