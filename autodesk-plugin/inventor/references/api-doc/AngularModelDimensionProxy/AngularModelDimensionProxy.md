# AngularModelDimensionProxy Object

Derived from: [AngularModelDimension](../AngularModelDimension/AngularModelDimension.md) Object

## Description

AngularModelDimensionProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CenterText](../AngularModelDimensionProxy/AngularModelDimensionProxy_CenterText.md) | Method that centers the dimension text on the dimension line. |
| [Delete](../AngularModelDimensionProxy/AngularModelDimensionProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../AngularModelDimensionProxy/AngularModelDimensionProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../AngularModelDimensionProxy/AngularModelDimensionProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../AngularModelDimensionProxy/AngularModelDimensionProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AngularModelDimensionProxy/AngularModelDimensionProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../AngularModelDimensionProxy/AngularModelDimensionProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../AngularModelDimensionProxy/AngularModelDimensionProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../AngularModelDimensionProxy/AngularModelDimensionProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../AngularModelDimensionProxy/AngularModelDimensionProxy_Definition.md) | Read-write property that gets and sets the definition associated with this dimension. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension. |
| [ExtensionLineOne](../AngularModelDimensionProxy/AngularModelDimensionProxy_ExtensionLineOne.md) | Read-only property that returns the first extension line of the dimension. This property may return Nothing in cases where there are no extension lines. |
| [ExtensionLineTwo](../AngularModelDimensionProxy/AngularModelDimensionProxy_ExtensionLineTwo.md) | Read-only property that returns the second extension line of the dimension. This property may return Nothing in cases where there are no extension lines. |
| [HealthStatus](../AngularModelDimensionProxy/AngularModelDimensionProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../AngularModelDimensionProxy/AngularModelDimensionProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../AngularModelDimensionProxy/AngularModelDimensionProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../AngularModelDimensionProxy/AngularModelDimensionProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelValue](../AngularModelDimensionProxy/AngularModelDimensionProxy_ModelValue.md) | Read-only property that gets the dimension value as defined in the model. |
| [Name](../AngularModelDimensionProxy/AngularModelDimensionProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../AngularModelDimensionProxy/AngularModelDimensionProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../AngularModelDimensionProxy/AngularModelDimensionProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../AngularModelDimensionProxy/AngularModelDimensionProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../AngularModelDimensionProxy/AngularModelDimensionProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../AngularModelDimensionProxy/AngularModelDimensionProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AngularModelDimensionProxy/AngularModelDimensionProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |