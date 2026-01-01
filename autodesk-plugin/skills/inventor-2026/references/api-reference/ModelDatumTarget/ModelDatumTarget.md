# ModelDatumTarget Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelDatumTarget Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelDatumTarget/ModelDatumTarget_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelDatumTarget/ModelDatumTarget_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelDatumTarget/ModelDatumTarget_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelDatumTarget/ModelDatumTarget_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelDatumTarget/ModelDatumTarget_AnnotationPlane.md) | Gets and sets the annotation plane for the model datum target. |
| [Application](../ModelDatumTarget/ModelDatumTarget_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AreaDiameter](../ModelDatumTarget/ModelDatumTarget_AreaDiameter.md) | Returns the parameter that controls the datum target area diameter. |
| [AreaHeight](../ModelDatumTarget/ModelDatumTarget_AreaHeight.md) | Returns the parameter that controls the datum target area height. |
| [AreaWidth](../ModelDatumTarget/ModelDatumTarget_AreaWidth.md) | Returns the parameter that controls the datum target area width. |
| [AttributeSets](../ModelDatumTarget/ModelDatumTarget_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelDatumTarget/ModelDatumTarget_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [HealthStatus](../ModelDatumTarget/ModelDatumTarget_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [Index](../ModelDatumTarget/ModelDatumTarget_Index.md) | Gets and sets the index of this model datum target object. |
| [InternalName](../ModelDatumTarget/ModelDatumTarget_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelDatumTarget/ModelDatumTarget_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelDatumTarget/ModelDatumTarget_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [ModelDatum](../ModelDatumTarget/ModelDatumTarget_ModelDatum.md) | Returns the parent model datum object. |
| [Name](../ModelDatumTarget/ModelDatumTarget_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelDatumTarget/ModelDatumTarget_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelDatumTarget/ModelDatumTarget_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TargetPoint](../ModelDatumTarget/ModelDatumTarget_TargetPoint.md) | Gets and sets the placement point of this model datum target object. |
| [TextPosition](../ModelDatumTarget/ModelDatumTarget_TextPosition.md) | Gets and sets the position of the datum target text. |
| [TopToleranceFeature](../ModelDatumTarget/ModelDatumTarget_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelDatumTarget/ModelDatumTarget_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelDatumTarget/ModelDatumTarget_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelDatumTargetProxy.NativeObject](../ModelDatumTargetProxy/ModelDatumTargetProxy_NativeObject.md), [ModelDatumTargets.Item](../ModelDatumTargets/ModelDatumTargets_Item.md)

## Derived Classes

[ModelDatumTargetProxy](../ModelDatumTargetProxy/ModelDatumTargetProxy.md)

## Version

Introduced in version 2023
