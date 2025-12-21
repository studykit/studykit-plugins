# AngularModelDimension Object

Derived from: [ModelDimension](../ModelDimension/ModelDimension.md) Object

## Description

AngularModelDimension Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CenterText](../AngularModelDimension/AngularModelDimension_CenterText.md) | Method that centers the dimension text on the dimension line. |
| [Delete](../AngularModelDimension/AngularModelDimension_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../AngularModelDimension/AngularModelDimension_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../AngularModelDimension/AngularModelDimension_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../AngularModelDimension/AngularModelDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AngularModelDimension/AngularModelDimension_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../AngularModelDimension/AngularModelDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../AngularModelDimension/AngularModelDimension_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../AngularModelDimension/AngularModelDimension_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [ExtensionLineOne](../AngularModelDimension/AngularModelDimension_ExtensionLineOne.md) | Read-only property that returns the first extension line of the dimension. This property may return Nothing in cases where there are no extension lines. |
| [ExtensionLineTwo](../AngularModelDimension/AngularModelDimension_ExtensionLineTwo.md) | Read-only property that returns the second extension line of the dimension. This property may return Nothing in cases where there are no extension lines. |
| [HealthStatus](../AngularModelDimension/AngularModelDimension_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../AngularModelDimension/AngularModelDimension_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../AngularModelDimension/AngularModelDimension_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../AngularModelDimension/AngularModelDimension_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../AngularModelDimension/AngularModelDimension_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../AngularModelDimension/AngularModelDimension_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../AngularModelDimension/AngularModelDimension_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../AngularModelDimension/AngularModelDimension_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../AngularModelDimension/AngularModelDimension_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../AngularModelDimension/AngularModelDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AngularModelDimension/AngularModelDimension_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[AngularModelDimensionProxy.NativeObject](../AngularModelDimensionProxy/AngularModelDimensionProxy_NativeObject.md), [AngularModelDimensions.Add](../AngularModelDimensions/AngularModelDimensions_Add.md), [AngularModelDimensions.Item](../AngularModelDimensions/AngularModelDimensions_Item.md)

## Derived Classes

[AngularModelDimensionProxy](../AngularModelDimensionProxy/AngularModelDimensionProxy.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |