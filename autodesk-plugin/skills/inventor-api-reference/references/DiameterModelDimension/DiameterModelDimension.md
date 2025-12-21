# DiameterModelDimension Object

Derived from: [ModelDimension](../ModelDimension/ModelDimension.md) Object

## Description

The DiameterModelDimension object represents a diameter model dimension in a part or assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DiameterModelDimension/DiameterModelDimension_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../DiameterModelDimension/DiameterModelDimension_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../DiameterModelDimension/DiameterModelDimension_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../DiameterModelDimension/DiameterModelDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DiameterModelDimension/DiameterModelDimension_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../DiameterModelDimension/DiameterModelDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../DiameterModelDimension/DiameterModelDimension_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../DiameterModelDimension/DiameterModelDimension_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [HealthStatus](../DiameterModelDimension/DiameterModelDimension_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../DiameterModelDimension/DiameterModelDimension_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../DiameterModelDimension/DiameterModelDimension_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../DiameterModelDimension/DiameterModelDimension_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../DiameterModelDimension/DiameterModelDimension_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../DiameterModelDimension/DiameterModelDimension_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../DiameterModelDimension/DiameterModelDimension_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../DiameterModelDimension/DiameterModelDimension_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../DiameterModelDimension/DiameterModelDimension_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../DiameterModelDimension/DiameterModelDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../DiameterModelDimension/DiameterModelDimension_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[DiameterModelDimensionProxy.NativeObject](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_NativeObject.md), [DiameterModelDimensions.Add](../DiameterModelDimensions/DiameterModelDimensions_Add.md), [DiameterModelDimensions.Item](../DiameterModelDimensions/DiameterModelDimensions_Item.md)

## Derived Classes

[DiameterModelDimensionProxy](../DiameterModelDimensionProxy/DiameterModelDimensionProxy.md)

## Version

Introduced in version 2018
