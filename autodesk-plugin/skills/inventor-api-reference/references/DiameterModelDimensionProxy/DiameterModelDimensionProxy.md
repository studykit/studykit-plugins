# DiameterModelDimensionProxy Object

Derived from: [DiameterModelDimension](../DiameterModelDimension/DiameterModelDimension.md) Object

## Description

DiameterModelDimensionProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [HealthStatus](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018
